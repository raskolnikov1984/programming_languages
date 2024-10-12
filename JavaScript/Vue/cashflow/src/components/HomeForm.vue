<template>
  <Layout>
    <template #header>
      <Header></Header>
    </template>
    <template #resume>
      <Resume></Resume>
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
   }
 }
</script>
