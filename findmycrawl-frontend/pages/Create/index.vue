<template>
    <div class="container">
        <h2>Create event</h2>
        <form @submit="createEvent">
            <strong>Name: </strong>
            <input type="text" v-model="event.name" placeholder="Name" />
            <strong>Description: </strong>
            <input type="textarea" v-model="event.description" placeholder="Describe your event" />
            <strong>Price: </strong>
            <input type="text" v-model="event.ticket_price" placeholder="Price" />
            <button class="btn" type="submit">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {

    data() {
        return {
            event: {
                name: '',
                description: '',
                ticket_price: null
            }
        }
    },

    methods: {
        async createEvent() {
            const config = {
                headers: {
                    'content-type': 'multipart/form-data'
                }
            };
            
            let formData = new FormData();

            try {
                let response = await this.$axios.$post('http://localhost:8000/events/', formData, config);
            } catch (e) {
                console.log(e);
            }
        }
    }
    
}
</script>

<style scoped>

</style>