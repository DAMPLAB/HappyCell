<template>
  <v-app>
    <Sidebar/>
    <v-container>
      <Navbar/>
      <v-main>

      </v-main>
    </v-container>
    <AdFooter/>
  </v-app>

</template>

<script>
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import AdFooter from "../components/AdFooter";


export default {
  name: 'BuildPage',
  components: {
    Sidebar,
    Navbar,
    AdFooter,
  },



data: () => ({
    //
  }),
};
</script>
