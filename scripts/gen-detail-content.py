#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Añade `slug`, `overview`, `benefits`, `tech` y `faq` a cada producto/servicio
en i18n/locales/es.json y en.json. Ejecutar: python3 scripts/gen-detail-content.py
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ES_PATH = os.path.join(ROOT, 'i18n', 'locales', 'es.json')
EN_PATH = os.path.join(ROOT, 'i18n', 'locales', 'en.json')

# ---------------------------------------------------------------------------
# Contenido ES — slug común (mismo en ambos idiomas), campos detallados
# ---------------------------------------------------------------------------
PRODUCTS_ES = {
    'vulnerabilities': {
        'name': 'Vulnerabilidades',
        'slug': 'vulnerabilities',
        'icon': 'shield-alert',
        'subtitle': 'Pentesting y auditorías',
        'description': 'Auditorías de seguridad y pruebas de penetración para encontrar y corregir vulnerabilidades antes que los atacantes.',
        'overview': 'Identificamos las debilidades de tu infraestructura, aplicaciones web y móviles antes de que alguien las explote. Ejecutamos pentesting controlado, escaneo de vulnerabilidades y auditorías de configuración, y entregamos un plan de remediación priorizado con evidencia y recomendaciones accionables.',
        'features': [
            'Pruebas de penetración en aplicaciones web, móviles y APIs',
            'Escaneo y correlación de vulnerabilidades (CVE)',
            'Auditoría de configuración de servidores y redes',
            'Análisis según OWASP Top 10 y estándares de la industria',
            'Informes ejecutivos con plan de remediación priorizado',
            'Re-testing para validar las correcciones aplicadas'
        ],
        'benefits': [
            {'icon': 'shield', 'title': 'Prevén brechas de seguridad', 'text': 'Detecta y corrige fallas antes de que se conviertan en incidentes costosos.'},
            {'icon': 'scale', 'title': 'Cumplimiento normativo', 'text': 'Documentación de auditorías que respalda certificaciones y regulaciones.'},
            {'icon': 'trending-up', 'title': 'Riesgos priorizados', 'text': 'Sabes exactamente qué corregir primero según el impacto real en tu negocio.'},
            {'icon': 'users', 'title': 'Confianza del cliente', 'text': 'Protege la información de tus usuarios y fortalece tu reputación.'}
        ],
        'tech': ['Nmap', 'Burp Suite', 'OWASP ZAP', 'Metasploit', 'Wireshark', 'Nikto'],
        'faq': [
            {'q': '¿Cuánto dura un pentesting?', 'a': 'Depende del alcance: una auditoría de aplicación web típica toma de 1 a 3 semanas, incluyendo el informe y la validación de correcciones.'},
            {'q': '¿Es seguro hacer una prueba de penetración?', 'a': 'Sí. Trabajamos con alcances y reglas de compromiso definidos por escrito, en entornos controlados y sin afectar la operación.'},
            {'q': '¿Qué entregamos al final?', 'a': 'Un informe ejecutivo y uno técnico con hallazgos, severidad, evidencia y un plan de remediación priorizado, además de re-testing de las correcciones.'}
        ]
    },
    'seismic-monitoring': {
        'name': 'Monitoreo Sísmico',
        'slug': 'seismic-monitoring',
        'icon': 'activity',
        'subtitle': 'Estaciones sísmicas en tiempo real',
        'description': 'Red de estaciones sísmicas con datos en tiempo real para alertar, analizar y visualizar actividad telúrica.',
        'overview': 'Construimos redes de estaciones sísmicas que capturan, transmiten y visualizan datos en tiempo real. Diseñamos el hardware, el firmware y la plataforma web para que equipos de protección civil, universidades y empresas reciban alertas tempranas y analicen el comportamiento sísmico desde un solo dashboard.',
        'features': [
            'Ingesta de datos desde estaciones y sensores (Raspberry Pi, acelerómetros)',
            'Visualización en tiempo real con series temporales y mapas geoespaciales',
            'Alertas automáticas por umbrales de magnitud e intensidad',
            'Almacenamiento de historial y análisis de eventos',
            'API de datos abierta para integraciones externas',
            'Dashboard con acceso multiusuario y roles'
        ],
        'benefits': [
            {'icon': 'zap', 'title': 'Alertas tempranas', 'text': 'Notificaciones automáticas que reducen tiempos de reacción ante eventos.'},
            {'icon': 'chart-bar', 'title': 'Decisiones con datos', 'text': 'Historial y análisis que respaldan estudios e informes técnicos.'},
            {'icon': 'globe', 'title': 'Acceso remoto', 'text': 'Monitorea todas tus estaciones desde cualquier lugar, en tiempo real.'},
            {'icon': 'database', 'title': 'Cero pérdida de datos', 'text': 'Arquitectura tolerante a fallos con almacenamiento redundante.'}
        ],
        'tech': ['Python', 'Node.js', 'InfluxDB', 'MQTT', 'Grafana', 'WebSockets'],
        'faq': [
            {'q': '¿Qué hardware necesito para una estación sísmica?', 'a': 'Trabajamos con sensores comerciales (acelerómetros, geófonos) y placas como Raspberry Pi o ESP32; nosotros diseñamos la integración y el firmware.'},
            {'q': '¿Puedo integrar estaciones que ya tengo?', 'a': 'Sí. Si tus estaciones ya generan datos (JSON, MQTT, CSV), los integramos a la plataforma sin reemplazar el hardware.'},
            {'q': '¿Las alertas llegan por WhatsApp o correo?', 'a': 'Configuramos los canales que necesites: WhatsApp, correo, SMS, webhooks o aplicación móvil.'}
        ]
    },
    'sports-results': {
        'name': 'Resultados Deportivos',
        'slug': 'sports-results',
        'icon': 'trophy',
        'subtitle': 'Plataforma live score',
        'description': 'Plataforma live score con resultados en tiempo real, estadísticas y notificaciones para ligas y torneos.',
        'overview': 'Desarrollamos plataformas de resultados deportivos en tiempo real: marcadores en vivo, estadísticas por partido, tablas de posiciones y notificaciones push. Diseñadas para ligas locales, torneos escolares y medios deportivos que quieren mantener a su audiencia informada al segundo.',
        'features': [
            'Marcadores en vivo con actualización en tiempo real',
            'Estadísticas por equipo, jugador y temporada',
            'Notificaciones push de goles y resultados',
            'Historial de partidos y tablas de posiciones',
            'API para integración con apps y sitios existentes',
            'Panel de administración para gestionar torneos'
        ],
        'benefits': [
            {'icon': 'users', 'title': 'Más interacción', 'text': 'Mantén a tu audiencia enganchada durante todo el partido.'},
            {'icon': 'trending-up', 'title': 'Nuevos ingresos', 'text': 'Espacios publicitarios y planes premium dentro de la plataforma.'},
            {'icon': 'zap', 'title': 'Tiempo real real', 'text': 'Latencia de segundos gracias a WebSockets y caché distribuida.'},
            {'icon': 'smartphone', 'title': 'Multiplataforma', 'text': 'Web, iOS y Android desde una sola base de código.'}
        ],
        'tech': ['WebSockets', 'Redis', 'Node.js', 'Flutter', 'Firebase', 'PostgreSQL'],
        'faq': [
            {'q': '¿De dónde salen los datos de los partidos?', 'a': 'De tus propios operadores (panel de administración) o de APIs externas de datos deportivos; los integramos y normalizamos.'},
            {'q': '¿Cuántos usuarios simultáneos soporta?', 'a': 'La arquitectura escala horizontalmente; para ligas locales manejamos miles de usuarios simultáneos sin problema.'},
            {'q': '¿Puedo tener una app móvil propia?', 'a': 'Sí. Generamos apps para iOS y Android con tu marca, disponibles en las tiendas.'}
        ]
    },
    'sales-analytics': {
        'name': 'Análisis de Ventas',
        'slug': 'sales-analytics',
        'icon': 'chart-bar',
        'subtitle': 'Dashboards y métricas',
        'description': 'Dashboards y métricas que transforman tus datos de ventas en decisiones accionables.',
        'overview': 'Convertimos los datos de tus ventas en dashboards claros y en tiempo real: ingresos, productos más vendidos, canales, regiones y pronósticos. Integramos tus fuentes (POS, ERP, e-commerce, hojas de cálculo) y automatizamos los reportes que hoy consumes horas en preparar.',
        'features': [
            'Dashboards ejecutivos con KPIs de ventas',
            'Monitoreo de métricas en tiempo real',
            'Segmentación por producto, canal, vendedor y región',
            'Pronósticos de ventas con modelos estadísticos',
            'Integración con POS, ERP y plataformas de e-commerce',
            'Exportación y reportes programados'
        ],
        'benefits': [
            {'icon': 'brain', 'title': 'Decisiones con datos', 'text': 'Deja de decidir por intuición: visualiza qué funciona y qué no.'},
            {'icon': 'trending-up', 'title': 'Oportunidades visibles', 'text': 'Detecta tendencias, estacionalidad y productos de bajo desempeño.'},
            {'icon': 'clock', 'title': 'Ahorro de tiempo', 'text': 'Reportes automáticos que se generan solos, sin intervención manual.'},
            {'icon': 'monitor', 'title': 'Claridad visual', 'text': 'Dashboards intuitivos que todo tu equipo entiende de un vistazo.'}
        ],
        'tech': ['Power BI', 'Tableau', 'D3.js', 'Looker Studio', 'PostgreSQL', 'Python'],
        'faq': [
            {'q': '¿Con qué fuentes de datos se conecta?', 'a': 'Con casi cualquier fuente: Excel, Google Sheets, POS, ERP, bases de datos y APIs. Centralizamos todo en un solo lugar.'},
            {'q': '¿Los dashboards se actualizan solos?', 'a': 'Sí. La actualización es automática en tiempo real o por lotes según tu necesidad.'},
            {'q': '¿Necesito un equipo de datos para usarlo?', 'a': 'No. Entregamos dashboards listos para usar y capacitamos a tu equipo en su operación.'}
        ]
    },
    'radio-streaming': {
        'name': 'Radio Streaming',
        'slug': 'radio-streaming',
        'icon': 'radio',
        'subtitle': 'Infraestructura de audio',
        'description': 'Infraestructura de audio para transmisión en vivo y bajo demanda con alta disponibilidad.',
        'overview': 'Montamos la infraestructura completa de streaming para tu emisora: servidores de audio, codificación, transmisión en vivo, podcasts y estadísticas de audiencia. Entregamos web player, apps móviles y paneles de control para que tu señal llegue al mundo entero sin caídas.',
        'features': [
            'Transmisión en vivo con alta disponibilidad',
            'Reproducción bajo demanda (podcasts y programas)',
            'Web player personalizable con la marca de la emisora',
            'Estadísticas de oyentes en tiempo real',
            'Grabación y publicación automática de podcasts',
            'Apps móviles para iOS y Android'
        ],
        'benefits': [
            {'icon': 'globe', 'title': 'Alcance global', 'text': 'Transmite para cualquier audiencia del mundo, sin límites geográficos.'},
            {'icon': 'trending-up', 'title': 'Monetización', 'text': 'Espacios publicitarios, suscripciones y reportes de audiencia para tus clientes.'},
            {'icon': 'zap', 'title': 'Estabilidad', 'text': 'Redundancia de servidores para evitar cortes de señal.'},
            {'icon': 'users', 'title': 'Audiencia medida', 'text': 'Conoce a tus oyentes: dónde están, cuándo escuchan y qué consumen.'}
        ],
        'tech': ['Icecast', 'Liquidsoap', 'HLS', 'FFmpeg', 'WebRTC', 'React'],
        'faq': [
            {'q': '¿Puedo transmitir con mi equipo actual?', 'a': 'Sí. Nos integramos a tus consolas, micrófonos y software existentes; no necesitas cambiar tu estudio.'},
            {'q': '¿Cuántos oyentes simultáneos soporta?', 'a': 'La infraestructura escala según tu audiencia; desde decenas hasta decenas de miles de oyentes.'},
            {'q': '¿Incluye la app móvil?', 'a': 'Sí, desarrollamos apps para iOS y Android con tu marca, publicadas en las tiendas.'}
        ]
    },
    'telemedicine': {
        'name': 'Sistema Telemedicina',
        'slug': 'telemedicine',
        'icon': 'heart-pulse',
        'subtitle': 'Consultas y expedientes',
        'description': 'Plataforma de consultas médicas virtuales con expedientes clínicos digitales seguros.',
        'overview': 'Construimos plataformas de telemedicina que conectan pacientes con médicos mediante videollamadas seguras, expedientes clínicos digitales, agendamiento de citas y recetas electrónicas. Diseñadas para clínicas, consultorios y empresas de salud que buscan ampliar su alcance sin sacrificar la seguridad de los datos.',
        'features': [
            'Videollamadas seguras médico-paciente',
            'Expedientes clínicos electrónicos (EHR)',
            'Agendamiento de citas en línea',
            'Recetas electrónicas y órdenes médicas',
            'Recordatorios automáticos de citas',
            'Roles y permisos para médicos, pacientes y administradores'
        ],
        'benefits': [
            {'icon': 'globe', 'title': 'Acceso remoto', 'text': 'Atiende pacientes en cualquier lugar, ampliando tu cobertura.'},
            {'icon': 'folder', 'title': 'Continuidad del cuidado', 'text': 'Historial clínico completo y accesible en cada consulta.'},
            {'icon': 'clock', 'title': 'Eficiencia clínica', 'text': 'Menos papeleo y más tiempo para la atención del paciente.'},
            {'icon': 'shield', 'title': 'Seguridad de datos', 'text': 'Cifrado y control de acceso para proteger la información médica.'}
        ],
        'tech': ['WebRTC', 'Node.js', 'PostgreSQL', 'AES-256', 'React Native', 'Docker'],
        'faq': [
            {'q': '¿Es segura la información médica?', 'a': 'Sí. Aplicamos cifrado en tránsito y en reposo, control de acceso por roles y registros de auditoría, alineados a normativas de salud.'},
            {'q': '¿Se integra con mi sistema actual?', 'a': 'Sí. Integramos el sistema con tu EHR, agenda y pasarelas de pago existentes.'},
            {'q': '¿Los pacientes necesitan instalar algo?', 'a': 'No. La consulta se realiza desde el navegador; la app móvil es opcional y gratuita para el paciente.'}
        ]
    },
    'ticketing': {
        'name': 'Reserva y Boletos',
        'slug': 'ticketing',
        'icon': 'ticket',
        'subtitle': 'Ticketing avanzado',
        'description': 'Plataforma de ticketing avanzado para eventos, transporte y espectáculos.',
        'overview': 'Desarrollamos plataformas de venta de boletos con mapa de asientos, códigos QR validables, pasarelas de pago y control de aforo. Desde conciertos y teatro hasta transporte y parques de atracciones: vendemos tus boletos en línea y controlamos el acceso desde un panel central.',
        'features': [
            'Venta de boletos en línea con múltiples pasarelas de pago',
            'Códigos QR dinámicos para validación de acceso',
            'Mapa de asientos interactivo con selección visual',
            'Control de aforo y tipos de entrada',
            'Panel de administración con reportes de ventas',
            'Integración con puntos de venta físicos'
        ],
        'benefits': [
            {'icon': 'zap', 'title': 'Menos filas', 'text': 'Tus asistentes compran en segundos y entran escaneando su código.'},
            {'icon': 'shield', 'title': 'Control de fraude', 'text': 'Códigos dinámicos que evitan la reventa y falsificación.'},
            {'icon': 'chart-bar', 'title': 'Reportes claros', 'text': 'Ventas, ocupación y recaudo en tiempo real.'},
            {'icon': 'smartphone', 'title': 'Experiencia móvil', 'text': 'Compra desde cualquier dispositivo, sin descargar apps.'}
        ],
        'tech': ['Node.js', 'Stripe', 'PostgreSQL', 'React', 'QR', 'Redis'],
        'faq': [
            {'q': '¿Qué pasarelas de pago usa?', 'a': 'Stripe, PayPal, Wompi y las principales pasarelas locales; también soporta pagos en efectivo y puntos físicos.'},
            {'q': '¿Cómo valido los boletos en el evento?', 'a': 'Con la app de validación escaneas el código QR desde el celular o con lector láser; la validación es instantánea y segura.'},
            {'q': '¿Puedo vender en taquilla también?', 'a': 'Sí, integramos el punto de venta físico con la misma plataforma y el mismo inventario.'}
        ]
    },
    'odoo-erp': {
        'name': 'Sistema Odoo CRM',
        'slug': 'odoo-erp',
        'icon': 'layers',
        'subtitle': 'Implementación ERP',
        'description': 'Implementación y personalización de Odoo para integrar CRM, ventas, inventario y contabilidad.',
        'overview': 'Implementamos Odoo para unificar la operación de tu empresa: CRM, ventas, compras, inventario, facturación y contabilidad en un solo sistema. Configuramos los módulos, migramos tus datos, personalizamos lo necesario y capacitamos a tu equipo para que la transición sea sin fricción.',
        'features': [
            'Implementación modular de Odoo (CRM, ventas, inventario, contabilidad)',
            'Personalización de módulos y flujos de trabajo',
            'Migración de datos desde sistemas legados y Excel',
            'Integraciones con pasarelas de pago y plataformas externas',
            'Capacitación de tu equipo en operación diaria',
            'Soporte y mantenimiento continuo'
        ],
        'benefits': [
            {'icon': 'layers', 'title': 'Un solo sistema', 'text': 'Todos tus procesos conectados, sin hojas sueltas ni doble digitación.'},
            {'icon': 'zap', 'title': 'Automatización', 'text': 'Flujos que se ejecutan solos: cotizaciones, órdenes y facturación.'},
            {'icon': 'trending-up', 'title': 'Escalable', 'text': 'Crece con tu empresa: añade módulos cuando los necesites.'},
            {'icon': 'receipt', 'title': 'Menos costos', 'text': 'Licenciamiento abierto y control total sobre tu sistema.'}
        ],
        'tech': ['Odoo', 'Python', 'PostgreSQL', 'XML-RPC', 'Docker', 'JavaScript'],
        'faq': [
            {'q': '¿Cuánto tarda una implementación?', 'a': 'Una implementación de CRM + ventas típica toma de 4 a 8 semanas, incluyendo migración y capacitación.'},
            {'q': '¿Migran mis datos actuales?', 'a': 'Sí. Migramos clientes, productos, historial de ventas y saldos desde Excel, sistemas legados u otras herramientas.'},
            {'q': '¿Necesito comprar la licencia de Odoo?', 'a': 'No necesariamente. Odoo Community es gratuito y cubre la mayoría de casos; evaluamos contigo si la versión Enterprise aporta valor.'}
        ]
    },
    'wordpress-plugins': {
        'name': 'Plugins WordPress',
        'slug': 'wordpress-plugins',
        'icon': 'puzzle',
        'subtitle': 'Desarrollo a medida',
        'description': 'Desarrollo de plugins y temas WordPress a medida para llevar tu sitio al siguiente nivel.',
        'overview': 'Creamos plugins y temas WordPress totalmente personalizados: funcionalidades únicas, integraciones con APIs externas, optimización de rendimiento y seguridad. Si tu negocio necesita algo que ningún plugin de catálogo hace, lo construimos a tu medida.',
        'features': [
            'Plugins WordPress a medida',
            'Temas personalizados y adaptación de diseños',
            'Integración con APIs y servicios externos',
            'Optimización de rendimiento y Core Web Vitals',
            'Hardening de seguridad y buenas prácticas',
            'Mantenimiento y actualizaciones continuas'
        ],
        'benefits': [
            {'icon': 'puzzle', 'title': 'Funcionalidad única', 'text': 'Tu sitio hace exactamente lo que tu negocio necesita, sin parches.'},
            {'icon': 'trending-up', 'title': 'Mejor SEO', 'text': 'Código limpio y rendimiento optimizado que los buscadores premian.'},
            {'icon': 'zap', 'title': 'Rendimiento', 'text': 'Plugins ligeros que no frenan la velocidad de tu página.'},
            {'icon': 'shield', 'title': 'Seguridad', 'text': 'Desarrollo siguiendo las mejores prácticas de WordPress.'}
        ],
        'tech': ['PHP', 'WordPress', 'WooCommerce', 'REST API', 'MySQL', 'JavaScript'],
        'faq': [
            {'q': '¿Pueden integrar mi sitio con otro sistema?', 'a': 'Sí. Conectamos WordPress con CRMs, pasarelas de pago, ERPs y cualquier API mediante plugins personalizados.'},
            {'q': '¿Mantienen mis plugins actualizados?', 'a': 'Ofrecemos planes de mantenimiento que incluyen actualizaciones, respaldos y monitoreo de seguridad.'},
            {'q': '¿Trabajan con WooCommerce?', 'a': 'Sí, desarrollamos sobre WooCommerce: plugins de envío, pasarelas, cupones avanzados y reportes personalizados.'}
        ]
    },
    'iot': {
        'name': 'IoT Internet de las Cosas',
        'slug': 'iot',
        'icon': 'chip',
        'subtitle': 'Hardware y sensores',
        'description': 'Hardware y sensores conectados con software para monitorear y automatizar en tiempo real.',
        'overview': 'Diseñamos soluciones IoT de principio a fin: seleccionamos o diseñamos el hardware, escribimos el firmware, implementamos la conectividad y construimos la plataforma web donde visualizas y controlas todo en tiempo real. Desde agricultura y logística hasta industria y hogar inteligente.',
        'features': [
            'Diseño y selección de hardware y sensores',
            'Desarrollo de firmware para microcontroladores',
            'Conectividad MQTT, LoRaWAN y redes celulares',
            'Plataforma IoT con dashboards en tiempo real',
            'Alertas y automatización basadas en reglas',
            'Integración con sistemas y APIs existentes'
        ],
        'benefits': [
            {'icon': 'monitor', 'title': 'Monitoreo 24/7', 'text': 'Visibilidad total de tus equipos y sensores desde cualquier lugar.'},
            {'icon': 'zap', 'title': 'Automatización', 'text': 'Reglas que activan acciones automáticas ante eventos.'},
            {'icon': 'trending-up', 'title': 'Ahorro real', 'text': 'Detecta fallas y desperdicios antes de que se conviertan en costos.'},
            {'icon': 'cpu', 'title': 'Escalable', 'text': 'Añade cientos o miles de dispositivos sin cambiar la arquitectura.'}
        ],
        'tech': ['ESP32', 'Raspberry Pi', 'MQTT', 'Node-RED', 'AWS IoT', 'C++'],
        'faq': [
            {'q': '¿Ya tengo sensores, pueden conectarlos?', 'a': 'Sí. Si tus sensores se comunican por protocolos comunes (MQTT, Modbus, HTTP), los integramos a la plataforma.'},
            {'q': '¿Qué pasa si pierdo conectividad?', 'a': 'Los dispositivos almacenan datos localmente y los sincronizan al reconectarse; no pierdes información.'},
            {'q': '¿El hardware lo proveen ustedes?', 'a': 'Podemos diseñar y ensamblar el hardware o trabajar con el tuyo; te asesoramos en la opción más rentable.'}
        ]
    },
    'medicine-prices': {
        'name': 'Precios Medicamentos',
        'slug': 'medicine-prices',
        'icon': 'pill',
        'subtitle': 'Comparador farmacéutico',
        'description': 'Comparador farmacéutico con precios actualizados de medicamentos en múltiples farmacias.',
        'overview': 'Construimos comparadores de precios de medicamentos que ayudan a los usuarios a encontrar dónde comprar más barato. Recopilamos precios de múltiples farmacias, los normalizamos y los mostramos en una interfaz clara con búsqueda por principio activo, marca o laboratorio.',
        'features': [
            'Base de datos de medicamentos y precios actualizada',
            'Búsqueda por nombre, principio activo y laboratorio',
            'Comparación de precios entre farmacias y zonas',
            'Alertas de cambio de precio para los usuarios',
            'Panel para que farmacias administren sus precios',
            'API para integrar el comparador en otros sitios'
        ],
        'benefits': [
            {'icon': 'trending-up', 'title': 'Ahorro para usuarios', 'text': 'Encuentran el mejor precio en segundos y ahorran cada mes.'},
            {'icon': 'chart-bar', 'title': 'Datos de mercado', 'text': 'Farmacias acceden a estadísticas de precios y competencia.'},
            {'icon': 'users', 'title': 'Tráfico y confianza', 'text': 'Una herramienta útil que atrae y retiene usuarios.'},
            {'icon': 'refresh', 'title': 'Siempre actualizado', 'text': 'Recolección y validación de precios automatizada.'}
        ],
        'tech': ['Web scraping', 'Node.js', 'PostgreSQL', 'React', 'Redis', 'Docker'],
        'faq': [
            {'q': '¿Cómo actualizan los precios?', 'a': 'Con procesos automatizados de recolección desde fuentes públicas y con el panel de las farmacias participantes.'},
            {'q': '¿Los precios son confiables?', 'a': 'Sí, aplicamos validación y marcas de tiempo; siempre mostramos la fecha de la última actualización.'},
            {'q': '¿Puedo integrarlo a mi web de salud?', 'a': 'Sí, ofrecemos una API pública para incrustar el comparador en otros portales.'}
        ]
    },
    'openclaw': {
        'name': 'OpenClaw',
        'slug': 'openclaw',
        'icon': 'gamepad',
        'subtitle': 'Control de hardware arcade',
        'description': 'Software de control para hardware arcade: máquinas, juegos y gestión de fichas.',
        'overview': 'Desarrollamos el software que controla el hardware arcade: gestión de máquinas, créditos y fichas, selección de juegos, dashboards de ingresos y mantenimiento remoto. Ideal para operadores de salas de juegos que quieren medir cada máquina y optimizar su rentabilidad.',
        'features': [
            'Control y monitoreo de máquinas arcade',
            'Gestión de créditos, fichas y tarjetas',
            'Dashboard de ingresos por máquina y por día',
            'Selección y actualización de juegos',
            'Diagnóstico y mantenimiento remoto',
            'Reportes de uso y rentabilidad'
        ],
        'benefits': [
            {'icon': 'chart-bar', 'title': 'Ingresos medibles', 'text': 'Sabes exactamente cuánto genera cada máquina cada día.'},
            {'icon': 'zap', 'title': 'Menos tiempo muerto', 'text': 'Detección remota de fallas y mantenimiento proactivo.'},
            {'icon': 'monitor', 'title': 'Gestión central', 'text': 'Controla todas tus sucursales desde un solo panel.'},
            {'icon': 'trending-up', 'title': 'Rentabilidad', 'text': 'Identifica juegos y máquinas de alto desempeño para optimizar tu operación.'}
        ],
        'tech': ['C++', 'Raspberry Pi', 'Python', 'MQTT', 'Node.js', 'SQLite'],
        'faq': [
            {'q': '¿Qué hardware arcade controla?', 'a': 'Trabajamos con placas basadas en Raspberry Pi, PC embebidos y controladores JAMMA; integramos el control sobre tu gabinete.'},
            {'q': '¿Los clientes pagan con tarjeta o fichas?', 'a': 'Soportamos fichas físicas, tarjetas recargables y códigos QR de pago, según el modelo de tu sala.'},
            {'q': '¿Puedo monitorear varias sucursales?', 'a': 'Sí, el panel central agrega todas tus máquinas y sucursales en tiempo real.'}
        ]
    },
    'barbershop-booking': {
        'name': 'Reserva Barbería',
        'slug': 'barbershop-booking',
        'icon': 'scissors',
        'subtitle': 'Sistema para peluquerías',
        'description': 'Sistema de reservas para barberías y peluquerías con recordatorios automáticos.',
        'overview': 'Implementamos sistemas de reservas para barberías y peluquerías: agenda en línea, elección de barbero y servicio, recordatorios automáticos por WhatsApp y gestión de clientes. Tu equipo se enfoca en cortar el pelo, no en contestar llamadas ni cuadrar la agenda.',
        'features': [
            'Agenda en línea con disponibilidad en tiempo real',
            'Elección de barbero, servicio y horario por el cliente',
            'Recordatorios automáticos por WhatsApp y correo',
            'Pagos en línea y reserva con anticipo',
            'Base de datos de clientes e historial',
            'Reportes de ingresos, servicios y ocupación'
        ],
        'benefits': [
            {'icon': 'clock', 'title': 'Menos ausencias', 'text': 'Recordatorios automáticos que reducen las citas perdidas.'},
            {'icon': 'trending-up', 'title': 'Más reservas', 'text': 'Tus clientes reservan a cualquier hora, incluso cuando estás cerrado.'},
            {'icon': 'zap', 'title': 'Ahorro de tiempo', 'text': 'Adiós a las llamadas de agenda y a la doble reserva.'},
            {'icon': 'star', 'title': 'Imagen profesional', 'text': 'Tus clientes perciben un negocio moderno y organizado.'}
        ],
        'tech': ['Node.js', 'React Native', 'Firebase', 'WhatsApp API', 'Stripe'],
        'faq': [
            {'q': '¿Los clientes necesitan crear cuenta?', 'a': 'No es obligatorio; pueden reservar en segundos con su nombre y celular. La cuenta es opcional.'},
            {'q': '¿Se conecta con el WhatsApp de la barbería?', 'a': 'Sí, los recordatorios y confirmaciones se envían automáticamente por WhatsApp desde tu número.'},
            {'q': '¿Funciona en el celular del cliente?', 'a': 'Sí, es una web app responsive: el cliente reserva desde el navegador sin instalar nada.'}
        ]
    },
    'facial-cleaning': {
        'name': 'Limpieza Facial',
        'slug': 'facial-cleaning',
        'icon': 'sparkles',
        'subtitle': 'Sistema para spas y clínicas',
        'description': 'Sistema para spas y clínicas estéticas: citas, expedientes y tratamiento de clientes.',
        'overview': 'Desarrollamos sistemas para spas, centros estéticos y clínicas de limpieza facial: agendamiento de tratamientos, expedientes de pacientes, historial de procedimientos, control de productos y recordatorios. Una experiencia premium para tus clientes y control total para tu equipo.',
        'features': [
            'Agendamiento de tratamientos y servicios',
            'Expedientes digitales de pacientes',
            'Historial de tratamientos y fotos de evolución',
            'Control de productos y consumo por tratamiento',
            'Recordatorios automáticos de citas',
            'Reportes de ingresos, servicios y ocupación'
        ],
        'benefits': [
            {'icon': 'sparkles', 'title': 'Experiencia premium', 'text': 'Un proceso digital impecable que complementa tu servicio.'},
            {'icon': 'box', 'title': 'Control de inventario', 'text': 'Sabes qué productos se consumen y cuándo reponerlos.'},
            {'icon': 'users', 'title': 'Fidelización', 'text': 'Historial completo para recomendar tratamientos y retener clientes.'},
            {'icon': 'folder', 'title': 'Organización total', 'text': 'Toda la información de tus pacientes en un solo lugar.'}
        ],
        'tech': ['React', 'Node.js', 'PostgreSQL', 'Tailwind', 'Docker'],
        'faq': [
            {'q': '¿Guarda fotos del antes y después?', 'a': 'Sí, el expediente incluye galerías de fotos con control de acceso privado para el paciente.'},
            {'q': '¿Sirve para clínicas con varios especialistas?', 'a': 'Sí, cada especialista tiene su agenda y sus pacientes; el panel central administra todo.'},
            {'q': '¿El paciente puede ver su historial?', 'a': 'Sí, con un portal de paciente puede consultar sus tratamientos, citas y recomendaciones.'}
        ]
    },
    'lms-moodle': {
        'name': 'Plataformas LMS y Moodle',
        'slug': 'lms-moodle',
        'icon': 'graduation',
        'subtitle': 'Cursos para escuelas y empresas',
        'description': 'Plataformas de aprendizaje para escuelas y empresas con Moodle y desarrollos a medida.',
        'overview': 'Implementamos plataformas LMS para escuelas, universidades y empresas: cursos en línea, evaluaciones, certificaciones y seguimiento del progreso. Trabajamos con Moodle y con desarrollos a medida para que la experiencia de aprendizaje lleve tu marca.',
        'features': [
            'Implementación de Moodle y LMS a medida',
            'Cursos con multimedia, cuestionarios y tareas',
            'Evaluaciones y certificaciones automáticas',
            'Gamificación y badges de logro',
            'Roles de docente, estudiante y administrador',
            'Integración con SSO, videoconferencia y pagos'
        ],
        'benefits': [
            {'icon': 'graduation', 'title': 'Escalable', 'text': 'Capacita a cientos o miles de estudiantes sin límites de aula.'},
            {'icon': 'chart-bar', 'title': 'Seguimiento real', 'text': 'Mide avance, calificaciones y finalización de cada curso.'},
            {'icon': 'globe', 'title': 'Accesible', 'text': 'Tus estudiantes aprenden desde cualquier dispositivo y lugar.'},
            {'icon': 'puzzle', 'title': 'Con tu marca', 'text': 'Personalizamos la plataforma con la identidad de tu institución.'}
        ],
        'tech': ['Moodle', 'PHP', 'MySQL', 'SCORM', 'React', 'Docker'],
        'faq': [
            {'q': '¿Moodle o plataforma a medida?', 'a': 'Depende de tu necesidad: Moodle es ideal para la mayoría; si necesitas algo muy específico, lo desarrollamos a medida.'},
            {'q': '¿Puedo vender cursos en línea?', 'a': 'Sí, integramos pasarelas de pago, cupones y acceso por suscripción o curso individual.'},
            {'q': '¿Incluye certificados?', 'a': 'Sí, emitimos certificados automáticos al aprobar cada curso, con diseño personalizable.'}
        ]
    },
    'laundry-rentals': {
        'name': 'Alquiler Lavadoras',
        'slug': 'laundry-rentals',
        'icon': 'washer',
        'subtitle': 'Gestión de rentas',
        'description': 'Gestión de rentas de lavadoras: máquinas, pagos, contratos y mantenimiento.',
        'overview': 'Construimos plataformas para empresas que alquilan lavadoras y secadoras: gestión de máquinas por ubicación, contratos de alquiler, facturación automática recurrente, pagos en línea y control de mantenimiento. Tu flota de máquinas, controlada desde un solo panel.',
        'features': [
            'Gestión de máquinas y ubicaciones',
            'Contratos de alquiler con facturación automática',
            'Cobros recurrentes y pagos en línea',
            'Estado de mantenimiento y alertas de servicio',
            'Panel para clientes con su facturación',
            'Reportes de ingresos, morosidad y uso'
        ],
        'benefits': [
            {'icon': 'repeat', 'title': 'Ingresos recurrentes', 'text': 'Facturación automática que cobra a tiempo, todos los meses.'},
            {'icon': 'trending-up', 'title': 'Control total', 'text': 'Sabes qué máquina, en qué ubicación, genera qué ingreso.'},
            {'icon': 'zap', 'title': 'Automatización', 'text': 'Contratos, cobros y recordatorios que se ejecutan solos.'},
            {'icon': 'users', 'title': 'Mejor soporte', 'text': 'Tus clientes consultan facturas y reportan novedades en línea.'}
        ],
        'tech': ['React', 'Node.js', 'PostgreSQL', 'Stripe', 'Docker'],
        'faq': [
            {'q': '¿Cómo se facturan los alquileres?', 'a': 'Generamos facturas automáticas con frecuencia mensual o personalizada, con cobro recurrente por tarjeta o PSE.'},
            {'q': '¿Pueden mis clientes ver sus facturas?', 'a': 'Sí, cada cliente tiene un portal con sus facturas, pagos y estado de cuenta.'},
            {'q': '¿Se integra con mi contabilidad?', 'a': 'Sí, exportamos la facturación a tu contador o la integramos con tu sistema contable.'}
        ]
    }
}

