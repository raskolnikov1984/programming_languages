<template>
  <Layout>
    <template #header>
      <Header></Header>
    </template>
    <template #resume>
      <Resume :label="label"
              :total-label="'Ahorro Total'"
              :amount="amount"
              :total-amount="totalAmount">
          <template #graphic>
              <Graphic :amounts="amounts" @select="select"/>
          </template>
          <template #action>
              <Action @create="create"/>
          </template>
      </Resume>
    </template>
    <template #movements>
      <Movements
        :movements="movements"
        @remove="remove"
        />
    </template>
  </Layout>
</template>

<script>
 import Layout from "./LayoutForm.vue";
 import Header from "./HeaderForm.vue";
 import Resume from "./Resume/IndexForm.vue";
 import Action from "./ActionModal.vue";
 import Movements from "./Movements/IndexForm.vue";
 import Graphic from "./Resume/GraphicView.vue";

 export default {
     name: 'HomeForm',
     components: {
         Layout,
         Header,
         Resume,
         Action,
         Movements,
         Graphic
     },
     data(){
         return {
             amount: null,
             label: null,
             // amounts: [100, 200, 500, 200, -400, -600, -300, 0, 300, 500],
             movements: []
         }
     },
     computed: {
         amounts() {
             const lastDays = this.movements
                                  .filter(m => {
                                      const today = new Date();
                                      const oldDate = today.setDate(today.getDate() - 30);

                                      return m.time > oldDate;
                                  })
                                  .map(m => m.amount);

             return lastDays.map((m, i) => {
                 const lastMovements = lastDays.slice(0, i+1);
                 return lastMovements.reduce((suma, movement) => {
                     return suma + movement
                 }, 0);
             });
         },
         totalAmount(){
             return this.movements.reduce((suma, m) => {
                 return suma + m.amount;
             }, 0)
         }
     },
     mounted(){
         const movements = JSON.parse(localStorage.getItem("movements"));
         if (Array.isArray(movements)){
             this.movements = movements.map(m => {
                 return { ...m, time: new Date(m.time) };
             });
         }
     },
     methods: {
         create(movement){
             this.movements.push(movement);
         },
         remove(id){
             const index = this.movements.findIndex(m => m.id === id);
             this.movements.splice(index, 1);
         },
         save(){
             localStorage.setItem("movements", JSON.stringify(this.movements));
         },
         select(el){
             this.amount = el;
         }
     }
 }

</script>
