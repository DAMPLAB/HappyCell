<template>
  <v-app>
    <v-main>

      <div align="center">
        <img src="./assets/HappyCell.png" width="10%">
        <h4>
          Welcome to HappyCell!
        </h4>
        <br/>
      </div>
        <RestrictionSiteViewer/>
      <AdFooter/>
    </v-main>
  </v-app>
</template>

<script>

import AdFooter from './components/AdFooter.vue'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import RestrictionSiteViewer from "@/components/Viewer/RestrictionSiteViewer";


export default {
  name: 'App',
  components: {RestrictionSiteViewer, AdFooter},
  methods: {
    },
};

</script>
