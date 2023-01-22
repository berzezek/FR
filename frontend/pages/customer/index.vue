<template>
  <section class="dark:bg-gray-900">
    <div class="grid h-screen place-items-center" v-if="pendingCustomers">
      <MainLoader/>
    </div>
    <div class="grid max-w-screen-xl py-8 mx-auto lg:gap-8 xl:gap-0 lg:py-16 lg:grid-cols-12 mb-16" v-else>
      <div class="place-self-center lg:col-span-6">
        <CustomerTable
            :customers="customers"
            @addCustomerDataToForm="addCustomerDataToForm"
        />
      </div>
      <div class="mx-auto place-self-top lg:col-span-6">
        <CustomerForm
            @customerAdd="customerAdd"
            @customerEdit="customerEdit"
            @clearForm="changeCustomerFormToAdd"
            @customerDelete="customerDelete"
            :customerData="customerData"
            :customerForm="customerForm"
        />
      </div>
    </div>
  </section>


</template>

<script setup>

import {useCustomersStore} from "~/stores/customers";

const customersStore = useCustomersStore();
customersStore.fetchCustomers();
const customers = computed(() => customersStore.customers);
const pendingCustomers = computed(() => customersStore.pendingCustomers);

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

const addCustomerDataToForm = (val) => {
  customerData.value = val
  customerForm.value = {
    tag: 'edit',
    title: 'Редактировать клиента',
    buttonTitle: 'Изменить',
  }
}

const customerAdd = async () => {
  await customersStore.addCustomer(customerData.value)
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
  await customersStore.updateCustomer(customerData.value)
  changeCustomerFormToAdd()
}


const customerDelete = async (id) => {
  await customersStore.deleteCustomer(id)
}

</script>

<style scoped>

</style>