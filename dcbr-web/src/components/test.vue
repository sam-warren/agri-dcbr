<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Operation Details</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <v-layout mx-2 mt-2>
                <h4>Best way to</h4>
              </v-layout>
              <v-container fluid>
                <v-flex>
                  <v-btn-toggle v-model="toggle_none" grid-list-md>
                    <v-btn dark class="primary white--text">E-mail</v-btn>
                    <v-btn>Mail</v-btn>
                  </v-btn-toggle>
                </v-flex>
              </v-container>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    firstname: "",
    radios: "radio-1",

    nameRules: [v => !!v || "Name is required"],
    email: "",
    emailRules: [v => !!v || "E-mail is required"]
  })
};
</script>
