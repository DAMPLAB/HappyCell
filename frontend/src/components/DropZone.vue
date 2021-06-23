<template>
  <v-container>
    <v-row
        align="center"
        justify="center"
        class="ma-2"
    >
      <v-sheet
          id="dropzone_sheet"
          ref="dzone"
          tabindex="0"
          color="white"
          width="85%"
          class="ma-2"
          elevation="5"
      >
        <vue-dropzone
            ref="sbol-input"
            id="dropzone"
            :options="dropzoneOptions"
            v-on:vdropzone-file-added="droppedSbol"
        >
        </vue-dropzone>
      </v-sheet>
    </v-row>
  </v-container>
</template>
<script>

import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
export default {
  name: 'app',
  components: {
    vueDropzone: vue2Dropzone
  },
  methods: {
    droppedSbol(input_file) {
      console.log(input_file)
      console.log('Hello!'+ "File Dropped :)")
    }
  },
  data: function () {
    return {
      dropzoneOptions: {
        url: 'http://localhost:8000/files/',
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        headers: {"My-Awesome-Header": "header value"},
        dictDefaultMessage: "<i class='fa fa-cloud-upload'></i>Input Fasta File"
      }
    }
  }
}
</script>
<style scoped>
@import url("https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");
</style>