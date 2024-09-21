<template>
  <div class="smallcontainer">
    <h1>EMPLOYEES</h1>
    <Employeeform @add:employee="addingdata"/>
    <Employeetable v-bind:edata="empdata" 
    @delete:employee="DeleteEmployee"
    @saved:employee="saved"/> 
  </div>
</template>

<script>
import Employeetable from './components/EmployeeTable.vue'
import Employeeform from './components/EmployeeForm.vue'
export default {
  name: 'App',
  components: {
    Employeetable,
    Employeeform
  },
  data(){
    return {
      empdata:[],
      api_url:'http://127.0.0.1:8000/'
    }
  },
  methods:{
    async addingdata(employee){
      try {
        await fetch(this.api_url+'create_employee/',
        { method:'post',
          body:JSON.stringify(employee),
          headers:{
            'content-type':'application/json; charset=UTF-8'
          }
        })
        // const data = await response.json()
        this.getemployees();
       
        //   // const lastid = this.empdata.length>0?this.empdata[this.empdata.length-1].id:0
        //   // const id = lastid + 1
        //   // const newemployee = {...employee,id}   
        // this.empdata=[...this.empdata,data];

      } catch(error) {
        console.log(error)
      }
      
    },
    async DeleteEmployee(id) {
      try{
        await fetch (this.api_url+'delete_employee/'+id,{
          method:'DELETE'
        })
        this.getemployees();
        // this.empdata=this.empdata.filter((e)=>{
        //   return e.id != id;
      // })
      } catch (error){
        console.log(error)
      } 
    },
    async saved(id,updatedemployee){
      try {

        await fetch(this.api_url+'update_employee/'+id,
        {
                method:'PUT',
                body:JSON.stringify(updatedemployee),
                headers:{
              'content-type':'application/json; charset=UTF-8'
              }
        })
        // const data = await response.json();

        // this.empdata.map((employee)=>{
        // return employee.id == id?data:employee;})

    } catch (error) {
      console.log(error)
    }
    },
    async getemployees(){
      try {
        const response = await fetch (this.api_url+'employee_api/',{method:'GET'})
        const data = await response.json();
        this.empdata = data;

      } catch(error) {
        console.log(error);
      }
    },
    
  },
  mounted() {
      this.getemployees();
    }
}
</script>

<style>
  .smallcontainer {
    max-width: 700px;
  }
</style>
