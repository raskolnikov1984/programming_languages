<template>
  <Layout>
    <template #header>
      <Header></Header>
    </template>
    <template #resume>
      <Resume :label="label"
              :total-label="'Ahorro Total'"
              :amount="amount"
              :total-amount="100000">
          <template #graphic>
              graphic
          </template>
          <template #action>
              action
          </template>
      </Resume>
    </template>
    <template #movements>
      <Movements></Movements>
    </template>
  </Layout>
</template>

<script>
 import Layout from "./LayoutForm.vue";
 import Header from "./HeaderForm.vue";
 import Resume from "./Resume/IndexForm.vue";
 import Movements from "./MovementsForm.vue";

 export default {
   name: 'HomeForm',
   components: {
     Layout,
     Header,
     Resume,
     Movements
   },
     data(){
         return {
             amount: null,
             label: null,
         }
     },
 }
</script>
