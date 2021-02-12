<template>
    <div class="event-list">
        <Event 
            v-for="event in events" 
            :key="event.id"
            :event="event"
            
        />
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
            perPage: 10
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

            this.events = res.data;
        } catch (err) {
            console.log(err)
        }
    },
}

</script>

<style scoped>
.event-list {
    padding: 1rem;
}
</style>