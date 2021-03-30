<template>
	<div class="homepage">
		<div class="hero-container">
			<div class="hero-content">
				<h1 class="title">
				Find Your Crawl
				</h1>
				<Search />
				<div id="map"></div>
			</div>		
			
		</div>
	</div>
</template>

<script>
import Search from '../components/Search';
// import { Loader, LoaderOptions } from 'google-maps';

const w3wApiKey = process.env.W3W_API_KEY;
const gmApiKey = process.env.GOOGLE_MAPS_API_KEY;

// const options = { libraries: ['bar'] };
// const loader = new Loader(gmApiKey, options);

export default {
	
	components: {
		Search
	},

	// mounted: async function() {
	// 	const google = await loader.load();
	// 	const map = new google.maps.Map(document.getElementById("map"), {
	// 		center: { lat: 47.1, lng: 15.5 },
	// 		zoom: 12
	// 	})
	// }
}
</script>

<style>

.hero-container {
	background-image: 
		linear-gradient(
			rgba(17,17,17,.35),
			rgba(17,17,17,.35)
		),
		url("https://images.unsplash.com/photo-1517457373958-b7bdd4587205?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80");
	background-size: cover;
	min-height: 100vh;
	box-sizing: border-box;
	margin: 0;
	display: flex;
	justify-content: center;
}

.hero-content {
	display: flex;
	flex-direction: column;
	align-items: center;
}

.title {
  font-family:
    'Quicksand',
    'Source Sans Pro',
    -apple-system,
    BlinkMacSystemFont,
    'Segoe UI',
    Roboto,
    'Helvetica Neue',
    Arial,
    sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: white;
  letter-spacing: 1px;
}

</style>
