<template>
  <header>
    <v-toolbar height="65" dark app color="#003366">
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">
          <img src="@/assets/logo.svg" height="45px" />
        </span>
      </v-toolbar-title>
      <h3>Cats and Dogs Breeder and Seller Registration</h3>
      <v-spacer></v-spacer>
      <v-btn height="30px" color="#fcba19">
        <v-icon>search</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>menu</v-icon>
      </v-btn>
    </v-toolbar>
  </header>
</template>


<script>
export default {
  data() {
    return {};
  }
};
</script>

<style scoped>
.header {
  border-bottom: 2px solid #fcba19;
}
</style>
