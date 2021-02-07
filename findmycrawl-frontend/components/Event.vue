<template>
    <nuxt-link :to="'events/' + id">
        <div class="event">
            <h6>{{ event.title }}</h6>
            <b-img-lazy 
                thumbnail 
                fluid 
                :src="event.cover_image_url"
                class="cover-image"
            ></b-img-lazy>
        </div>
    </nuxt-link>
</template>

<script>
export default {
    name: "Event",
    props: ['event', 'id']
}
</script>

<style scoped>
.event {
    padding: 1rem;
    border: 1px solid gray;
    margin: 1rem;
    color: black;
    flex: 1 1 30%;
}

.cover-image {
    width: auto;
    height: auto;
    overflow: hidden;
}
</style>