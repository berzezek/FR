<template>
  <section class="">
    <div class="grid h-screen place-items-center" v-if="pendingNewsletterStatistic">
      <MainLoader/>
    </div>
    <div class="overflow-x-auto relative shadow-md sm:rounded-lg mb-12" v-cloak>
      <div class="pb-4 ">
        <label for="table-search" class="sr-only">Search</label>
        <div class="relative mt-1">
          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
            <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" aria-hidden="true" fill="currentColor"
                 viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd"
                    d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                    clip-rule="evenodd"></path>
            </svg>
          </div>
          <input type="text" id="table-search"
                 class="block p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                 v-model="searchQuery" @input="searchNewsletterStatisticById"
                 placeholder="Введите id рассылки">
        </div>
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
            :class="isDateExpired(ns.newsletter.start_launch_date, ns.newsletter.end_launch_date)">
          <th scope="row" class="py-4 px-6 font-medium whitespace-nowrap dark:text-white">
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

import {convertDate} from "../mixins/convertDate";

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