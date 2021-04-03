<template>
    <div class="container">
        <nuxt-link to="/events"><fa :icon="['fas', 'arrow-left']" /></nuxt-link>
        <!-- <small>{{ $route.params.id }}</small> -->
        <!-- <p>{{ $route.params.name }}</p> -->
        <h2>{{ event.name }}</h2>
        <img :src="event.main_picture" />
        <p>{{ event.description }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {

    data() {
        return {
            event: {}
        };
    },

    async created() {

        const config = {
            headers: {
                "content-type": "application/json"
            }
        };

        try {
            const res = await axios.get(`http://localhost:8000/events/${this.$route.params.id}`, config);
            this.event = res.data;
        } catch (err) {
            console.log(err);
        };

    },
}
</script>