SERVICES_ES = {
    'data-engineering': {
        'overview': 'Diseñamos la columna vertebral de tu estrategia de datos: pipelines robustos y escalables que llevan información desde cualquier fuente hasta donde tu negocio la necesita. Procesamiento en tiempo real o por lotes, gobernanza y calidad de datos como parte del diseño, no como una ocurrencia tardía.',
        'benefits': [
            {'icon': 'database', 'title': 'Pipelines confiables', 'text': 'Flujos de datos que no se caen y se recuperan solos.'},
            {'icon': 'zap', 'title': 'Tiempo real o por lotes', 'text': 'La velocidad que tu negocio necesita, ni más ni menos.'},
            {'icon': 'cloud', 'title': 'En la nube', 'text': 'Arquitecturas modernas en AWS, GCP y Azure.'},
            {'icon': 'shield', 'title': 'Calidad y gobernanza', 'text': 'Datos limpios, trazables y con dueño definido.'}
        ],
        'tech': ['Apache Spark', 'Kafka', 'Airflow', 'dbt', 'BigQuery', 'Snowflake'],
        'faq': [
            {'q': '¿Qué fuentes pueden integrar?', 'a': 'Bases de datos, APIs, archivos, SaaS, logs y streaming: prácticamente cualquier fuente con datos.'},
            {'q': '¿Cuánto tarda un pipeline de datos?', 'a': 'Un pipeline típico se entrega en 2 a 4 semanas, incluyendo monitoreo y documentación.'},
            {'q': '¿Migran mi infraestructura actual a la nube?', 'a': 'Sí, planificamos y ejecutamos la migración sin interrumpir tu operación.'}
        ]
    },
    'data-extraction-etl': {
        'overview': 'Extraemos datos de cualquier fuente y los transformamos en formatos limpios y estructurados, listos para analizar. Integraciones multi-fuente, ingestión de APIs y webhooks, y migración de sistemas heredados con estrategias que respetan el volumen y la criticidad de tu información.',
        'benefits': [
            {'icon': 'filter', 'title': 'Multi-fuente', 'text': 'Conectamos bases de datos, APIs, archivos y SaaS.'},
            {'icon': 'refresh', 'title': 'Automatizado', 'text': 'Procesos programados que corren solos y se monitorean.'},
            {'icon': 'box', 'title': 'Datos limpios', 'text': 'Normalización y limpieza que eliminan ruido y duplicados.'},
            {'icon': 'trending-up', 'title': 'Listo para analizar', 'text': 'Tu equipo recibe datos directamente utilizables.'}
        ],
        'tech': ['Python', 'Airbyte', 'dbt', 'Apache Airflow', 'PostgreSQL', 'REST APIs'],
        'faq': [
            {'q': '¿Pueden extraer de sistemas que no tienen API?', 'a': 'Sí, usamos técnicas como lectura de archivos, scraping controlado y conectores a bases de datos.'},
            {'q': '¿Qué pasa durante una migración?', 'a': 'Ejecutamos migraciones incrementales con validación continua y plan de rollback.'},
            {'q': '¿Qué entregables incluye?', 'a': 'Documentación, monitoreo, validaciones y capacitación de tu equipo.'}
        ]
    },
    'data-visualization': {
        'overview': 'Convertimos datos complejos en visuales claros que empoderan decisiones rápidas. Dashboards interactivos, reportes ejecutivos y monitoreo de KPIs en tiempo real, construidos con las mejores herramientas del mercado o con componentes completamente personalizados.',
        'benefits': [
            {'icon': 'monitor', 'title': 'Dashboards interactivos', 'text': 'Explora, filtra y profundiza sin depender de un analista.'},
            {'icon': 'zap', 'title': 'KPIs en tiempo real', 'text': 'Tu operación monitoreada al segundo, no al cierre de mes.'},
            {'icon': 'puzzle', 'title': 'A tu medida', 'text': 'Visualizaciones únicas cuando la herramienta estándar no alcanza.'},
            {'icon': 'users', 'title': 'Para tu audiencia', 'text': 'Reportes ejecutivos que tu junta directiva entiende.'}
        ],
        'tech': ['Tableau', 'Power BI', 'D3.js', 'Looker Studio', 'ECharts', 'Vue.js'],
        'faq': [
            {'q': '¿Qué herramienta me recomiendan?', 'a': 'Evaluamos tu caso: Power BI o Tableau para la mayoría, D3.js o ECharts para visuales a medida.'},
            {'q': '¿Los dashboards son móviles?', 'a': 'Sí, los optimizamos para verse bien en celular y tablet.'},
            {'q': '¿Pueden conectarse a varias fuentes?', 'a': 'Sí, un dashboard puede combinar bases de datos, APIs y hojas de cálculo en una sola vista.'}
        ]
    },
    'data-mining-management': {
        'overview': 'Descubrimos los insights ocultos en tus datos. Aplicamos minería de datos para detectar patrones y anomalías, segmentar clientes y descubrir reglas de asociación; y gestionamos la calidad con catálogos de datos y linaje que te dan visibilidad y control total.',
        'benefits': [
            {'icon': 'brain', 'title': 'Insights ocultos', 'text': 'Patrones y anomalías que no se ven a simple vista.'},
            {'icon': 'users', 'title': 'Segmentación', 'text': 'Conoce y agrupa a tus clientes para campañas efectivas.'},
            {'icon': 'folder', 'title': 'Catálogo de datos', 'text': 'Sabes qué datos tienes, dónde están y quién los usa.'},
            {'icon': 'shield', 'title': 'Gobernanza', 'text': 'Control sobre la calidad y el uso de tu información.'}
        ],
        'tech': ['Python', 'scikit-learn', 'pandas', 'SQL', 'Atlas', 'dbt'],
        'faq': [
            {'q': '¿Qué es el linaje de datos?', 'a': 'Es el rastreo del recorrido de cada dato: de dónde viene, cómo se transforma y dónde se usa.'},
            {'q': '¿Pueden detectar fraude con esto?', 'a': 'Sí, la detección de anomalías es clave para identificar comportamientos inusuales.'},
            {'q': '¿Necesito muchos datos para empezar?', 'a': 'Trabajamos con los datos que tienes; la escala crece contigo.'}
        ]
    },
    'desktop-software': {
        'overview': 'Construimos aplicaciones de escritorio nativas con rendimiento y seguridad de nivel empresarial, para Windows, macOS y Linux. Aplicaciones offline-first, integraciones con ERP y CRM, y sistemas de actualización automática que mantienen a tu equipo siempre en la última versión.',
        'benefits': [
            {'icon': 'monitor', 'title': 'Multiplataforma', 'text': 'Una sola app para Windows, macOS y Linux.'},
            {'icon': 'zap', 'title': 'Rendimiento nativo', 'text': 'Velocidad y fluidez que las apps web no igualan.'},
            {'icon': 'box', 'title': 'Offline-first', 'text': 'Trabaja sin conexión y sincroniza cuando vuelvas.'},
            {'icon': 'refresh', 'title': 'Actualizaciones automáticas', 'text': 'Tu equipo siempre con la última versión.'}
        ],
        'tech': ['Electron', 'Tauri', 'C#', 'Java', 'Python', 'SQLite'],
        'faq': [
            {'q': '¿Electron o Tauri?', 'a': 'Depende del caso: Tauri es más ligero, Electron tiene mayor ecosistema. Evaluamos contigo cuál conviene.'},
            {'q': '¿Funciona sin internet?', 'a': 'Sí, diseñamos arquitecturas offline-first que sincronizan al reconectarse.'},
            {'q': '¿Se integra con mi ERP?', 'a': 'Sí, integramos con SAP, Odoo, Microsoft Dynamics y sistemas propios.'}
        ]
    },
    'machine-learning': {
        'overview': 'Desplegamos sistemas inteligentes que automatizan decisiones complejas. Analítica predictiva, modelos de NLP y visión por computadora, fine-tuning de LLMs con RAG y MLOps completo para que tus modelos pasen del laboratorio a producción y se mantengan saludables.',
        'benefits': [
            {'icon': 'brain', 'title': 'Predicción', 'text': 'Pronósticos de demanda, riesgo y comportamiento.'},
            {'icon': 'zap', 'title': 'Automatización', 'text': 'Decisiones repetitivas resueltas por modelos, sin errores humanos.'},
            {'icon': 'monitor', 'title': 'MLOps real', 'text': 'Monitoreo, versionado y reentrenamiento continuo.'},
            {'icon': 'trending-up', 'title': 'Ventaja competitiva', 'text': 'Capacidades que tu competencia aún no tiene.'}
        ],
        'tech': ['Python', 'PyTorch', 'scikit-learn', 'LangChain', 'Hugging Face', 'Vertex AI'],
        'faq': [
            {'q': '¿Qué problemas resuelve bien el ML?', 'a': 'Predicción, clasificación, detección de anomalías, procesamiento de lenguaje y visión: si tienes datos históricos, probablemente hay un caso.'},
            {'q': '¿Cuántos datos necesito?', 'a': 'Depende del problema; evaluamos tu caso y te decimos si hay suficiente señal en tus datos.'},
            {'q': '¿Los modelos se actualizan solos?', 'a': 'Con MLOps sí: monitoreamos su desempeño y los reentrenamos automáticamente.'}
        ]
    },
    'mobile-development': {
        'overview': 'Creamos aplicaciones móviles pulidas y de alto rendimiento para iOS y Android. Desarrollo nativo con Swift y Kotlin, multiplataforma con React Native y Flutter, PWAs con capacidad offline, notificaciones push y optimización completa para las tiendas de aplicaciones.',
        'benefits': [
            {'icon': 'smartphone', 'title': 'Nativo o multiplataforma', 'text': 'La tecnología correcta según tu presupuesto y objetivo.'},
            {'icon': 'zap', 'title': 'Alto rendimiento', 'text': 'Apps rápidas y fluidas que los usuarios aman usar.'},
            {'icon': 'trending-up', 'title': 'Monetización', 'text': 'Compras in-app, suscripciones y anuncios integrados.'},
            {'icon': 'star', 'title': 'Lista para publicar', 'text': 'Optimización de ASO para App Store y Play Store.'}
        ],
        'tech': ['Swift', 'Kotlin', 'React Native', 'Flutter', 'Firebase', 'GraphQL'],
        'faq': [
            {'q': '¿Cuánto cuesta una app móvil?', 'a': 'Depende del alcance; te presentamos una propuesta clara con fases y costos después de una consulta.'},
            {'q': '¿Cuánto tarda el desarrollo?', 'a': 'Un MVP típico se entrega en 6 a 12 semanas; apps complejas en 3 a 6 meses.'},
            {'q': '¿La publican en las tiendas?', 'a': 'Sí, gestionamos la publicación en App Store y Play Store, incluyendo cuentas y revisión.'}
        ]
    },
    'on-demand-systems': {
        'overview': '¿Necesitas una solución personalizada, rápido? Arquitectamos y entregamos sistemas adaptados a tus requisitos y plazos: prototipado rápido y MVPs, arquitecturas de microservicios y serverless, plataformas SaaS, diseño API-first y DevOps completo con CI/CD.',
        'benefits': [
            {'icon': 'rocket', 'title': 'Velocidad', 'text': 'Prototipos en días y MVPs en semanas, sin perder calidad.'},
            {'icon': 'zap', 'title': 'Moderno', 'text': 'Microservicios y serverless que escalan con tu demanda.'},
            {'icon': 'repeat', 'title': 'SaaS', 'text': 'Construimos tu producto como servicio, multi-tenant.'},
            {'icon': 'monitor', 'title': 'DevOps incluido', 'text': 'CI/CD, monitoreo y despliegues automáticos desde el día uno.'}
        ],
        'tech': ['Node.js', 'AWS Lambda', 'Docker', 'Kubernetes', 'GraphQL', 'GitHub Actions'],
        'faq': [
            {'q': '¿Qué es un MVP?', 'a': 'Un producto mínimo viable: la versión más pequeña que resuelve el problema y valida el mercado.'},
            {'q': '¿Pueden mantener el sistema después?', 'a': 'Sí, ofrecemos soporte continuo y evoluciones con metodología ágil.'},
            {'q': '¿Trabajan con mi stack?', 'a': 'Nos adaptamos a tu tecnología o te recomendamos la más adecuada para el proyecto.'}
        ]
    },
    'web-development': {
        'overview': 'Diseñamos experiencias web de alto rendimiento: desde landing pages que convierten hasta plataformas empresariales complejas. Frontends con React, Next.js y Vue.js; backends con Laravel, Node.js y Django; e-commerce y marketplaces, optimización de Core Web Vitals e integraciones con CMS headless.',
        'benefits': [
            {'icon': 'zap', 'title': 'Rendimiento', 'text': 'Sitios rápidos que Google y tus usuarios premian.'},
            {'icon': 'trending-up', 'title': 'Conversión', 'text': 'Diseño y UX pensados para convertir visitas en clientes.'},
            {'icon': 'cart', 'title': 'E-commerce', 'text': 'Tiendas completas con pagos, envíos y catálogo.'},
            {'icon': 'monitor', 'title': 'Escalable', 'text': 'De landing page a plataforma empresarial sin reescribir.'}
        ],
        'tech': ['React', 'Next.js', 'Vue.js', 'Laravel', 'Node.js', 'Django'],
        'faq': [
            {'q': '¿Cuánto cuesta un sitio web?', 'a': 'Depende del alcance: una landing page profesional desde un monto accesible; te cotizamos sin compromiso en 48 horas.'},
            {'q': '¿Qué es un CMS headless?', 'a': 'Un sistema donde el contenido se administra por separado y se sirve a cualquier plataforma: web, móvil, kioscos.'},
            {'q': '¿Hacen mantenimiento?', 'a': 'Sí, ofrecemos planes de mantenimiento, monitoreo, seguridad y mejoras continuas.'}
        ]
    }
}

