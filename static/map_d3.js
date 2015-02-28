//var data = [{x:-8,y:100},{x:-10,y:110},{x: -12,y:120}];
 // Test Data
var beacon = {x: 0, y: 0};
	// Only one beacon allowed for now since translation loops on global data rather than beacons. 
var beacons = [beacon]; 

/*
var data = [{
    userId: 1,
    distance: 215
}, {
    userId: 2,
    distance: 75
}, {
    userId: 3,
    distance: 192
}];*/

var MAX_COLORS = 5; // Should make this fail better.

/*var colorMap = {
    1:"#0000FF",
    2:"#00FF00",
    3:"#9900CC"
}*/

function generateColorMap(numColors) {
	map = {};
	for (i = 0; i < numColors; i++) { 
	    map[i] = rainbow(numColors, i);
	}
	return map;
};

var SCALE = 15; // # pixels per unit radius.
var colorMap = generateColorMap(MAX_COLORS);

var interval = 750;

var width = 960,
    height = 500;

var projection = d3.geo.mercator()
    .center([0, 0])
    .scale(1275)
    .translate([width / 2, height / 2])
    .clipExtent([
    [0, 0],
    [width, height]
])
    .precision(.1);

var path = d3.geo.path()
    .projection(projection);

var graticule = d3.geo.graticule()
    .step([5, 5]);
    

function translateCircle(beacon, index) {
	console.log("translate(" + projection([beacon.x, beacon.y]) + ")");
	return "translate(" + projection([beacon.x, beacon.y]) + ")";
	console.log('Beacon:' + beacon);
	//console.log("translate(" + projection([originX, originY]) + ")");
	//return "translate(" + projection([originX, originY]) + ")";

};