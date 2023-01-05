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
            @newsletterAdd="newsletterAdd"
            @newsletterEdit="newsletterEdit"
            @newsletterDelete="newsletterDelete"
            @newsletterLaunch="newsletterLaunch"
            :newsletterData="newsletterData"
            :newsletterForm="newsletterForm"
        />
      </div>
    </div>
  </section>


</template>

<script setup>

import {useCustomersStore} from "~/stores/customers";

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

const {
  pending: pendingNewsletters,
  data: newsletters
} = await useLazyAsyncData('newsletters', () => $fetch(`${config.public.BASE_API_URL}newsletter/`))
const refreshNewsletters = () => refreshNuxtData('newsletters')


const addNewsletterDataToForm = (val) => {
  newsletterForm.value = {
    tag: 'edit',
    title: 'Редактировать рассылку',
    buttonTitle: 'Изменить',
  }
  newsletterData.value = val
}

const newsletterAdd = async () => {
  await useFetch(`${config.public.BASE_API_URL}newsletter/`,
      {
        method: 'POST',
        body: newsletterData.value,
        onResponse({request, response, options}) {
          if (response.status !== 201) {
            alert('Ошибка при добавлении клиента')
          } else {
            console.log(response._data)
            alert(`Рассылка c сообщением: ${response._data.message} - успешно добавлена`)
            refreshNewsletters();
            newsletterData.value = {}
          }
        }
      },
  )
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

const newsletterEdit = async (val) => {
  await useFetch(`${config.public.BASE_API_URL}newsletter/${newsletterData.value.id}/`,
      {
        method: 'PUT',
        body: val,
      });
  await refreshNewsletters();
  changeNewsletterFormToAdd();
}

const newsletterDelete = async (id) => {
  console.log(id)
  await useFetch(`${config.public.BASE_API_URL}newsletter/${id}/`,
      {method: 'DELETE'});
  await refreshNewsletters();
  changeNewsletterFormToAdd()
}

const convertDate = (date) => {
  return date.toISOString().slice(0, 19).replace('T', ' ')
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
  // for (let customer of customersFiltered.value) {
  if (val.is_valid) {

    await useFetch(`${config.public.BASE_API_URL}newsletter-statistic/`, {
      method: 'POST',
      body: {
        customers: customersFiltered.value,
        id: val.id,
        message: val.message,
        newsletter: val.id,
      }
    })
  }
  // }
}

</script>

<style scoped>

</style>