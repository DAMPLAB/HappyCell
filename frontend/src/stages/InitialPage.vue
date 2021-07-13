<template>
  <v-app>
    <Navbar/>
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
export default {
  name: 'InitialPage',
  components: {
    Description,
    Navbar,
    Dropzone,
    AdFooter,
    Title,
  },
  data: () => ({
    //
  }),
};
</script>
