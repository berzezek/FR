<template>
  <section class="dark:bg-gray-900">
    <div class="grid h-screen place-items-center" v-if="pendingNewsletters">
      <MainLoader/>
    </div>
    <div class="grid max-w-screen-xl py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12" v-else>
      <div class="place-self-center lg:col-span-6 mr-3">
        <NewsletterTable
            :newsletters="newsletters"
            @addNewsletterDataToForm="addNewsletterDataToForm"
            @changeNewsletterFormToAdd="changeNewsletterFormToAdd"
        />
      </div>
      <div class="mx-auto place-self-top lg:col-span-6">
        <NewsletterForm
            :newsletterData="newsletterData"
            :newsletterForm="newsletterForm"
            @newsletterAdd="newsletterAdd"
            @newsletterEdit="newsletterEdit"
            @newsletterDelete="newsletterDelete"
            @newsletterLaunch="newsletterLaunch"
            @clearForm="changeNewsletterFormToAdd"
        />
      </div>
    </div>
  </section>


</template>

<script setup>

import {useCustomersStore} from "~/stores/customers";
import {useNewslettersStore} from "~/stores/newsletters";

const newslettersStore = useNewslettersStore();
newslettersStore.fetchNewsletters();
const newsletters = computed(() => newslettersStore.newsletters)
const pendingNewsletters = computed(() => newslettersStore.pendingNewsletters)

const newsletterData = ref({
  id: null,
  start_launch_date: new Date().toISOString().slice(0, 19).replace('T', ' '),
  end_launch_date: new Date(new Date().getTime() + 24 * 60 * 60 * 1000).toISOString().slice(0, 19).replace('T', ' '),
  customer_filter: '',
  message: '',
})

const newsletterForm = ref({
  tag: 'add',
  title: 'Добавить рассылку',
  buttonTitle: 'Создать',
})

const config = useRuntimeConfig()

const addNewsletterDataToForm = (val) => {
  newsletterData.value = val
  newsletterForm.value = {
    tag: 'edit',
    title: 'Редактировать рассылку',
    buttonTitle: 'Изменить',
  }
}

const newsletterAdd = async () => {
  newslettersStore.addNewsletter(newsletterData.value)
  newslettersStore.fetchNewsletters()
}

const changeNewsletterFormToAdd = () => {
  newsletterData.value = {
    id: null,
    start_launch_date: new Date().toISOString().slice(0, 19).replace('T', ' '),
    end_launch_date: new Date(new Date().getTime() + 24 * 60 * 60 * 1000).toISOString().slice(0, 19).replace('T', ' '),
    customer_filter: '',
    message: '',
  }
  newsletterForm.value = {
    tag: 'add',
    title: 'Добавить клиента',
    buttonTitle: 'Создать',
  }
}

const newsletterEdit = async () => {
  newslettersStore.updateNewsletter(newsletterData.value)
  newslettersStore.fetchNewsletters()
}

const newsletterDelete = async (id) => {
  await newslettersStore.deleteNewsletter(id)
  await newslettersStore.fetchNewsletters()
}

const newsletterLaunch = async (val) => {
  const customersStore = useCustomersStore();
  await customersStore.fetchCustomers();
  const customers = computed(() => customersStore.customers);
  const customersFiltered = computed(() => {
    return customers.value.filter((customer) => {
      return customer.tag === val.customer_filter
    })
  })
  if (val.is_valid) {
    newslettersStore.launchNewsletter(val.id, customersFiltered.value, val.message)
  } else {
    alert('Невозможно запустить рассылку, так как дата окончания рассылки меньше текущей даты')
  }
}

</script>

<style scoped>

</style>