# ---------------------------------------------------------------------------
# Traducciones EN
# ---------------------------------------------------------------------------
PRODUCTS_EN = {
    'vulnerabilities': {
        'name': 'Vulnerabilities',
        'slug': 'vulnerabilities',
        'icon': 'shield-alert',
        'subtitle': 'Pen testing and audits',
        'description': 'Security audits and penetration testing to find and fix vulnerabilities before attackers do.',
        'overview': 'We identify weaknesses in your infrastructure, web and mobile apps before anyone exploits them. We run controlled penetration testing, vulnerability scanning and configuration audits, and deliver a prioritized remediation plan with evidence and actionable recommendations.',
        'features': [
            'Penetration testing for web apps, mobile apps and APIs',
            'Vulnerability scanning and correlation (CVE)',
            'Server and network configuration audits',
            'Analysis against OWASP Top 10 and industry standards',
            'Executive reports with a prioritized remediation plan',
            'Re-testing to validate the fixes applied'
        ],
        'benefits': [
            {'icon': 'shield', 'title': 'Prevent breaches', 'text': 'Find and fix flaws before they become costly incidents.'},
            {'icon': 'scale', 'title': 'Regulatory compliance', 'text': 'Audit documentation that supports certifications and regulations.'},
            {'icon': 'trending-up', 'title': 'Prioritized risk', 'text': 'Know exactly what to fix first based on real business impact.'},
            {'icon': 'users', 'title': 'Customer trust', 'text': 'Protect your users\u2019 data and strengthen your reputation.'}
        ],
        'tech': ['Nmap', 'Burp Suite', 'OWASP ZAP', 'Metasploit', 'Wireshark', 'Nikto'],
        'faq': [
            {'q': 'How long does a pen test take?', 'a': 'It depends on scope: a typical web app audit takes 1 to 3 weeks, including the report and validation of fixes.'},
            {'q': 'Is penetration testing safe?', 'a': 'Yes. We work with written scopes and rules of engagement, in controlled environments, without disrupting operations.'},
            {'q': 'What do we deliver at the end?', 'a': 'An executive and a technical report with findings, severity, evidence and a prioritized remediation plan, plus re-testing of fixes.'}
        ]
    },
    'seismic-monitoring': {
        'name': 'Seismic Monitoring',
        'slug': 'seismic-monitoring',
        'icon': 'activity',
        'subtitle': 'Real-time seismic stations',
        'description': 'A network of seismic stations streaming real-time data to alert, analyze and visualize seismic activity.',
        'overview': 'We build seismic monitoring networks that capture, transmit and visualize data in real time. We design the hardware, firmware and web platform so civil protection teams, universities and companies receive early alerts and analyze seismic behavior from a single dashboard.',
        'features': [
            'Data ingestion from stations and sensors (Raspberry Pi, accelerometers)',
            'Real-time visualization with time series and geospatial maps',
            'Automatic alerts based on magnitude and intensity thresholds',
            'Event history storage and analysis',
            'Open data API for external integrations',
            'Multi-user dashboard with roles'
        ],
        'benefits': [
            {'icon': 'zap', 'title': 'Early alerts', 'text': 'Automatic notifications that cut reaction times during events.'},
            {'icon': 'chart-bar', 'title': 'Data-driven decisions', 'text': 'History and analysis that back studies and technical reports.'},
            {'icon': 'globe', 'title': 'Remote access', 'text': 'Monitor all your stations from anywhere, in real time.'},
            {'icon': 'database', 'title': 'Zero data loss', 'text': 'Fault-tolerant architecture with redundant storage.'}
        ],
        'tech': ['Python', 'Node.js', 'InfluxDB', 'MQTT', 'Grafana', 'WebSockets'],
        'faq': [
            {'q': 'What hardware do I need for a seismic station?', 'a': 'We work with commercial sensors (accelerometers, geophones) and boards like Raspberry Pi or ESP32; we design the integration and firmware.'},
            {'q': 'Can I integrate stations I already have?', 'a': 'Yes. If your stations already produce data (JSON, MQTT, CSV), we integrate them without replacing the hardware.'},
            {'q': 'Do alerts arrive via WhatsApp or email?', 'a': 'We set up whatever channels you need: WhatsApp, email, SMS, webhooks or a mobile app.'}
        ]
    },
    'sports-results': {
        'name': 'Sports Results',
        'slug': 'sports-results',
        'icon': 'trophy',
        'subtitle': 'Live score platform',
        'description': 'A live score platform with real-time results, statistics and notifications for leagues and tournaments.',
        'overview': 'We build real-time sports result platforms: live scores, per-game statistics, standings and push notifications. Designed for local leagues, school tournaments and sports media that want to keep their audience informed by the second.',
        'features': [
            'Live scores updated in real time',
            'Statistics per team, player and season',
            'Push notifications for goals and results',
            'Match history and standings tables',
            'API for integration with existing apps and sites',
            'Admin panel to manage tournaments'
        ],
        'benefits': [
            {'icon': 'users', 'title': 'More engagement', 'text': 'Keep your audience hooked throughout the match.'},
            {'icon': 'trending-up', 'title': 'New revenue', 'text': 'Ad spaces and premium plans inside the platform.'},
            {'icon': 'zap', 'title': 'Real real-time', 'text': 'Second-level latency thanks to WebSockets and distributed cache.'},
            {'icon': 'smartphone', 'title': 'Multi-platform', 'text': 'Web, iOS and Android from a single codebase.'}
        ],
        'tech': ['WebSockets', 'Redis', 'Node.js', 'Flutter', 'Firebase', 'PostgreSQL'],
        'faq': [
            {'q': 'Where does match data come from?', 'a': 'From your own operators (admin panel) or from external sports data APIs; we integrate and normalize it.'},
            {'q': 'How many concurrent users does it support?', 'a': 'The architecture scales horizontally; for local leagues we handle thousands of concurrent users without issues.'},
            {'q': 'Can I have my own mobile app?', 'a': 'Yes. We build iOS and Android apps with your branding, available in the stores.'}
        ]
    },
    'sales-analytics': {
        'name': 'Sales Analytics',
        'slug': 'sales-analytics',
        'icon': 'chart-bar',
        'subtitle': 'Dashboards and metrics',
        'description': 'Dashboards and metrics that turn your sales data into actionable decisions.',
        'overview': 'We turn your sales data into clear, real-time dashboards: revenue, best-selling products, channels, regions and forecasts. We integrate your sources (POS, ERP, e-commerce, spreadsheets) and automate the reports you currently spend hours preparing.',
        'features': [
            'Executive dashboards with sales KPIs',
            'Real-time metric monitoring',
            'Segmentation by product, channel, seller and region',
            'Sales forecasting with statistical models',
            'Integration with POS, ERP and e-commerce platforms',
            'Exports and scheduled reports'
        ],
        'benefits': [
            {'icon': 'brain', 'title': 'Data-driven decisions', 'text': 'Stop deciding by intuition: see what works and what does not.'},
            {'icon': 'trending-up', 'title': 'Visible opportunities', 'text': 'Spot trends, seasonality and underperforming products.'},
            {'icon': 'clock', 'title': 'Time savings', 'text': 'Automatic reports that generate themselves, with no manual work.'},
            {'icon': 'monitor', 'title': 'Visual clarity', 'text': 'Intuitive dashboards your whole team understands at a glance.'}
        ],
        'tech': ['Power BI', 'Tableau', 'D3.js', 'Looker Studio', 'PostgreSQL', 'Python'],
        'faq': [
            {'q': 'What data sources does it connect to?', 'a': 'Almost any source: Excel, Google Sheets, POS, ERP, databases and APIs. We centralize everything in one place.'},
            {'q': 'Do dashboards update by themselves?', 'a': 'Yes. Updates are automatic, real-time or batched, depending on your needs.'},
            {'q': 'Do I need a data team to use it?', 'a': 'No. We deliver ready-to-use dashboards and train your team to operate them.'}
        ]
    },
    'radio-streaming': {
        'name': 'Radio Streaming',
        'slug': 'radio-streaming',
        'icon': 'radio',
        'subtitle': 'Audio infrastructure',
        'description': 'Audio infrastructure for live and on-demand broadcasting with high availability.',
        'overview': 'We set up the complete streaming infrastructure for your station: audio servers, encoding, live broadcasting, podcasts and audience analytics. We deliver a web player, mobile apps and control panels so your signal reaches the world without downtime.',
        'features': [
            'Live broadcasting with high availability',
            'On-demand playback (podcasts and shows)',
            'Customizable web player with station branding',
            'Real-time listener statistics',
            'Automatic recording and podcast publishing',
            'iOS and Android mobile apps'
        ],
        'benefits': [
            {'icon': 'globe', 'title': 'Global reach', 'text': 'Broadcast to any audience in the world, with no geographic limits.'},
            {'icon': 'trending-up', 'title': 'Monetization', 'text': 'Ad spaces, subscriptions and audience reports for your clients.'},
            {'icon': 'zap', 'title': 'Stability', 'text': 'Server redundancy to avoid signal outages.'},
            {'icon': 'users', 'title': 'Measured audience', 'text': 'Know your listeners: where they are, when they listen, what they consume.'}
        ],
        'tech': ['Icecast', 'Liquidsoap', 'HLS', 'FFmpeg', 'WebRTC', 'React'],
        'faq': [
            {'q': 'Can I broadcast with my current equipment?', 'a': 'Yes. We integrate with your existing consoles, microphones and software; no studio changes needed.'},
            {'q': 'How many concurrent listeners does it support?', 'a': 'The infrastructure scales with your audience, from dozens to tens of thousands of listeners.'},
            {'q': 'Does it include the mobile app?', 'a': 'Yes, we build iOS and Android apps with your branding, published in the stores.'}
        ]
    },
    'telemedicine': {
        'name': 'Telemedicine System',
        'slug': 'telemedicine',
        'icon': 'heart-pulse',
        'subtitle': 'Consultations and records',
        'description': 'A virtual medical consultation platform with secure digital clinical records.',
        'overview': 'We build telemedicine platforms that connect patients with doctors through secure video calls, digital clinical records, appointment scheduling and e-prescriptions. Built for clinics, practices and health companies looking to expand their reach without compromising data security.',
        'features': [
            'Secure doctor-patient video calls',
            'Electronic health records (EHR)',
            'Online appointment scheduling',
            'E-prescriptions and medical orders',
            'Automatic appointment reminders',
            'Roles and permissions for doctors, patients and admins'
        ],
        'benefits': [
            {'icon': 'globe', 'title': 'Remote access', 'text': 'Treat patients anywhere, expanding your coverage.'},
            {'icon': 'folder', 'title': 'Continuity of care', 'text': 'Complete clinical history accessible at every visit.'},
            {'icon': 'clock', 'title': 'Clinical efficiency', 'text': 'Less paperwork and more time for patient care.'},
            {'icon': 'shield', 'title': 'Data security', 'text': 'Encryption and access control protect medical information.'}
        ],
        'tech': ['WebRTC', 'Node.js', 'PostgreSQL', 'AES-256', 'React Native', 'Docker'],
        'faq': [
            {'q': 'Is medical information secure?', 'a': 'Yes. We apply encryption in transit and at rest, role-based access control and audit logs, aligned with health regulations.'},
            {'q': 'Does it integrate with my current system?', 'a': 'Yes. We integrate with your existing EHR, schedule and payment gateways.'},
            {'q': 'Do patients need to install anything?', 'a': 'No. Consultations happen in the browser; the mobile app is optional and free for patients.'}
        ]
    },
    'ticketing': {
        'name': 'Bookings & Tickets',
        'slug': 'ticketing',
        'icon': 'ticket',
        'subtitle': 'Advanced ticketing',
        'description': 'An advanced ticketing platform for events, transport and shows.',
        'overview': 'We build ticket sales platforms with seat maps, scannable QR codes, payment gateways and capacity control. From concerts and theater to transport and theme parks: sell tickets online and control access from a central panel.',
        'features': [
            'Online ticket sales with multiple payment gateways',
            'Dynamic QR codes for access validation',
            'Interactive seat map with visual selection',
            'Capacity and ticket-type management',
            'Admin panel with sales reports',
            'Integration with physical point-of-sale'
        ],
        'benefits': [
            {'icon': 'zap', 'title': 'Shorter lines', 'text': 'Attendees buy in seconds and enter by scanning their code.'},
            {'icon': 'shield', 'title': 'Fraud control', 'text': 'Dynamic codes prevent resale and forgery.'},
            {'icon': 'chart-bar', 'title': 'Clear reports', 'text': 'Sales, occupancy and revenue in real time.'},
            {'icon': 'smartphone', 'title': 'Mobile experience', 'text': 'Buy from any device, no app downloads.'}
        ],
        'tech': ['Node.js', 'Stripe', 'PostgreSQL', 'React', 'QR', 'Redis'],
        'faq': [
            {'q': 'Which payment gateways does it use?', 'a': 'Stripe, PayPal, Wompi and major local gateways; it also supports cash and physical sales points.'},
            {'q': 'How do I validate tickets at the event?', 'a': 'With the validation app you scan the QR code from a phone or laser reader; validation is instant and secure.'},
            {'q': 'Can I also sell at the box office?', 'a': 'Yes, we integrate the physical point of sale with the same platform and inventory.'}
        ]
    },
    'odoo-erp': {
        'name': 'Odoo CRM System',
        'slug': 'odoo-erp',
        'icon': 'layers',
        'subtitle': 'ERP implementation',
        'description': 'Odoo implementation and customization to unify CRM, sales, inventory and accounting.',
        'overview': 'We implement Odoo to unify your operations: CRM, sales, purchasing, inventory, invoicing and accounting in a single system. We configure modules, migrate your data, customize what is needed and train your team for a frictionless transition.',
        'features': [
            'Modular Odoo implementation (CRM, sales, inventory, accounting)',
            'Customization of modules and workflows',
            'Data migration from legacy systems and Excel',
            'Integrations with payment gateways and external platforms',
            'Team training for daily operations',
            'Ongoing support and maintenance'
        ],
        'benefits': [
            {'icon': 'layers', 'title': 'One system', 'text': 'All your processes connected, no loose spreadsheets or double entry.'},
            {'icon': 'zap', 'title': 'Automation', 'text': 'Workflows that run themselves: quotes, orders and invoicing.'},
            {'icon': 'trending-up', 'title': 'Scalable', 'text': 'Grows with your company: add modules when you need them.'},
            {'icon': 'receipt', 'title': 'Lower costs', 'text': 'Open licensing and full control over your system.'}
        ],
        'tech': ['Odoo', 'Python', 'PostgreSQL', 'XML-RPC', 'Docker', 'JavaScript'],
        'faq': [
            {'q': 'How long does an implementation take?', 'a': 'A typical CRM + sales implementation takes 4 to 8 weeks, including migration and training.'},
            {'q': 'Do you migrate my current data?', 'a': 'Yes. We migrate customers, products, sales history and balances from Excel, legacy systems or other tools.'},
            {'q': 'Do I need to buy the Odoo license?', 'a': 'Not necessarily. Odoo Community is free and covers most cases; we evaluate with you whether Enterprise adds value.'}
        ]
    },
    'wordpress-plugins': {
        'name': 'WordPress Plugins',
        'slug': 'wordpress-plugins',
        'icon': 'puzzle',
        'subtitle': 'Custom development',
        'description': 'Custom WordPress plugins and themes to take your site to the next level.',
        'overview': 'We build fully customized WordPress plugins and themes: unique features, external API integrations, performance optimization and security. If your business needs something no catalog plugin does, we build it to your specifications.',
        'features': [
            'Custom WordPress plugins',
            'Custom themes and design adaptation',
            'Integration with APIs and external services',
            'Performance optimization and Core Web Vitals',
            'Security hardening and best practices',
            'Ongoing maintenance and updates'
        ],
        'benefits': [
            {'icon': 'puzzle', 'title': 'Unique functionality', 'text': 'Your site does exactly what your business needs, no patches.'},
            {'icon': 'trending-up', 'title': 'Better SEO', 'text': 'Clean code and optimized performance that search engines reward.'},
            {'icon': 'zap', 'title': 'Performance', 'text': 'Lightweight plugins that never slow your page down.'},
            {'icon': 'shield', 'title': 'Security', 'text': 'Development following WordPress best practices.'}
        ],
        'tech': ['PHP', 'WordPress', 'WooCommerce', 'REST API', 'MySQL', 'JavaScript'],
        'faq': [
            {'q': 'Can you integrate my site with another system?', 'a': 'Yes. We connect WordPress with CRMs, payment gateways, ERPs and any API using custom plugins.'},
            {'q': 'Do you keep my plugins updated?', 'a': 'We offer maintenance plans that include updates, backups and security monitoring.'},
            {'q': 'Do you work with WooCommerce?', 'a': 'Yes, we build on WooCommerce: shipping plugins, gateways, advanced coupons and custom reports.'}
        ]
    },
    'iot': {
        'name': 'IoT Internet of Things',
        'slug': 'iot',
        'icon': 'chip',
        'subtitle': 'Hardware and sensors',
        'description': 'Connected hardware and sensors with software to monitor and automate in real time.',
        'overview': 'We design IoT solutions end to end: we select or design the hardware, write the firmware, implement connectivity and build the web platform where you visualize and control everything in real time. From agriculture and logistics to industry and smart home.',
        'features': [
            'Hardware and sensor design and selection',
            'Firmware development for microcontrollers',
            'MQTT, LoRaWAN and cellular connectivity',
            'IoT platform with real-time dashboards',
            'Rule-based alerts and automation',
            'Integration with existing systems and APIs'
        ],
        'benefits': [
            {'icon': 'monitor', 'title': '24/7 monitoring', 'text': 'Full visibility of your equipment and sensors from anywhere.'},
            {'icon': 'zap', 'title': 'Automation', 'text': 'Rules that trigger automatic actions upon events.'},
            {'icon': 'trending-up', 'title': 'Real savings', 'text': 'Detect failures and waste before they become costs.'},
            {'icon': 'cpu', 'title': 'Scalable', 'text': 'Add hundreds or thousands of devices without changing the architecture.'}
        ],
        'tech': ['ESP32', 'Raspberry Pi', 'MQTT', 'Node-RED', 'AWS IoT', 'C++'],
        'faq': [
            {'q': 'I already have sensors, can you connect them?', 'a': 'Yes. If your sensors communicate via common protocols (MQTT, Modbus, HTTP), we integrate them into the platform.'},
            {'q': 'What happens if I lose connectivity?', 'a': 'Devices store data locally and sync when they reconnect; you do not lose information.'},
            {'q': 'Do you supply the hardware?', 'a': 'We can design and assemble the hardware or work with yours; we advise you on the most cost-effective option.'}
        ]
    },
    'medicine-prices': {
        'name': 'Medicine Prices',
        'slug': 'medicine-prices',
        'icon': 'pill',
        'subtitle': 'Pharmaceutical comparator',
        'description': 'A pharmaceutical price comparator with up-to-date medicine prices across multiple pharmacies.',
        'overview': 'We build medicine price comparators that help users find where to buy cheaper. We collect prices from multiple pharmacies, normalize them and show them in a clear interface with search by active ingredient, brand or lab.',
        'features': [
            'Up-to-date medicine and price database',
            'Search by name, active ingredient and lab',
            'Price comparison across pharmacies and areas',
            'Price-change alerts for users',
            'Panel for pharmacies to manage their prices',
            'API to embed the comparator on other sites'
        ],
        'benefits': [
            {'icon': 'trending-up', 'title': 'Savings for users', 'text': 'Find the best price in seconds and save every month.'},
            {'icon': 'chart-bar', 'title': 'Market data', 'text': 'Pharmacies access price and competition statistics.'},
            {'icon': 'users', 'title': 'Traffic and trust', 'text': 'A useful tool that attracts and retains users.'},
            {'icon': 'refresh', 'title': 'Always up to date', 'text': 'Automated price collection and validation.'}
        ],
        'tech': ['Web scraping', 'Node.js', 'PostgreSQL', 'React', 'Redis', 'Docker'],
        'faq': [
            {'q': 'How do you update prices?', 'a': 'With automated collection processes from public sources and the participating pharmacies\u2019 panel.'},
            {'q': 'Are the prices reliable?', 'a': 'Yes, we apply validation and timestamps; we always show the last update date.'},
            {'q': 'Can I integrate it into my health site?', 'a': 'Yes, we offer a public API to embed the comparator on other portals.'}
        ]
    },
    'openclaw': {
        'name': 'OpenClaw',
        'slug': 'openclaw',
        'icon': 'gamepad',
        'subtitle': 'Arcade hardware control',
        'description': 'Control software for arcade hardware: machines, games and token management.',
        'overview': 'We develop the software that controls arcade hardware: machine management, credits and tokens, game selection, revenue dashboards and remote maintenance. Ideal for game room operators who want to measure every machine and optimize profitability.',
        'features': [
            'Arcade machine control and monitoring',
            'Credits, tokens and card management',
            'Revenue dashboard per machine and per day',
            'Game selection and updates',
            'Remote diagnostics and maintenance',
            'Usage and profitability reports'
        ],
        'benefits': [
            {'icon': 'chart-bar', 'title': 'Measurable revenue', 'text': 'Know exactly what each machine generates every day.'},
            {'icon': 'zap', 'title': 'Less downtime', 'text': 'Remote fault detection and proactive maintenance.'},
            {'icon': 'monitor', 'title': 'Central management', 'text': 'Control all your branches from a single panel.'},
            {'icon': 'trending-up', 'title': 'Profitability', 'text': 'Identify high-performing games and machines to optimize operations.'}
        ],
        'tech': ['C++', 'Raspberry Pi', 'Python', 'MQTT', 'Node.js', 'SQLite'],
        'faq': [
            {'q': 'What arcade hardware does it control?', 'a': 'We work with Raspberry Pi-based boards, embedded PCs and JAMMA controllers; we integrate control over your cabinet.'},
            {'q': 'Do customers pay with cards or tokens?', 'a': 'We support physical tokens, rechargeable cards and QR payment codes, depending on your room\u2019s model.'},
            {'q': 'Can I monitor several branches?', 'a': 'Yes, the central panel aggregates all your machines and branches in real time.'}
        ]
    },
    'barbershop-booking': {
        'name': 'Barber Booking',
        'slug': 'barbershop-booking',
        'icon': 'scissors',
        'subtitle': 'System for barbershops',
        'description': 'A booking system for barbershops and hair salons with automatic reminders.',
        'overview': 'We implement booking systems for barbershops and hair salons: online scheduling, barber and service selection, automatic WhatsApp reminders and client management. Your team focuses on cutting hair, not answering calls or juggling the schedule.',
        'features': [
            'Online booking with real-time availability',
            'Barber, service and time selection by the client',
            'Automatic WhatsApp and email reminders',
            'Online payments and deposits',
            'Customer database and history',
            'Revenue, service and occupancy reports'
        ],
        'benefits': [
            {'icon': 'clock', 'title': 'Fewer no-shows', 'text': 'Automatic reminders that reduce missed appointments.'},
            {'icon': 'trending-up', 'title': 'More bookings', 'text': 'Clients book anytime, even when you are closed.'},
            {'icon': 'zap', 'title': 'Time savings', 'text': 'Goodbye scheduling calls and double bookings.'},
            {'icon': 'star', 'title': 'Professional image', 'text': 'Clients perceive a modern, organized business.'}
        ],
        'tech': ['Node.js', 'React Native', 'Firebase', 'WhatsApp API', 'Stripe'],
        'faq': [
            {'q': 'Do clients need to create an account?', 'a': 'No. They can book in seconds with their name and phone. Accounts are optional.'},
            {'q': 'Does it connect to the shop\u2019s WhatsApp?', 'a': 'Yes, reminders and confirmations are sent automatically via WhatsApp from your number.'},
            {'q': 'Does it work on the client\u2019s phone?', 'a': 'Yes, it is a responsive web app: clients book from the browser without installing anything.'}
        ]
    },
    'facial-cleaning': {
        'name': 'Facial Cleaning',
        'slug': 'facial-cleaning',
        'icon': 'sparkles',
        'subtitle': 'System for spas and clinics',
        'description': 'A system for spas and aesthetic clinics: appointments, records and client treatments.',
        'overview': 'We build systems for spas, aesthetic centers and facial cleaning clinics: treatment scheduling, patient records, procedure history, product control and reminders. A premium experience for your clients and full control for your team.',
        'features': [
            'Treatment and service scheduling',
            'Digital patient records',
            'Treatment history and progress photos',
            'Product and per-treatment consumption control',
            'Automatic appointment reminders',
            'Revenue, service and occupancy reports'
        ],
        'benefits': [
            {'icon': 'sparkles', 'title': 'Premium experience', 'text': 'A flawless digital process that complements your service.'},
            {'icon': 'box', 'title': 'Inventory control', 'text': 'Know what products are consumed and when to reorder.'},
            {'icon': 'users', 'title': 'Client loyalty', 'text': 'Complete history to recommend treatments and retain clients.'},
            {'icon': 'folder', 'title': 'Total organization', 'text': 'All patient information in one place.'}
        ],
        'tech': ['React', 'Node.js', 'PostgreSQL', 'Tailwind', 'Docker'],
        'faq': [
            {'q': 'Does it store before/after photos?', 'a': 'Yes, the record includes photo galleries with private access control for the patient.'},
            {'q': 'Does it work for clinics with several specialists?', 'a': 'Yes, each specialist has their own schedule and patients; the central panel manages everything.'},
            {'q': 'Can patients view their history?', 'a': 'Yes, with a patient portal they can check their treatments, appointments and recommendations.'}
        ]
    },
    'lms-moodle': {
        'name': 'LMS & Moodle Platforms',
        'slug': 'lms-moodle',
        'icon': 'graduation',
        'subtitle': 'Courses for schools and companies',
        'description': 'Learning platforms for schools and companies with Moodle and custom development.',
        'overview': 'We implement LMS platforms for schools, universities and companies: online courses, assessments, certifications and progress tracking. We work with Moodle and custom development so the learning experience carries your brand.',
        'features': [
            'Moodle implementation and custom LMS',
            'Courses with multimedia, quizzes and assignments',
            'Automatic assessments and certifications',
            'Gamification and achievement badges',
            'Teacher, student and admin roles',
            'SSO, videoconferencing and payments integration'
        ],
        'benefits': [
            {'icon': 'graduation', 'title': 'Scalable', 'text': 'Train hundreds or thousands of students with no classroom limits.'},
            {'icon': 'chart-bar', 'title': 'Real tracking', 'text': 'Measure progress, grades and completion of every course.'},
            {'icon': 'globe', 'title': 'Accessible', 'text': 'Your students learn from any device, anywhere.'},
            {'icon': 'puzzle', 'title': 'Your branding', 'text': 'We customize the platform with your institution\u2019s identity.'}
        ],
        'tech': ['Moodle', 'PHP', 'MySQL', 'SCORM', 'React', 'Docker'],
        'faq': [
            {'q': 'Moodle or a custom platform?', 'a': 'It depends on your needs: Moodle fits most cases; if you need something very specific, we build it custom.'},
            {'q': 'Can I sell online courses?', 'a': 'Yes, we integrate payment gateways, coupons and subscription or per-course access.'},
            {'q': 'Does it include certificates?', 'a': 'Yes, we issue automatic certificates upon passing each course, with customizable design.'}
        ]
    },
    'laundry-rentals': {
        'name': 'Laundry Rental',
        'slug': 'laundry-rentals',
        'icon': 'washer',
        'subtitle': 'Rental management',
        'description': 'Washer rental management: machines, payments, contracts and maintenance.',
        'overview': 'We build platforms for companies that rent washers and dryers: machine management by location, rental contracts, automatic recurring billing, online payments and maintenance control. Your entire fleet, managed from a single panel.',
        'features': [
            'Machine and location management',
            'Rental contracts with automatic billing',
            'Recurring charges and online payments',
            'Maintenance status and service alerts',
            'Client panel with their billing',
            'Revenue, delinquency and usage reports'
        ],
        'benefits': [
            {'icon': 'repeat', 'title': 'Recurring revenue', 'text': 'Automatic billing that collects on time, every month.'},
            {'icon': 'trending-up', 'title': 'Total control', 'text': 'Know which machine, in which location, generates which income.'},
            {'icon': 'zap', 'title': 'Automation', 'text': 'Contracts, billing and reminders that run themselves.'},
            {'icon': 'users', 'title': 'Better support', 'text': 'Your clients check invoices and report issues online.'}
        ],
        'tech': ['React', 'Node.js', 'PostgreSQL', 'Stripe', 'Docker'],
        'faq': [
            {'q': 'How are rentals billed?', 'a': 'We generate automatic invoices on a monthly or custom frequency, with recurring payment by card or PSE.'},
            {'q': 'Can my clients see their invoices?', 'a': 'Yes, each client has a portal with their invoices, payments and account status.'},
            {'q': 'Does it integrate with my accounting?', 'a': 'Yes, we export billing to your accountant or integrate it with your accounting system.'}
        ]
    }
}

