<template>
  <v-app>
    <v-row>
      <Sidebar/>
      <Navbar/>
      <v-col>
        <v-main>
<span>Hello!</span>
        </v-main>
      </v-col>
    </v-row>
    <AdFooter/>
  </v-app>
</template>

<script>
import Navbar from "./components/Navbar";
import AdFooter from "./components/AdFooter";
import Sidebar from "./components/Sidebar";
export default {
  name: 'ScoringPage',
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
