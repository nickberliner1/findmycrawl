<template>
    <nuxt-link :to="'events/' + id">
        <div class="event">
            <p>{{ event.title }}</p>
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
}
</style>