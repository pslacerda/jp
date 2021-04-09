import Vue from 'vue'
import './plugins/axios'
import App from './App.vue'
import Buefy from 'buefy'
import './assets/scss/app.scss'
import store from './store'
import VueFormulate from '@braid/vue-formulate'


Vue.use(VueFormulate)
Vue.use(Buefy)

Vue.config.productionTip = false

new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
