// const url = `https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=${apiKey}`;

// requestFile( url );


// function requestFile( url ) {

//     const xhr = new XMLHttpRequest();
//     xhr.open( 'GET', url, true );
//     xhr.onerror = function( xhr ) { console.log( 'error:', xhr  ); };
//     xhr.onprogress = function( xhr ) { console.log( 'bytes loaded:', xhr.loaded  ); };
//     xhr.onload = callback;
//     xhr.send( null );

//     function callback( xhr ) {

//         let response, json, lines;

//         response = xhr.target.response;
//         app.innerText = response;

//         json = JSON.parse( response );



//     }

// }


let vm = new Vue({
    el: '#app',
    data {
        stock: [],
        return {
            info: null,
            loading: true,
            errored: false,
        }
    },
    methods: {
        searchStocks: function () {
            axios({
                url: `https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey=${apiKey}`,
                method: "get",
                params: {
                    filter: this.search
                }
                }). then(response => {
                    this.stocks = 
                }) 
        }

    }
        
            
    
})