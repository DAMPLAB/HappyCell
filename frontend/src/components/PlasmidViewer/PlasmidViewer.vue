<template>
  <PlasmidMap v-bind:displayConfig="{
								width: 500,
								height: 500,
								viewBox: {
									width: 400,
									height: 400,
								},
							}">
		<PlasmidTrack v-bind:layout="layout"
					v-bind:displayConfig="{
						distance: 110,
						width: 3,
						style: 'stroke: gray; fill: gray;',
					}">
			<Axis v-bind:layout="layout"
						v-bind:location="{start: 1, end: 5472}"
						v-bind:displayConfig="{
							distance: 100,
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


		</PlasmidTrack>
		<Label v-bind:layout="layout"
           v-bind:text= "plasmid_name"
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
		<Label v-bind:layout="layout"
           v-bind:text= "size_bp"
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
</template>


<script>
import YAPV from '@yapv/core';
import PlasmidMap from './PlasmidMap.vue';
import PlasmidTrack from './PlasmidTrack.vue';
//import PlasmidMarker from './PlasmidMarker.vue';
import Axis from './PlasmidAxis.vue';
import Label from './PlasmidLabel.vue';
//import axios from "axios";
const layout = YAPV.layout.circular({ length: 5472 });
const plasmid_name = 'plasmid name'
const size_bp = '5200 bp'
export default {
  name: 'PlasmidViewer',
  components: {
		PlasmidMap,
		PlasmidTrack,
		//PlasmidMarker,
		Axis,
		Label,
	},
  methods: {
  },
	data () {
		return {
			layout,plasmid_name,size_bp
		}
	},
}
</script>
