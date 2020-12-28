<template>
  <div class="inner_content">
    <div class="content_block">
      <p class="inner_header">{{all_projects.title}}</p>
      <a class="back_link" @click="$router.go(-1)"><img alt="" class="back_arrow" src="../../imgs/back2.png">Вернуться к
        проектам
      </a>
      <p class="inner_header mobile_header">{{all_projects.title}}</p>
      <div class="proj_descr">

        <div class="project_item" :class="[all_projects.galleries.length>3 ? 'big_proj_header': 'small_proj_header']">
          <div class="pi_img" :style="[Pi_image_style()]">
            <gallery :image-path="item.image" v-on:showImage="showImage" ref="project_image" v-for="(item, index) in all_projects.galleries" :style="Project_image_style()"></gallery>
<!--            <img ref="project_image" v-for="(item, index) in all_projects.galleries" :style="Project_image_style()" :src="item.image" alt="">-->
          </div>
          <div class="pi_descr">
<!--            <p class="pi_descr_title">{{ all_projects.title }}</p>-->
            <p class="pi_descr_text" v-html="all_projects.text"></p>
          </div>

        </div>
      </div>
    </div>
    <div id="overlay" ref="overlay" v-show="showBigImage" @click="showBigImage = !showBigImage"></div>
    <div id="magnify" ref="magnify" v-show="showBigImage">
      <img :src="BigImageSrc" ref="bigImage" v-show="showBigImage">
      <div id="closepopup" ref="closepopup" @click="showBigImage = !showBigImage"><i></i>
      </div>
    </div>
  </div>
</template>

<script>
  import Gallery from "../components/Gallery";
  export default {
    name: "Project",
    components: {
      gallery: Gallery,
    },
    data() {
      return {
        id: this.$route.params['id'],
        def_img_height: window.innerHeight*0.25,
        all_projects: [],
        showBigImage: false,
        BigImageSrc: ''
      }
    },
    components: {
      gallery: Gallery,
    },
    watch: {
      $route(toR, fromR) {
        this.id = toR.params['id']
      }
    },
    created() {
      this.loadProjects()
    },
    mounted() {
      this.CalcImage()
    },
    updated() {
    },
    methods: {
      loadProjects: function () {
        this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/projects/' + this.id)
          .then(response => {
            return response.json()
          })
          .then(projects => {
            this.all_projects = projects
            //console.log (projects)
          })
        // this.all_projects=[
        //   {
        //     id: 1,
        //     title: "title 1",
        //     text: "text 1 ",
        //     img: "https://zefirka.net/wp-content/uploads/2019/02/krasota-prirody-na-fotografiyax-1-3.jpg"
        //   },
        //   {
        //     id: 2,
        //     title: "title 2 ",
        //     text: "text 2 ",
        //     img: "https://avatars.mds.yandex.net/get-pdb/1340633/d7876509-062a-4073-a12f-7e6523281b39/orig"
        //   },
        //   {
        //     id: 3,
        //     title: "title 3 ",
        //     text: "text 3 ",
        //     img: "https://zefirka.net/wp-content/uploads/2019/02/krasota-prirody-na-fotografiyax-1-3.jpg"
        //   },
        // ]
      },
      CalcImage: function () {
        let context = this
        console.log('22', context.def_img_height, context.$refs)
        if (window.innerWidth>768) {
          if (context.def_img_height == '0') {
            console.log('33')
            context.def_img_height = window.innerHeight * 0.3;
            let arr = context.$refs.project_image
            console.log(arr)
            arr.forEach(function (values, item, arr) {
              console.log('111 ', context.def_img_height, arr[item].height)
              if (arr[item].height < context.def_img_height) {
                context.def_img_height = arr[item].height;
              }
            });
          }
      }
      },
      Pi_image_style: function () {
        if (window.innerWidth>768) {
          let str = this.all_projects.galleries.length > 3 ? {height: this.def_img_height-30 + 'px'} : {height: '12em'}
          return str
        }
      },
      Project_image_style: function () {
        if (window.innerWidth>768) {
          let str = {width: 100 / this.all_projects.galleries.length + '%'}
          return str
        }
      },
      showImage: function(Path) {
        console.log('path from parent ',Path);
        this.showBigImage = true;
        this.BigImageSrc = Path;
        // this.$refs.magnify
      }
    }
  }
</script>
<style scoped>
</style>
