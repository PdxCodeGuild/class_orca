Vue.component("current-conditions", {
    template:   `<div>
                    <p><button type="submit" @click="getCurrent(); show = !show">Current Conditions</button></p>
                    <div v-if="show">
                        <p v-for="(parameter, value) in current">{{ value }}: {{ parameter }}</p> 
                    </div>                
                </div>`,
    data: function () {
        return {
            current: {
                temperature: null,
                feels_like: null,
                humidity: null,
                wind_speed: null,
            },
        }
    },
    props: ["conditions", "show"],
    methods: {
        getCurrent: function() {
            this.current.feels_like = this.conditions.current.feels_like
            this.current.humidity = this.conditions.current.humidity
            this.current.temperature = this.conditions.current.temp
            this.current.description = this.conditions.current.weather[0].description
            this.current.wind_speed = this.conditions.current.wind_speed
        }
    },
})

let vm = new Vue({
    el: "#weather-app",
    data: {
        locationText: "",
        location: {},
        location_history: {},
        lat: null,
        log: null,
        conditions: {},
        show: false,
        hourly: [],
        daily: [],
    },
    methods: {
        getLocation: function () {
            axios({
                url: "http://www.mapquestapi.com/geocoding/v1/address",
                params: {
                    key: "XrRARpiA1UUYmTV52MRug56U8Qjb5vyA",
                    location: this.locationText
                },
            }).then(response => {
                this.conditions = {}
                this.show = false
                this.location = response.data.results[0].locations[0]
                this.lat = response.data.results[0].locations[0].latLng.lat
                this.log = response.data.results[0].locations[0].latLng.lng
                this.getConditions()
                console.log(this.location)
            })
        },
        getConditions: function () {
            axios({
                url: "https://api.openweathermap.org/data/2.5/onecall",
                params: {
                    lat: this.lat,
                    lon: this.log,
                    appid: "f1fd2255277fef09d38fee6bc2305592",
                    units: "imperial"
                },
                method: "get",
            }).then(response => {
                this.conditions = response.data
            })
        },
    }
})

// Vue.component("hourly-conditions", {
//     template:   `<div>
//                     <p><button type="submit" @click="getHourly">Hourly Conditions</button></p>
//                     <div v-if="description">
//                         <p v-for="(parameter, value) in hourly">{{ parameter }}: {{ value }}</p> 
//                     </div> 
//                 </div>`,
//     data: function () {
//         return {}
//     },
//     props: ["conditions"],
//     methods: {
//         getHourly: function() {
//             this.hourly = this.conditions.hourly 
//             this.hourly.feels_like = this.conditions.hourly.feels_like
//             this.hourly.humidity = this.conditions.hourly.humidity
//             this.hourly.temperature = this.conditions.hourly.temp
//             this.hourly.description = this.conditions.hourly.weather[0].description
//             this.hourly.wind_speed = this.conditions.hourly.wind_speed
//         }
//     },
// })