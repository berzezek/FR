<template>

    <MainNav/>
    <slot/>
    <MainFooter/>

</template>

<script>
export default {
  name: "default"
}
</script>

<style scoped>
/*div {*/
/*  display: flex;*/
/*  flex-direction: column;*/
/*  min-height: 100vh;*/
/*  background-color: rgb(17, 24, 39, 1);*/
/*}*/
</style>