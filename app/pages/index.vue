<script setup lang="ts">
import { company } from '~/data/config'

const { t } = useI18n()
const { public: { siteUrl } } = useRuntimeConfig()

useSeoMeta({
  title: () => t('seo.title'),
  ogTitle: () => t('seo.title'),
  description: () => t('seo.description'),
  ogDescription: () => t('seo.description')
})

// Datos estructurados: Organization + WebSite
const orgSchema = computed(() => ({
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'Organization',
      '@id': `${siteUrl}#organization`,
      name: 'Hamster Software',
      alternateName: 'HamsterSoftware',
      url: siteUrl,
      logo: { '@type': 'ImageObject', url: `${siteUrl}/favicon.svg` },
      description: t('seo.description'),
      address: {
        '@type': 'PostalAddress',
        addressLocality: 'Popayán',
        addressRegion: 'Cauca',
        addressCountry: 'CO'
      },
      contactPoint: {
        '@type': 'ContactPoint',
        telephone: `+${company.whatsappNumber}`,
        email: company.email,
        contactType: 'sales',
        availableLanguage: ['es', 'en']
      }
    },
    {
      '@type': 'WebSite',
      '@id': `${siteUrl}#website`,
      url: siteUrl,
      name: 'Hamster Software',
      inLanguage: ['es', 'en']
    }
  ]
}))

useHead(() => ({
  script: [{ type: 'application/ld+json', children: JSON.stringify(orgSchema.value) }]
}))
</script>

<template>
  <div>
    <HeroSection />
    <StatsSection />
    <ServicesSection />
    <SolutionsSection />
    <SecuritySection />
    <CasesSection />
    <IndustriesSection />
    <ProcessSection />
    <ContactSection />
  </div>
</template>
