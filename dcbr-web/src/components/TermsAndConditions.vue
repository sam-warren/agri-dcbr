<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex xs12>
        <v-card flat>
          <v-form>
            <v-container>
              <!--Name Section  -->
              <v-layout row wrap mx-2>
                <v-flex>
                  <v-checkbox v-model="hasAgreed" name="hasAgreed" required>
                    <template v-slot:label>
                      <div>
                        I have read and agree to the
                        <v-tooltip bottom>
                          <template v-slot:activator="{ on }">
                            <a
                              target="_blank"
                              href="https://www2.qa.gov.bc.ca/assets/gov/farming-natural-resources-and-industry/agriculture-and-seafood/animal-and-crops/animal-health/animal-welfare/cat_and_dog_commercial_breeder_regulation.pdf"
                              @click.stop
                              v-on="on"
                            >terms and conditions</a>
                          </template>
                          Opens in new window
                        </v-tooltip> and
                      </div>
                    </template>
                  </v-checkbox>
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
import { mapState } from "vuex";
export default {
  valid: false,
  mask: "",
  computed: {
    ...mapState({
      termsAndConditions: state => state.termsAndConditions
    }),
    hasAgreed: {
      get() {
        return this.$store.getters["termsAndConditions/hasAgreed"];
      },
      set(value) {
        console.log(value)
        this.$store.dispatch("termsAndConditions/hasAgreed", value);
      }
    }
  }
};
</script>
