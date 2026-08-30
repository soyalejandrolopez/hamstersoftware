# Hamster Software — Sitio web

Landing page corporativa para **Hamster Software** (empresa de software en Popayán, Colombia).
Construida con **Nuxt 4 + Tailwind CSS + @nuxtjs/i18n** (ES/EN), inspirada en el estilo de BairesDev.

- **Sitio en producción:** https://hamster-software-999907861828.us-central1.run.app
- **Proyecto GCP:** `hamster-software-web` (org `64900497525`)
- **Idiomas:** `/` = español · `/en` = inglés (estrategia `prefix_except_default`)

## Desarrollo local

```bash
npm install
npm run dev        # http://localhost:3000
```

## Estructura

- `app/components/` — componentes de UI (Header con mega-menú, Hero, Servicios, Ciberseguridad, Casos, Industrias, Proceso, Contacto, Footer, LangSwitcher)
- `i18n/locales/es.json` y `en.json` — todo el contenido traducido
- `app/data/config.ts` — datos no traducibles (WhatsApp, email, ubicación)
- `app/composables/useContent.ts` — acceso tipado y reactivo al contenido por idioma

> ⚠️ Reemplaza en `app/data/config.ts` el número de WhatsApp (`whatsappNumber`) y los datos de contacto reales antes de publicar.

## Despliegue en Google Cloud (Cloud Run)

El proyecto usa **Cloud Run** (SSR) con build vía **Cloud Build** (usa el `Dockerfile` multi-stage).

```bash
# Cuentas: negocios.alejandrolopezmurillo@gmail.com = Owner del proyecto
#          business.alejandrolopezmurillo@gmail.com = Editor + billing.projectManager + billing.admin (cuenta de facturación)

# Solo la primera vez
gcloud config set account negocios.alejandrolopezmurillo@gmail.com
gcloud config set project hamster-software-web
gcloud services enable run.googleapis.com cloudbuild.googleapis.com artifactregistry.googleapis.com

# Redesplegar tras cambios
gcloud config set account business.alejandrolopezmurillo@gmail.com
gcloud run deploy hamster-software --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080 \
  --memory 1Gi \
  --max-instances 5 \
  --project hamster-software-web
```

Notas:
- La org prohíbe usuarios externos como Owner (`ORG_MUST_INVITE_EXTERNAL_OWNERS`): la cuenta `business...` usa `roles/billing.projectManager` para vincular billing.
- Para conectar un dominio propio: Cloud Run → dominios personalizados (verificar propiedad del dominio + registro DNS).

## Google Cloud CDN (balanceador + CDN delante de Cloud Run)

La app corre en **Cloud Run** (SSR) y **Google Cloud CDN** se coloca delante mediante un balanceador de carga HTTP(S) global. Cloud CDN cachea **solo los assets estáticos** (`/_nuxt/*`, favicons, `robots.txt`, `sitemap.xml`) con TTL largo; el HTML se sigue generando en Cloud Run para conservar el nonce CSP por petición.

### Cabeceras de caché (código)
Las `routeRules` de `nuxt.config.ts` emiten el `Cache-Control` que el CDN respeta (modo `USE_ORIGIN_HEADERS` en el backend service):

- `/_nuxt/**`, favicons → `public, max-age=31536000, immutable`
- `robots.txt`, `sitemap.xml` → `public, max-age=3600, s-maxage=86400`
- `/api/chat` → `no-store` (POST: el CDN nunca lo cachea de todos modos)

### Crear la infraestructura

```bash
gcloud services enable compute.googleapis.com
bash scripts/setup-cloud-cdn.sh
```

El script crea: IP estática global, serverless NEG → Cloud Run, backend service con CDN (`--cache-mode=USE_ORIGIN_HEADERS`), URL map, certificado SSL gestionado por Google, forwarding rule HTTPS **y la redirección HTTP → HTTPS en el puerto 80** (que antes hacía el mapeo de dominio de Cloud Run). Es idempotente.

### DNS

1. Apunta un registro **A** de `hamstersoftware.com` (y `www`) a la IP que imprime el script.
2. Espera a que el certificado pase a estado `ACTIVE` (puede tardar minutos).
3. (Opcional, cuando todo funcione) elimina el mapeo de dominio de Cloud Run para evitar confusión:
   `gcloud run domain-mappings delete --domain hamstersoftware.com --region us-central1 --project hamster-software-web`

### Verificación

```bash
# 1) El asset debe mostrar la cabecera inmutable (con o sin CDN):
curl -sI https://hamstersoftware.com/favicon.svg | grep -i cache-control
# => cache-control: public, max-age=31536000, immutable

# 2) Prueba real contra el CDN (antes de cambiar el DNS): dos peticiones a la IP
#    del balanceador; la segunda debe incluir cabecera 'age' (>0) = cache hit:
IP=$(gcloud compute addresses describe hamster-software-cdn-ip --global --format='value(address)')
curl -sI -H 'Host: hamstersoftware.com' https://$IP/favicon.svg -o /dev/null
curl -sI -H 'Host: hamstersoftware.com' https://$IP/favicon.svg | grep -iE '^(age|cache-control|via)'

# 3) Config CDN del backend (debe salir 'True  USE_ORIGIN_HEADERS') y certificado:
gcloud compute backend-services describe hamster-software-cdn-backend --global --format='value(enableCDN, cdnPolicy.cacheMode)'
gcloud compute ssl-certificates describe hamster-software-ssl-cert --global --format='table(managed.status)'
# Nota: get-health no aplica a backends serverless NEG (no es un error).
```

El **cache hit ratio** se consulta en la consola GCP: *Network Services → Cloud CDN*.

> ⚠️ El HTML no se cachea a propósito: mantiene el nonce CSP por petición (ver `server/plugins/csp.ts`). Si en el futuro se quiere cachear páginas enteras (p. ej. con SWR), habrá que asumir un nonce fijo mientras dure la caché o migrar el CSP a hashes.
