<template>
  <div class="inner_content">
    <div class="content_block proj_block" ref="proj_block">
    <p class="inner_header">Проекты</p>
      <a class="back_link" @click="$router.go(-1)"><img alt="" class="back_arrow" src="../../imgs/back2.png">Вернуться назад
      </a>
    <div class="projects" ref="projects">
      <router-link :class="[itemClass, calcClass]" :key="index" :to="'/category/'+item.id" ref="proj_item"
                   v-for="(item, index) in all_projects">
        <!--          <div class="act_img">-->
        <div class="proj_title">{{ item.title }}</div>
        <div class="proj_title_red">{{ item.title }}</div>
        <img :class="imageClass" :src="item.image" alt="" ref="proj_image">
      </router-link>
    </div>
  </div>
  </div>
</template>
<script>
  export default {
    name: "Projects",
    data() {
      return {
        all_projects: [],
        itemClass: 'proj_item',
        calcClass: 'aiw_100',
        imageClass: 'wide'
      }
    },
    beforeMount() {
      this.loadProjects()
    },
    mounted() {
      this.calculateClass(),
        this.calculateImageClass()
    },
    updated() {
      this.calculateClass(),
        this.calculateImageClass()
    },
    methods: {
      loadProjects: function () {

        this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/categories')
          .then(response => {
            return response.json()
          })
          .then(projects => {
            this.all_projects = projects.results
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
      },
      calculateClass: function () {
        if (this.calcClass != 'aiw_10') {
          let arrayOfStrings = this.calcClass.split('_');
          if (this.$refs.projects.scrollHeight > this.$refs.proj_block.offsetHeight) {
            this.calcClass = 'aiw_' + (parseInt(arrayOfStrings[1]) - 10)
          }
          console.log('height', this.$refs.projects.scrollHeight, this.$refs.proj_block.offsetHeight, this.calcClass)
        }

      },
      calculateImageClass: function () {

        this.imageClass = (this.$refs.proj_image.clientWidth / this.$refs.proj_image.clientHeight > 1) ? 'tall' : 'wide';

      }
    }
  }

</script>
<style scoped>
</style>
