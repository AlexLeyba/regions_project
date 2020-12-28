<template>
  <div class="inner_content">
    <div class="content_block sub_cat_block" ref="proj_block">
      <p class="inner_header">{{all_projects.title}}</p>
      <a class="back_link" @click="$router.go(-1)"><img alt="" class="back_arrow" src="../../imgs/back2.png">Вернуться назад
      </a>
      <p class="inner_header mobile_header">{{all_projects.title}}</p>
      <div class="projects proj_cat" ref="projects">
        <router-link :style="{backgroundImage: 'url('+item.image+') '}" :class="[itemClass, calcClass]" :key="index" :to="'/item/'+item.id" ref="proj_cat_item"
                     v-for="(item, index) in all_projects.pod_categories">
          <!--          <div class="act_img">-->
          <div class="proj_title">{{ item.title }}</div>
          <div class="proj_title_red">{{ item.title }}</div>
<!--          <img :class="imageClass" :src="item.image" alt="" ref="proj_image">-->

        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: "Category",
    data() {
      return {
        id: this.$route.params['id'],
        all_projects: [],
        itemClass: 'proj_cat_item',
        calcClass: '',
        imageClass: ''
      }
    },
    watch: {
      $route(toR, fromR) {
        this.id = toR.params['id']
      }
    },
    beforeMount() {
      this.loadProjects()
    },
    mounted() {

    },
    updated() {

    },
    methods: {
      loadProjects: function () {

        this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/categories/'+this.id)
          .then(response => {
            return response.json()
          })
          .then(projects => {
            this.all_projects = projects
            console.log(projects)
          })


        // this.all_projects = [{
        //     date: "1954 - 1980",
        //     items: [
        //       { id: 1, img: "https://ktonanovenkogo.ru/image/priroda-gora.jpg" },
        //       { id: 2, img: "https://2krota.ru/wp-content/uploads/2018/10/1e76283681120b8a74b6f8c7f2dea911.jpg" },
        //       { id: 3, img: "https://2krota.ru/wp-content/uploads/2018/10/1-7.jpg" }
        //     ]
        //   },
        //   {
        //     date: "1954 - 1980",
        //     items: [
        //       { id: 10, img: "https://ktonanovenkogo.ru/image/priroda-gora.jpg" },
        //       { id: 11, img: "https://2krota.ru/wp-content/uploads/2018/10/1e76283681120b8a74b6f8c7f2dea911.jpg" },
        //       { id: 12, img: "https://2krota.ru/wp-content/uploads/2018/10/1-7.jpg" },
        //       { id: 13, img: "https://2krota.ru/wp-content/uploads/2018/10/1-7.jpg" }
        //     ]
        //   },
        //   {
        //     date: "1990",
        //     items: [
        //       { id: 4, img: "https://ktonanovenkogo.ru/image/priroda-gora.jpg" },
        //       { id: 5, img: "https://2krota.ru/wp-content/uploads/2018/10/1e76283681120b8a74b6f8c7f2dea911.jpg" },
        //       { id: 6, img: "https://2krota.ru/wp-content/uploads/2018/10/1-7.jpg" },
        //       { id: 7, img: "https://ktonanovenkogo.ru/image/priroda-gora.jpg" },
        //       { id: 8, img: "https://2krota.ru/wp-content/uploads/2018/10/1e76283681120b8a74b6f8c7f2dea911.jpg" },
        //       { id: 9, img: "https://2krota.ru/wp-content/uploads/2018/10/1-7.jpg" }
        //     ]
        //   }
        // ]
      }
    }
  }

</script>
<style scoped>
</style>
