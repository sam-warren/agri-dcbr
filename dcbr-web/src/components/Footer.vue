<template>
  <v-footer block height="auto" color="grey">
    <v-layout justify-center row wrap>
      <v-flex grey lighten-3 py-3 text-xs-center xs12>
        &copy;2019 —
        <strong>BC Gov</strong>
      </v-flex>
    </v-layout>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    links: ["Home", "", "Team", "Services", "Blog", "Contact Us"]
  })
};
</script>