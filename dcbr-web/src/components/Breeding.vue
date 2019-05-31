<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Breeding Details</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!-- INTACT BREEDING DOG -->
              <v-layout mx-2 mt-4>
                <subheader>How many intact breeding female dogs over the age of eight months do you have?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field label="Number of Female Dogs"></v-text-field>
                </v-flex>
              </v-layout>
              <!-- INTACT BREEDING CAT -->
              <v-layout mx-2 mt-4>
                <subheader>How many intact breeding female cats over the age of xxxx months do you have?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field label="Number of Female Cats"></v-text-field>
                </v-flex>
              </v-layout>
              <!-- Type of Animal -->
              <v-layout mx-2 mt-4>
                <subheader>How many litters were whelped in one calendar year overall (all female dogs combined)?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field label="Whelped Litters"></v-text-field>
                </v-flex>
              </v-layout>
              <!-- Type of Animal -->
              <v-layout mx-2 mt-4>
                <subheader>How many litters were queened in one calendar year overall (all female cats combined)?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field label="Queened Litters"></v-text-field>
                </v-flex>
              </v-layout>

              <v-layout mx-2 mt-4>
                <subheader>What number of puppies did you ............... in the previous calendar year?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field label="Transfer"></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Sell"></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Trade"></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Lease"></v-text-field>
                </v-flex>
              </v-layout>
              <v-layout mx-2 mt-4>
                <subheader>What numnber of kittens did you ............... in the previous calendar year?</subheader>
              </v-layout>

              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field label="Transfer"></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Sell"></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Trade"></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Lease"></v-text-field>
                </v-flex>
              </v-layout>
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

    middlename: "",
    row: null,
    type: null,
    animal: null,

    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    email: "",
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ]
  })
};
</script>
