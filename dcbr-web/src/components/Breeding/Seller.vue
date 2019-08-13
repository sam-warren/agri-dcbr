<template>
  <v-container grid-list-md text-xs-center>
    <v-layout row wrap>
      <v-flex>
        <v-card-title primary-title>
          <v-layout>
            <h4>Seller</h4>
          </v-layout>
        </v-card-title>
        <v-card flat>
          <v-layout mx-2>
            <subheader>Seller related questions will go here ?</subheader>
          </v-layout>
          <v-layout mx-2>
            <v-radio-group v-model="hasId" row>
              <v-radio label="Yes" value="true"></v-radio>
              <v-radio label="No" value="false"></v-radio>
            </v-radio-group>
          </v-layout>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {};
</script>

<style>
</style>