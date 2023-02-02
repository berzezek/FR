// https://v3.nuxtjs.org/api/configuration/nuxt.config
export default defineNuxtConfig({
    runtimeConfig: {
        public: {}
    },
    css: ['~/assets/css/main.css'],
    postcss: {
        plugins: {
            tailwindcss: {},
            autoprefixer: {},
        },
    },
    modules: [
        '@pinia/nuxt',
        '@nuxtjs/tailwindcss'
    ],
    vite: {
        server: {
            hmr: {
                protocol: 'http',
                // port: 8000
            }
        },
    },
})