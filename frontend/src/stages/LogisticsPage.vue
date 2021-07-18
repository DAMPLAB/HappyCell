<template>
  <v-app>
    <Sidebar/>
    <v-container>
      <Navbar/>
      <v-main>

        <v-row style="padding-left: 15%; height: 800px">
          <v-col>
            <v-card
                class="pa-2"
                outlined
                tile
                style="border-style: solid; border-width: 3px; outline-color: darkgrey; height: 800px"
            >
              <v-card-title style="justify-content: center">
                This is the Logistics Page
              </v-card-title>
            </v-card>
          </v-col>
        </v-row>
      </v-main>
    </v-container>
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
