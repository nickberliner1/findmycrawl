<template>
    <div class="container">
        <h2>Create event</h2>
        <form @submit="createEvent">
            <strong>Name: </strong>
            <input type="text" v-model="name" placeholder="Name" />
            <strong>Description: </strong>
            <input type="textarea" v-model="description" placeholder="Describe your event" />
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
            description: '',
            ticket_price: ''
        }
    },

    methods: {
        async createEvent() {
            const res = await this.$axios.$post(
                `http://localhost:8000/events`,
                {
                    name: 'name',
                    description: 'description',
                    ticket_price: 'ticket_price'
                }
            );
        }
    }
    
}
</script>

<style scoped>

</style>