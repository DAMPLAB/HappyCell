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
                Attribution Information
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
  name: 'CitationPage',
  components: {
    AdFooter,
    Sidebar,
    Navbar,
  },
  data: () => ({
    cardDetails: [
      {
        title: "Plasmid Viewer Goes Here",
        subtitle: "Should be circular plasmid viewer with restriction sites.",
        width: 100,
        height: 400,
        columns: 6,
      },
      {
        title: "Textual Description of Passed in File Goes Here.",
        subtitle: "Should be a line describing the symbology of the " +
            "genetic circuit.",
        width: 50,
        height: 50,
        columns: 6,
      }
    ],
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
