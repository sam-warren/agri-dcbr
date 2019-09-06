<template>
  <v-container>
    <v-layout>
      <v-card>
        <v-flex ma-4>
          <h2 class="text-md-center">Welcome!</h2>
          <br />
          <p>
            Starting in [Date], commercial cat and dog breeders and sellers in B.C. will need to register with the provincial government.
            <strong>It is a legislated requirement to register.</strong>
            Individuals and businesses breeding and/or selling dogs and/or cats in B.C. will be able to complete their registration online by providing:
          </p>
          <p class="text-md-left">
            1. Contact information
            <br />2. Email address
            <br />3. Location of operation(s)
            <br />4. Number of cats and/or dogs
            <br />5. Number of litters
          </p>
          <p>There is no fee to register. Commercial cat and dog breeders and/or sellers must confirm they are aware of and abide by the obligations of the Cat and Dog Commercial Breeding Regulation.
          <br><br>

            <strong>Who must register?</strong><br>
          
            If you are a commercial breeder and/or seller of dogs and/or cats in British Columbia it is mandatory for you to register, provide accurate information, and follow the Operator Duties and Standards of Care in the Cat and Dog Commercial Breeding Regulation. <br><br>
            Exceptions: Persons or businesses that are intending to give puppies and/or kittens away with no monetary or other considerable exchange. In this case, registration is not mandatory, nor is adhering to the Commercial Dog and Cat Breeders and Sellers Standards of Care. <br><br>
            If persons or businesses plan to sell, trade or lease the offspring of a one-time accidental breeding, registration is mandatory, and they must adhere to the relevant sections of the Cat and Dog Commercial Breeding Regulation. <br><br>
            Other exceptions include registered charities such as humane societies, rescue societies, the BC SPCA, etc.<br><br>

            <strong>Why register?</strong><br>
            This regulatory framework was established to 1) ensure a minimum level of animal care and well-being for dogs and cats bred and sold in BC; and 2) provide consumers with a means to verify that a particular breeder and/or seller has agreed to adhere to the regulatory framework. <br><br>
            The Registry will provide:
          </p>
          <p class="text-md-left">
            1. A repository where breeders/sellers will register their operation(s);
            <br />2. A means for breeders/sellers to agree to follow a minimum standard of care;
            <br />3. Communicate important documents (provincial minimum Standards of Care regulation) and educational documents with operators;
            <br />4. Provide the public with a place to search for registered breeders and their status.
          </p>
          <p><strong>How to register?</strong><br>
            - Online<br>
            - By Phone<br>
            - By Mail or Fax<br>
          </p>
          <p>
            YOUR PERSONAL INFORMATION IS COLLECTED BY THE MINISTRY OF AGRICULTURE UNDER SECTION(S) 26 (C) & (E) OF THE FREEDOM OF INFORMATION AND PROTECTION OF PRIVACY ACT FOR THE PURPOSE OF LOCATING IRRESPONSIBLE DOG AND CAT BREEDERS AND SELLERS. FOR ANY QUESTIONS ABOUT THIS COLLECTION, PLEASE CONTACT:
          </p>
          <p>
            MINISTRY OF AGRICULTURE <br><br>PHONE NUMBER (TBD) AND E-MAIL (TBD)
          </p>
        </v-flex>
      </v-card>
    </v-layout>
    <v-layout>
      <v-flex>
        <v-btn large round block dark class="primary">
          <button @click="$router.push('register')">Start Registration</button>
        </v-btn>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
// import Navbar from "@/components/Navbar";
export default {
  components: {
    // Navbar
  }
};
</script>

