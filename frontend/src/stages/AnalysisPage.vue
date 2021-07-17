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






        <v-container>
          <div v-if="viewerState.fileDropped" style="text-align: center;" >

          <v-row style="padding-left: 15%;">
          <v-col>
            <v-card
                class="pa-2"
                outlined
                tile
                height=400px
                style="border-style: solid; border-width: 3px; outline-color: darkgrey"
            >
              <v-card-title style="justify-content: center">
                Description of the input file

              </v-card-title>

              <v-card-subtitle style="justify-content: center">

                Plasmid name: Cloning vector pCI-neo
                <br/>
                Source/Vendor: Promega
                <br/>
                https://www.promega.jp/-/media/files/resources/protocols/technical-bulletins/0/pci-neo-mammalian-expression-vector-protocol.pdf?la=en
                <br/>
                Plasmid Type: Mammalian expression vector
                <br/>
                Cloning Method:  Restriction Enzyme
                <br/>
                Size: 5472
                <br/>
                Bacterial Resistance:	 Ampicillin
                <br/>
                Selectable Marker:	Neomycin
                <br/>
                GenBank: U47120.2
                <br/>
                https://www.ncbi.nlm.nih.gov/nuccore/U47120.2
                <br/>
                More info:
                <br/>
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
          </div>
          </v-container>

        <vue-dropzone
            ref="sbol-input"
            id="dropzone"
            :options="dropzoneOptions"
            v-on:vdropzone-success="droppedFastaFile">
        </vue-dropzone>


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
import RestrictionSiteViewer from "../components/Viewer/RestrictionSiteViewer";
export default {
  name: 'AnalysisPage',
  components: {
    AdFooter,
    Sidebar,
    Navbar,
    RestrictionSiteViewer,

  },
  methods: {
    droppedFastaFile(input_file, resp) {
      console.log(input_file)
      console.log(resp)
      this.viewerState.fileDropped = true;
      console.log('Hello!' + "File Dropped :)")
    }
  },

  data: function () {
    return {
      viewerState: {
        fileDropped: false,
      },
      dropzoneOptions: {
        url: 'http://localhost:8000/display_plasmid/',
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        headers: {"My-Awesome-Header": "header value"},
        dictDefaultMessage: "<i class='fa fa-cloud-upload'></i>Input Fasta File"
      },
    }
  },

//  data: () => ({
//    cardDetails: [
//      {
//        title: "Plasmid Viewer Goes Here",
//        subtitle: "Should be circular plasmid viewer with restriction sites.",
//        width: 100,
//        height: 400,
//        columns: 6,
//      },
//      {
//        title: "Textual Description of Passed in File Goes Here.",
//        subtitle: "Should be a line describing the symbology of the " +
//            "genetic circuit.",
//        width: 50,
//        height: 50,
//        columns: 6,
//      }
//    ],
//    scoringResults: [
//      {
//        title: "Dynamic Range",
//        score: "90"
//      },
//      {
//        title: "Blade",
//        score: "90"
//      },
//      {
//        title: "Assembly",
//        score: "90"
//      },
//    ]
//  }),
};
</script>
