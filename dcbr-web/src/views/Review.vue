<template>
  <div class="grey lighten-4">
    <v-stepper flat>
      <v-stepper-header>
        <v-stepper-step complete step="1">Registration</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step complete editable step="2">Review & Submit</v-stepper-step>
        <v-divider></v-divider>
        <v-stepper-step step="3">Confirmation</v-stepper-step>
      </v-stepper-header>
    </v-stepper>
    <RegistrationForm formType="review"/>
  </div>
</template>

<script>
import RegistrationForm from "@/components/RegistrationForm.vue"
export default {
  components: {
    RegistrationForm
  },    
};
</script>