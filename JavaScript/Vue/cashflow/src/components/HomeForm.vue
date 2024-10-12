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
      <Movements :movements="movements"></Movements>
    </template>
  </Layout>
</template>

<script>
 import Layout from "./LayoutForm.vue";
 import Header from "./HeaderForm.vue";
 import Resume from "./Resume/IndexForm.vue";
 import Movements from "./Movements/IndexForm.vue";

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
             movements: [
                 {id: 0, title: "Movimiento1",
                  description: "Description", amount: 1000},
                 {id: 1, title: "Movimiento2", description: "Description", amount: 2000},
                 {id: 2, title: "Movimiento3", description: "Description", amount: -3000}
             ]
         }
     },
 }
</script>
