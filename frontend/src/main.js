import Vue from 'vue'
//import App from './App.vue' ???
import vuetify from './plugins/vuetify'
import dropzone from "./components/dropzone";

Vue.config.productionTip = false


new Vue({
  vuetify,
  render: h => h(dropzone)
}).$mount('#app')
