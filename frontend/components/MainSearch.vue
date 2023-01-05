<template>
    <div class="mb-8 text-center">
      <label for="searchById">Фильтр по ID</label>
      <input type="number" id="searchById"
             class="w-full border-2 border-gray-300 bg-white h-10 px-5 pr-16 rounded-lg text-sm focus:outline-none"
             placeholder="Введите id рассылки" v-model="searchQuery" @input="searchById">
    </div>
</template>

<script setup>

const emit = defineEmits(['searchById'])

const searchQuery = ref('');

const searchById = () => {
  emit('searchById', searchQuery.value)
}

</script>

<style scoped>

</style>