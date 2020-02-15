#!/usr/bin/python
import csv
import geoip2.webservice
import socket

ID=121017
license_key='PM0t8JSl7Urg'
client = geoip2.webservice.Client(ID, license_key)

f= open("map.html","w+")

map1='''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no">
<meta charset="utf-8">
<title>Circles</title>
<style>
#map {
height: 100%;
}
html, body {
height: 100%;
margin: 0;
padding: 0;
}
</style>
</head>
<body>
<div id="map"></div>
<script>

var citymap = {'''

f.write(map1)

with open('top500.cvs', 'rb') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    i=1
    for row in rows:
        hostname1=str(row[1])
        print hostname1

        try:
            response=client.city(socket.gethostbyname(hostname1))
            lat=str(response.location.latitude)
            longi=str(response.location.longitude)

            f.write('website'+str(i)+': { center: {lat:'+lat+', lng: '+longi+ '}, population:'+row[5]+'},'+'\n')
            i=i+1
        except Exception:
            pass


map2='''};
function initMap() {
var map = new google.maps.Map(document.getElementById('map'), {
zoom: 3,
center: {lat: 20.945099 , lng: 7.413900},
mapTypeId: "terrain"
});

for (var city in citymap) {
var cityCircle = new google.maps.Circle({
strokeColor: "#FF0000",
strokeOpacity: 0.8,
strokeWeight: 0,
fillColor: "#FF0000",
fillOpacity: 0.15,
map: map,
center: citymap[city].center,
radius: Math.sqrt(citymap[city].population-7.22) * 500000
});
}
}
</script>
<script async defer
src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD8O_AHvbfS0TsYL8v7WCjteWQ572dTgBc&callback=initMap">
</script>
</body>
</html>'''
f.write(map2)
