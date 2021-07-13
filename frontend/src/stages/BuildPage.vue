<template>
  <v-app>
    <v-container>
      <Navbar/>
      <v-main>
        <Sidebar/>
        <v-row style="padding-left: 15%;">
          <v-col
              v-for="n in cardDetails"
              :key="n"
              :cols="n.columns"
          >
            <v-card
                class="pa-2"
                outlined
                tile
                height=250px
            >
              <v-card-title style="justify-content: center">
                {{n.title}}
              </v-card-title>
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
                height=460px
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
    <!--          <v-col cols="2">-->
    <!--            <Sidebar/>-->
    <!--          </v-col>-->
    <!--            <v-col-->
    <!--                v-for="n in cardDetails"-->
    <!--                :key="n"-->
    <!--                cols="8"-->
    <!--                sm="4"-->
    <!--            >-->
    <!--              <v-card-->
    <!--                  class="pa-2"-->
    <!--                  outlined-->
    <!--                  tile-->
    <!--                  style="justify-content: center"-->
    <!--              >-->
    <!--                <v-card-title style="justify-content: center">{{ n.title }}</v-card-title>-->
    <!--                <v-card-subtitle style="justify-content: center">{{ n.subtitle }}</v-card-subtitle>-->
    <!--              </v-card>-->
    <!--            </v-col>-->
    <!--        </v-main>-->
    <!--      </v-row>-->
    <!--      <AdFooter/>-->
    <!--    </v-container>-->
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";
// import AdFooter from "@/components/AdFooter";
import Sidebar from "@/components/Sidebar";
export default {
  name: 'BuildPage',
  components: {
    Sidebar,
    // Sidebar,
    Navbar,
    // AdFooter,
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
