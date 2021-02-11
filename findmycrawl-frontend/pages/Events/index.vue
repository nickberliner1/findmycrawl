<template>
    <div class="event-list">
        <Event 
            v-for="event in events" 
            :key="event.id"
            :id="event.id"
            :event="event"
            :name="event.name"
            :pic="event.cover_image_url"
            :city="event.city"
        />
    </div>
</template>

<script>
import Event from '../../components/Event.vue';
import axios from 'axios';

export default {
    components: { 
        Event 
    },
    
    data() {
        return {
            events: [],
            currentPage: 1,
            perPage: 10
        };
    },

    async asyncData({ $axios, params }) {
        try {
            this.events = await $axios.$get(`/events/`);
            return {
                events
            };
        } catch (err) {
            return {
                events: []
            };
        }
    },

    // async created() {
        
    //     const config = {
    //         headers: {
    //             'Accept': "application/json"
    //         }
    //     };

    //     try {
    //         const res = await axios.get('https://sandbox.musement.com/api/v3/activities?&limit=10', config);
    //         this.events = res.data;

    //         console.log(res.data.data);

    //     } catch (err) {
    //         console.log(err);
    //     }

    // },
}

</script>

<style scoped>
.event-list {
    padding: 1rem;
}
</style>