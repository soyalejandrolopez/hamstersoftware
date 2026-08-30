export interface FaqItem {
  q: string
  a: string
}

export interface Benefit {
  icon: string
  title: string
  text: string
}

export interface Service {
  id: string
  slug: string
  icon: string
  title: string
  description: string
  overview: string
  features: string[]
  benefits: Benefit[]
  tech: string[]
  faq: FaqItem[]
}

export interface Product {
  name: string
  slug: string
  icon: string
  subtitle: string
  description: string
  overview: string
  features: string[]
  benefits: Benefit[]
  tech: string[]
  faq: FaqItem[]
}

export interface Stat {
  value: number
  suffix: string
  label: string
  icon: string
}

export type SeverityKey = 'critical' | 'high' | 'medium' | 'low'

export interface SecurityFeedItem {
  id: string
  title: string
  severity: SeverityKey
  time: string
}

export interface SecurityContent {
  eyebrow: string
  title: string
  description: string
  features: string[]
  cta: string
  feedTitle: string
  feedSource: string
  live: string
  updatedNote: string
  monitoredToday: string
  feed: SecurityFeedItem[]
}

export interface CaseStudy {
  id: string
  category: string
  title: string
  description: string
  tags: string[]
  stat?: string
  visualType?: 'spa' | 'salon' | 'web' | 'app' | string
  image?: string
}

export interface ProcessStep {
  number: string
  icon: string
  title: string
  description: string
}

export interface Industry {
  name: string
  icon: string
}

export interface HeroServiceCard {
  icon: string
  title: string
  desc: string
}

export interface HeroContent {
  eyebrow: string
  titleA: string
  titleHighlight: string
  titleB: string
  subtitle: string
  description: string
  ctaPrimary: string
  ctaSecondary: string
  badges: string[]
  serviceCards: HeroServiceCard[]
}

export interface ContactContent {
  eyebrow: string
  titleStart: string
  titleHighlight: string
  description: string
  assurances: string[]
  whatsappCta: string
  whatsappGreeting: string
  fieldName: string
  fieldEmail: string
  fieldCompany: string
  fieldService: string
  fieldMessage: string
  emailLabel: string
  nameLabel: string
  namePlaceholder: string
  emailPlaceholder: string
  companyLabel: string
  companyPlaceholder: string
  serviceLabel: string
  servicePlaceholder: string
  otherOption: string
  projectLabel: string
  messagePlaceholder: string
  submit: string
  formNote: string
  successTitle: string
  successText: string
  resend: string
}
