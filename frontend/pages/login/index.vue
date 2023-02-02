<template>
  <div class="grid h-screen place-items-center" v-if="pendingUser">
    <MainLoader/>
  </div>
  <div v-else class="relative w-full max-w-md h-full md:h-auto mx-auto">
    <LoginForm
        :isRegister="registerForm"
        @sendFormData="sendFormData"
        @switchForm="switchForm"
    />
  </div>
</template>


<script setup>

import {useUserStore} from "~/stores/login";
import {onMounted} from 'vue'
import {
  initModals,
} from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
  initModals();
})

const router = useRouter();
const registerForm = ref(false);

const userStore = useUserStore();
const pendingUser = computed(() => userStore.pendingUser);
const sendFormData = async (user, isRegister) => {
  if (isRegister) {
    await userStore.signUser(user.value);
    await userStore.fetchUser();
    await router.push('/')
  } else {
    await userStore.loginUser(user.value);
    await userStore.fetchUser();
    await router.push('/');
  }
}
const oauthLogin = async () => {
  await userStore.loginOauth(user.value);
  await router.back();
}

const switchForm = () => {
  registerForm.value = !registerForm.value;
}

</script>