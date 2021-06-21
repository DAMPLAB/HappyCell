<template>
  <v-app>
    <v-main>
      <div align="center">
        <img src="./assets/HappyCell.png" width="20%">
        <h1>
          Welcome to HappyCell!
        </h1>
       <v-btn
            elevation="2"
            v-on:click="click_button"
        >find restriction site.</v-btn>
        <div id="thinger">
          {{ restriction_site }}
          <div class="text-center">
          </div>

        </div>
      <v-btn
            elevation="2"
            rounded
            color="primary"
            dark
            v-on:click="click_button2"
        >Upload the fasta file </v-btn>
      </div>
    </v-main>
  </v-app>
</template>


<script>
import axios from "axios";
export default {
  name: 'App',
  components: {},
  methods: {
    click_button() {
      console.log('This is the Frontend.')
      axios
          .get('http://localhost:8000/find_restriction_site/pCI_neo_sequence.fasta/XhoI.txt')
          .then(response => (this.restriction_site = response.data.restriction_sites[0]))
    },

    click_button2(){
      console.log('This is the Frontend2.')
          //axios({
          //  method: 'post',
          //  url: "http://localhost:8000/echo/h",
          //  data: 'test',
          //  headers: {'content-type': 'application/x-www-form-urlencoded'}
          //})

          axios.post("http://localhost:8000/echopost/hi")
              .then(function (response) {
              console.log(response);
            })
            .catch(function (error) {
              console.log(error);
               });

      axios({
            method: 'post',
            url: "http://localhost:8000/postStringTest/",
            data:{"name":"test string to the backend"},

        /*
        transformRequest:function(obj) {
              var str = [];
              for ( var p in obj) {
                str.push(encodeURIComponent(p) + "="
                    + encodeURIComponent(obj[p]));
              }
              return str.join("&");
            }

         */


          })
      .then(function (response) {
              console.log(response);
            })

    }
  },
  data: () => ({
    restriction_site: 0
  }),
};

</script>


