<template>
  <section class="dark:bg-gray-900">
    <div class="mr-auto place-self-center" v-if="pendingCustomers">
      Loading...
    </div>
    <div class="grid max-w-screen-xl py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12" v-else>
      <div class="place-self-center lg:col-span-6">
        <CustomerTable
            :customers="customers"
            @addCustomerDataToForm="addCustomerDataToForm"
            @changeCustomerFormToAdd="changeCustomerFormToAdd"
        />
      </div>
      <div class="mx-auto place-self-top lg:col-span-6">
        <CustomerForm
            @customerAdd="customerAdd"
            @customerEdit="customerEdit"
            @customerDelete="customerDelete"
            :customerData="customerData"
            :customerForm="customerForm"
        />
      </div>
    </div>
  </section>


</template>

<script setup>

// const customersStore = useCustomersStore();
// customersStore.fetchCustomers();
// const myCustomer = computed(() => customersStore.customers);

const customerData = ref({
  id: null,
  phone_number: '',
  phone_prefix: '',
  tag: '',
  customer_time_zone: '',
})

const customerForm = ref({
  tag: 'add',
  title: 'Добавить клиента',
  buttonTitle: 'Создать',
})

const timezones = [
  'Europe/London',
  'Europe/Paris',
  'Europe/Berlin',
  'Europe/Moscow',
]

const config = useRuntimeConfig()

const {
  pending: pendingCustomers,
  data: customers
} = await useLazyAsyncData('customers', () => $fetch(`${config.public.BASE_API_URL}customer/`))
const refreshCustomers = () => refreshNuxtData('customers')


const addCustomerDataToForm = (val) => {
  customerData.value = val
  customerForm.value = {
    tag: 'edit',
    title: 'Редактировать клиента',
    buttonTitle: 'Изменить',
  }
}

const customerAdd = async () => {
  await useFetch(`${config.public.BASE_API_URL}customer/`,
      {
        method: 'POST',
        body: customerData.value,
        onResponse({request, response, options}) {
          if (response.status > 299) {
            alert('Ошибка при добавлении клиента')
          } else {
            console.log(response._data)
            alert(`Клиент c номером: ${response._data.phone_number} - успешно добавлен`)
            refreshCustomers();
            customerData.value = {}
          }
        }
      },
  )
}

const changeCustomerFormToAdd = () => {
  customerData.value = {
    id: null,
    phone_number: '',
    phone_prefix: '',
    tag: '',
    customer_time_zone: '',
  }
  customerForm.value = {
    tag: 'add',
    title: 'Добавить клиента',
    buttonTitle: 'Создать',
  }
}

const customerEdit = async () => {
  console.log(customerData.value)
  await useFetch(`${config.public.BASE_API_URL}customer/${customerData.value.id}/`,
      {
        method: 'PUT',
        body: customerData.value,
      });
  await refreshCustomers();
  changeCustomerFormToAdd();
}

const customerDelete = async (id) => {
  console.log(id)
  await useFetch(`${config.public.BASE_API_URL}customer/${id}/`,
      {method: 'DELETE'});
  await refreshCustomers();
  changeCustomerFormToAdd()
}

</script>

<style scoped>

</style>