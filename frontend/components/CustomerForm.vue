<template>

  <form @submit.prevent="props.customerForm.tag === 'add' ? customerAdd : customerEdit" class="text-gray-500">
    <h2 class="text-gray-500 text-center mb-5">{{ props.customerForm.title }}</h2>
    <div class="grid md:grid-cols-2 md:gap-6">
      <div class="relative z-0 mb-6 w-full group">
        <input type="tel" pattern="[0-9]{3}" name="floating_phone_prefix"
               id="floating_phone_prefix"
               v-model="props.customerData.phone_prefix"
               class="block py-2.5 px-0 w-full text-sm bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
               placeholder=" " required/>
        <label for="floating_phone_prefix"
               class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Код
          телефона</label>
      </div>
      <div class="relative z-0 mb-6 w-full group">
        <input type="tel" pattern="[0-9]{10}" name="floating_phone" id="floating_phone"
               v-model="props.customerData.phone_number"
               class="block py-2.5 px-0 w-full text-sm bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
               placeholder=" " required/>
        <label for="floating_phone"
               class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Номер
          телефона</label>
      </div>
    </div>

    <div class="relative z-0 mb-6 group">
      <input type="text" name="floating_tag" id="floating_tag"
             v-model="props.customerData.tag"
             class="block py-2.5 px-0 w-full text-sm bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
             placeholder=" " required/>
      <label for="floating_tag"
             class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
        Тег</label>
    </div>
    <div class="relative z-0 mb-6 group">
      <label for="countries" class="block mb-2 text-sm font-medium dark:text-white">Select an
        option</label>
      <select id="countries"
              v-model="props.customerData.customer_time_zone"
              class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
        <option selected disabled value="">Choose a timezone</option>
        <option v-for="timezone in timezones" :value="timezone">{{ timezone }}</option>
      </select>
    </div>

    <button
        v-if="props.customerForm.tag === 'add'"
        @click="customerAdd"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
      {{ props.customerForm.buttonTitle }}
    </button>
    <div v-else-if="props.customerForm.tag === 'edit'">
      <button

          @click="customerEdit"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        {{ props.customerForm.buttonTitle }}
      </button>
      <button
          @click="customerDelete"
          class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800 ml-3">
        Удалить
      </button>
    </div>

  </form>
</template>

<script setup>
const props = defineProps({
  customerData: {
    type: Object,
    required: true,
    default: () => ({
      id: null,
      phone_prefix: '',
      phone_number: '',
      tag: '',
      customer_time_zone: '',
    }),
  },
  customerForm: {
    type: Object,
    required: true,
    default: () => ({
      tag: 'add',
      title: '',
      buttonTitle: '',
    }),
  },
})

const customerData = ref({
  ...props.customerData,
})

const timezones = [
  'Europe/London',
  'Europe/Paris',
  'Europe/Berlin',
  'Europe/Moscow',
]

const emit = defineEmits(['customerAdd', 'customerEdit', 'customerDelete'])

const customerAdd = () => {
  emit('customerAdd', customerData.value)
}

const customerEdit = () => {
  emit('customerEdit')
}

const customerDelete = () => {
  emit('customerDelete', props.customerData.id)
}


</script>

<style scoped>

</style>