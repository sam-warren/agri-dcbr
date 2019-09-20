  
<template>
  <v-container>
    <v-layout>
      <v-flex xs12 md4>
        <v-btn large round dark color="#fcba19" @click="navTo('register')">Renew</v-btn>
      </v-flex>

      <v-flex>
        <v-btn large round block dark class="primary" @click="navTo('preamble')">Register</v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
// import Navbar from "@/components/Navbar";
export default {
  components: {
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
