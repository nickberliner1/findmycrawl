<template>
    <div>
        <nuxt-link to="/events">Back</nuxt-link>
        <h2>{{ event.title }}</h2>
        <img :src="event.cover_image_url" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            event: {}
        };
    },

    async created() {
        this.event = await fetch(
            `https://api.musement.com/api/v3/venues/164/activities?&offset=0&id=${this.event.uuid}`,
        {
            "method": "GET",
            headers: {
                "content-type": "application/json"
            }
        }).then(res => res.json())
	    .catch(error => {
		    console.log(error);
        });
        
        console.log(this.event);
    },
}
</script>