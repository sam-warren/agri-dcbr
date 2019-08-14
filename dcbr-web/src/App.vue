<template>
  <v-app class="grey">
    <div id="app">
      <Navbar />
      <div id="nav">
        <br />
        <br />
        <!-- <button @click="$keycloak.logoutFn" v-if="$keycloak.authenticated">Log out</button> -->
      </div>
      <router-view />
    </div>
    <Footer />
  </v-app>
</template>

<script>
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";

export default {
  components: {
    Navbar,
    Footer
  }
};
</script>


<style>
#nav {
  padding: 10px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}
</style>