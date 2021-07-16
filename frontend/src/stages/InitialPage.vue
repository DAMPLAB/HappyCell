<template>
  <v-app>
    <Navbar/>
    <Sidebar/>
    <v-container>
      <v-main>
        <Title/>
        <v-row style="padding-left: 15%; height: 800px">
          <v-col>
            <v-card
                class="pa-2"
                outlined
                tile
                style="border-style: solid; border-width: 3px; outline-color: darkgrey; height: 800px"
            >
              <v-card-title style="justify-content: center">
                <Description/>
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
import Title from "../components/Title";
import AdFooter from "../components/AdFooter";
import Description from "../components/Description";
import Sidebar from "../components/Sidebar";
export default {
  name: 'InitialPage',
  components: {
    Description,
    Navbar,
    AdFooter,
    Title,
    Sidebar,
  },
  data: () => ({
    //
  }),
};
</script>
