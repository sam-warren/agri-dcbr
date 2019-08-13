<template>
  <v-form v-model="valid">
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex>
          <v-card-title primary-title>
            <v-layout>
              <h4>Dog Breeder</h4>
            </v-layout>
          </v-card-title>
          <v-card flat>
            <!-- INTACT BREEDING DOG -->
            <v-layout mx-2 mt-4>
              <subheader>How many intact breeding female dogs over the age of eight months do you have?</subheader>
            </v-layout>

            <v-layout row wrap ma-2>
              <v-flex xs12 md4>
                <v-text-field
                  v-model.number="femaleDogNum"
                  type="number"
                  label="Number of Female Dogs"
                ></v-text-field>
              </v-flex>
            </v-layout>
            <!-- Type of Animal -->
            <v-layout mx-2 mt-4>
              <subheader>How many litters were whelped in one calendar year overall (all female dogs combined)?</subheader>
            </v-layout>

            <v-layout row wrap ma-2>
              <v-flex xs12 md4>
                <v-text-field v-model.number="littersWhelped" type="number" label="Whelped Litters"></v-text-field>
              </v-flex>
            </v-layout>

            <v-layout mx-2 mt-4>
              <subheader>What number of puppies did you ............... in the previous calendar year?</subheader>
            </v-layout>

            <v-layout row wrap ma-2>
              <v-flex xs12 md4>
                <v-text-field v-model.number="dogsTransferred" type="number" label="Transfer"></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field v-model.number="dogsSold" type="number" label="Sell"></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field v-model.number="dogsTraded" type="number" label="Trade"></v-text-field>
              </v-flex>
              <v-flex xs12 md4>
                <v-text-field v-model.number="dogsLeased" type="number" label="Lease"></v-text-field>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-form>
</template>
<script>
export default {
  data: () => ({
    valid: false,
    femaleDogNum: null,
    dogsTransferred: null,
    dogsSold: null,
    dogsTraded: null,
    dogsLeased: null
  })
};
</script>