<template>

  <div class="overflow-x-auto relative shadow-md sm:rounded-lg mb-12">
    <h3 class="text-center mb-2">Список клиентов</h3>
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
      <tr>
        <th scope="col" class="py-3 px-6">
          Номер телефона
        </th>
        <th scope="col" class="py-3 px-6">
          код страны
        </th>
        <th scope="col" class="py-3 px-6">
          Тег
        </th>
        <th scope="col" class="py-3 px-6">
          Время
        </th>
      </tr>
      </thead>
      <tbody>
      <tr
          v-for="customer in customers" :key="customer.id"
          @click="addCustomerDataToForm(customer)"
          class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
        <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
          {{ customer.phone_number }}
        </th>
        <td class="py-4 px-6">
          {{ customer.phone_prefix }}
        </td>
        <td class="py-4 px-6 text-right">
          {{ customer.tag }}
        </td>
        <td class="py-4 px-6 text-right">
          {{ customer.customer_time_zone }}
        </td>
      </tr>

      </tbody>
    </table>
  </div>

</template>

<script setup lang="ts">

const props = defineProps({
  customers: {
    type: Array,
    required: true,
    default: () => [],
  },
})

const emit = defineEmits(['addCustomerDataToForm'])

const addCustomerDataToForm = (customer: any) => {
  emit('addCustomerDataToForm', customer)
}

</script>

<style scoped>

</style>