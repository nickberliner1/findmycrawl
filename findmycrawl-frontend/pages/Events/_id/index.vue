<template>
    <div>
        <nuxt-link to="/events">Back</nuxt-link>
        <h2>{{ $route.params.id }}</h2>
        <img :src="$route.params.cover_image_url" />
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
            const res = await axios.get(`https://sandbox.musement.com/api/v3/activities?offset=0&limit=10/${this.$route.params.id}`, config);
            this.events = res.data.data;
        } catch (err) {
            console.log(err);
        };

        // this.event = await fetch(
        //     `https://api.musement.com/api/v3/venues/164/activities?&offset=0&id=${this.event.uuid}`,
        // {
        //     "method": "GET",
        //     headers: {
        //         "content-type": "application/json"
        //     }
        // }).then(res => res.json())
	    // .catch(error => {
		//     console.log(error);
        // });
        
        // console.log(this.event);
    },
}
</script>