SERVICES_EN = {
    'data-engineering': {
        'overview': 'We design the backbone of your data strategy: robust, scalable pipelines that move information from any source to where your business needs it. Real-time or batch processing, with governance and data quality built in from day one, not an afterthought.',
        'benefits': [
            {'icon': 'database', 'title': 'Reliable pipelines', 'text': 'Data flows that do not break and recover on their own.'},
            {'icon': 'zap', 'title': 'Real-time or batch', 'text': 'The speed your business needs, no more, no less.'},
            {'icon': 'cloud', 'title': 'Cloud native', 'text': 'Modern architectures on AWS, GCP and Azure.'},
            {'icon': 'shield', 'title': 'Quality and governance', 'text': 'Clean, traceable data with defined ownership.'}
        ],
        'tech': ['Apache Spark', 'Kafka', 'Airflow', 'dbt', 'BigQuery', 'Snowflake'],
        'faq': [
            {'q': 'What sources can you integrate?', 'a': 'Databases, APIs, files, SaaS, logs and streaming: virtually any source with data.'},
            {'q': 'How long does a data pipeline take?', 'a': 'A typical pipeline is delivered in 2 to 4 weeks, including monitoring and documentation.'},
            {'q': 'Do you migrate my current infrastructure to the cloud?', 'a': 'Yes, we plan and execute the migration without interrupting your operations.'}
        ]
    },
    'data-extraction-etl': {
        'overview': 'We extract data from any source and transform it into clean, structured formats ready for analysis. Multi-source integrations, API and webhook ingestion, and legacy system migration with strategies that respect the volume and criticality of your information.',
        'benefits': [
            {'icon': 'filter', 'title': 'Multi-source', 'text': 'We connect databases, APIs, files and SaaS.'},
            {'icon': 'refresh', 'title': 'Automated', 'text': 'Scheduled processes that run on their own and are monitored.'},
            {'icon': 'box', 'title': 'Clean data', 'text': 'Normalization and cleaning that remove noise and duplicates.'},
            {'icon': 'trending-up', 'title': 'Ready to analyze', 'text': 'Your team receives directly usable data.'}
        ],
        'tech': ['Python', 'Airbyte', 'dbt', 'Apache Airflow', 'PostgreSQL', 'REST APIs'],
        'faq': [
            {'q': 'Can you extract from systems without an API?', 'a': 'Yes, we use techniques like file reading, controlled scraping and database connectors.'},
            {'q': 'What happens during a migration?', 'a': 'We run incremental migrations with continuous validation and a rollback plan.'},
            {'q': 'What deliverables are included?', 'a': 'Documentation, monitoring, validations and team training.'}
        ]
    },
    'data-visualization': {
        'overview': 'We turn complex data into clear visuals that empower fast decisions. Interactive dashboards, executive reports and real-time KPI monitoring, built with the best market tools or with fully custom components.',
        'benefits': [
            {'icon': 'monitor', 'title': 'Interactive dashboards', 'text': 'Explore, filter and drill down without depending on an analyst.'},
            {'icon': 'zap', 'title': 'Real-time KPIs', 'text': 'Your operation monitored by the second, not at month-end.'},
            {'icon': 'puzzle', 'title': 'Tailor-made', 'text': 'Unique visualizations when the standard tool is not enough.'},
            {'icon': 'users', 'title': 'For your audience', 'text': 'Executive reports your board actually understands.'}
        ],
        'tech': ['Tableau', 'Power BI', 'D3.js', 'Looker Studio', 'ECharts', 'Vue.js'],
        'faq': [
            {'q': 'Which tool do you recommend?', 'a': 'We evaluate your case: Power BI or Tableau for most, D3.js or ECharts for custom visuals.'},
            {'q': 'Are dashboards mobile-friendly?', 'a': 'Yes, we optimize them to look great on phones and tablets.'},
            {'q': 'Can they connect to several sources?', 'a': 'Yes, a dashboard can combine databases, APIs and spreadsheets in a single view.'}
        ]
    },
    'data-mining-management': {
        'overview': 'We uncover the hidden insights in your data. We apply data mining to detect patterns and anomalies, segment customers and discover association rules; and we manage quality with data catalogs and lineage that give you full visibility and control.',
        'benefits': [
            {'icon': 'brain', 'title': 'Hidden insights', 'text': 'Patterns and anomalies invisible to the naked eye.'},
            {'icon': 'users', 'title': 'Segmentation', 'text': 'Know and group your customers for effective campaigns.'},
            {'icon': 'folder', 'title': 'Data catalog', 'text': 'Know what data you have, where it is and who uses it.'},
            {'icon': 'shield', 'title': 'Governance', 'text': 'Control over the quality and use of your information.'}
        ],
        'tech': ['Python', 'scikit-learn', 'pandas', 'SQL', 'Atlas', 'dbt'],
        'faq': [
            {'q': 'What is data lineage?', 'a': 'It tracks each data point\u2019s journey: where it comes from, how it is transformed and where it is used.'},
            {'q': 'Can you detect fraud with this?', 'a': 'Yes, anomaly detection is key to spotting unusual behavior.'},
            {'q': 'Do I need a lot of data to start?', 'a': 'We work with the data you have; the scale grows with you.'}
        ]
    },
    'desktop-software': {
        'overview': 'We build native desktop applications with enterprise-grade performance and security for Windows, macOS and Linux. Offline-first apps, ERP and CRM integrations, and automatic update systems that keep your team always on the latest version.',
        'benefits': [
            {'icon': 'monitor', 'title': 'Cross-platform', 'text': 'One app for Windows, macOS and Linux.'},
            {'icon': 'zap', 'title': 'Native performance', 'text': 'Speed and smoothness web apps cannot match.'},
            {'icon': 'box', 'title': 'Offline-first', 'text': 'Work offline and sync when you are back.'},
            {'icon': 'refresh', 'title': 'Auto-updates', 'text': 'Your team always on the latest version.'}
        ],
        'tech': ['Electron', 'Tauri', 'C#', 'Java', 'Python', 'SQLite'],
        'faq': [
            {'q': 'Electron or Tauri?', 'a': 'It depends: Tauri is lighter, Electron has a bigger ecosystem. We evaluate together which fits.'},
            {'q': 'Does it work offline?', 'a': 'Yes, we design offline-first architectures that sync when reconnected.'},
            {'q': 'Does it integrate with my ERP?', 'a': 'Yes, we integrate with SAP, Odoo, Microsoft Dynamics and proprietary systems.'}
        ]
    },
    'machine-learning': {
        'overview': 'We deploy intelligent systems that automate complex decisions. Predictive analytics, NLP models and computer vision, LLM fine-tuning with RAG and full MLOps so your models move from the lab to production and stay healthy.',
        'benefits': [
            {'icon': 'brain', 'title': 'Prediction', 'text': 'Demand, risk and behavior forecasts.'},
            {'icon': 'zap', 'title': 'Automation', 'text': 'Repetitive decisions solved by models, without human error.'},
            {'icon': 'monitor', 'title': 'Real MLOps', 'text': 'Monitoring, versioning and continuous retraining.'},
            {'icon': 'trending-up', 'title': 'Competitive edge', 'text': 'Capabilities your competition does not have yet.'}
        ],
        'tech': ['Python', 'PyTorch', 'scikit-learn', 'LangChain', 'Hugging Face', 'Vertex AI'],
        'faq': [
            {'q': 'What problems does ML solve well?', 'a': 'Prediction, classification, anomaly detection, language processing and vision: if you have historical data, there is likely a use case.'},
            {'q': 'How much data do I need?', 'a': 'It depends on the problem; we evaluate your case and tell you whether your data has enough signal.'},
            {'q': 'Do models update themselves?', 'a': 'With MLOps, yes: we monitor performance and retrain them automatically.'}
        ]
    },
    'mobile-development': {
        'overview': 'We create polished, high-performance mobile apps for iOS and Android. Native development with Swift and Kotlin, cross-platform with React Native and Flutter, offline-capable PWAs, push notifications and full optimization for the app stores.',
        'benefits': [
            {'icon': 'smartphone', 'title': 'Native or cross-platform', 'text': 'The right technology for your budget and goals.'},
            {'icon': 'zap', 'title': 'High performance', 'text': 'Fast, fluid apps users love to use.'},
            {'icon': 'trending-up', 'title': 'Monetization', 'text': 'In-app purchases, subscriptions and ads built in.'},
            {'icon': 'star', 'title': 'Ready to publish', 'text': 'ASO optimization for App Store and Play Store.'}
        ],
        'tech': ['Swift', 'Kotlin', 'React Native', 'Flutter', 'Firebase', 'GraphQL'],
        'faq': [
            {'q': 'How much does a mobile app cost?', 'a': 'It depends on scope; we present a clear phased proposal after a consultation.'},
            {'q': 'How long does development take?', 'a': 'A typical MVP is delivered in 6 to 12 weeks; complex apps take 3 to 6 months.'},
            {'q': 'Do you publish to the stores?', 'a': 'Yes, we manage publishing on App Store and Play Store, including accounts and review.'}
        ]
    },
    'on-demand-systems': {
        'overview': 'Need a custom solution, fast? We architect and deliver systems tailored to your requirements and deadlines: rapid prototyping and MVPs, microservices and serverless architectures, SaaS platforms, API-first design and full DevOps with CI/CD.',
        'benefits': [
            {'icon': 'rocket', 'title': 'Speed', 'text': 'Prototypes in days and MVPs in weeks, without losing quality.'},
            {'icon': 'zap', 'title': 'Modern', 'text': 'Microservices and serverless that scale with your demand.'},
            {'icon': 'repeat', 'title': 'SaaS', 'text': 'We build your product as a multi-tenant service.'},
            {'icon': 'monitor', 'title': 'DevOps included', 'text': 'CI/CD, monitoring and automatic deploys from day one.'}
        ],
        'tech': ['Node.js', 'AWS Lambda', 'Docker', 'Kubernetes', 'GraphQL', 'GitHub Actions'],
        'faq': [
            {'q': 'What is an MVP?', 'a': 'A minimum viable product: the smallest version that solves the problem and validates the market.'},
            {'q': 'Can you maintain the system afterwards?', 'a': 'Yes, we offer ongoing support and evolution with agile methodology.'},
            {'q': 'Do you work with my stack?', 'a': 'We adapt to your technology or recommend the most suitable for the project.'}
        ]
    },
    'web-development': {
        'overview': 'We design high-performance web experiences: from landing pages that convert to complex enterprise platforms. Frontends with React, Next.js and Vue.js; backends with Laravel, Node.js and Django; e-commerce and marketplaces, Core Web Vitals optimization and headless CMS integrations.',
        'benefits': [
            {'icon': 'zap', 'title': 'Performance', 'text': 'Fast sites that Google and your users reward.'},
            {'icon': 'trending-up', 'title': 'Conversion', 'text': 'Design and UX built to turn visits into customers.'},
            {'icon': 'cart', 'title': 'E-commerce', 'text': 'Complete stores with payments, shipping and catalog.'},
            {'icon': 'monitor', 'title': 'Scalable', 'text': 'From landing page to enterprise platform without rewrites.'}
        ],
        'tech': ['React', 'Next.js', 'Vue.js', 'Laravel', 'Node.js', 'Django'],
        'faq': [
            {'q': 'How much does a website cost?', 'a': 'It depends on scope: a professional landing page starts at an affordable price; we quote you without commitment within 48 hours.'},
            {'q': 'What is a headless CMS?', 'a': 'A system where content is managed separately and served to any platform: web, mobile, kiosks.'},
            {'q': 'Do you provide maintenance?', 'a': 'Yes, we offer maintenance plans with monitoring, security and continuous improvements.'}
        ]
    }
}

