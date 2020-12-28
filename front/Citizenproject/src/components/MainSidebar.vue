<template>
  <div class="block_title">
    <div class="main_page_logo">
      <router-link to="/home" class="navBurger" role="navigation" id="navToggle"></router-link>
      <router-link to="/home" class="main_page_text"><span>Главная </span>страница</router-link>
    </div>
    <div class="main_title">
      <p class="small_title">АО «Проектный институт» </p>
      <p class="big_title">Липецк-<br/>гражданпроект </p>
    </div>
  </div>
</template>

<script>
    export default {
        name: "MainSidebar"
    }
</script>

<style scoped>

</style>
