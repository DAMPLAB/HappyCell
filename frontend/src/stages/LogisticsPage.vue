<template>
  <v-app>
    <Sidebar/>
    <v-row>
      <Navbar/>
      <v-col>
        <v-main align="center">
          <span>This is the Logistics Page</span>
        </v-main>
      </v-col>
    </v-row>
    <AdFooter/>
  </v-app>
</template>

<script>
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import AdFooter from "../components/AdFooter";
export default {
  name: 'LogisticsPage',
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
