<template>
    <div class="container">
        <div class="return">
            <nuxt-link class="back" to="/events"><fa class="back-arrow" :icon="['fas', 'arrow-left']" />Back to events</nuxt-link>
        </div>
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

<style scoped>
.return {
    margin-bottom: 2em;
}

.back-arrow {
    display: none;
}

.back:hover .back-arrow {
    display: inline-block;
}
</style>