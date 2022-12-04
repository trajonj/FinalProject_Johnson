var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

const axios = require('axios');

app.use(bodyParser.urlencoded());

app.set('view engine', 'ejs');



//login api
app.get('/', function(req, res) {
    res.render("pages/login.ejs", {});
});

app.post('/process_login', function(req, res)
{
    var username = req.body.username;
    var password = req.body.password;

        axios.get('http://127.0.0.1:5000/api/login', {
        masterUsername: username,
        masterPassword: password
    });
})



//Flights CRD apis
app.get('/flights', function(req, res) {

    axios.get(`http://127.0.0.1:5000/api/flight/all`)
    .then((response)=>{
        
        var flights = response.data;
        var tagline = "Current Flights";
        console.log(flights);
        res.render('pages/flights', {
            flights: flights,
            tagline: tagline
        });
    });
});

app.post('/add_flight', function(req, res){
    
    axios.post('http://127.0.0.1:5000/api/flight/', {
        var dateinput = req.body.dateinput;
        var airportfromidinput = req.body.airportfromidinput;
        var airporttoidinput = req.body.airportfromidinput;
        var planeidinput = req.body.planeidinput;
        var message = "Your entry has been recorded."

        res.render('pages/flights', {
            date: dateinput,
            airportfromid: airportfromidinput,
            airporttoid: airporttoidinput,
            planeid: planeidinput,
            message: message
        
        });
    });
    
});

app.delete('/delete_flight', function(req, res){
    
    axios.delete('http://127.0.0.1:5000/api/flight/', {
        var flightiddelete = req.body.flightiddelete;
        var message = "Your entry has been recorded."

        res.render('pages/flights', {
            idtodelete: flightiddelete,
            message: message
        
        });
    });
    
});


//Airports CRUD apis
app.get('/airports', function(req, res) {

    axios.get(`http://127.0.0.1:5000/api/airports/all`)
    .then((response)=>{
        
        var airports = response.data;
        var tagline = "Current Airports";
        console.log(airports);
        res.render('pages/airports', {
            airports: airports,
            tagline: tagline
        });
    });
});

app.post('/add_airport', function(req, res){
    
    axios.post('http://127.0.0.1:5000/api/airports/', {
        var airportidinput = req.body.airportidinput;
        var airportcodeinput = req.body.airportcodeinput;
        var airportnameinput = req.body.airportnameinput;
        var airportcountryinput = req.body.airportcountryinput;
        var message = "Your entry has been recorded."

        res.render('pages/flights', {
            airportid: airportidinput,
            airportcode: airportcodeinput,
            name: airportnameinput,
            country: airportcountryinput,
            message:message
        
        });
    });
    
});

app.put('/update_airport', function(req, res){
    
    axios.put('http://127.0.0.1:5000/api/airports/', {
        var airportidupdate = req.body.airportidupdate;
        var airportcodeupdate = req.body.airportcodeupdate;
        var airportnameupdate = req.body.airportnameupdate;
        var airportcountryupdate = req.body.airportcountryupdate;
        var message = "Your entry has been recorded."

        res.render('pages/flights', {
            id: airportidupdate,
            airportcode: airportcodeupdate,
            airportname: airportnameupdate,
            country: airportcountryupdate,
            message:message
        
        });
    });
    
});

app.delete('/delete_airport', function(req, res){
    
    axios.delete('http://127.0.0.1:5000/api/airports/', {
        var airportiddelete = req.body.airportiddelete;
        var message = "Your entry has been recorded."

        res.render('pages/flights', {
            idtodelete: airportiddelete,
            message: message
        
        });
    });
    
});


//Planes CRUD apis
app.get('/planes', function(req, res) {

    axios.get(`http://127.0.0.1:5000/api/planes/all`)
    .then((response)=>{
        
        var planes = response.data;
        var tagline = "Current Planes";
        console.log(planes);
        res.render('pages/planes', {
            planes: planes,
            tagline: tagline
        });
    });
});

app.post('/add_plane', function(req, res){
    
    axios.post('http://127.0.0.1:5000/api/planes/', {
        var planeidinput = req.body.planeidinput;
        var yearinput = req.body.yearinput;
        var capacityinput = req.body.capacityinput;
        var makeinput = req.body.makeinput;
        var modelinput = req.body.modelinput;
        var message = "Your entry has been recorded."

        res.render('pages/flights', {
            planeid: planeidinput,
            ayear: yearinput,
            capacity: capacityinput,
            make: makeinput,
            model: modelinput
            message:message
        
        });
    });
    
});

app.put('/update_plane', function(req, res){
    
    axios.put('http://127.0.0.1:5000/api/planes/', {
        var planeidupdate = req.body.planeidupdate;
        var yearinput = req.body.yearinput;
        var planecapacityupdate = req.body.planecapacityupdate;
        var planemakeupdate = req.body.planemakeupdate;
        var planemodelupdate = req.body.planemodelupdate;
        var message = "Your entry has been recorded."

        res.render('pages/flights', {
            planeid: planeidupdate,
            ayear: yearinput,
            capacity: planecapacityupdate,
            make: planemakeupdate,
            model: modelinput
            message:message
        
        });
    });
    
});

app.delete('/delete_plane', function(req, res){
    
    axios.delete('http://127.0.0.1:5000/api/planes/', {
        var planeiddelete = req.body.planeiddelete;
        var message = "Your entry has been recorded."

        res.render('pages/flights', {
            idtodelete: planeiddelete,
            message:message
        
        });
    });
    
});


app.listen(8084);
console.log('8084 is the magic port!');

