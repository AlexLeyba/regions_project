<template>
  <div class="inner_content">
    <div class="content_block">
      <p class="inner_header">{{all_items.title}}</p>
      <a class="back_link" @click="$router.go(-1)"><img alt="" class="back_arrow" src="../../imgs/back2.png">Вернуться назад
      </a>
      <p class="inner_header mobile_header">{{all_items.title}}</p>
      <div class="category_items">
        <router-link v-for="item in all_items.pod_projects" :to="'/projects/'+item.id" :key="item.id" class="category_item">
          <div class="cat_img">
            <img v-if="item.galleries.length>0" :src="item.galleries[0].image" alt="">
            <img v-else src="../../imgs/no_image.jpg" alt="">
          </div>
          <div class="cat_content">
            <p class="cat_title">{{ item.title }}</p>
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
        id: this.$route.params['id'],
        all_items: []
      }
    },
    beforeMount() {
      this.loadItems()
    },
    mounted() {

    },
    updated() {

    },
    watch: {
      $route(toR, fromR) {
        this.id = toR.params['id']
      }
    },
    methods: {
      loadItems: function () {
        this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/pod-category/'+this.id)
          .then(response => {
            return response.json()
          })
          .then(categories => {
            console.log('categories',categories)
            this.all_items = categories
          })

        // this.all_news=[
        //   {id:1, title: 'Название новости', text:'Старейшая проектная организация в сфере жилого и гражданского строительства, основанная в 1954 году. Мы осуществляем все виды проектных работ, в том числе благоустройство, озеленение и инженерные коммуникации... ', img: 'https://mobimg.b-cdn.net/pic/v2/gallery/preview/more-pejzazh-priroda-46891.jpg'},
        //   {id:2, title: 'Название новости', text:'Старейшая проектная организация в сфере жилого и гражданского строительства, основанная в 1954 году. Мы осуществляем все виды проектных работ, в том числе благоустройство, озеленение  и инженерные коммуникации... ', img: 'https://mobimg.b-cdn.net/pic/v2/gallery/preview/more-pejzazh-priroda-46891.jpg'}
        // ]
      }
    }
  }
</script>

<style scoped>

</style>
