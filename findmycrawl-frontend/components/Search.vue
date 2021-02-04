<template>
    <div>
        <b-form-input
            class="search"
            placeholder="Search your city"
            :search="search"
        ></b-form-input>
    </div>
</template>

<script>

export default {
    name: 'Search',
    components: {
        
    },

	methods: {
		search(input) {
			if (input.length < 1) { 
                return [] 
            }
			return cities.filter(city => {
                return city.toLowerCase()
                .startsWith(input.toLowerCase())
			})
		}
  	}
    
}
</script>

<style scoped>

.search {
    border-radius: 10px;
    width: 40vw;
    height: 7vh;
}

</style>