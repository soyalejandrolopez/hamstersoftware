#!/usr/bin/env bash
# ============================================================================
# Google Cloud CDN delante de Cloud Run — Hamster Software
# ============================================================================
# Crea toda la infraestructura para servir el sitio a través de un balanceador
# de carga HTTP(S) global con Cloud CDN habilitado:
#
#   1. IP estática global
#   2. Serverless NEG  ->  Cloud Run (hamster-software)
#   3. Backend service  con CDN (modo USE_ORIGIN_HEADERS)
#   4. URL map
#   5. Certificado SSL gestionado por Google (hamstersoftware.com + www)
#   6. Proxy HTTPS
#   7. Forwarding rule (443)
#   8. Redirección HTTP -> HTTPS (puerto 80)
#
# REQUISITOS:
#   - gcloud autenticado:  gcloud auth login
#   - API Compute habilitada: gcloud services enable compute.googleapis.com
#   - Permisos: roles/compute.admin  (o compute.networkAdmin + compute.securityAdmin)
#
# USO:
#   bash scripts/setup-cloud-cdn.sh
#
# DESPUÉS de ejecutarlo:
#   - Crea en tu DNS un registro A de hamstersoftware.com (y www) apuntando a
#     la IP que imprime el script (paso final).
#   - Espera a que el certificado pase a estado ACTIVE.
#
# El script es idempotente: si un recurso ya existe, lo salta y continúa.
# ============================================================================

set -euo pipefail

# ------------------- Variables (ajusta si es necesario) ---------------------
PROJECT_ID="hamster-software-web"
REGION="us-central1"
CLOUD_RUN_SERVICE="hamster-software"
DOMAIN="hamstersoftware.com"
WWW_DOMAIN="www.hamstersoftware.com"

IP_NAME="hamster-software-cdn-ip"
NEG_NAME="hamster-software-run-neg"
BACKEND_SERVICE="hamster-software-cdn-backend"
URL_MAP="hamster-software-url-map"
HTTPS_PROXY="hamster-software-https-proxy"
CERT_NAME="hamster-software-ssl-cert"
FORWARDING_RULE="hamster-software-https-fwd"

# ------------------- 1/9 IP estática global ---------------------------------
echo "==> 1/9 Reservando IP estática global..."
if ! gcloud compute addresses describe "$IP_NAME" --global --project "$PROJECT_ID" >/dev/null 2>&1; then
  gcloud compute addresses create "$IP_NAME" --global --project "$PROJECT_ID"
else
  echo "    (ya existe, se reutiliza)"
fi

# ------------------- 2/9 Serverless NEG -> Cloud Run ------------------------
echo "==> 2/9 Creando serverless NEG hacia Cloud Run '$CLOUD_RUN_SERVICE'..."
if ! gcloud compute network-endpoint-groups describe "$NEG_NAME" --region="$REGION" --project "$PROJECT_ID" >/dev/null 2>&1; then
  gcloud compute network-endpoint-groups create "$NEG_NAME" \
    --region="$REGION" \
    --network-endpoint-type=serverless \
    --cloud-run-service="$CLOUD_RUN_SERVICE" \
    --project "$PROJECT_ID"
else
  echo "    (ya existe)"
fi

# ------------------- 3/9 Backend service con CDN ----------------------------
# USE_ORIGIN_HEADERS: el CDN solo cachea respuestas que tengan Cache-Control
# público (las routeRules de nuxt.config.ts). El HTML no lleva Cache-Control,
# así que NUNCA se cachea y el nonce CSP se genera por petición.
echo "==> 3/9 Creando backend service con Cloud CDN (USE_ORIGIN_HEADERS)..."
if ! gcloud compute backend-services describe "$BACKEND_SERVICE" --global --project "$PROJECT_ID" >/dev/null 2>&1; then
  # Ojo: en modo USE_ORIGIN_HEADERS Google NO permite --default-ttl ni --max-ttl
  # (solo aplican a CACHE_ALL_STATIC / FORCE_CACHE_ALL). Los TTL los dicta el
  # origen vía Cache-Control: los assets inmutables llevan max-age=1 año.
  gcloud compute backend-services create "$BACKEND_SERVICE" \
    --global \
    --enable-cdn \
    --cache-mode=USE_ORIGIN_HEADERS \
    --project "$PROJECT_ID"
else
  echo "    (ya existe)"
fi

# ------------------- 4/9 Conectar el NEG al backend -------------------------
echo "==> 4/9 Conectando el NEG al backend service..."
if ! gcloud compute backend-services describe "$BACKEND_SERVICE" --global \
    --format='value(backends[].group)' --project "$PROJECT_ID" | grep -q "$NEG_NAME"; then
  gcloud compute backend-services add-backend "$BACKEND_SERVICE" \
    --global \
    --network-endpoint-group="$NEG_NAME" \
    --network-endpoint-group-region="$REGION" \
    --project "$PROJECT_ID"
else
  echo "    (el NEG ya estaba conectado al backend)"
fi

