<template>
  <v-menu
    ref="menu"
    :close-on-content-click="false"
    :nudge-right="40"
    lazy
    transition="scale-transition"
    offset-y
    full-width
    min-width="290px"
  >
    <template v-slot:activator="{ on }">
      <v-text-field v-model="date" label="Expiry Date" prepend-icon="event" readonly v-on="on"></v-text-field>
    </template>
    <v-date-picker
      ref="picker"
      v-model="date"
      :max="new Date().toISOString().substr(0, 10)"
      min="1950-01-01"
      :error="datePickerRules"
    ></v-date-picker>
  </v-menu>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    datePickerRules: [
      v => !!v || "Expiry date is required",
    ],
  }),
  computed: {
    date: {
      // getter
      get() {
        return this.$store.getters["renewal/expiryDate"]
      },
      // setter
      set(value) {
        this.$store.dispatch("renewal/expiryDate", value);
      }
    }
  }
};
</script>