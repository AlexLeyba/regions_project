<template>
  <div class="inner_content">
    <div class="content_block">
      <p class="inner_header">Новости</p>
      <a class="back_link" @click="$router.go(-1)"><img alt="" class="back_arrow" src="../../imgs/back2.png">Вернуться назад
      </a>
      <div class="news">
        <router-link v-for="item in all_news" :to="'/new/'+item.id" :key="item.id" class="new_item">
          <div class="new_img">
            <img :src="item.image" alt="">
          </div>
          <div class="new_content">
            <p class="news_title">{{ item.title }}</p>
<!--            <div class="new_descr" v-html="item.text"></div>-->
          </div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "News",
    data () {
      return {
        all_news: []
      }
    },
    beforeMount() {
      this.loadNews()
    },
    methods: {
      loadNews: function () {
        this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/news')
          .then(response => {
            return response.json()
          })
          .then(news => {
            this.all_news = news.results
          })

        // this.all_news=[
        //   {id:1, title: 'Название новости', text:'Старейшая проектная организация в сфере жилого и гражданского строительства, основанная в 1954 году. Мы осуществляем все виды проектных работ, в том числе благоустройство, озеленение и инженерные коммуникации... ', img: 'https://mobimg.b-cdn.net/pic/v2/gallery/preview/more-pejzazh-priroda-46891.jpg'},
        //   {id:2, title: 'Название новости', text:'Старейшая проектная организация в сфере жилого и гражданского строительства, основанная в 1954 году. Мы осуществляем все виды проектных работ, в том числе благоустройство, озеленение  и инженерные коммуникации... ', img: 'https://mobimg.b-cdn.net/pic/v2/gallery/preview/more-pejzazh-priroda-46891.jpg'}
        // ]
        //Change massive field "text" for 100 symbols
        // all_news.forEach(function(item, i, arr) {
        //   item.text=item.text.substring(0, 100)+'...'
        // });
      }
    }
  }
</script>

<style scoped>

</style>
