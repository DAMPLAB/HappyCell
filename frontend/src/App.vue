<template>
  <v-app>
    <v-main>
      <div align="center">
        <img src="./assets/HappyCell.png" width="10%">
        <h4>
          Welcome to HappyCell!
        </h4>
        <br/>
        <br/> <br/>
        <v-btn
            elevation="2"
            rounded
            color="primary"
            dark
            v-on:click="click_button"
        >pass two strings to backend
        </v-btn>
        <br/> <br/>
      </div>
      <br/>
      <Drop-Zone/>
      <div align="center">
      <PlasmidViewer/>
        </div>
      <AdFooter/>
    </v-main>
  </v-app>
</template>


<script>

import axios from "axios";

import DropZone from './components/DropZone.vue'
import AdFooter from './components/AdFooter.vue'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import PlasmidViewer from "./components/PlasmidViewer/PlasmidViewer";

export default {
  name: 'App',
  components: {PlasmidViewer, DropZone, AdFooter},


  methods: {

    click_button() {
      // buttons is for testing axios.post,
      // and pass string by two different ways: URL and parameter
      console.log('This is the Frontend2.')
      axios
          .post("http://localhost:8000/echopost/hi")
          .then(function (response) {
            console.log(response);
          })
          .catch(function (error) {
            console.log(error);
          });


      // pass short string using para
      axios({
        method: 'post',
        url: "http://localhost:8000/postStringTest/",
        data: {"name": "test string to the backend"},
      })
          .then(function (response) {
            console.log(response);
          })
    },
  },
  data: () => ({
    restriction_site: 0
  }),
};

</script>
