// https://nuxt.com/docs/api/configuration/nuxt-config
// Куда проксировать /api. В docker это имя сервиса, на хосте можно переопределить
// через NUXT_API_PROXY_TARGET=http://localhost:8000
const apiProxyTarget = process.env.NUXT_API_PROXY_TARGET ?? "http://backend:80";

export default defineNuxtConfig({
  modules: ["@nuxt/eslint", "@nuxt/ui", "@vueuse/nuxt"],

  devtools: {
    enabled: true,
  },

  css: ["~/assets/css/main.css"],

  nitro: {
    // useFetch("/api/...") на SSR уходит не в сеть, а во внутренний h3-обработчик
    // Nuxt. Без devProxy он отдаёт 404 "Page not found".
    // devProxy отрезает совпавший префикс, поэтому /api/v1/home/ -> /v1/home/
    devProxy: {
      "/api": {
        target: `${apiProxyTarget}`,
        changeOrigin: true,
      },
    },
  },

  routeRules: {
    // То же самое для production-сборки (nuxt build/start):
    // /api/v1/home/ -> /v1/home/
    "/api/**": {
      proxy: `${apiProxyTarget}/**`,
    },
  },

  compatibilityDate: "2026-06-30",

  eslint: {
    config: {
      stylistic: {
        commaDangle: "never",
        braceStyle: "1tbs",
      },
    },
  },

  vite: {
    optimizeDeps: {
      include: ["@tanstack/table-core", "date-fns", "zod"],
    },
  },
});
