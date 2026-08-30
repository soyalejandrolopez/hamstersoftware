# ============================================================
# Hamster Software — Nuxt 4 SSR en Google Cloud Run
# ============================================================

# --- Stage 1: instalar dependencias (cacheable) ---------------
FROM node:24-alpine AS deps
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

# --- Stage 2: compilar la aplicación ---------------------------
FROM node:24-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

# --- Stage 3: imagen de producción -----------------------------
FROM node:24-alpine AS runner
WORKDIR /app

ENV NODE_ENV=production
# Cloud Run inyecta $PORT en tiempo de ejecución; estos son valores
# por defecto seguros (Nitro escucha en 0.0.0.0 dentro del contenedor).
ENV HOST=0.0.0.0
ENV PORT=8080

# Usuario sin privilegios (buena práctica de seguridad en Cloud Run)
RUN addgroup --system --gid 1001 nodejs && \
    adduser --system --uid 1001 nuxt && \
    chown -R nuxt:nodejs /app

# Solo se copia la salida autocontenida de Nitro (sin node_modules)
COPY --from=builder --chown=nuxt:nodejs /app/.output ./.output

USER nuxt

EXPOSE 8080

CMD ["node", ".output/server/index.mjs"]
