<template>
  <div class="z-50 w-full p-4 overflow-y-auto md:inset-0 h-modal md:h-full">
    <div class="relative w-full h-full max-w-md md:h-auto">
      <!-- Modal content -->
      <div class="relative bg-white rounded-lg shadow dark:bg-gray-700">
        <div class="px-6 py-6 lg:px-8">
          <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white text-center">
            {{ props.isRegister ? 'Регистрация' : 'Вход' }}
          </h3>

          <form class="space-y-6" @submit.prevent="sendFormData">
            <div>
              <label for="login" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                Ваш логин</label>
              <input type="text" name="username" id="username"
                     v-model="user.username"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                     placeholder="Ваш логин" required>
            </div>
            <div>
              <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
                Ваш пароль</label>
              <input type="password" name="password" id="password" placeholder="••••••••"
                     v-model="user.password"
                     class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                     required>
            </div>
            <button type="submit"
                    class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
              {{ props.isRegister ? 'Зарегистрироваться' : 'Войти' }}
            </button>
            <button type="submit"
                    class="w-full text-white bg-yellow-700 hover:bg-yellow-800 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-yellow-600 dark:hover:bg-yellow-700 dark:focus:ring-yellow-800">
              OAUTH2.0
            </button>
            <div
                class="text-sm font-medium text-primary-500 dark:text-primary-300"
                @click="switchForm"
            >
              {{ props.isRegister ? 'Уже есть аккаунт?' : 'Нет аккаунта?' }}
            </div>
          </form>

        </div>
      </div>
    </div>
  </div>

</template>

<script setup>

const props = defineProps({
  isRegister: {
    type: Boolean,
    default: false
  }
})

const user = ref({
  username: '',
  password: ''
})

const emit = defineEmits(['sendFormData', 'switchForm'])
const sendFormData = () => {
  emit('sendFormData', user, props.isRegister)
}
const switchForm = () => {
  emit('switchForm')
}

</script>

<style scoped>

</style>