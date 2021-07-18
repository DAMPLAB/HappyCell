<template>
  <div style="padding-left:8%; padding-right:8%;
     word-break: break-word">

    <div style="font-size:16px">
      <br/>Our goal is to help researchers to simplify their plasmid design work.
      You can visualize plasmid and genetic circuit,
      error checking the genetic design assembly,
      save time and labor in the lab.
      <br/>
      <br/>
      <v-divider></v-divider>
    </div>
    <br/>
    <v-row>
      <v-col class="text-subtitle-2">
        <div align="center" style="padding-right:15%">
          Design analysis
        </div>
        <br/>

        <div class="text-body-2">
          Visualize plasmid and genetic circuit, access circuit statistics and scores.
        </div>
      </v-col>
      <br/><br/>

      <v-col class="text-subtitle-2">

        <div align="center" style="padding-right:20%">
          Assembly logistics
        </div>
        <br/>

        <div class="text-body-2">
          This section will provide the error checking of the assembly, material (enzyme) list, safety warnings to
          prevent accidents…
        </div>
      </v-col>
      <br/>

      <v-col class="text-subtitle-2">
        <div align="center" style="padding-right:10%">
          Build
        </div>
        <br/>

        <div class="text-body-2">
          This section shows the pathway of building your DNA design.
          It connects Cello and Puppeteer.
          We can easily “click” to build & monitoring.
        </div>
      </v-col>
    </v-row>
    <br/>
    <v-divider></v-divider>

     <div style="font-size:16px">
      <br/>
       Features
      <br/>
    </div>

    <div  class="text-body-2"
          style="padding-left:8%;
          padding-right:5%;">
    <br/>
      Built-in database: commonly used commercial plasmids map, and information including, vendor information,
    restriction sites, and annotation...
    <br/><br/>
    SBOL Representation of Circuit
    <br/><br/>
    Simple click and drop files (Fasta file/SBOL file)
    <br/><br/><br/><br/>
    </div>



  </div>
</template>

<script>
export default {
  name: "Description"
}
</script>

<style scoped>
</style>
