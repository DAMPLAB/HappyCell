<template>
  <v-footer
      style= "z-index:120;position:fixed; top:88%;"
      app
      color="light-blue lighten-5"
      height="100%"
  >
    <v-row align-content="stretch" justify="space-between" align="center">
      <v-img
          contain
          max-height="40"
          max-width="200"
          src="https://cidar-logo-asset-bucket.s3.amazonaws.com/Boston+University+Logo.png"
      ></v-img>
      <v-img
          contain
          max-height="40"
          max-width="200"
          src="https://cidar-logo-asset-bucket.s3.amazonaws.com/cidar_cropped.png"
      ></v-img>
      <v-img
          contain
          max-height="40"
          max-width="200"
          src="https://cidar-logo-asset-bucket.s3.amazonaws.com/damp-lab-logo-1x.png"
      ></v-img>
    <div class="mt-10">
      <p class="black--text">Copyright 2021, CIDAR Lab - All Rights Reserved</p>
    </div>
    </v-row>
  </v-footer>
</template>
<script>
export default {
  name: "AdFooter"
}
</script>
<style scoped>
</style>