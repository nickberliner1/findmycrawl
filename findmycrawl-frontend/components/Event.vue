<template>
    <nuxt-link :to="'events/' + id">
        <div class="event">
            <p>{{ event }}</p>
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

</style>