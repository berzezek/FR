<template>
  <div class="max-w-screen-xl mx-auto lg:gap-12 xl:gap-0 lg:py-16 lg:grid-cols-12 mb-16">
    <form @submit.prevent>
      <div class="mb-6">
        <label for="login" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your login</label>
        <input type="text" id="login"
               class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
               v-model="user.username"
               placeholder="name@fr.com" required>
      </div>
      <div class="mb-6">
        <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your password</label>
        <input type="password" id="password"
               class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
               v-model="user.password"
               required>
      </div>
      <button @click="loginUser"
              class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        Submit
      </button>
      <button @click="oauthLogin"
              class="ml-3 text-white bg-yellow-700 hover:bg-yellow-800 focus:ring-4 focus:outline-none focus:ring-yellow-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-yellow-600 dark:hover:bg-yellow-700 dark:focus:ring-yellow-800">
        OAuth
      </button>
    </form>
  </div>

</template>

<script setup>

import {useUserStore} from "~/stores/login";

const router = useRouter();

const user = ref(
    {
      username: 'berzezek',
      password: 'alpine12',
    }
)

const userStore = useUserStore();
const loginUser = async () => {
  await userStore.loginUser(user.value);
  await userStore.fetchUser()
  await router.push('/newsletter')
}
const oauthLogin = async () => {
  await userStore.loginOauth(user.value);
}
</script>

<style scoped>

</style>