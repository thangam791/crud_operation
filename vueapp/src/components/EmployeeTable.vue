<template>
    <div id="employee-table">
        <p v-if="edata.length<1">No Employees</p>
        <table v-else>
            <thead>
                <tr>
                    <th>Employee name</th>
                    <th>Employee email</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="emp in edata" v-bind:key="emp.id">
                    <td v-if="editing == emp.id">
                        <input type="text" v-model="emp.name">
                    </td>
                    <td v-else>{{ emp.name }}</td>
                    <td v-if="editing == emp.id">
                        <input type="text" v-model="emp.email">
                    </td>
                    <td v-else>{{ emp.email }}</td>
                    <td v-if="editing == emp.id">
                        <button @click="saveemployee(emp)">save</button>
                        <button @click="canceledit(emp)">cancel</button>
                    </td>
                    <td v-else>
                        <button @click="editmode(emp)">Edit</button>
                        <button @click="$emit('delete:employee',emp.id)">Delete</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>
<script>
export default {
    name :'employee-table',
    props:{
        edata:Array
    },
    data(){
        return{
            editing:null,
            // editemployee:{
            //     name:'',
            //     email:''
            // }
            catchedemployee:null,
        }
    },
    methods: {
        editmode(emp){
            this.editing = emp.id
            this.catchedemployee = Object.assign({},emp)
        },
        saveemployee(employee){
            if(employee.name == ''||employee.email =='') {
                return ;
            }
            this.$emit('saved:employee',employee.id,employee)
            this.editing=null;
        },
        canceledit(employee){
            this.editing=null
            Object.assign(employee,this.catchedemployee);
        }
    }
}
</script>
<style>
    button {
        margin:0 0.5rem 0 0;
    }
</style>