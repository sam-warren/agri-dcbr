<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex>
        <v-card-title primary-title>
          <v-layout>
            <h4>Cat Breeder</h4>
          </v-layout>
        </v-card-title>
        <v-card flat>
          <!-- INTACT BREEDING CAT -->
          <v-layout mx-2 mt-4>
            <subheader>How many intact breeding female cats over the age of xxxx months do you have?</subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field
                v-model.number="femaleIntactCat"
                type="number"
                label="Number of Female Cats"
              ></v-text-field>
            </v-flex>
          </v-layout>
          <!-- Type of Animal -->
          <v-layout mx-2 mt-4>
            <subheader>How many litters were queened in one calendar year overall (all female cats combined)?</subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field v-model.number="littersQueened" type="number" label="Queened Litters"></v-text-field>
            </v-flex>
          </v-layout>

          <v-layout mx-2 mt-4>
            <subheader>What numnber of kittens did you ............... in the previous calendar year?</subheader>
          </v-layout>

          <v-layout row wrap ma-2>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsTransferred" type="number" label="Transfer"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsSold" type="number" label="Sell"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsTraded" type="number" label="Trade"></v-text-field>
            </v-flex>
            <v-flex xs12 md4>
              <v-text-field v-model.number="catsLeased" type="number" label="Lease"></v-text-field>
            </v-flex>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    valid: false,

    femaleIntactCat: null,

    littersQueened: null,

    catsTransferred: null,
    catsSold: null,
    catsTraded: null,
    catsLeased: null
  })
};
</script>


<style>
</style>