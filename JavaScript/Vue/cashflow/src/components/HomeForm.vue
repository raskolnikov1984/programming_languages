<template>
  <Layout>
    <template #header>
      <Header></Header>
    </template>
  </Layout>
</template>

<script>
  import Layout from "./LayoutForm.vue";
  import Header from "./HeaderForm.vue";

  export default {
    name: 'HomeForm',
      components: {
          Layout,
          Header,
      }

  }
</script>
