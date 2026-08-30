import type { Config } from 'tailwindcss'

export default <Partial<Config>>{
  content: [
    './app/components/**/*.{vue,js,ts}',
    './app/layouts/**/*.vue',
    './app/pages/**/*.vue',
    './app/app.vue',
    './app/error.vue',
    './app/data/**/*.{js,ts}'
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eef5ff',
          100: '#d9e8ff',
          200: '#bcd7ff',
          300: '#8ebcff',
          400: '#5997ff',
          500: '#3374fc',
          600: '#2563eb',
          700: '#1d4ed8',
          800: '#1e40af',
          900: '#1e3a8a',
          950: '#172554'
        },
        ink: {
          900: '#0b1220',
          950: '#070c18'
        }
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'sans-serif'],
        display: ['"Space Grotesk"', 'Inter', 'ui-sans-serif', 'system-ui', 'sans-serif']
      },
      boxShadow: {
        card: '0 1px 2px rgba(16, 24, 40, 0.04), 0 8px 24px -8px rgba(16, 24, 40, 0.08)',
        'card-hover': '0 2px 4px rgba(16, 24, 40, 0.05), 0 24px 48px -16px rgba(16, 24, 40, 0.18)',
        'relief-sm': 'inset 0 1px 0 rgba(255, 255, 255, 0.9), 0 1px 3px rgba(15, 23, 42, 0.06), 0 1px 2px rgba(15, 23, 42, 0.04)',
        'relief-card': 'inset 0 1px 0 0 rgba(255, 255, 255, 0.95), 0 1px 3px 0 rgba(15, 23, 42, 0.05), 0 12px 28px -6px rgba(15, 23, 42, 0.09)',
        'relief-card-hover': 'inset 0 1px 0 0 rgba(255, 255, 255, 1), 0 0 0 1px rgba(37, 99, 235, 0.2), 0 22px 48px -10px rgba(15, 23, 42, 0.16), 0 10px 20px -4px rgba(37, 99, 235, 0.12)',
        'relief-btn-primary': 'inset 0 1px 0 0 rgba(255, 255, 255, 0.3), inset 0 -1.5px 0 0 rgba(0, 0, 0, 0.25), 0 4px 14px 0 rgba(37, 99, 235, 0.35), 0 1px 2px 0 rgba(0, 0, 0, 0.12)',
        'relief-btn-primary-hover': 'inset 0 1px 0 0 rgba(255, 255, 255, 0.4), inset 0 -1.5px 0 0 rgba(0, 0, 0, 0.3), 0 8px 24px 0 rgba(37, 99, 235, 0.45), 0 2px 4px 0 rgba(0, 0, 0, 0.15)',
        'relief-btn-white': 'inset 0 1px 0 0 rgba(255, 255, 255, 1), inset 0 -1.5px 0 0 rgba(203, 213, 225, 0.8), 0 4px 12px 0 rgba(15, 23, 42, 0.08), 0 1px 2px 0 rgba(15, 23, 42, 0.05)',
        'relief-btn-amber': 'inset 0 1px 0 0 rgba(255, 255, 255, 0.6), inset 0 -1.5px 0 0 rgba(180, 83, 9, 0.4), 0 6px 18px 0 rgba(245, 158, 11, 0.4), 0 1px 2px 0 rgba(0, 0, 0, 0.12)',
        'relief-dark': 'inset 0 1px 0 0 rgba(255, 255, 255, 0.14), inset 0 0 0 1px rgba(255, 255, 255, 0.05), 0 25px 50px -12px rgba(0, 0, 0, 0.7)',
        glow: '0 0 0 1px rgba(37, 99, 235, 0.12), 0 12px 40px -8px rgba(37, 99, 235, 0.35)',
        'glow-lg': '0 0 60px -10px rgba(37, 99, 235, 0.5), 0 0 120px -20px rgba(99, 102, 241, 0.3)'
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0)' },
          '50%': { transform: 'translateY(-12px)' }
        },
        'pulse-dot': {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.35' }
        },
        shimmer: {
          '0%': { backgroundPosition: '-200% center' },
          '100%': { backgroundPosition: '200% center' }
        },
        'spin-slow': {
          from: { transform: 'rotate(0deg)' },
          to: { transform: 'rotate(360deg)' }
        },
        'spin-slow-reverse': {
          from: { transform: 'rotate(0deg)' },
          to: { transform: 'rotate(-360deg)' }
        },
        'fade-up': {
          '0%': { opacity: '0', transform: 'translateY(20px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' }
        },
        'slide-in-right': {
          '0%': { opacity: '0', transform: 'translateX(40px)' },
          '100%': { opacity: '1', transform: 'translateX(0)' }
        }
      },
      animation: {
        float: 'float 6s ease-in-out infinite',
        'float-slow': 'float 9s ease-in-out infinite',
        'pulse-dot': 'pulse-dot 2s ease-in-out infinite',
        shimmer: 'shimmer 3s linear infinite',
        'spin-slow': 'spin-slow 20s linear infinite',
        'spin-slow-reverse': 'spin-slow-reverse 25s linear infinite',
        'fade-up': 'fade-up 0.6s ease-out forwards',
        'slide-in-right': 'slide-in-right 0.7s ease-out forwards'
      }
    }
  }
}
