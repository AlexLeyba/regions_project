<template>
  <div class="inner_content">
    <div class="content_block">
      <p class="inner_header">Новости</p>
      <a class="back_link" @click="$router.go(-1)"><img alt="" class="back_arrow" src="../../imgs/back2.png">Вернуться назад
      </a>
      <div class="new">

        <p class="new_title single_new">{{ the_new.title }}</p>
        <gallery :image-path="the_new.image" v-on:showImage="showImage"></gallery>
<!--        <img :src="the_new.image" alt="">-->
        <div class="new_text" v-html="the_new.text"></div>
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
  name: "New",
  data() {
    return {
      id: this.$route.params['id'],
      the_new: {
        id: -1,
        title: '',
        text: '',
        image: ''
      },
      showBigImage: false,
      BigImageSrc: ''
    }
  },
  components: {
    gallery: Gallery,
  },
  beforeMount() {
    this.loadNew()
  },
  watch: {
    $route(toR, fromR) {
      this.id = toR.params['id']
    }
  },
  methods: {
    goBack: function() {
      this.$router.push('/news');
    },
    loadNew: function() {
      var new_id=this.id
      var context=this;
      this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/news')
        .then(response => {
          return response.json()
        })
        .then(news => {
          var array=news.results;
          array.forEach(function(values, item) {
           // console.log (values, 'new_id: ',values.id, 'route_id: ', new_id)
           if (values.id == new_id) {

              context.the_new=values

            }
          });


        })
      // this.the_new = {id:this.id, title: 'Название новости ' + this.id, text:'Повседневная практика показывает, что высококачественный прототип будущего проекта не оставляет шанса для поставленных обществом задач. Предварительные выводы неутешительны: сложившаяся структура организации говорит о возможностях новых предложений. Для современного мира базовый вектор развития требует анализа поставленных обществом задач. И нет сомнений, что независимые государства являются только методом политического участия и объявлены нарушающими общечеловеческие нормы этики и морали. Как уже неоднократно упомянуто, ключевые особенности структуры проекта являются только методом политического участия и призваны к ответу. Кстати, предприниматели в сети интернет, которые представляют собой яркий пример континентально-европейского типа политической культуры, будут указаны как претенденты на роль ключевых факторов. Современные технологии достигли такого уровня, что высокотехнологичная концепция общественного уклада создаёт предпосылки для вывода текущих активов. Противоположная точка зрения подразумевает, что сделанные на базе интернет-аналитики выводы набирают популярность среди определенных слоев населения, а значит, должны быть призваны к ответу. В своём стремлении улучшить пользовательский опыт мы упускаем, что представители.', img: 'https://g.io.ua/img_aa/large/3018/87/30188725.jpg'}
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
