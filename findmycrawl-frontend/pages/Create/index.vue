<template>
    <div class="container">
        <h2>Create event</h2>
        <form @submit="createEvent">
            <strong>Name: </strong>
            <input type="text" v-model="name" placeholder="Name" />
            <strong>Price: </strong>
            <input type="text" v-model="ticket_price" placeholder="Price" />
            <button class="btn">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {

    data() {
        return {
            name: '',
            ticket_price: ''
        }
    },

    methods: {
        async createEvent() {
            await axios.post(`http://localhost:8000/events`, {
                name: this.name,
                ticket_price: this.ticket_price
            })
            .then(res => {
                console.log(res);
            })
            .catch(err => {
                console.log(err);
            })
        }
    }
    
}
</script>

<style scoped>

</style>