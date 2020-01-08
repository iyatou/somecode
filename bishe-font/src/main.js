// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ViewUI from 'view-design';
import 'view-design/dist/styles/iview.css';
import VueParticles from 'vue-particles'
import axios from 'axios'
import moment from 'moment'


Vue.prototype.$moment = moment
Vue.use(router)
Vue.use(ViewUI)
Vue.use(VueParticles)
axios.defaults.headers.post['Content-Type'] = 'application/json;charset=UTF-8';
axios.defaults.baseURL = 'http://localhost:8088'
axios.defaults.withCredentials = true
// 将API方法绑定到全局
Vue.prototype.$axios = axios

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