# ------------------- 5/9 URL map ---------------------------------------------
echo "==> 5/9 Creando URL map..."
if ! gcloud compute url-maps describe "$URL_MAP" --project "$PROJECT_ID" >/dev/null 2>&1; then
  gcloud compute url-maps create "$URL_MAP" \
    --default-service="$BACKEND_SERVICE" \
    --project "$PROJECT_ID"
else
  echo "    (ya existe)"
fi

# ------------------- 6/9 Certificado SSL gestionado ---------------------------
echo "==> 6/9 Creando certificado SSL gestionado por Google..."
if ! gcloud compute ssl-certificates describe "$CERT_NAME" --global --project "$PROJECT_ID" >/dev/null 2>&1; then
  gcloud compute ssl-certificates create "$CERT_NAME" \
    --domains="$DOMAIN,$WWW_DOMAIN" \
    --global \
    --project "$PROJECT_ID"
else
  echo "    (ya existe)"
fi

# ------------------- 7/9 Proxy HTTPS -------------------------------------------
echo "==> 7/9 Creando proxy HTTPS..."
if ! gcloud compute target-https-proxies describe "$HTTPS_PROXY" --project "$PROJECT_ID" >/dev/null 2>&1; then
  gcloud compute target-https-proxies create "$HTTPS_PROXY" \
    --url-map="$URL_MAP" \
    --ssl-certificates="$CERT_NAME" \
    --project "$PROJECT_ID"
else
  echo "    (ya existe)"
fi

# ------------------- 8/9 Forwarding rule -----------------------------------------
echo "==> 8/9 Creando forwarding rule HTTPS (puerto 443)..."
if ! gcloud compute forwarding-rules describe "$FORWARDING_RULE" --global --project "$PROJECT_ID" >/dev/null 2>&1; then
  gcloud compute forwarding-rules create "$FORWARDING_RULE" \
    --global \
    --target-https-proxy="$HTTPS_PROXY" \
    --address="$IP_NAME" \
    --ports=443 \
    --project "$PROJECT_ID"
else
  echo "    (ya existe)"
fi

# ------------------- 9/9 Redirección HTTP -> HTTPS ------------------------------
# Cloud Run redirigía HTTP->HTTPS con su mapeo de dominio; una vez el DNS apunte
# al balanceador, este URL map hace lo mismo en el puerto 80.
HTTP_URL_MAP="$URL_MAP-http-redirect"
HTTP_PROXY="$HTTPS_PROXY-http"
HTTP_FORWARDING_RULE="$FORWARDING_RULE-http"

echo "==> 9/9 Creando redirección HTTP -> HTTPS (puerto 80)..."
if ! gcloud compute url-maps describe "$HTTP_URL_MAP" --project "$PROJECT_ID" >/dev/null 2>&1; then
  # gcloud no tiene una flag --default-url-redirect en url-maps create; se crea
  # importando un URL map YAML con defaultUrlRedirect (httpsRedirect=true).
  TMP_YAML="/tmp/${HTTP_URL_MAP}.yaml"
  cat > "$TMP_YAML" <<EOF
name: ${HTTP_URL_MAP}
defaultUrlRedirect:
  redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
  httpsRedirect: true
EOF
  gcloud compute url-maps import "$HTTP_URL_MAP" \
    --source="$TMP_YAML" \
    --global \
    --project "$PROJECT_ID" --quiet
  rm -f "$TMP_YAML"
else
  echo "    (ya existe)"
fi
if ! gcloud compute target-http-proxies describe "$HTTP_PROXY" --project "$PROJECT_ID" >/dev/null 2>&1; then
  gcloud compute target-http-proxies create "$HTTP_PROXY" \
    --url-map="$HTTP_URL_MAP" \
    --project "$PROJECT_ID"
else
  echo "    (ya existe)"
fi
if ! gcloud compute forwarding-rules describe "$HTTP_FORWARDING_RULE" --global --project "$PROJECT_ID" >/dev/null 2>&1; then
  gcloud compute forwarding-rules create "$HTTP_FORWARDING_RULE" \
    --global \
    --target-http-proxy="$HTTP_PROXY" \
    --address="$IP_NAME" \
    --ports=80 \
    --project "$PROJECT_ID"
else
  echo "    (ya existe)"
fi

# ------------------- Resumen y siguientes pasos ---------------------------------
IP=$(gcloud compute addresses describe "$IP_NAME" --global --format='value(address)' --project "$PROJECT_ID")
echo ""
echo "============================================================"
echo " Infraestructura creada. IP estática del balanceador: $IP"
echo ""
echo " SIGUIENTE PASO (DNS):"
echo "   Crea estos registros A en tu DNS:"
echo "     $DOMAIN      ->  $IP"
echo "     $WWW_DOMAIN  ->  $IP"
echo ""
echo " Verifica el certificado (debe pasar a ACTIVE, tarda minutos):"
echo "   gcloud compute ssl-certificates describe $CERT_NAME --global \\"
echo "     --format='table(managed.status)'"
echo ""
echo " Verificación de caché (debe mostrar 'public, max-age=31536000, immutable'):"
echo "   curl -sI https://$DOMAIN/favicon.svg | grep -i cache-control"
echo ""
echo " Cache hit ratio en consola: Network Services -> Cloud CDN"
echo "============================================================"
