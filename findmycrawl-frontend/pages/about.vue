<template>
    <div>
        <h1>About Us</h1>
        <p>this is an app that displays bar crawls</p>
    </div>
</template>

<script>

export default {
    head() {
        return {
            title: 'About Us',
            meta: [
                {
                    hid: 'description',
                    name: 'description',
                    content: 'Find bar crawl near you'
                }
            ]
        }
    }
}
</script>

<style scoped>

</style>