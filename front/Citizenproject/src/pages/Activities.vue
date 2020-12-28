<template>
  <div class="inner_content">
    <div class="content_block act_block" ref="act_block">
      <p class="inner_header">Виды деятельности</p>
      <a class="back_link" @click="$router.go(-1)"><img alt="" class="back_arrow" src="../../imgs/back2.png">Вернуться
        назад
      </a>
      <div class="activities" ref="activities">
        <div v-for="(item, index) in all_Activities" ref="act_item" :key="index" :class="[itemClass, calcClass]">
          <div class="act_title disable-selection">{{ item.title }}</div>
          <div class="act_title_red">{{ item.title }}</div>
          <img :src="item.image" ref="act_image" alt="" :class="imageClass">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "Activities",
    data() {
      return {
        all_Activities: [],
        itemClass: 'act_item',
        calcClass: 'aiw_100',
        imageClass: 'wide'
      }
    },
    beforeMount() {
      this.loadActivities()
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
      loadActivities: function () {
        this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/activity')
          .then(response => {
            return response.json()
          })
          .then(acts => {
            this.all_Activities = acts.results

          })
        // this.all_Activities=[
        //     {
        //       "id": 4,
        //       "image": "https://cfo.admlr.lipetsk.ru/media/images/Natura-Polski.jpg",
        //       "title": "Вид деятельности",
        //       "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //     },
        //     {
        //       "id": 1,
        //       "image": "https://cfo.admlr.lipetsk.ru/media/images/zvezdy_nebo_kosmos_avtomobil_113629_1920x1080.jpg",
        //       "title": "деятельность 1",
        //       "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //     },
        //     {
        //       "id": 2,
        //       "image": "https://cfo.admlr.lipetsk.ru/media/images/zdanie_reka_vodopad_152079_1920x1080.jpg",
        //       "title": "Деятельность 2",
        //       "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //     },
        //     {
        //       "id": 3,
        //       "image": "https://cfo.admlr.lipetsk.ru/media/images/zamok_tuman_gory_122718_1920x1080.jpg",
        //       "title": "Деятельность 3",
        //       "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //     },
        //     {
        //       "id": 7,
        //       "image": "https://cfo.admlr.lipetsk.ru/media/images/Natura-Polski_rvIrI1N.jpg",
        //       "title": "деятельность 5",
        //       "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //     },
        //     {
        //       "id": 8,
        //       "image": "https://cfo.admlr.lipetsk.ru/media/images/original_7193_oboi_morskie_kameshki_1920x1200_NZUMusX.jpg",
        //       "title": "Проектирование зданий",
        //       "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //     }
        //   // {
        //   //   "id": 9,
        //   //   "image": "https://cfo.admlr.lipetsk.ru/media/images/original_7193_oboi_morskie_kameshki_1920x1200_NZUMusX.jpg",
        //   //   "title": "Деятельность 9",
        //   //   "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //   // },
        //   // {
        //   //   "id": 10,
        //   //   "image": "https://cfo.admlr.lipetsk.ru/media/images/original_7193_oboi_morskie_kameshki_1920x1200_NZUMusX.jpg",
        //   //   "title": "Деятельность 10",
        //   //   "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //   // },
        //   // {
        //   //   "id": 11,
        //   //   "image": "https://cfo.admlr.lipetsk.ru/media/images/Natura-Polski_rvIrI1N.jpg",
        //   //   "title": "деятельность 11",
        //   //   "desc": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\r\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
        //   // }
        //
        //    ]
      },
      calculateClass: function () {
        if (this.calcClass != 'aiw_10') {
          let arrayOfStrings = this.calcClass.split('_');
          if (this.$refs.activities.scrollHeight > this.$refs.act_block.offsetHeight) {
            this.calcClass = 'aiw_' + (parseInt(arrayOfStrings[1]) - 10)
          }
          console.log('height', this.$refs.activities.scrollHeight, this.$refs.act_block.offsetHeight, this.calcClass)
        }
      },
      calculateImageClass: function () {
        this.imageClass = (this.$refs.act_image.clientWidth / this.$refs.act_image.clientHeight > 1) ? 'tall' : 'wide';
      }

    },
    computed: {}
  }
</script>

<style scoped>

</style>
