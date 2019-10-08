<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs12>
        <v-card flat>
          <v-form>
            <v-container>
              <!--Name Section  -->
              <v-layout row wrap align-center>
                <v-tooltip v-model="show" bottom>
                  <template v-slot:activator="{ on }">
                    <div v-on="on">
                      <v-checkbox
                        :disabled="!hasClicked"
                        v-model="hasAgreed"
                        name="hasAgreed"
                        required
                      ></v-checkbox>
                    </div>
                  </template>
                  <span>Please read the terms and conditions before agreeing</span>
                </v-tooltip>
                <div class="v-label theme--light mb-1">
                  I have read and agree to the
                  <a
                    class="v-label"
                    @click="clickedTaC()"
                    target="_blank"
                    href="https://www2.qa.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/agriculture-and-seafood/animal-and-crops/animal-health/animal-welfare/cat_and_dog_commercial_breeder_regulation.pdf"
                  >terms and conditions</a>
                </div>
              </v-layout>
            </v-container>
          </v-form>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>
<script>
import { mapState } from "vuex";
export default {
  valid: false,
  mask: "",
  data: () => ({
    hasClicked: false,
    show: false
  }),
  methods: {
    clickedTaC() {
      this.hasClicked = true;
    }
  },
  computed: {
    ...mapState({
      termsAndConditions: state => state.termsAndConditions
    }),
    hasAgreed: {
      get() {
        return this.$store.getters["termsAndConditions/hasAgreed"];
      },
      set(value) {
        console.log(value);
        this.$store.dispatch("termsAndConditions/hasAgreed", value);
      }
    }
  }
};
</script>
<style scoped>
.v-input {
  flex: none;
}
</style>