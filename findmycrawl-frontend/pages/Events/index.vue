<template>
    <div 
        v-if="this.apiLoaded"
        class="event-list"
    >
        <Event 
            v-for="event in events" 
            :key="event.id"
            :event="event"
        />
    </div>
    <div v-else 
        class="no-events"
    >
        <h2>We're sorry, there aren't any events here</h2>
    </div>

<!-- :name="event.name"
            :pic="event.cover_image_url"
            :city="event.city" 
            :id="event.id"

            
            -->

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
            perPage: 10,
            apiLoaded: false
        };
    },

    async created() {
        const config = {
            headers: {
                'Accept': "application/json"
            }
        };
        try {
            const res = await axios.get(`http://localhost:8000/events`, config);
            // const res = await axios.get('https://sandbox.musement.com/api/v3/activities?&limit=10', config);
            console.log(res);
            
            this.apiLoaded = true;
            this.events = res.data;
        } catch (err) {
            console.log(err)
        }
    },
}

</script>

<style scoped>
a {
    text-decoration: none;
}
.event-list {
    padding: 1rem;
}
.no-events {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 5rem;
}
</style>