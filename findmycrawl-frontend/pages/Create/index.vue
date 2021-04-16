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
            <button class="btn" type="submit">Submit</button>
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
        createEvent() {
            const data = {
                name: '',
                description: '',
                ticket_price: ''
            };

            axios.post(`http://localhost:8000/events/?format=api`, data, {
                headers: {
                    'Content-type': 'application/json'
                }
            })
            .then(res => {
                console.log(res)
            })
            .catch(err => {
                console.log(err.res)
            })
        }
    }
    
}
</script>

<style scoped>

</style>