<template>
  <div>
    <v-row justify="center" align="center" class="mt-1">
      <v-col
          cols="12"
          sm="8"
      >
        <v-sheet
            tabindex="0"
            color="white"
            class="d-flex align-center justify-center pa-1 mx-auto"
            outlined
        >
          <span class="subtext--text" style="padding-left: 20%;">



            <br/>

            Our goal is to help researchers to simplify their plasmid design work.
            <br/>
            You can visualize plasmid and genetic circuit; error checking the genetic design assembly…
            <br/><br/><br/>

            <v-row class="text-h5">
            HappyCell have three modules:
              </v-row>
            <br/>
            <v-row>
              <v-col class="text-subtitle-2">
            Design analysis
                <br/><br/>

                <div class="text-body-2">
            In this section we visualize plasmid and genetic circuit.
                <br/>
            The circuit statistics related to score and assembly is showed at bottom.
                  </div>
                </v-col>
              <br/><br/>

              <v-col class="text-subtitle-2">
                Assembly logistics
                <br/><br/>

                <div class="text-body-2">
                This section will provide the error checking of the assembly, material (enzyme) list, safety warnings to prevent accidents…
                </div>
              </v-col>
              <br/><br/>

              <v-col class="text-subtitle-2">
                Build
                <br/><br/>

                <div class="text-body-2">
                This section shows the pathway of building your DNA design.
                <br/>
                Integration point between Cello and Puppeteer.
                <br/>
                Easy “click” to build & monitoring
                  </div>
              </v-col>
              </v-row>
            <br/><br/>

            <v-row class="text-h5">
            Features:
              </v-row>
            <br/>
            - Built-in database: commonly used commercial plasmids map, and information including, vendor information, restriction sites, and annotation...
            <br/>
            - SBOL Representation of Circuit
            <br/>
            - Simple click and drop files (Fasta file/SBOL file)
            <br/><br/><br/>


          </span>
        </v-sheet>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Description"
}
</script>

<style scoped>
</style>
