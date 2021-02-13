<template>
    <nuxt-link 
        :to="'events/' + event.id"
    >
        <div class="event">
            <!-- <b-img-lazy 
                thumbnail 
                fluid 
                :src="event.main_picture"
                class="cover-image"
            ></b-img-lazy> -->
            <div class="info">
                <h5>{{ event.name }}</h5>
                <span v-if="event.comes_with_free_drinks">
                    <fa :icon="['far', 'lightbulb']" />
                </span>
                <p>{{ event.ticket_price }}</p>
            </div>
        </div>
    </nuxt-link>
</template>

<script>
export default {
    name: "Event",
    props: ['id', 'event', 'name']
}
</script>

<style scoped>

.event {
    display: flex;
    padding: 1rem;
    margin: 1rem auto;
    width: 80%;
    top: 0px;
    position: relative;
    border-radius: 10px;
    box-shadow: rgba(0, 0, 0, 0.247) 0px 5px 15px;
    color: black;
    transition-property: top;
    transition-duration: 0.1s;
    transition-timing-function: linear;
}

.event:hover {
    position: relative;
    top: -4px;
    box-shadow: rgba(0, 0, 0, 0.377) 0px 5px 15px;
}

.cover-image {
    width: 10rem;
    height: auto;
    overflow: hidden;
}

.info {
    margin-left: 5rem;
}
</style>