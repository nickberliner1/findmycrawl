<template>
    <div class="event-list">
        <Event 
            v-for="event in events" 
            :key="event.id"
            :id="event.id"
            :title="event.title"
            :pic="event.cover_image_url"
            :city="event.city"
        />
    </div>
</template>

<script>
import Event from '../../components/Event.vue';
import axios from 'axios';

export default {
  components: { Event },
    
    data() {
        return {
            events: [],
            currentPage: 1,
            perPage: 10
        };
    },

    async created() {
        // this.events = await fetch(
        //     `https://api.musement.com/api/v3/venues/164/activities?&page=${this.currentPage}&limit=${this.perPage}&offset=0`,
        // {
        //     "method": "GET",
        //     headers: {
        //         "content-type": "application/json"
        //     }
        // }).then(res => res.json())
	    // .catch(error => {
		//     console.log(error);
        // });
        
        const config = {
            headers: {
                'Accept': "application/json"
            }
        };

        try {
            const res = await axios.get('https://sandbox.musement.com/api/v3/activities?&limit=10', config);
            
            this.events = res.data.data;

            console.log(res.data.data);

        } catch (err) {
            console.log(err);
        }

    },
}

</script>

<style scoped>
.event-list {
    padding: 1rem;
}
</style>