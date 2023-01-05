<template>
  <section class="dark:bg-gray-900">
    <div class="place-self-center" v-if="pendingNewsletters">
      <div class="text-center">
        <div role="status">
          <svg class="inline mr-2 w-8 h-8 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600"
               viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor"/>
            <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill"/>
          </svg>
          <span class="sr-only">Loading...</span>
        </div>
      </div>
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