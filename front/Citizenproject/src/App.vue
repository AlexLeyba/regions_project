<template>
  <section class="main" :class="{long: isLong}">
    <router-view name="sidebar"></router-view>
    <router-view name="content"></router-view>
  </section>
</template>

<script>
  export default {
    name: "App",
    computed:{
      isLong: function () {
        if (this.$route.meta['isLongStyle'])
          return  this.$route.meta['isLongStyle']
        else
          return  false
      }
    }
}
</script>

<style scoped>

</style>
