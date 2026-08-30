/**
 * Motor de respuestas offline para el Chatbot de Hamster Software.
 * Funciona 100% en local sin depender de modelos externos ni API keys.
 */

function normalizeText(text: string): string {
  return text
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .trim()
}

export function getOfflineChatReply(query: string, locale: string = 'es'): string {
  const isEn = locale === 'en'
  const q = normalizeText(query)

  // 1. Saludos
  if (/^(hola|buenos\s*dias|buenas\s*tardes|buenas\s*noches|hey|hi|hello|saludos|que\s*tal|buenas)/i.test(q) || q === 'hola' || q === 'hello' || q === 'hi') {
    return isEn
      ? "Hello! 👋 Welcome to Hamster Software. We specialize in custom software development, mobile apps, Cloud, DevOps, Vector DBs, AI/SLMs, and business automation. How can we help your business today?"
      : "¡Hola! 👋 Te damos la bienvenida a Hamster Software. Desarrollamos software a la medida, aplicaciones móviles, Nube, DevOps, Bases de Datos Vectoriales, IA/SLMs y automatización empresarial. ¿En qué podemos ayudarte hoy?"
  }

  // 2. Servicios generales
  if (q.includes('servicio') || q.includes('que hacen') || q.includes('que ofrecen') || q.includes('service') || q.includes('what do you do') || q.includes('capacidades')) {
    return isEn
      ? "We offer 22 specialized engineering & software services:\n\n• 🌐 Web Development, Mobile Apps & Desktop Software\n• 🧠 Vector Databases, Chatbots, Neural Networks & SLMs\n• ☁️ Cloud Computing, Servers & DevOps CI/CD\n• ⚡ Enterprise Automation (RPA), IT Automation & BPM\n• 📊 Data Engineering, Advanced Analytics & Middleware\n• 🛡️ Cybersecurity & Pentesting\n\nWould you like a free quote for any of these services?"
      : "Ofrecemos 22 servicios especializados de ingeniería y software:\n\n• 🌐 Desarrollo Web, Apps Móviles y Software de Escritorio\n• 🧠 Bases de Datos Vectoriales, Chatbots, Redes Neuronales y SLMs\n• ☁️ Nube, Computación/Servidores y DevOps CI/CD\n• ⚡ Automatización Empresarial (RPA), Automatización TI y BPM\n• 📊 Ingeniería de Datos, Analítica Avanzada y Middleware\n• 🛡️ Ciberseguridad y Pentesting\n\n¿Te gustaría cotizar alguno de estos servicios para tu empresa?"
  }

  // 3. Bases de Datos Vectoriales
  if (q.includes('vector') || q.includes('embedding') || q.includes('qdrant') || q.includes('pinecone') || q.includes('milvus') || q.includes('chroma') || q.includes('pgvector')) {
    return isEn
      ? "We implement high-performance Vector Databases (Qdrant, Milvus, pgvector, Chroma, Pinecone) for semantic search, recommendation engines, and high-scale RAG pipelines with sub-10ms query times.\n\nWould you like to integrate vector search into your application?"
      : "Implementamos Bases de Datos Vectoriales de alto rendimiento (Qdrant, Milvus, pgvector, Chroma, Pinecone) para búsqueda semántica, sistemas de recomendación y pipelines RAG a gran escala con consultas sub-10ms.\n\n¿Te gustaría integrar búsqueda vectorial en tu aplicación?"
  }

  // 4. Chatbots y Asistentes
  if (q.includes('chatbot') || q.includes('asistente') || q.includes('bot') || q.includes('conversacional') || q.includes('virtual assistant')) {
    return isEn
      ? "We build smart AI Chatbots & Virtual Assistants connected to official WhatsApp Business API, Web, Telegram, and CRMs, grounded on your real data with automated human escalation.\n\nReady to automate customer service 24/7? Message us on WhatsApp: +57 302 579 0274."
      : "Desarrollamos Chatbots y Asistentes Virtuales con IA conectados a WhatsApp Business oficial, Web, Telegram y CRMs, basados 100% en tus datos reales y con derivación automática a asesores humanos.\n\n¿Quieres automatizar tu atención al cliente 24/7? Escríbenos por WhatsApp al +57 302 579 0274."
  }

  // 5. Redes Neuronales y Deep Learning
  if (q.includes('neuronal') || q.includes('neural') || q.includes('deep learning') || q.includes('vision') || q.includes('cnn') || q.includes('transformer') || q.includes('pytorch') || q.includes('tensorflow')) {
    return isEn
      ? "We design, train, and deploy Deep Neural Networks (PyTorch, TensorFlow, TensorRT) for computer vision, object detection, signal processing, and time-series forecasting with full IP ownership for your company.\n\nWould you like to discuss a custom Deep Learning model?"
      : "Diseñamos, entrenamos y desplegamos Redes Neuronales y Deep Learning (PyTorch, TensorFlow, TensorRT) para visión artificial, detección de objetos, procesamiento de señales y series temporales con 100% de propiedad intelectual para tu empresa.\n\n¿Te gustaría evaluar un modelo de Deep Learning a medida?"
  }

  // 6. Analítica Avanzada
  if (q.includes('analitica') || q.includes('analytics') || q.includes('bi') || q.includes('estadistica') || q.includes('cohortes') || q.includes('churn') || q.includes('ltv') || q.includes('predictiv')) {
    return isEn
      ? "Our Advanced Analytics service delivers predictive churn models, customer LTV analysis, propensity scoring, and executive dashboards with Power BI, Python, and DuckDB to drive revenue growth.\n\nContact us on WhatsApp at +57 302 579 0274 for an analytics assessment."
      : "Nuestro servicio de Analítica Avanzada ofrece modelos predictivos de abandono (churn), análisis de LTV, propensión de compra y cuadros de mando ejecutivos en Power BI, Python y DuckDB para acelerar tu crecimiento.\n\nEscríbenos por WhatsApp al +57 302 579 0274 para una evaluación analítica."
  }

  // 7. Gestión de Activos
  if (q.includes('activo') || q.includes('asset') || q.includes('inventario') || q.includes('itam') || q.includes('licencia') || q.includes('snipe')) {
    return isEn
      ? "We deploy centralized IT Asset Management (ITAM) platforms with QR/RFID tagging, automated hardware/server inventory, license renewal tracking, and stress-free audit compliance.\n\nWant complete visibility of your company's tech assets? Let's talk!"
      : "Implementamos plataformas centralizadas de Gestión de Activos de TI (ITAM) con códigos QR/RFID, inventario automatizado de servidores/equipos, control de licencias y cumplimiento de auditorías.\n\n¿Quieres visibilidad total de los activos de tu empresa? ¡Hablemos!"
  }

  // 8. Automatización Empresarial (RPA)
  if (q.includes('automatizacion empresarial') || q.includes('rpa') || q.includes('n8n') || q.includes('airflow') || q.includes('flujo de trabajo') || q.includes('conciliacion') || q.includes('workflow')) {
    return isEn
      ? "We build Enterprise RPA Automations with n8n, Python, and Airflow to automate invoices, bank reconciliations, CRM syncs, and manual operational routines, saving up to 90% of staff time.\n\nMessage us on WhatsApp (+57 302 579 0274) to automate your processes."
      : "Construimos Automatizaciones Empresariales (RPA) con n8n, Python y Airflow para automatizar facturas, conciliaciones bancarias, sincronización de CRM y tareas repetitivas, ahorrando hasta 90% del tiempo operativo.\n\nEscríbenos por WhatsApp (+57 302 579 0274) para automatizar tus procesos."
  }

  // 9. Operaciones de Negocios (BPM)
  if (q.includes('operacion') || q.includes('bpm') || q.includes('camunda') || q.includes('bpmn') || q.includes('cuello de botella') || q.includes('sla') || q.includes('tramite') || q.includes('business operation')) {
    return isEn
      ? "We digitize Business Operations (BPM) with Camunda and modern web portals: multi-level approval workflows, cycle time tracking, SLA enforcement, and integrated digital signatures.\n\nReady to eliminate operational bottlenecks? Reach out on WhatsApp!"
      : "Digitalizamos Operaciones de Negocios (BPM) con Camunda y portales web modernos: flujos de aprobación multinivel, control de tiempos de ciclo (SLAs), eliminación de cuellos de botella y firma digital.\n\n¿Listo para optimizar tus operaciones? ¡Escríbenos por WhatsApp!"
  }

  // 10. Nube y Cloud Computing
  if (q.includes('nube') || q.includes('cloud') || q.includes('aws') || q.includes('gcp') || q.includes('azure') || q.includes('cloudflare') || q.includes('finops') || q.includes('migracion cloud')) {
    return isEn
      ? "We architect, migrate, and optimize resilient Cloud Infrastructure on AWS, GCP, Azure, and Cloudflare with 99.99% high availability, Disaster Recovery, and FinOps cost optimization.\n\nContact us on WhatsApp at +57 302 579 0274 to plan your cloud migration."
      : "Diseñamos, migramos y optimizamos Infraestructura en la Nube (AWS, GCP, Azure, Cloudflare) con alta disponibilidad (99.99%), Disaster Recovery y optimización de costos FinOps.\n\nContáctanos por WhatsApp al +57 302 579 0274 para planificar tu migración a la nube."
  }

  // 11. Computación y Servidores
  if (q.includes('servidor') || q.includes('server') || q.includes('computacion') || q.includes('proxmox') || q.includes('kvm') || q.includes('vps') || q.includes('bare metal') || q.includes('hosting')) {
    return isEn
      ? "We manage dedicated servers, VPS, bare-metal clusters, and virtualization platforms (Proxmox, KVM, Linux/Windows) with OS security hardening, 24/7 monitoring, and high-performance storage (ZFS/Ceph).\n\nNeed enterprise server management? We can help!"
      : "Administramos servidores dedicados, VPS, clústeres bare-metal y plataformas de virtualización (Proxmox, KVM, Linux/Windows) con hardening de seguridad, monitoreo 24/7 y almacenamiento ZFS.\n\n¿Necesitas soporte o administración de servidores? ¡Escríbenos!"
  }

  // 12. DevOps y CI/CD
  if (q.includes('devops') || q.includes('ci/cd') || q.includes('cicd') || q.includes('pipeline') || q.includes('docker') || q.includes('kubernetes') || q.includes('terraform') || q.includes('github actions')) {
    return isEn
      ? "We implement automated DevOps & CI/CD pipelines (GitHub Actions, Docker, Kubernetes, Terraform IaC) with zero-downtime Blue-Green releases and instant rollbacks to ship software faster and defect-free.\n\nReady to elevate your engineering speed? Let's connect!"
      : "Implementamos prácticas de DevOps y pipelines CI/CD automatizados (GitHub Actions, Docker, Kubernetes, Terraform IaC) con despliegues Blue-Green sin caídas y rollbacks en un clic.\n\n¿Quieres acelerar el ritmo de despliegue de tu software? ¡Contáctanos!"
  }

  // 13. Automatización de TI
  if (q.includes('automatizacion de ti') || q.includes('it automation') || q.includes('powershell') || q.includes('bash') || q.includes('script') || q.includes('sysadmin') || q.includes('zabbix')) {
    return isEn
      ? "Our IT Automation services eliminate routine sysadmin chores with self-healing service scripts, automated workstation provisioning, scheduled backups, and fleet-wide patch management.\n\nContact us on WhatsApp: +57 302 579 0274."
      : "Nuestra Automatización de TI elimina tareas rutinarias de soporte con scripts de auto-reparación de servicios, aprovisionamiento desatendido, backups automáticos y gestión de parches masivos.\n\nEscríbenos por WhatsApp al +57 302 579 0274."
  }

  // 14. Middleware e Integración
  if (q.includes('middleware') || q.includes('integracion') || q.includes('kafka') || q.includes('rabbitmq') || q.includes('cola') || q.includes('broker') || q.includes('event driven') || q.includes('integration')) {
    return isEn
      ? "We build high-throughput Middleware & System Integration layers with Apache Kafka, RabbitMQ, Redis, and unified REST/GraphQL gateways to synchronize ERPs, banking, and e-commerce platforms with zero lost data.\n\nNeed to integrate disparate software? Reach out on WhatsApp!"
      : "Desarrollamos Middleware e Integración de Sistemas de alto rendimiento con Apache Kafka, RabbitMQ, Redis y APIs REST/GraphQL para comunicar ERPs, pasarelas de pago y plataformas sin pérdida de datos.\n\n¿Necesitas conectar sistemas heterogéneos? ¡Escríbenos por WhatsApp!"
  }

  // 15. Modelos de Lenguaje Pequeño (SLMs) / IA
  if (q.includes('slm') || q.includes('pequeno') || q.includes('small language') || q.includes('ia') || q.includes('ai') || q.includes('inteligencia artificial') || q.includes('machine learning') || q.includes('modelo') || q.includes('llm') || q.includes('ollama')) {
    return isEn
      ? "In AI, we specialize in:\n\n• 🧠 Small Language Models (SLMs): Compact, high-precision models (Phi-3, Gemma, LLaMA 3, Qwen) running on your own servers with 100% privacy and zero token fees.\n• 📈 Machine Learning: Predictive analytics, computer vision, and local RAG pipelines.\n\nWould you like to deploy private, on-premise AI in your organization?"
      : "En Inteligencia Artificial nos especializamos en:\n\n• 🧠 Modelos de Lenguaje Pequeño (SLMs): Modelos compactos y de alta precisión (Phi-3, Gemma, LLaMA 3, Qwen) que se ejecutan en tus propios servidores con 100% de privacidad y cero costos por token.\n• 📈 Machine Learning: Analítica predictiva, visión computacional y arquitecturas RAG privadas.\n\n¿Te gustaría implementar IA local y privada en tu empresa?"
  }

  // 16. Desarrollo Web / Páginas / Tiendas
  if (q.includes('web') || q.includes('pagina') || q.includes('sitio') || q.includes('landing') || q.includes('ecommerce') || q.includes('tienda') || q.includes('portal') || q.includes('website') || q.includes('online store')) {
    return isEn
      ? "We build high-performance websites, high-converting landing pages, online stores, and enterprise platforms using modern frameworks like Next.js, Vue.js, Laravel, and Tailwind CSS.\n\nWe optimize for Core Web Vitals, SEO, and fast load times. Contact us on WhatsApp at +57 302 579 0274 for a proposal!"
      : "Diseñamos y desarrollamos sitios web de alto rendimiento, landing pages que convierten, tiendas virtuales (e-commerce) y plataformas empresariales con Next.js, Vue.js, Laravel y Tailwind CSS.\n\nOptimizamos velocidad, SEO y experiencia de usuario. ¡Escríbenos por WhatsApp al +57 302 579 0274 para enviarte una propuesta!"
  }

  // 17. Desarrollo Móvil / Apps
  if (q.includes('movil') || q.includes('app') || q.includes('aplicacion') || q.includes('ios') || q.includes('android') || q.includes('iphone') || q.includes('flutter') || q.includes('react native') || q.includes('pwa') || q.includes('celular') || q.includes('mobile')) {
    return isEn
      ? "We develop native and cross-platform mobile apps for iOS and Android using Swift, Kotlin, React Native, and Flutter, as well as offline-first PWAs and store publishing.\n\nHave an app idea? Chat with our engineering team on WhatsApp: +57 302 579 0274."
      : "Desarrollamos aplicaciones móviles nativas e híbridas para iOS y Android con Swift, Kotlin, React Native y Flutter, además de PWAs con soporte offline y publicación en tiendas.\n\n¿Tienes una idea de app? Escríbenos por WhatsApp al +57 302 579 0274 y te asesoramos."
  }

  // 18. Precios / Cotización / Costos
  if (q.includes('precio') || q.includes('costo') || q.includes('cuanto vale') || q.includes('cuanto cuesta') || q.includes('cotiz') || q.includes('presupuesto') || q.includes('tarifa') || q.includes('valor') || q.includes('price') || q.includes('cost') || q.includes('how much') || q.includes('quote') || q.includes('budget')) {
    return isEn
      ? "Pricing is tailored to your project's scope and technical requirements. We offer a free initial consultation and send a clear, detailed estimate within 24–48 hours.\n\nTo get your free quote, message us directly on WhatsApp at +57 302 579 0274 or email info@hamstersoftware.com."
      : "El costo depende del alcance y requerimientos específicos de tu proyecto. Ofrecemos una consulta inicial gratuita y te entregamos una cotización clara en menos de 24–48 horas.\n\nPara cotizar tu proyecto, escríbenos directamente por WhatsApp al +57 302 579 0274 o al correo info@hamstersoftware.com."
  }

  // 19. Contacto / WhatsApp / Teléfono / Correo
  if (q.includes('contacto') || q.includes('contactar') || q.includes('whatsapp') || q.includes('correo') || q.includes('email') || q.includes('telefono') || q.includes('celular') || q.includes('llamar') || q.includes('hablar') || q.includes('contact') || q.includes('phone') || q.includes('call')) {
    return isEn
      ? "You can reach us through any of our official channels:\n\n• 📲 WhatsApp: +57 302 579 0274 (wa.me/573025790274)\n• ✉️ Email: info@hamstersoftware.com\n• 📍 Location: Popayán, Cauca, Colombia\n\nWe respond quickly to all inquiries!"
      : "Puedes comunicarte con nosotros por cualquiera de nuestros canales oficiales:\n\n• 📲 WhatsApp: +57 302 579 0274 (wa.me/573025790274)\n• ✉️ Correo: info@hamstersoftware.com\n• 📍 Ubicación: Popayán, Cauca, Colombia\n\n¡Te responderemos en minutos!"
  }

  // 20. Ubicación / Dónde están
  if (q.includes('donde estan') || q.includes('ubicacion') || q.includes('popayan') || q.includes('cauca') || q.includes('colombia') || q.includes('donde quedan') || q.includes('location') || q.includes('where are you')) {
    return isEn
      ? "Our team is based in Popayán, Cauca, Colombia. We build software for local and international companies with dedicated agile teams.\n\nReach out on WhatsApp at +57 302 579 0274."
      : "Nuestra sede principal está en Popayán, Cauca, Colombia. Desarrollamos software para empresas en Colombia y el mundo con equipos dedicados y metodologías ágiles.\n\nContáctanos por WhatsApp al +57 302 579 0274."
  }

  // 21. Ciberseguridad
  if (q.includes('seguridad') || q.includes('ciberseguridad') || q.includes('pentest') || q.includes('auditoria') || q.includes('vulnerabilidad') || q.includes('cve') || q.includes('security') || q.includes('cybersecurity')) {
    return isEn
      ? "We provide proactive cybersecurity services: penetration testing (web, mobile, APIs), real-time CVE monitoring, code audits, and DevSecOps to keep your systems protected against threats."
      : "Ofrecemos servicios de Ciberseguridad proactiva: pruebas de penetración (pentesting), monitoreo de vulnerabilidades en tiempo real (CVEs), auditorías de código y DevSecOps para proteger tu empresa."
  }

  // 22. Datos / ETL / Dashboards
  if (q.includes('dato') || q.includes('etl') || q.includes('dashboard') || q.includes('power bi') || q.includes('tableau') || q.includes('pipeline') || q.includes('data')) {
    return isEn
      ? "We architect modern data pipelines, ETL extraction, and executive dashboards with Power BI, Tableau, and D3.js to turn your complex data into smart business decisions."
      : "Diseñamos pipelines de datos, procesos ETL y dashboards ejecutivos en Power BI, Tableau y D3.js para transformar tus datos en decisiones estratégicas inteligentes."
  }

  // 23. Soluciones específicas (RentaYa, Odoo, etc.)
  if (q.includes('rentaya') || q.includes('clasificado') || q.includes('odoo') || q.includes('inmueble') || q.includes('auto') || q.includes('vehiculo') || q.includes('moodle') || q.includes('lms')) {
    return isEn
      ? "We build tailored platforms like RentaYa (Real Estate & Automotive marketplace with direct WhatsApp connection), Odoo ERP integrations, and custom LMS platforms.\n\nMessage us on WhatsApp at +57 302 579 0274 to explore a similar project."
      : "Desarrollamos soluciones como RentaYa (Portal de Clasificados Inmobiliarios y Vehículos con conexión directa por WhatsApp), integraciones Odoo ERP y plataformas LMS.\n\nEscríbenos por WhatsApp al +57 302 579 0274 para diseñar tu plataforma."
  }

  // Fallback amigable
  return isEn
    ? "Thanks for reaching out! To give you the exact details and a personalized quote for your project, chat directly with our team on WhatsApp: +57 302 579 0274 or email us at info@hamstersoftware.com."
    : "¡Gracias por tu mensaje! Para brindarte asesoría detallada y una cotización personalizada para tu proyecto, escríbenos directamente por WhatsApp al +57 302 579 0274 o a info@hamstersoftware.com. ¡Estamos atentos para ayudarte!"
}
