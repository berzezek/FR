<template>

  <div class="overflow-x-auto relative shadow-md sm:rounded-lg mb-12" v-cloak>
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400"
             >
      <tr>
        <th scope="col" class="py-3 px-6">
          Рассылка
        </th>
        <th scope="col" class="py-3 px-6">
          Начало рассылки
        </th>
        <th scope="col" class="py-3 px-6">
          Конец рассылки
        </th>

      </tr>
      </thead>
      <tbody>
      <tr
          v-for="ns in newslettersStatistic"
          class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
        <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
          {{ ns.id }}
        </th>
        <td class="py-4 px-6">
          {{ ns.newsletter.start_launch_date}}
        </td>
        <td class="py-4 px-6">
          {{ ns.newsletter.end_launch_date}}
        </td>

      </tr>

      </tbody>
    </table>
  </div>

</template>

<script setup lang="ts">
import { useNewslettersStatisticStore } from "~/stores/newslettersStatistic";

const newslettersStatisticStore = useNewslettersStatisticStore();
newslettersStatisticStore.fetchNewslettersStatistic();
const newslettersStatistic = computed(() => newslettersStatisticStore.newslettersStatistic);


</script>

<style scoped>

</style>