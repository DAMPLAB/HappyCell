<template>
  <v-app>
    <Navbar/>
    <Sidebar/>
    <v-main>
      <Title/>
      <Description/>
      <Dropzone/>
    </v-main>
    <AdFooter/>
  </v-app>
</template>

<script>
import Navbar from "../components/Navbar";
import Title from "../components/Title";
import Dropzone from "../components/DropZone";
import AdFooter from "../components/AdFooter";
import Description from "../components/Description";
import Sidebar from "../components/Sidebar";
export default {
  name: 'InitialPage',
  components: {
    Description,
    Navbar,
    Dropzone,
    AdFooter,
    Title,
    Sidebar,
  },
  data: () => ({
    //
  }),
};
</script>
