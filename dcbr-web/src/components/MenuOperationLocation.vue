<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-card-title primary-title>
        <div>
          <h2>Operation Locations</h2>
        </div>
      </v-card-title>
      <v-flex xs12>
        <v-card flat>
          <v-form v-model="valid">
            <v-container>
              <!--OPERATION DETAILS-NAME  -->

              <!-- Type of Operator -->
              <v-layout mt-4>
                <v-subheader>Do you have additional operation locations?</v-subheader>
              </v-layout>

              <v-radio-group v-model="hasAdditionalLocations" row>
                <v-radio label="Yes" value="true"></v-radio>
                <v-radio label="No" value="false"></v-radio>
              </v-radio-group>
              <div v-if="this.hasAdditionalLocations == 'true'">
                <v-card-title primary-title>
                  <h2>Operation Location(s)</h2>
                </v-card-title>
                <div v-for="(location, index) in locations" :key="index">
                  <OperationLocation :number="index" />
                </div>
                <div class="text-center">
                  <v-btn @click="addLocation()">
                    Add
                    <v-icon dark>add</v-icon>
                  </v-btn>
                  <v-btn @click="removeLocation()" :disabled="this.locations.length == 1">
                    Remove
                    <v-icon dark>remove</v-icon>
                  </v-btn>
                </div>
              </div>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import OperationLocation from "@/components/OperationLocation";
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
  components: {
    OperationLocation
  },
  methods: {
     addLocation() {
      this.$store.dispatch("operationLocations/locations", { operation: "add" });
    },
    removeLocation() {
      if (this.$store.getters["operationLocations/locations"].length > 1) {
        this.$store.dispatch("operationLocations/locations", { operation: "remove" });
      }
    }
  },
  computed: {
    hasAdditionalLocations: {
      // getter
      get() {
        return this.$store.getters["operationLocations/hasAdditionalLocations"];
      },
      // setter
      set(value) {
        this.$store.dispatch("operationLocations/hasAdditionalLocations", value);
        if(value == "true") {
          if(this.$store.getters["operationLocations/locations"].length == 0) {
            this.$store.dispatch("operationLocations/locations", { operation: "add" });
          }
        }
      }
    },
    locations: {
      // getter
      get() { 
        return this.$store.getters["operationLocations/locations"];
      },
    },
  },
};
</script>
