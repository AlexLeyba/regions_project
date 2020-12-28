<template>
  <div class="inner_content">
    <div class="content_block">
      <div class="main_page_credits">
        <div class="mp_credits_left">
          <p class="mp_credits_text_title">Липецкгражданпроект</p>
          <p class="mp_credits_text">Старейшая проектная организация в сфере жилого и гражданского строительства, основанная в 1954 году. Мы осуществляем все виды проектных работ, в том числе благоустройство, озеленение  и инженерные коммуникации.</p>
        </div>
        <div class="mp_credits_right">
          <p class="mp_credits_address"><img src="imgs/marker.png" alt="">Россия, Липецкая область, г. Липецк, пл. Победы, д. 8 </p>
          <p class="mp_credits_phone"><img src="imgs/phone.png" alt="">+7 (4742) 77-43-54</p>
        </div>
      </div>
      <p class="mp_credits_text_title about_title">Наши сотрудники</p>
      <div class="our_workers">
        <div v-for="(item, index) in all_workers"  :key="index" class="worker">
          <div class="worker_img">
            <img :src="item.image" alt="">
          </div>
          <p class="worker_name">{{item.title}}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "About",
    data () {
      return {
        all_workers: []
      }
    },
    mounted() {
      this.loadWorkers()
    },
    methods: {
      loadWorkers: function () {

        this.$http.get('https://cfo.admlr.lipetsk.ru/citizen/about')
          .then(response => {
            return response.json()
          })
          .then(workers => {
            this.all_workers = workers.results
          })

        // this.all_workers=[
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'},
        //   {id:1, fullName: 'Сергей Двачковчикус', text:'xxxx', img: 'https://st2.depositphotos.com/2111141/5308/i/450/depositphotos_53087525-stock-photo-handsome-guy.jpg'},
        //   {id:2, fullName: 'Юлия Красовская', text:'xxxx', img: 'https://cdn.trinixy.ru/pics5/20160811/beautiful_girls_06.jpg'}
        // ]
      }
    }
  }
</script>

<style scoped>

</style>
