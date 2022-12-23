<template>
  <div class="flex-1 w-full h-full flex items-center justify-center p-4">
    <div
        class="max-w-[500px] overflow-hidden bg-black text-primary-100 bg-opacity-10 border border-primary-800 border-opacity-50 text-center rounded-lg">
      <div class="px-8 pb-8 pt-4"><h1 class="text-2xl font-bold mb-4">Тестовое задание</h1>
        <p class="text-primary-300"></p></div>
      <div
          class="flex flex-col md:flex-row items-center h-24 md:h-12 bg-black bg-opacity-20 border-t border-primary-800 border-opacity-50">
        <nuxt-link class="flex items-center justify-center gap-2 h-full flex-1 hover:text-emerald-500"
                   to="https://www.craft.do/s/n6OVYFVUpq0o6L" target="_blank">
          Просмотр задания
        </nuxt-link>
        <div class="w-full h-[1px] md:h-full md:w-[1px] bg-primary-800 bg-opacity-50"></div>
        <a class="flex items-center justify-center gap-2 h-full flex-1 hover:text-emerald-500"
           href="#" target="_blank">
          <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" aria-hidden="true"
               role="img" class="icon relative -top-[1px]" width="20px" height="20px" viewBox="0 0 24 24"
               data-v-ca945699="">
            <path fill="currentColor"
                  d="M12 2A10 10 0 0 0 2 12c0 4.42 2.87 8.17 6.84 9.5c.5.08.66-.23.66-.5v-1.69c-2.77.6-3.36-1.34-3.36-1.34c-.46-1.16-1.11-1.47-1.11-1.47c-.91-.62.07-.6.07-.6c1 .07 1.53 1.03 1.53 1.03c.87 1.52 2.34 1.07 2.91.83c.09-.65.35-1.09.63-1.34c-2.22-.25-4.55-1.11-4.55-4.92c0-1.11.38-2 1.03-2.71c-.1-.25-.45-1.29.1-2.64c0 0 .84-.27 2.75 1.02c.79-.22 1.65-.33 2.5-.33c.85 0 1.71.11 2.5.33c1.91-1.29 2.75-1.02 2.75-1.02c.55 1.35.2 2.39.1 2.64c.65.71 1.03 1.6 1.03 2.71c0 3.82-2.34 4.66-4.57 4.91c.36.31.69.92.69 1.85V21c0 .27.16.59.67.5C19.14 20.16 22 16.42 22 12A10 10 0 0 0 12 2Z"></path>
          </svg>
          Репозиторий</a></div>
    </div>
  </div>
</template>

<script>
import MainNav from "~/components/MainNav.vue";

export default {
  name: "index",
  components: {MainNav}
}
</script>

<style scoped>

</style>