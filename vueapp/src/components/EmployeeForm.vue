<template>
    <div id="employee-form">
        <form v-on:submit.prevent="handlesubmit">
            <label>Employee Name</label> 
            <input type="text" v-model="employee.name"
            :class="{'has-error' : submitting&&invalidName}"
            @focus="clearstatus"
            @keypress="clearstatus"
            ref="firstInput"
            />

            <label>Employee Email</label>
            <input type="text" v-model="employee.email"
            :class="{'has-error':submitting&&invalidEmail}"
            @focus="clearstatus"
            @keypress="clearstatus"
            />

            <p v-if="submitting && error" class="error-message">please fill out all the required fields!</p>
            <p v-if="success" class="success-message">successfully added Employee!</p>

            <button>Add Employee</button>
        </form>
    </div>
</template>
<script>
export default {
    name:'employee-form',
    data() {
        return{
            submitting:false,
            success:false,
            error:false,
            employee:{
                name:'',
                email:'',
        }
        }
    },
    methods:{
        handlesubmit(){
            this.submitting=true;
            this.clearstatus();

            if(this.invalidName||this.invalidEmail) {
                this.error=true;
                return;
            }
            this.$emit('add:employee',this.employee)
            this.$refs.firstInput.focus();

            this.employee = {
                name:'',
                email:'',
            };

            this.success=true;
            this.error=false;
            this.submitting=false;
        },
        clearstatus() {
            this.success=false;
            this.error=false;
        },
    },
    computed:{
        invalidName() {
            return this.employee.name==='';
        },
        invalidEmail() {
            return this.employee.email==='';
        },
    }
}
</script>
<style scoped>
    form {
        margin-bottom: 2rem;
    }
    [class*='-message'] {
        font-weight: 500;
    }
    .error-message {
        color:red;
    }
    .success-message {
        color:green;
    }
</style>