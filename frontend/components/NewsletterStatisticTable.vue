<template>
  <section class="dark:bg-gray-900">
    <div class="grid h-screen place-items-center" v-if="pendingNewsletterStatistic">
      <MainLoader/>
    </div>
    <div class="overflow-x-auto relative shadow-md sm:rounded-lg mb-12" v-cloak>
      <div class="mb-8 text-center">
        <label for="searchNewsletterStatisticById">Фильтр по ID</label>
        <input type="number" id="searchNewsletterStatisticById"
               class="w-full border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none mt-2"
               placeholder="Введите id рассылки" v-model="searchQuery" @input="searchNewsletterStatisticById">
      </div>

      <h3 class="text-center mb-2">Список запущенных рассылок</h3>
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
            v-for="ns in newslettersStatisticBySearch" :key="ns.id"
            @click="viewNewsletterStatisticDetail(ns)"
            :class="                                                                                                                  isDateExpired(ns.newsletter.start_launch_date, ns.newsletter.end_launch_date)">
          <th scope="row" class="py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white">
            {{ ns.id }}
          </th>
          <td class="py-4 px-6">
            {{ convertDate(ns.newsletter.start_launch_date) }}
          </td>
          <td class="py-4 px-6">
            {{ convertDate(ns.newsletter.end_launch_date) }}
          </td>

        </tr>

        </tbody>
      </table>
    </div>
  </section>

</template>

<script setup>

import { convertDate } from "../mixins/convertDate";

import {useNewslettersStatisticStore} from "../stores/newslettersStatistic";

const newslettersStatisticStore = useNewslettersStatisticStore()
newslettersStatisticStore.fetchNewslettersStatistic()
const newslettersStatistic = computed(() => newslettersStatisticStore.newslettersStatistic)
const pendingNewsletterStatistic = computed(() => newslettersStatisticStore.pendingNewslettersStatistic)


const emit = defineEmits(['viewNewsletterStatisticDetail'])

const props = defineProps({
  newslettersStatistic: {
    type: Array,
    required: false
  }
})

const searchQuery = ref('');

const newslettersStatisticBySearch = computed(() => newslettersStatistic.value.filter((ns) => {
  return ns.id.toString().includes(searchQuery.value);
}));

const viewNewsletterStatisticDetail = (ns) => {
  emit('viewNewsletterStatisticDetail', ns)
}

const searchNewsletterStatisticById = (event) => {
  searchQuery.value = event.target.value;
}


const isDateExpired = (start_date, end_date) => {
  if (new Date(end_date) < new Date()) {
    return 'bg-red border-b dark:bg-red-800 dark:border-gray-700 hover:bg-red-900 dark:hover:bg-red-600'
  } else if (new Date(start_date) > new Date()) {
    return 'bg-green border-b dark:bg-green-800 dark:border-gray-700 hover:bg-green-900 dark:hover:bg-green-600'
  } else {
    return 'bg-gray border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-yellow-900 dark:hover:bg-gray-600'
  }
}

</script>

<style scoped>

</style>