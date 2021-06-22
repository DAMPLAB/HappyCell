<template>
  <v-app>
    <v-main>
      <div align="center">
        <img src="./assets/HappyCell.png" width="10%">
        <h4>
          Welcome to HappyCell!
        </h4>
        <br/>
        <v-btn
            elevation="2"
            v-on:click="click_button1"

        >find restriction site
        </v-btn>

        <div id="thinger">
          {{ restriction_site }}
          <div class="text-center">
          </div>
        </div>
        <br/> <br/>
        <v-btn
            elevation="2"
            rounded
            color="primary"
            dark
            v-on:click="click_button2"
        >pass two strings to backend
        </v-btn>
        <br/> <br/>
      </div>
      <br/>

      <Drop-Zone/>
      <AdFooter/>
    </v-main>
  </v-app>
</template>


<script>

// question: run in pycharm failed??? both App.vue and main.py?

// so many buttons: visually messy, is that better to write them in components?

// big picture of the projects/ 40hr/pace / short Zooms

import axios from "axios";

import DropZone from './components/DropZone.vue'
import AdFooter from './components/AdFooter.vue'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'

export default {
  name: 'App',
  components: {DropZone, AdFooter},

  methods: {
    click_button1() {
      // button1 to return a restriction sites index
      console.log('This is the Frontend.')
      axios
          .get('http://localhost:8000/findsites/pCINeoSequence.fasta')
          .then(response =>
              (this.restriction_site = response.data.restriction_sites[0]))
    },

    click_button2() {
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


      // pass short string using data???
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

  // ???? why this data:() is here? so far from button1???
  data: () => ({
    restriction_site: 0
  }),
};

</script>
