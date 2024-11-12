<template>
  <Layout>
    <template #header>
      <Header></Header>
    </template>
    <template #resume>
      <Resume :label="label"
              :total-label="'Ahorro Total'"
              :amount="amount"
              :total-amount="1000000">
          <template #graphic>
              <Graphic :amounts="amounts"/>
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
             movements: [
                 {
                     id: 0,
                     title: "Movimiento 1",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 100,
                     time: new Date("20-10-2024"),
                 },
                 {
                     id: 1,
                     title: "Movimiento 2",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 200,
                     time: new Date("02-01-2024"),
                 },
                 {
                     id: 2,
                     title: "Movimiento 3",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 500,
                     time: new Date("02-01-2024"),
                 },
                 {
                     id: 3,
                     title: "Movimiento 4",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 200,
                     time: new Date("02-01-2024"),
                 },
                 {
                     id: 4,
                     title: "Movimiento 5",
                     description: "Lorem ipsum dolor sit amet",
                     amount: -400,
                     time: new Date("02-01-2024"),
                 },
                 {
                     id: 5,
                     title: "Movimiento 6",
                     description: "Lorem ipsum dolor sit amet",
                     amount: -600,
                     time: new Date("02-01-2024"),
                 },
                 {
                     id: 6,
                     title: "Movimiento 7",
                     description: "Lorem ipsum dolor sit amet",
                     amount: -300,
                     time: new Date("02-01-2024"),
                 },
                 {
                     id: 7,
                     title: "Movimiento 8",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 100,
                     time: new Date("10-20-2024"),
                 },
                 {
                     id: 8,
                     title: "Movimiento 9",
                     description: "Lorem ipsum dolor sit amet",
                     amount: -300,
                     time: new Date("10-25-2024"),
                 },
                 {
                     id: 9,
                     title: "Movimiento 10",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 500,
                     time: new Date("10-28-2024"),
                 },
                 {
                     id: 10,
                     title: "Movimiento 11",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 500,
                     time: new Date("10-29-2024"),
                 },
                 {
                     id: 11,
                     title: "Movimiento 11",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 500,
                     time: new Date("10-30-2024"),
                 },
                 {
                     id: 12,
                     title: "Movimiento 11",
                     description: "Lorem ipsum dolor sit amet",
                     amount: 500,
                     time: new Date("10-31-2024"),
                 },
             ]
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
                 const lastMovements = lastDays.slice(0, i);

                 return lastMovements.reduce((suma, movement) => {
                     return suma + movement
                 }, 0);
             });
         },
     },
     methods: {
         create(movement){
             this.movements.push(movement);
         },
         remove(id){
             const index = this.movements.findIndex(m => m.id === id);
             this.movements.splice(index, 1);
         }
     }
 }

</script>
