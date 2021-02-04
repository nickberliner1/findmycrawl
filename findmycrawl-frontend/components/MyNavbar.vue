<template>
    <b-navbar type="dark" variant="dark" class="navbar">
        <b-navbar-nav>
            <b-nav-item href="#">Home</b-nav-item>
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