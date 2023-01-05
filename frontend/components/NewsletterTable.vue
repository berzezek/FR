<template>

  <div class="overflow-x-auto relative shadow-md sm:rounded-lg mb-12">
    <h3 class="text-center mb-2">Список рассылок</h3>
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
             @click="changeNewsletterFormToAdd">
      <tr>
        <th scope="col" class="py-3 px-6">
          Начало рассылки
        </th>
        <th scope="col" class="py-3 px-6">
          Окончание рассылки
        </th>
        <th scope="col" class="py-3 px-6">
          Фильтр
        </th>
        <th scope="col" class="py-3 px-6">
          Сообщение
        </th>
      </tr>
      </thead>
      <tbody>
      <tr
          v-for="newsletter in newsletters" :key="newsletter.id"
          @click="addNewsletterDataToForm(newsletter)"
          class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
        <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
          {{ convertDate(newsletter.start_launch_date) }}
        </th>
        <td class="py-4 px-6">
          {{ convertDate(newsletter.end_launch_date) }}
        </td>
        <td class="py-4 px-6 text-right">
          {{ newsletter.customer_filter }}
        </td>
        <td class="py-4 px-6 text-right">
          {{ newsletter.message }}
        </td>
      </tr>

      </tbody>
    </table>
  </div>

</template>

<script setup lang="ts">

const props = defineProps({
  newsletters: {
    type: Array,
    required: true,
    default: () => [],
  },
})

const emit = defineEmits(['addNewsletterDataToForm', 'changeNewsletterFormToAdd'])

const addNewsletterDataToForm = (newsletter: any) => {
  emit('addNewsletterDataToForm', newsletter)
}

const changeNewsletterFormToAdd = () => {
  emit('changeNewsletterFormToAdd')
}

const convertDate = (date: Date) => {
  return new Date(date).toLocaleString('ru-RU', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
    second: '2-digit',
  })
}

</script>

<style scoped>

</style>