<template>

  <form @submit.prevent="props.newsletterForm.tag === 'add' ? newsletterAdd : newsletterEdit" class="text-gray-500">
    <h2 class="text-gray-500 text-center mb-5">{{ props.newsletterForm.title }}</h2>
    <div class="grid md:grid-cols-2 md:gap-6">
      <div class="relative z-0 mb-6 w-full group">
        <input type="text"
               id="floating-start-launch-date"
               v-model="props.newsletterData.start_launch_date"
               class="block py-2.5 px-0 w-full text-sm bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-gray-400 dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
               placeholder=" " required/>
        <label for="floating-end-launch-date"
               class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Начало
          рассылки</label>
      </div>
      <div class="relative z-0 mb-6 w-full group">
        <input type="text" name="floating-end-launch-date" id="floating-end-launch-date"
               v-model="props.newsletterData.end_launch_date"
               class="block py-2.5 px-0 w-full text-sm bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-gray-400 dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
               placeholder=" " required/>
        <label for="floating-end-launch-date"
               class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Окончание
          рассылки</label>
      </div>
    </div>
    <div class="relative z-0 mb-6">
      <input type="text" name="floating-filter" id="floating-filter"
             v-model="props.newsletterData.customer_filter"
             class="block py-2.5 px-0 w-full text-sm bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
             placeholder=" " required/>
      <label for="floating-tag"
             class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
        Фильтр</label>
    </div>
    <div class="relative z-0 mb-6">
      <input type="text" name="floating-message" id="floating-message"
             v-model="props.newsletterData.message"
             class="block py-2.5 px-0 w-full text-sm bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
             placeholder=" " required/>
      <label for="floating-message"
             class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
        Сообщение</label>
    </div>
    <div class="flex">

      <button
          v-if="props.newsletterForm.tag === 'add'"
          @click="newsletterAdd"
          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        {{ props.newsletterForm.buttonTitle }}
      </button>
      <div v-else-if="props.newsletterForm.tag === 'edit'">
        <button

            @click="newsletterEdit"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
          {{ props.newsletterForm.buttonTitle }}
        </button>
        <button
            @click="newsletterDelete"
            class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800 ml-3">
          Удалить
        </button>
        <button
            @click="newsletterLaunch"
            class="text-white bg-green-700 hover:bg-green-800 focus:ring-4 focus:outline-none focus:ring-green-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-green-600 dark:hover:bg-green-700 dark:focus:ring-green-800 ml-3">
          Запустить
        </button>
      </div>
      <div>
        <button
            @click="clearForm"
            class="text-white bg-yellow-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-yellow-600 dark:hover:bg-yellow-700 dark:focus:ring-yellow-800 ml-3">
          Очистить
        </button>
      </div>
    </div>
  </form>
</template>

<script setup>
const props = defineProps({
  newsletterData: {
    type: Object,
    required: false,
    default: () => ({
      id: null,
      start_launch_date: '',
      end_launch_date: '',
      customer_filter: '',
      message: '',
      is_valid: true,
    }),
  },
  newsletterForm: {
    type: Object,
    required: false,
    default: () => ({
      tag: 'add',
      title: '',
      buttonTitle: 'Создать',
    }),
  },
})

const newsletterData = ref({
  ...props.newsletterData,
})


const emit = defineEmits(['newsletterAdd', 'newsletterEdit', 'newsletterDelete'])

const newsletterAdd = () => {
  emit('newsletterAdd', newsletterData.value)
}

const newsletterEdit = () => {
  emit('newsletterEdit')
}

const newsletterDelete = () => {
  emit('newsletterDelete', props.newsletterData.id)
}
const clearForm = () => {
  emit('clearForm')
}

const newsletterLaunch = () => {
  if (props.newsletterData.is_valid) {
    if (confirm(`Вы уверены, что хотите запустить рассылку ${props.newsletterData.message}?`)) {
      emit('newsletterLaunch', props.newsletterData)
    }
  } else {
    alert('Невозможно запустить рассылку, так как она не прошла валидацию')
  }


}

</script>

<style scoped>

</style>