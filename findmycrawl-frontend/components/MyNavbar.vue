<template>
    <b-navbar type="dark" variant="dark" class="navbar">
        <b-navbar-nav>
            <nuxt-link to="/">Home</nuxt-link>
            <nuxt-link to="/about">About</nuxt-link>
            <nuxt-link to="/events">Events</nuxt-link>

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
    justify-content: space-between;
    align-items: center;
    padding-bottom: 1rem;
}
</style>