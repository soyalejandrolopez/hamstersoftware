<script setup lang="ts">
import { company } from '~/data/config'
import { useContent } from '~/composables/useContent'

const { t } = useI18n()
const { services, contact } = useContent()

const form = reactive({
  name: '',
  email: '',
  company: '',
  service: '',
  message: ''
})

const sent = ref(false)

const whatsappHref = computed(() => {
  const text = encodeURIComponent(
    `${t('contact.whatsappGreeting', { name: company.name })}\n\n` +
      `${t('contact.fieldName')}: ${form.name || '—'}\n` +
      `${t('contact.fieldEmail')}: ${form.email || '—'}\n` +
      `${t('contact.fieldCompany')}: ${form.company || '—'}\n` +
      `${t('contact.fieldService')}: ${form.service || '—'}\n` +
      `${t('contact.fieldMessage')}: ${form.message || '—'}`
  )
  return `https://wa.me/${company.whatsappNumber}?text=${text}`
})

function submit() {
  window.open(whatsappHref.value, '_blank', 'noopener,noreferrer')
  sent.value = true
}

function resetForm() {
  sent.value = false
  form.name = ''
  form.email = ''
  form.company = ''
  form.service = ''
  form.message = ''
}
</script>

<template>
  <section id="contacto" class="scroll-mt-24 bg-white py-20 sm:py-28">
    <div class="container-site">
      <div
        class="relative overflow-hidden rounded-3xl p-8 shadow-relief-dark sm:p-12 lg:p-16"
        style="
          background: linear-gradient(140deg, #070c18 0%, #0b1220 50%, #0f172a 100%);
          border: 1px solid rgba(255, 255, 255, 0.12);
          box-shadow: inset 0 1px 0 0 rgba(255, 255, 255, 0.18), 0 30px 60px -15px rgba(0, 0, 0, 0.7), 0 0 0 1px rgba(37, 99, 235, 0.15);
        "
      >
        <div class="pointer-events-none absolute inset-0 bg-grid-dark opacity-35" />
        <div class="pointer-events-none absolute -left-32 -top-32 h-96 w-96 rounded-full bg-brand-600/25 blur-3xl" />
        <div class="pointer-events-none absolute -bottom-32 -right-32 h-96 w-96 rounded-full bg-amber-400/15 blur-3xl" />
        <div class="absolute inset-x-12 top-0 h-px bg-gradient-to-r from-transparent via-white/35 to-transparent pointer-events-none" />

        <div class="relative grid items-center gap-12 lg:grid-cols-[1.05fr_0.95fr] lg:gap-16">
          <!-- Copy -->
          <div class="text-white">
            <span
              class="inline-flex items-center gap-2 rounded-full border border-white/15 bg-white/5 px-4 py-2 text-xs font-semibold uppercase tracking-widest text-brand-300 shadow-relief-sm backdrop-blur-md"
            >
              <AppIcon name="zap" class="h-3.5 w-3.5 text-amber-400" />
              {{ contact.eyebrow }}
            </span>
            <h2
              class="mt-6 font-display text-3xl font-bold tracking-tight sm:text-4xl lg:text-[2.75rem] lg:leading-[1.12]"
            >
              {{ contact.titleStart }}
              <span class="text-gradient-light drop-shadow-sm">{{ contact.titleHighlight }}</span>
            </h2>
            <p class="mt-5 max-w-lg text-lg text-slate-300">{{ contact.description }}</p>

            <ul class="mt-8 space-y-3.5">
              <li
                v-for="b in contact.assurances"
                :key="b"
                class="flex items-center gap-3 text-slate-200"
              >
                <span class="flex h-6 w-6 items-center justify-center rounded-full bg-emerald-400/20 text-emerald-400 shadow-inner ring-1 ring-emerald-400/30">
                  <AppIcon name="check" class="h-3.5 w-3.5" />
                </span>
                <span class="text-sm font-medium">{{ b }}</span>
              </li>
            </ul>

            <a
              :href="`https://wa.me/${company.whatsappNumber}`"
              target="_blank"
              rel="noopener noreferrer"
              class="btn btn-amber btn-lg mt-9"
            >
              <AppIcon name="whatsapp" class="h-5 w-5" />
              {{ contact.whatsappCta }}
            </a>

            <div class="mt-8 flex flex-wrap gap-x-8 gap-y-3 text-sm text-slate-400">
              <span class="flex items-center gap-2">
                <AppIcon name="mail" class="h-4 w-4 text-brand-400" />
                {{ company.email }}
              </span>
              <span class="flex items-center gap-2">
                <AppIcon name="map-pin" class="h-4 w-4 text-brand-400" />
                {{ company.location }}
              </span>
            </div>
          </div>

          <!-- Formulario con acabado en alto relieve blanco -->
          <div
            class="rounded-2xl bg-white p-7 shadow-[0_25px_60px_-15px_rgba(0,0,0,0.5),inset_0_1px_0_rgba(255,255,255,1)] sm:p-9"
            style="border: 1px solid rgba(255,255,255,0.9);"
          >
            <div v-if="sent" class="flex flex-col items-center py-10 text-center">
              <span class="flex h-14 w-14 items-center justify-center rounded-full bg-emerald-100 text-emerald-600 shadow-inner">
                <AppIcon name="check" class="h-7 w-7" />
              </span>
              <h3 class="mt-4 font-display text-xl font-bold text-slate-900">
                {{ contact.successTitle }}
              </h3>
              <p class="mt-2 max-w-xs text-sm text-slate-600">
                {{ t('contact.successText', { number: company.whatsappLabel }) }}
              </p>
              <button class="btn btn-outline btn-md mt-6" @click="resetForm">
                {{ contact.resend }}
              </button>
            </div>

            <form v-else class="space-y-4" @submit.prevent="submit">
              <div class="grid gap-4 sm:grid-cols-2">
                <div>
                  <label class="label" for="contact-name">{{ contact.nameLabel }}</label>
                  <input id="contact-name" v-model="form.name" required type="text" :placeholder="contact.namePlaceholder" class="input" />
                </div>
                <div>
                  <label class="label" for="contact-email">{{ t('contact.emailLabel') }}</label>
                  <input id="contact-email" v-model="form.email" required type="email" :placeholder="contact.emailPlaceholder" class="input" />
                </div>
              </div>

              <div class="grid gap-4 sm:grid-cols-2">
                <div>
                  <label class="label" for="contact-company">{{ contact.companyLabel }}</label>
                  <input id="contact-company" v-model="form.company" type="text" :placeholder="contact.companyPlaceholder" class="input" />
                </div>
                <div>
                  <label class="label" for="contact-service">{{ contact.serviceLabel }}</label>
                  <select id="contact-service" v-model="form.service" class="input">
                    <option value="" disabled selected>{{ contact.servicePlaceholder }}</option>
                    <option v-for="s in services" :key="s.id" :value="s.title">{{ s.title }}</option>
                    <option :value="contact.otherOption">{{ contact.otherOption }}</option>
                  </select>
                </div>
              </div>

              <div>
                <label class="label" for="contact-message">{{ contact.projectLabel }}</label>
                <textarea
                  id="contact-message"
                  v-model="form.message"
                  required
                  rows="4"
                  :placeholder="contact.messagePlaceholder"
                  class="input resize-none"
                />
              </div>

              <button type="submit" class="btn btn-primary btn-lg w-full">
                <AppIcon name="send" class="h-4 w-4" />
                {{ contact.submit }}
              </button>
              <p class="text-center text-xs text-slate-400">{{ contact.formNote }}</p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
