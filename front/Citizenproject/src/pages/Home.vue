<template>
  <div class="main_content">
    <div class="content_block">
      <ul class="nav">
        <li class="first_nav">
          <router-link to="/activities">
            <!-- <img src="../../imgs/1.png" alt=""> -->
            <div class="nav_img activ_img"></div>
            <div class="home_title">Виды деятельности</div>
            <div class="home_title_red">Виды деятельности</div>
          </router-link>
        </li>
        <li class="second_nav">
          <router-link to="/news">
            <!-- <img src="../../imgs/4.png" alt=""> -->
            <div class="nav_img news_img"></div>
            <div class="home_title">Новости</div>
            <div class="home_title_red">Новости</div>

          </router-link>
        </li>
        <li class="third_nav">
          <router-link to="/docs">
            <!-- <img src="../../imgs/3.png" alt=""> -->
            <div class="nav_img about_img"></div>
            <div class="home_title">Нормативные документы</div>
            <div class="home_title_red">Нормативные документы</div>

          </router-link>
        </li>
        <li class="fourth_nav">
          <router-link to="/projects">
            <!-- <img src="../../imgs/4.png" alt=""> -->
            <div class="nav_img proj_img"></div>
            <div class="home_title">Проекты</div>
            <div class="home_title_red">Проекты</div>
          </router-link>
        </li>


      </ul>
      <div class="main_page_credits">
        <div class="mp_credits_left">
          <p class="mp_credits_text_title">Липецкгражданпроект</p>
          <p class="mp_credits_text">Старейшая проектная организация в сфере жилого и гражданского строительства, основанная в 1954 году. Мы осуществляем все виды проектных работ, в том числе благоустройство, озеленение  и инженерные коммуникации.</p>
        </div>
        <div class="mp_credits_right">
          <p class="mp_credits_address"><img src="../../imgs/marker.png" alt="">Россия, Липецкая область, г. Липецк, пл. Победы, д. 8 </p>
          <p class="mp_credits_phone"><img src="../../imgs/phone.png" alt="">+7 (4742) 77-43-54</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Home",
}

</script>
<style scoped>
</style>
