<template>
  <v-app>
    <!-- <project/> -->
    <v-content>
      <Header/>

      <v-container grid-list-xl text-xs-center>
        <v-layout>
          <v-flex xs12>
            <Form/>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import Project from "@/components/Project";
import Header from "@/components/Header";
import Form from "@/components/Form";
export default {
  name: "App",
  components: {
    Header,
    Form,
    Project
  }
};
</script>


