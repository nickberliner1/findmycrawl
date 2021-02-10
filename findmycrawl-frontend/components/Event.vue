<template>
    <nuxt-link :to="'events/' + id">
        <div class="event">
            <h6>{{ event }}</h6>
            <!-- <b-img-lazy 
                thumbnail 
                fluid 
                :src="cover_image_url"
                class="cover-image"
            ></b-img-lazy> -->
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
    width: 10rem;
    height: auto;
    overflow: hidden;
}
</style>