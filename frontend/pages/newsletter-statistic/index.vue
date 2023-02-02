<template>
  <div class="grid h-screen place-items-center" v-if="pendingNewslettersStatistic">
    <MainLoader/>
  </div>

  <div class="grid max-w-screen-xl py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12 mb-5" v-else v-cloak>
    <div class="place-self-center lg:col-span-6 mr-3">
      <NewsletterStatisticTable
          @viewNewsletterStatisticDetail="viewNewsletterStatisticDetail"
          :newslettersStatistic="newslettersStatistic"
      />
    </div>
    <div class="mx-auto place-self-top lg:col-span-6">
      <NewsletterStatisticDetail
          :ns="ns"
      />
    </div>
  </div>


</template>

<script setup>

import {useNewslettersStatisticStore} from "~/stores/newslettersStatistic";

const newslettersStatisticStore = useNewslettersStatisticStore();
newslettersStatisticStore.fetchNewslettersStatistic();

const newslettersStatistic = computed(() => newslettersStatisticStore.newslettersStatistic);
const pendingNewslettersStatistic = computed(() => newslettersStatisticStore.pendingNewslettersStatistic);


const ns = ref({})

const viewNewsletterStatisticDetail = (val) => {
  ns.value = val
}

</script>

<style scoped>

</style>