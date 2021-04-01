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
            // await axios.post(`http://localhost:8000/events`, {
            //     name : this.name,
            //     ticket_price : this.ticket_price
            // })
            // .then(res => (this.info = res.data))
            // .catch(err => {
            //     console.log(err);
            // })
            await axios({
                method: 'post',
                url: 'http://localhost:8000/events',
                headers: {
                    'accept': 'application/json',
                    "X-CSRFToken": Cookies.get('csrftoken')
                },
                data: {
                    name: this.name,
                    ticket_price: this.ticket_price
                }
            })
            .then(response => (this.name = response.data))
        }
    }
    
}
</script>

<style scoped>

</style>