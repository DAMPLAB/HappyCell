<template>

  <v-card style= "z-index:100;position:fixed; top:60px;
  left:2px;"
          elevation="1"
          height="75%"
          outlined
          max-width="220"
  >

    <v-navigation-drawer permanent>

      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="text-h6" style="text-align: center">
            HappyCell

          </v-list-item-title>
        </v-list-item-content>

      </v-list-item>


      <v-divider></v-divider>

      <v-list
          two-line
          dense
          nav
      >
        <v-list-item
            v-for="item in items"
            :key="item.title"
            link
            v-on:click="navigatePush($event, item.route)"
        >
          <v-list-item-icon style= "position:absolute; top:5px">
            <v-icon>{{ item.icon}}</v-icon>

          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title style= "position:absolute; left:50px">
              {{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
  </v-card>
</template>

<script>
export default {
  name: "Sidebar",
  data() {
    return {
      items: [
        {
          title: 'Home',
          icon: 'mdi-home',
          route: '/'
        },
        {
          title: 'Design Analysis',
          icon: 'mdi-microscope',
          route: 'analysis'
        },
        {
          title: 'Assembly Logistics',
          icon: 'mdi-cog-outline',
          route: 'logistics'
        },
        {
          title: 'Build',
          icon: 'mdi-hammer-screwdriver',
          route: 'build'
        },
        {
          title: 'Citation',
          icon: 'mdi-comment-quote',
          route: 'citation'
        },
      ],
      right: null,
    }
  },
  methods: {
    navigatePush(event, destination) {
      console.log(destination)
      this.$router.replace(destination)
    }
  },
}
</script>

<style scoped>
</style>
