<template>
  <section class="dark:bg-gray-900">
    <div class="grid max-w-screen-xl px-4 py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12">
      <div v-if="pending">
        Loading...
      </div>

      <div class="mr-auto place-self-center lg:col-span-6" v-else>
        <CustomerTable
            :customers="customers"
            @editCustomer="editCustomer"
        />
      </div>
      <div class="mr-auto place-self-top lg:col-span-6">
        <CustomerForm
            @customerAdd="customerAdd"
            :customerData="customerData"
            :customerForm="customerForm"
        />
      </div>
    </div>
  </section>


</template>

<script setup>

const customerData = ref({
  phone_number: '',
  phone_prefix: '',
  tag: '',
  customer_time_zone: '',
})

const customerForm = ref({
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
  pending,
  data: customers
} = await useLazyAsyncData('customers', () => $fetch(`${config.public.BASE_API_URL}customer/`))
const refresh = () => refreshNuxtData('customers')

const customerAdd = async (customerData) => {
  await useFetch(`${config.public.BASE_API_URL}customer/`,
      {
        method: 'POST',
        body: customerData.value,
      });
  await refresh();
  customerData.value = {
    phone_number: '',
    phone_prefix: '',
    tag: '',
    customer_time_zone: '',
  }
}


const editCustomer = async (val) => {
  customerData.value = val
  console.log(customerData.value)
  customerForm.value = {
    title: 'Редактировать клиента',
    buttonTitle: 'Сохранить',
  }
}
</script>

<style scoped>

</style>