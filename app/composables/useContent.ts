import type {
  CaseStudy,
  ContactContent,
  HeroContent,
  Industry,
  ProcessStep,
  Product,
  SecurityContent,
  Service,
  Stat
} from '~/types/content'

/**
 * Acceso reactivo al contenido traducible de los archivos de locale.
 * Se fuerza la dependencia de `locale` dentro de cada computed para
 * garantizar la reactividad aunque `tm()` no la tenga por sí sola.
 *
 * IMPORTANTE: los mensajes se normalizan para que servidor y cliente
 * produzcan exactamente el mismo contenido:
 *  - En el bundle del cliente, `tm()` devuelve nodos AST compilados en lugar
 *    de strings; se resuelven con `rt()` (ver https://vue-i18n.intlify.dev/api/composition#tm).
 *  - En el servidor (y en producción), los archivos de locale se incrustan
 *    como JSON crudo, así que los escapes del formato de mensaje (p. ej.
 *    `\@` para un `@` literal) llegan tal cual; se desescapan aquí.
 */
export function useContent() {
  const { locale, tm, rt } = useI18n()

  // Desescapa el formato de mensaje de vue-i18n en cadenas crudas:
  // `\@` -> `@`, `\{` -> `{`, `\|` -> `|`, `\\` -> `\`
  function unescape(raw: string): string {
    return raw.replace(/\\([@{}|\\])/g, '$1')
  }

  // Convierte los nodos de mensaje compilados (solo existen en el cliente)
  // de vuelta a strings, dejando intacto el resto de la estructura.
  function resolve(value: unknown): unknown {
    if (value === null || typeof value !== 'object') {
      return typeof value === 'string' ? unescape(value) : value
    }
    if (Array.isArray(value)) {
      return value.map(resolve)
    }
    const record = value as Record<string, unknown>
    // Nodo AST de mensaje compilado: type numérico + loc + body
    if (typeof record.type === 'number' && 'loc' in record && 'body' in record) {
      return rt(record)
    }
    const out: Record<string, unknown> = {}
    for (const key of Object.keys(record)) {
      out[key] = resolve(record[key])
    }
    return out
  }

  const services = computed(() => {
    void locale.value
    return resolve(tm('services')) as unknown as Service[]
  })

  const products = computed(() => {
    void locale.value
    return resolve(tm('products')) as unknown as Product[]
  })

  const stats = computed(() => {
    void locale.value
    return resolve(tm('stats')) as unknown as Stat[]
  })

  const hero = computed(() => {
    void locale.value
    return resolve(tm('hero')) as unknown as HeroContent
  })

  const security = computed(() => {
    void locale.value
    return resolve(tm('security')) as unknown as SecurityContent
  })

  const cases = computed(() => {
    void locale.value
    return resolve(tm('cases')) as unknown as CaseStudy[]
  })

  const industries = computed(() => {
    void locale.value
    return resolve(tm('industries')) as unknown as Industry[]
  })

  const processSteps = computed(() => {
    void locale.value
    return resolve(tm('process')) as unknown as ProcessStep[]
  })

  const contact = computed(() => {
    void locale.value
    return resolve(tm('contact')) as unknown as ContactContent
  })

  return { services, products, stats, hero, security, cases, industries, processSteps, contact }
}
