<template>
  <v-app>
    <Sidebar/>
    <v-container>
      <Navbar/>\
      <v-main>


        <v-row style="padding-left: 15%;">
          <v-col>
            <RestrictionSiteViewer/>
          </v-col>
        </v-row>


        <v-row style="padding-left: 15%;">
          <v-col>
            <v-card
                class="pa-2"
                outlined
                tile
                height=100px
                style="border-style: solid; border-width: 3px; outline-color: darkgrey"
            >
              <v-card-title style="justify-content: center">
                Stuff about Plasmid

              </v-card-title>

              <v-card-subtitle style="justify-content: center">

                Plasmid name: Cloning vector pCI-neo

Source/Vendor: Promega
https://www.promega.jp/-/media/files/resources/protocols/technical-bulletins/0/pci-neo-mammalian-expression-vector-protocol.pdf?la=en
Plasmid Type: Mammalian expression vector
Cloning Method:  Restriction Enzyme
Size: 5472
Bacterial Resistance:	 Ampicillin
Selectable Marker:	Neomycin
GenBank: U47120.2
https://www.ncbi.nlm.nih.gov/nuccore/U47120.2
More info:
https://www.addgene.org/vector-database/2184/
              </v-card-subtitle>

            </v-card>
          </v-col>
        </v-row>


        <v-row style="padding-left: 15%;">
          <v-col>
            <v-card
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
                class="pa-2"
                outlined
                tile
                height=420px
            >
              <v-card-title>
                Circuit Statistics related to score and assembly.
              </v-card-title>
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
import AdFooter from "../components/AdFooter";
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import RestrictionSiteViewer from "../components/PlasmidViewer/RestrictionSiteViewer";
export default {
  name: 'AnalysisPage',
  components: {
    AdFooter,
    Sidebar,
    Navbar,
    RestrictionSiteViewer,
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
