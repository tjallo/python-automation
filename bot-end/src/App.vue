<template>
  <div>
    <v-app>
      <Navbar />
    </v-app>
    <v-main>
      <router-view></router-view>
    </v-main>
  </div>
</template>

<script>
import Navbar from "./components/Navbar";

export default {
  components: {
    Navbar,
  },
};
</script>
<style>
</style>
