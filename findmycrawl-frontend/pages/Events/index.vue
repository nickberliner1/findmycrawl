<template>
    
</template>

<script>
import axios from "axios";


export default {
    
    headers: {
        'x-rapidapi-key': '4571ec82e7msh34c5415899a888bp1847cejsnbef4ed279e9c',
        'x-rapidapi-host': 'robby.p.rapidapi.com'
    },

    async asyncData({ $axios }) {
        const results = await $axios.$get('https://robby.p.rapidapi.com/search.json', {
            params: {
                key: '4571ec82e7msh34c5415899a888bp1847cejsnbef4ed279e9c',
                country: 'US',
                lng: '-74.00597',
                city: 'New York',
                lat: '40.71435',
                to: '2016-08-01T20:30:00+08:00',
                limit: '30',
                distance: '10',
                from: '2016-06-30T20:30:00'
            }
        });
        return { results };
    },

}

// axios.request(options).then(function (response) {
// 	console.log(response.data);
// }).catch(function (error) {
// 	console.error(error);
// });

</script>

const options = {
  method: 'GET',
  url: 'https://robby.p.rapidapi.com/search.json',
  params: {
    key: '4571ec82e7msh34c5415899a888bp1847cejsnbef4ed279e9c',
    country: 'US',
    lng: '-74.00597',
    city: 'New York',
    lat: '40.71435',
    to: '2016-08-01T20:30:00+08:00',
    limit: '30',
    distance: '10',
    from: '2016-06-30T20:30:00'
  },