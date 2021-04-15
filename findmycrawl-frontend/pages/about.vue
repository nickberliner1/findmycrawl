<template>
    <div class="container">
        <div class="heading">
            <h1>About Us</h1>
            <p>this is an app that displays bar crawls</p>
        </div>
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
.heading {
    position: relative;
}

.heading::after {
    position: absolute;
    top: 0;
    width: 100vw;
    background-color: green;
}

</style>