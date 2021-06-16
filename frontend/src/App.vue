<template>
  <v-app>
    <v-main>
      <div align="center">
        <img src="./assets/HappyCell.png" width="10%">
        <h1>
          Welcome to HappyCell!
        </h1>
        <v-btn
            elevation="2"
            v-on:click="click_button"
        >Click to be awesome.</v-btn>
        <div id="thinger">
          {{ restriction_site }}
          <div class="text-center">
    <v-btn
      rounded
      color="primary"
      dark
    >
      Find the restriction site
    </v-btn>
          </div>

        </div>
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
  },
  data: () => ({
    restriction_site: 0
  }),
};
</script>



