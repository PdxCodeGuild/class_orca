Vue.component("current-conditions", {
    template:   `
    <div id="current-conditions">
        <p><button type="submit" @click="getCurrent(); showCurrent = !showCurrent">Current Conditions</button></p>
        <div v-if="showCurrent">
            <p v-for="value in current">{{ value }}</p> 
        </div>                
    </div>
    `,
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
    props: ["conditions", "showCurrent"],
    methods: {
        getCurrent: function () {
            this.current.temperature = `Current temperature: ${this.conditions.current.temp}F.`
            this.current.feels_like = `Feels like: ${this.conditions.current.feels_like}F.`
            this.current.humidity = `Relative humidity: ${this.conditions.current.humidity}%.`
            this.current.wind_speed = `Wind speed: ${this.conditions.current.wind_speed}mph.`
        }
    },
})
Vue.component("hourly-conditions", {
    template: `
    <div id="hourly-conditions">
        <p><button type="submit" @click="getHourly(); showHourly = !showHourly">Hourly Forecast</button></p>
        <div id="hour-box" v-if="showHourly">
            <div id="hour" v-for="hour in hourly" :key=hour.index>
                <p v-for="value in hour">{{ value }}</p>
            </div> 
        </div>
    </div>
    `,
    data: function () {
        return {
            hourly: [],
            hour: {
                // hourX: null,
                temperature: null,
                description: null,
                rain: null,
            },
        }
    },
    props: ["conditions", "showHourly"],
    methods: {
        getHourly: function () {
            this.hourly = []
            for (hour in this.conditions.hourly) {
                this.hour = {}
                this.hour.temperature = `Temperature: ${this.conditions.hourly[hour].temp}F.`
                this.hour.description = `Sky conditions: ${this.conditions.hourly[hour].weather[0].description}.`
                this.hour.rain = `Chance of rain: ${this.conditions.hourly[hour].pop}%.`
                this.hourly.push(this.hour)
            }
        }
    }
})
Vue.component("daily-conditions", {
    template: ` 
    <div id="daily-conditions">
        <p><button type="submit" @click="getDaily(); showDaily = !showDaily">Daily Forecast</button></p>
        <div v-if="showDaily">
            <div v-for="day in daily" :key=day.index>
                <p v-for="value in day">{{ value }}</p>
            </div> 
        </div>
    </div>
    `,
    data: function () {
        return {
            daily: [],
            day: {
                sunrise: null,
                sunset: null,
                max_temperature: null,
                min_temperature: null,
                description: null,
                rain: null,
            },
        }
    },
    props: ["conditions", "showDaily"],
    methods: {
        getDaily: function () {
            this.daily = []
            for (day in this.conditions.daily) {
                this.day = {}
                this.day.sunrise = `Sunrise: ${this.conditions.daily[day].sunrise}AM.`
                this.day.sunset = `Sunset: ${this.conditions.daily[day].sunset}PM.`
                this.day.max_temperature = `Temperature high: ${this.conditions.daily[day].temp.max}F.`
                this.day.min_temperature = `Temperature low: ${this.conditions.daily[day].temp.min}F.`
                this.day.description = `Sky conditions: ${this.conditions.daily[day].weather[0].description}.`
                this.day.rain = `Chance of rain: ${this.conditions.daily[day].pop}%.`
                this.daily.push(this.day)
            }
            // console.log(this.conditions.daily, this.daily)
        }
    }
})              
Vue.component("weather-app", {
    template:  `
    <div id="weather-app">
        <div id="location-input">
            <h3>Weather</h3>
            <input v-model="locationText" @keydown.enter="getLocation" type="text" placeholder=" Enter location" style="width: 250px">
            <button @click="getLocation" type="submit">Search</button>
        </div>
        <div id="weather-summary" v-if="conditions.current">
            <p>{{ location.adminArea5 }} {{ location.adminArea3 }}</p> 
            <p>{{ conditions.current.temp }}F with {{conditions.current.weather[0].description}}.</p>            
        </div>
        <div id="available-conditions" v-if="conditions.current">
            <current-conditions :conditions="conditions"></current-conditions> 
            <hourly-conditions :conditions="conditions"></hourly-conditions> 
            <daily-conditions :conditions="conditions"></daily-conditions> 
        </div>
    </div>
    `,
    data: function () {
        return {
        locationText: "",
        location: {},
        location_history: {},
        lat: null,
        log: null,
        conditions: {},
        hourly: [],
        daily: [],
        }
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
                this.location = response.data.results[0].locations[0]
                this.lat = response.data.results[0].locations[0].latLng.lat
                this.log = response.data.results[0].locations[0].latLng.lng
                this.getConditions()
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