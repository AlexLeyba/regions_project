import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import router from './routes'
import Home from './pages/Home.vue'
import MainSidebar from "./components/MainSidebar.vue";
import App from "./App.vue"

Vue.component('MainSidebar', MainSidebar)
Vue.use(VueRouter)
Vue.use(VueResource)

new Vue({
  el: '#app',
  render: h => h(App),
  router
})


