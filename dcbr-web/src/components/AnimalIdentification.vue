<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Animal Identification</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!--OPERATION DETAILS-NAME  -->

              <!-- Type of Operator -->
              <v-layout mx-2 mt-4>
                <v-subheader>Do you maintain a permanent identification of your animals?</v-subheader>
              </v-layout>
              <v-layout mx-2>
                <v-radio-group v-model="hasPermId" name="hasPermId" row>
                  <v-radio label="Yes" :value="true"></v-radio>
                  <v-radio label="No" :value="false"></v-radio>
                </v-radio-group>
              </v-layout>
              <!-- Type of Animal -->
              <div v-if="hasPermId == true">
                <v-layout mx-2 mt-4>
                  <v-subheader>What type of identification technology do you use?</v-subheader>
                </v-layout>
                <v-layout mx-2>
                  <v-radio-group v-model="permIdType" name="permIdType" row>
                    <v-radio label="Microchip" value="MICROCHIP"></v-radio>
                    <v-radio label="Tattoo" value="TATTOO"></v-radio>
                    <v-radio label="Other" value="OTHER"></v-radio>
                  </v-radio-group>
                </v-layout>
                <v-layout row wrap ma-2>
                  <v-flex xs12 md4 v-if="permIdType == 'OTHER'">
                    <v-text-field v-model="otherPermIdType" label="Other Method" name="otherPermIdType"></v-text-field>
                  </v-flex>
                </v-layout>
              </div>
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
    visited: false,
    nameRules: [
      v => !!v || "Name is required",
      v => v.length <= 50 || "Name must be less than 50 characters"
    ],
    email: "",
    emailRules: [
      v => !!v || "E-mail is required",
      v => /.+@.+/.test(v) || "E-mail must be valid"
    ]
  }),

  computed: {
    hasPermId: {
      // getter
      get() {
        if (this.visited == false) {
          return "";
        } else {
          return this.$store.getters["animalIdentification/hasPermId"];
        }
      },
      // setter
      set(value) {
        if (this.hasPermId == "") {
          this.visited = true;
        }
        console.log(value);
        this.$store.dispatch("animalIdentification/hasPermId", value);
        if (value == false) {
          this.$store.dispatch("animalIdentification/permIdType", "");
          this.$store.dispatch("animalIdentification/otherPermIdType", "");
        }
      },
    },
    permIdType: {
      // getter
      get() {
        return this.$store.getters["animalIdentification/permIdType"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("animalIdentification/permIdType", value);
        if (value != "OTHER") {
          this.$store.dispatch("animalIdentification/otherPermIdType", "");
        }
      },
    },
    otherPermIdType: {
      // getter
      get() {
        return this.$store.getters["animalIdentification/otherPermIdType"];
      },
      // setter
      set(value) {
        console.log(value);
        this.$store.dispatch("animalIdentification/otherPermIdType", value);
      },
    }
  }
};
</script>
