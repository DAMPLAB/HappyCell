<template>
  <v-app>
    <Sidebar/>
    <v-container>
      <Navbar/>
      <v-main>
        <v-row style="padding-left: 15%;">
          <v-col
          :cols="12">
            <v-card  color="grey lighten-5"
                class="pa-2"
                outlined
                tile
                height=600px
            >
              <v-card-title style="justify-content: center">
                {{cardDetails_1.title}}

              </v-card-title>



              <v-card-actions>
                <RestrictionSiteViewer/>
              </v-card-actions>
            </v-card>
          </v-col>

        </v-row>
        <v-row style="padding-left: 15%;">
          <v-col>
            <v-card  color="grey lighten-5"
                class="pa-2"
                outlined
                tile
                height=100px
                style="border-style: solid; border-width: 3px; outline-color: darkgrey"
            >
              <v-card-title style="justify-content: center">
                Horizontal SBOL Representation of Circuit, if available.
              </v-card-title>
            </v-card>
          </v-col>
        </v-row>
        <v-row style="padding-left: 15%; ">
          <v-col>
            <v-card
                align="center"
                color="grey lighten-5"
                class="pa-2"
                outlined
                tile
                height=460px
            >
              <v-card-title style="justify-content: center">
                Circuit Statistics related to score and assembly.
              </v-card-title>
              <v-list-item>
                <v-list-item-content >
                  <v-list-item-title>Single-line item</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Single-line item</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Single-line item</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
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
import RestrictionSiteViewer from "../components/Viewer/RestrictionSiteViewer";
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import AdFooter from "../components/AdFooter";


export default {
  name: 'AnalysisPage',
  components: {
    RestrictionSiteViewer,
    Sidebar,
    Navbar,
    AdFooter,

  },



  data: () => ({

    cardDetails_1:
      {
        title: "Plasmid Viewer",
        subtitle: "Should be circular plasmid viewer with restriction sites.",
        width: 100,
        height: 400,
        columns: 6,
      },
     // cardDetails_2:
     //  {
     //    title: "Description",
     //    subtitle: "Should be a line describing the symbology of the genetic circuit",
     //    width: 100,
     //    height: 400,
     //    columns: 6,
     //  },

    scoringResults: [
      {
        title: "Dynamic Range",
        score: "90"
      },
      {
        title: "Blade",
        score: "90"
      },
      {
        title: "Assembly",
        score: "90"
      },
    ]
  }),
};
</script>


