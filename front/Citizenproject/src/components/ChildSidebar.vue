<template>
  <div class="block_title">
    <div class="main_page_logo">
      <router-link to="/home" class="navBurger" role="navigation" id="navToggle"></router-link>
      <router-link to="/home" class="main_page_text"><span>Главная </span>страница</router-link>
    </div>
    <div class="main_title inner_transform">
      <p class="inner_title ">Липецкгражданпроект</p>
      <p class="big_title">{{sideTitle}} </p>
    </div>
  </div>
</template>

<script>
  export default {
    name: "ChildSidebar",
    computed: {
      sideTitle: function () {
        if (this.$route.meta['title'])
          return this.$route.meta['title']
        else
          return "" //дефолтный заголовок
      }
    }
  }
</script>

<style scoped>

</style>
