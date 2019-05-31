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
              <!--OPERATION DETAILS-NAME  -->
              <v-layout mx-2 mt-4>
                <subheader>Does your operation run under a specific name? i.e "business name" (Optional)</subheader>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4 mr-5>
                  <v-text-field label="Operation Name"></v-text-field>
                </v-flex>

                <v-flex xs12 md4>
                  <v-text-field label="Link to your Website "></v-text-field>
                </v-flex>
              </v-layout>
              <!-- Type of Operator -->
              <v-layout mx-2 mt-4>
                <subheader>What type of operator are you?</subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="type" row>
                  <v-radio label="Breeder" value="radio-a"></v-radio>
                  <v-radio label="Seller" value="radio-b"></v-radio>
                  <v-radio label="Breeder & Seller" value="radio-c"></v-radio>
                </v-radio-group>
              </v-layout>
              <!-- Type of Animal -->
              <v-layout mx-2 mt-4>
                <subheader>What type of animal do you work with?</subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="animal" row>
                  <v-radio label="Dogs" value="radio-a"></v-radio>
                  <v-radio label="Cats" value="radio-b"></v-radio>
                  <v-radio label="Dogs & Cats" value="radio-c"></v-radio>
                </v-radio-group>
              </v-layout>
              <!-- ACCIDENTAL BREEDING -->
              <v-layout mx-2 mt-4>
                <subheader>Over the past calendar year, did you have an accidental breeding?</subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="row" row>
                  <v-radio label="Yes" value="radio-1"></v-radio>
                  <v-radio label="No" value="radio-2"></v-radio>
                </v-radio-group>
              </v-layout>
              <!-- How many breeds -->
              <v-layout mx-2 mt-4>
                <subheader>How many breeds of animals are you currently breeding/selling?</subheader>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="phone" :mask="digit" label="Number of Dog Breeds"></v-text-field>
                </v-flex>
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="phone" :mask="digit" label="Number of Cat Breeds"></v-text-field>
                </v-flex>
              </v-layout>
              <!-- NUMBER OF EMPLOYEES -->
              <v-layout mx-2 mt-4>
                <subheader>How many people are currently working in your operation including yourself?</subheader>
              </v-layout>
              <v-layout row wrap mx-2>
                <v-flex xs12 md4 lg6>
                  <v-text-field v-model="phone" :mask="digit" label="Number of Employees"></v-text-field>
                </v-flex>
              </v-layout>
              <!--ASSOCIATION REALTION -->
              <v-layout mx-2 mt-4>
                <subheader>Are you a member of a relevant breeding or selling association? (Optional)</subheader>
              </v-layout>
              <v-layout row wrap ma-2>
                <v-flex xs12 md4>
                  <v-text-field label="Association Name"></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Membership #"></v-text-field>
                </v-flex>
                <v-flex xs12 md4>
                  <v-text-field label="Website "></v-text-field>
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
