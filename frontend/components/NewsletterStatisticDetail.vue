<template>
  <div v-if="ns.id">

    <h2 class="my-3 text-center" >Детали рассылки - {{ ns.id }}</h2>
    <div class="overflow-x-auto relative shadow-md sm:rounded-lg mb-8" v-cloak>

      <h4 class="text-center mb-2">Клиенты для рассылки</h4>
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
        >
        <tr>
          <th scope="col" class="py-3 px-6">
            Номер телефона
          </th>
          <th scope="col" class="py-3 px-6">
            Тег
          </th>
          <th scope="col" class="py-3 px-6">
            Временная зона
          </th>

        </tr>
        </thead>
        <tbody>
        <tr
            v-for="customer in ns.customer_to_send" :key="customer.id"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
          <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
            {{ customer.phone_number }}
          </th>
          <td class="py-4 px-6">
            {{ customer.tag }}
          </td>
          <td class="py-4 px-6">
            {{ customer.customer_time_zone }}
          </td>

        </tr>

        </tbody>
      </table>
      <h4 class="text-center mt-8 mb-2">Получили рассылку</h4>
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
        >
        <tr>
          <th scope="col" class="py-3 px-6">
            Номер телефона
          </th>
          <th scope="col" class="py-3 px-6">
            Тег
          </th>
          <th scope="col" class="py-3 px-6">
            Временная зона
          </th>

        </tr>
        </thead>
        <tbody>
        <tr
            v-for="customer in ns.customer_send" :key="customer.id"
            class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
          <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
            {{ customer.phone_number }}
          </th>
          <td class="py-4 px-6">
            {{ customer.tag }}
          </td>
          <td class="py-4 px-6">
            {{ customer.customer_time_zone }}
          </td>

        </tr>

        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
const props = defineProps<{
  ns: any;
}>();

</script>

<style scoped>

</style>