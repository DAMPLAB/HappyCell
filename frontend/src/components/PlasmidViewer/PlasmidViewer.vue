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
						width: 2,
						style: 'stroke: gray; fill: gray;',
					}">
			<Axis v-bind:layout="layout"
						v-bind:location="{start: 1, end: 5322}"
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
			<PlasmidMarker v-bind:layout="layout"
							v-bind:displayConfig="{
								width: 10,
								distance: 110,
								style: 'stroke: #755A96; fill: #755A96; stroke-width: 1;',
								anchor: {
									width: 10,
									height: 10
								}
							}"
							v-bind:location="{ start: 1, end: 208 }"
							direction="+"
							>
				<Label v-bind:layout="layout"
								text='pLacL'
								v-bind:location="{ start: 1, end: 208 }"
								v-bind:displayConfig="{
									type: 'text',
									distance: 110,
									style: 'text-anchor: middle; font: 12px \'Arial\', sans-serif; fill: black;',
									hOffset: 0,
									vOffset: -30,
								}">
				</Label>
				<Label v-bind:layout="layout"
								text='(1 - 208)'
								v-bind:location="{ start: 1, end: 208 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 8px \'Arial\', sans-serif; fill: black;',
								hOffset: 0,
								vOffset: -20,
								}">
				</Label>
			</PlasmidMarker>
			<PlasmidMarker v-bind:layout="layout"
							v-bind:displayConfig="{
								width: 10,
								distance: 110,
								style: 'stroke: #292B57; fill: #292B57; stroke-width: 1;',
								anchor: {
									width: 20,
									height: 10
								}
							}"
							v-bind:location="{ start: 232, end: 981 }"
							direction="+"
							>
				<Label v-bind:layout="layout"
								text='esaR'
								v-bind:location="{ start: 232, end: 981 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 12px \'Arial\', sans-serif; fill: black;',
								hOffset: 30,
								vOffset: -20,
								}">
				</Label>
				<Label v-bind:layout="layout"

								text='(232 - 981)'
								v-bind:location="{ start: 232, end: 981 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 8px \'Arial\', sans-serif; fill: black;',
								hOffset: 30,
								vOffset: -10,
								}">
				</Label>
			</PlasmidMarker>
			<PlasmidMarker v-bind:layout="layout"
							v-bind:displayConfig="{
								width: 10,
								distance: 110,
								style: 'stroke: #428bca; fill: #428bca; stroke-width: 1;',
								anchor: {
									width: 20,
									height: 10
								}
							}"
							v-bind:location="{ start: 1028, end: 1663 }"
							direction="+"
							>
				<Label v-bind:layout="layout"
								text='esaL'
								v-bind:location="{ start: 1028, end: 1663 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 12px \'Arial\', sans-serif; fill: black;',
								hOffset: 40,
								vOffset: -10,
								}">
				</Label>
				<Label v-bind:layout="layout"

								text='(1028 - 1663)'
								v-bind:location="{ start: 1028, end: 1663 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 8px \'Arial\', sans-serif; fill: black;',
								hOffset: 40,
								vOffset: 0,
								}">
				</Label>
			</PlasmidMarker>
			<PlasmidMarker v-bind:layout="layout"
							v-bind:displayConfig="{
								width: 10,
								distance: 110,
								style: 'stroke: black; fill: black; stroke-width: 1;',
							}"
							v-bind:location="{ start: 1670, end: 1802 }"
							direction="#"
							>
				<Label v-bind:layout="layout"
								text='Terminator R0015'
								v-bind:location="{ start: 1670, end: 1802 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 12px \'Arial\', sans-serif; fill: black;',
								hOffset: 60,
								vOffset: 0,
								}">
				</Label>
				<Label v-bind:layout="layout"
								text='(1620 - 1802)'
								v-bind:location="{ start: 1670, end: 1802 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 8px \'Arial\', sans-serif; fill: black;',
								hOffset: 50,
								vOffset: 10,
								}">
				</Label>
			</PlasmidMarker>
			<PlasmidMarker v-bind:layout="layout"
							v-bind:displayConfig="{
								width: 10,
								distance: 110,
								style: 'stroke: #d9534f; fill: #d9534f; stroke-width: 1;',
								anchor: {
									width: 20,
									height: 10
								}
							}"
							v-bind:location="{ start: 3462, end: 4121 }"
							direction="-"
							>
				<Label v-bind:layout="layout"
								text='CmR'
								v-bind:location="{ start: 3462, end: 4121 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 12px \'Arial\', sans-serif; fill: black;',
								hOffset: -40,
								vOffset: 0,
								}">
				</Label>
				<Label v-bind:layout="layout"
								text='(3462 - 4121)'
								v-bind:location="{ start: 3462, end: 4121 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 8px \'Arial\', sans-serif; fill: black;',
								hOffset: -40,
								vOffset: 10,
								}">
				</Label>
			</PlasmidMarker>
			<PlasmidMarker v-bind:layout="layout"
							v-bind:displayConfig="{
								width: 10,
								distance: 110,
								style: 'stroke: #5cb85c; fill: #5cb85c; stroke-width: 1;',
							}"
							v-bind:location="{ start: 4200, end: 4615 }"
							direction="#"
							>
				<Label v-bind:layout="layout"
								text='p15A'
								v-bind:location="{ start: 4200, end: 4615 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 12px \'Arial\', sans-serif; fill: black;',
								hOffset: -40,
								vOffset: -10,
								}">
				</Label>
				<Label v-bind:layout="layout"
								text='(4200 - 4615)'
								v-bind:location="{ start: 4200, end: 4615 }"
								v-bind:displayConfig="{
								type: 'text',
								distance: 110,
								style: 'text-anchor: middle; font: 8px \'Arial\', sans-serif; fill: black;',
								hOffset: -40,
								vOffset: 0,
								}">
				</Label>
			</PlasmidMarker>
		</PlasmidTrack>
		<Label v-bind:layout="layout"
						text='pAC-EsaR-EsaI'
						v-bind:location="{ start: 0, end: 0 }"
						v-bind:displayConfig="{
						type: 'text',
						distance: 0,
						style: 'text-anchor: middle; font: 16px \'Arial\', sans-serif; fill: black; stroke-width: 1; stroke: black;',
						hOffset: 0,
						vOffset: 0,
						}">
		</Label>
		<Label v-bind:layout="layout"
						text='5332 bp'
						v-bind:location="{ start: 0, end: 0 }"
						v-bind:displayConfig="{
						type: 'text',
						distance: 0,
						style: 'text-anchor: middle; font: 14px \'Arial\', sans-serif; fill: black;',
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
import PlasmidMarker from './PlasmidMarker.vue';
import Axis from './PlasmidAxis.vue';
import Label from './PlasmidLabel.vue';

const layout = YAPV.layout.circular({ length: 5322 });

export default {
  name: 'PlasmidViewer',
  components: {
		PlasmidMap,
		PlasmidTrack,
		PlasmidMarker,
		Axis,
		Label,
	},
	data () {
		return {
			layout,
		}
	},
}
</script>
