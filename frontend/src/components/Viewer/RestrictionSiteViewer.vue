<template>
  <v-container>
    <div v-if="viewerState.fileDropped"
         style="align-items: center;">
      <v-row>
        <v-col
            :cols="6">
          <PlasmidMap
              v-bind:displayConfig="{
								width: 350,
								height: 450,
								viewBox: {
									width: 350,
									height: 350,
								},
							}">
            <PlasmidTrack v-bind:layout="plasmidState.plasmidLayout"
                          v-bind:displayConfig="{
						distance: 125,
						width: 3,
						style: 'stroke: gray; fill: gray;',
					}">
              <Axis v-bind:layout="plasmidState.plasmidLayout"
                    v-bind:location="{start: 1, end: 5472}"
                    v-bind:displayConfig="{
							distance: 120,
							style: 'stroke: transparent; fill: transparent;',
							scales: [
								{
									distance: 0,
									interval: 200,
									width: 5,
								}
							],
							width: 0,
						}"
              ></Axis>

              <PlasmidMarker
                  v-for="(m,n) in maps"
                  :key="n"
                  direction="+"
                  v-bind:displayConfig="{
								width: 10,
								distance: 125,
								style: 'stroke: #428bca; fill: #428bca; stroke-width: 1;',
								anchor: {
									width: 10,
									height: 10
								}
							}"
                  v-bind:layout="plasmidState.plasmidLayout"
                  v-bind:location="{ start: m-10, end: m+10 }"
              >

              </PlasmidMarker>


              <Label
                  v-for="(m,n) in indexs"
                  :key="m"
                  direction="+"
                  v-bind:displayConfig="{
									type: 'text',
									distance: 155,
									style: 'text-anchor: middle; font: 9px \'Arial\', sans-serif; fill: black;',
									hOffset: 0,
									vOffset: 0,
								}"
                  v-bind:layout="plasmidState.plasmidLayout"
                  v-bind:location="{ start: m-50, end: m+80 }"
                  v-bind:text="n">
              </Label>


            </PlasmidTrack>
            <Label v-bind:layout="plasmidState.plasmidLayout"
                   v-bind:text="plasmidState.plasmidName"
                   v-bind:location="{ start: 0, end: 0 }"
                   v-bind:displayConfig="{
						type: 'text',
						distance: 0,
						style: 'text-anchor: middle; font: 16px \'Arial\',' +
						'sans-serif; fill: black; stroke-width: 1; stroke: black;',
						hOffset: 0,
						vOffset: 0,
						}">
            </Label>
            <Label v-bind:layout="plasmidState.plasmidLayout"
                   v-bind:text="plasmidState.plasmidLengthString"
                   v-bind:location="{ start: 0, end: 0 }"
                   v-bind:displayConfig="{
						type: 'text',
						distance: 0,
						style: 'text-anchor: middle; font: 14px \'Arial\', ' +
						'sans-serif; fill: black;',
						hOffset: 0,
						vOffset: 20,
						}">
            </Label>
          </PlasmidMap>
        </v-col>

        <v-col cols="1">
          </v-col>

        <v-col >
          <PlasmidDescription/>
        </v-col>
      </v-row>
    </div>


    <v-row style="padding-top:60px;"
           v-else
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
        <vue-dropzone style="padding-top: 10%;
        padding-bottom: 10%;"
                      ref="sbol-input"
                      id="dropzone"
                      :options="dropzoneOptions"
                      v-on:vdropzone-success="droppedFastaFile">
        </vue-dropzone>
      </v-sheet>
    </v-row>
  </v-container>
</template>
<script>


import vue2Dropzone from 'vue2-dropzone'
import 'vue2-dropzone/dist/vue2Dropzone.min.css'
import PlasmidMap from "./PlasmidMap.vue";
import PlasmidTrack from "./PlasmidTrack.vue";
import PlasmidMarker from "./PlasmidMarker.vue";
import Axis from "./PlasmidAxis.vue";
import Label from "./PlasmidLabel.vue";
import YAPV from "@yapv/core";
import PlasmidDescription from "../PlasmidDescription";


export default {
  name: 'RestrictionSiteViewer',
  components: {
    vueDropzone: vue2Dropzone,
    PlasmidMap,
    PlasmidTrack,
    PlasmidMarker,
    Axis,
    Label,
    PlasmidDescription,
  },
  methods: {
    droppedFastaFile(input_file, resp) {
      console.log(input_file)
      console.log(resp)
      this.viewerState.fileDropped = true;
      this.plasmidState.plasmidLayout = YAPV.layout.circular({length: resp['sequence_length']})
      this.plasmidState.plasmidLength = resp['sequence_length']
      this.plasmidState.plasmidName = resp['sequence_name']
      this.plasmidState.plasmidLengthString = resp['basepair_name']
      this.maps = resp['restriction_sites']
      this.indexs = resp['site_index']


      // console testing all res_site and index
      // for(var key in resp['site_index']) {
      //   console.log(key);
      //   console.log(resp['site_index'][key]);
      // }
      console.log('Hello!' + "File Dropped :)")
    }

  },


  data: function () {
    return {
      viewerState: {
        fileDropped: false,
      },
      plasmidState: {
        plasmidLength: 0,
        plasmidName: 'Unknown',
        plasmidLayout: YAPV.layout.circular({length: 0}),
        plasmidLengthString: "0 bp"
      },
      maps: {},
      indexs: {},

      dropzoneOptions: {
        url: 'http://localhost:8000/display_plasmid/',
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        headers: {"My-Awesome-Header": "header value"},
        dictDefaultMessage: "<i class='fa fa-cloud-upload'></i>Input Fasta File"
      },

    }
  }
}
</script>
<style scoped>
@import url("https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css");
</style>