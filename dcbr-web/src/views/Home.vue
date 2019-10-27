  
<template>
  <v-container fluid>
    <v-layout row>
      <v-flex xs12 my-4 mr-2>
        <v-btn large round block dark color="#fcba19" @click="navTo('register')">Renew</v-btn>
      </v-flex>
      <v-flex xs12 my-4 ml-2>
        <v-btn large round block dark class="primary" @click="navTo('preamble')">Register</v-btn>
      </v-flex>
    </v-layout>
    <v-layout justify-center>
      <PublicSearch/>
    </v-layout>
  </v-container>
</template>
<script>
// import Navbar from "@/components/Navbar";
import PublicSearch from "@/components/PublicSearch.vue";
export default {
  components: {
    PublicSearch
    // Navbar
  },
  methods: {
    navTo(route) {
      if (route === "preamble") {
        this.$store.dispatch("routeProtection/formType", "register");
        this.$router.push("preamble");
      } else if (route === "register") {
        this.$store.dispatch("routeProtection/formType", "renewal");
        this.$router.push("register");
      }
    }
  }
};
</script>