# ---------------------------------------------------------------------------
# Merge en los JSON manteniendo el orden de claves existente
# ---------------------------------------------------------------------------
def merge_item(existing, extra, extra_keys_order):
    """Fusiona `extra` en `existing`, insertando las claves nuevas en el orden dado."""
    out = {}
    used = set()
    for k in existing:
        out[k] = existing[k]
        used.add(k)
    for k in extra_keys_order:
        if k in extra and k not in used:
            out[k] = extra[k]
            used.add(k)
    return out

PRODUCT_KEYS = ['slug', 'description', 'overview', 'features', 'benefits', 'tech', 'faq']
SERVICE_KEYS = ['slug', 'overview', 'benefits', 'tech', 'faq']

# Mapeo slug (EN) -> id de servicio ES
ES_SERVICE_IDS = {
    'data-engineering': 'ingenieria-de-datos',
    'data-extraction-etl': 'extraccion-datos-etl',
    'data-visualization': 'visualizacion-de-datos',
    'data-mining-management': 'mineria-y-gestion-de-datos',
    'desktop-software': 'software-de-escritorio',
    'machine-learning': 'machine-learning',
    'mobile-development': 'desarrollo-movil',
    'on-demand-systems': 'sistemas-bajo-demanda',
    'web-development': 'desarrollo-web'
}

for lang, path, products, services in [
    ('es', ES_PATH, PRODUCTS_ES, SERVICES_ES),
    ('en', EN_PATH, PRODUCTS_EN, SERVICES_EN),
]:
    with open(path, encoding='utf-8') as f:
        data = json.load(f)

    for slug, extra in products.items():
        target = next((p for p in data['products'] if p['name'] == extra['name']), None)
        if target is None:
            raise SystemExit(f'Producto no encontrado en {lang}: {extra["name"]}')
        merged = merge_item(target, extra, PRODUCT_KEYS)
        data['products'][data['products'].index(target)] = merged

    for slug, extra in services.items():
        extra = dict(extra)
        extra['slug'] = slug  # el slug común ES/EN es la clave del dict
        if lang == 'es':
            target = next((s for s in data['services'] if s['id'] == ES_SERVICE_IDS[slug]), None)
        else:
            target = next((s for s in data['services'] if s['id'] == slug), None)
        if target is None:
            raise SystemExit(f'Servicio no encontrado en {lang}: {slug}')
        merged = merge_item(target, extra, SERVICE_KEYS)
        data['services'][data['services'].index(target)] = merged

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(f'OK {lang}: {path}')

print('Listo.') 
