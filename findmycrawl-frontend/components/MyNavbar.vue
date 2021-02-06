<template>
    <b-navbar type="dark" variant="dark">
        <b-navbar-nav class="navbar">
            <nuxt-link to="/" class="link">Home</nuxt-link>
            <nuxt-link to="/about" class="link">About</nuxt-link>
            <nuxt-link to="/events" class="link">Events</nuxt-link>
        </b-navbar-nav>
    </b-navbar>
</template>

<script>
export default {
    name: 'MyNavbar'
}
</script>

<style scoped>
.navbar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    padding-bottom: 1rem;
}

.link {
    margin-right: 2rem;
}
</style>