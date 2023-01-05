<template>
  <section class="dark:bg-gray-900">
    <div class="grid h-screen place-items-center" v-if="pendingNewslettersStatistic">
      <MainLoader/>
    </div>

    <div class="grid max-w-screen-xl py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12" v-else>
      <div class="place-self-center lg:col-span-6 mr-3">
        <NewsletterStatisticTable
            @viewNewsletterStatisticDetail="viewNewsletterStatisticDetail"
            :newslettersStatistic="newslettersStatistic"
        />
      </div>
      <div class="place-self-top lg:col-span-6 mr-3">
        <NewsletterStatisticDetail
            :ns="ns"
        />
      </div>
    </div>
  </section>


</template>

<script setup>

const config = useRuntimeConfig()

const {
  pending: pendingNewslettersStatistic,
  data: newslettersStatistic
} = await useLazyAsyncData('newslettersStatistic', () => $fetch(`${config.public.BASE_API_URL}newsletter-statistic/`))

const ns = ref({})

const viewNewsletterStatisticDetail = (val) => {
  ns.value = val
}

</script>

<style scoped>

</style>