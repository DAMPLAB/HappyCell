
<template>
  <div id="app">
    <div className="content">
      <transition name="fade">
        <router-view/>
      </transition>
    </div>
  </div>
</template>

<style>
</style>
<script>
export default {
  name: 'App',
  components: {},
  data: () => ({
    //
  }),
};
</script>