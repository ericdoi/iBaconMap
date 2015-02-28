// Expected field names 
var UID_NAME = 'user_id'; 
var DIST_NAME = 'proximity';

//var DATA_SOURCE = "http://iheartbacon.retentionsandbox.com/sites/1/who-wants-my-bacon";
var DATA_SOURCE = "/getdists";
		
var globalData; // Store location data globally.
var uidVisitOrder = {}; // Global. Track the order in which new uids are seen.

// Load the data.
var callback = function (data) {
	//update_data(data); // Update global data
	//update_table('#feed');
};

var update_data = function(data) {
	globalData = data;
	for (var dict in globalData) {
		var thisUser = globalData[dict][UID_NAME];
		if (!(thisUser in uidVisitOrder)) {
			uidVisitOrder[thisUser] = Object.keys(uidVisitOrder).length;
		}
		if (globalData[dict][DIST_NAME] < 0.0) {
			globalData[dict][DIST_NAME] = 0.0; // Just in case
		}
	}
	console.log('Visit mapping:');
	console.log(uidVisitOrder);
	console.log('Color mapping:');
	console.log(colorMap);
}

var update_table = function(reference) {
	$(reference).empty();
	var str = ''
	for (var dict in globalData) {
		str += 'userId: ' + 
			globalData[dict][UID_NAME] + 
			' distance: ' + 
			globalData[dict][DIST_NAME] + '<p>'
		//console.log('Drawing the update on reference ' + reference)
	}
	$(reference).html(str)
}

var update_map = function(reference, data) {

}

//d3.json("/getdists", callback);
d3.json(DATA_SOURCE, callback);

$(document).ready(function() {
	// $("body").css("background-color",rainbow(maxColors,2));
	(function poll() {
		setTimeout(function() {
			$.ajax({
				//url: "/getdists",
				url: DATA_SOURCE,
				type: "GET",
				success: function(data) {
					update_data(data);
					update_table('#feed');
					update_map('#map');
					console.log("Poll")
				},
				dataType: "json",
				crossDomain: true,
				complete: poll,
				timeout: 1000
			}) //, 5000  <-- oops.
		}, 1000); // <-- should be here instead
	})();
	
	/* Add D3 to HTML */
    var svg = d3.select("#map").append("svg")
        .attr("width", width)
        .attr("height", height);

    svg.append("path")
        .datum(graticule)
        .attr("class", "graticule")
        .attr("d", path);

    svg.selectAll("circle")
        .data(beacons)
        .enter()
        .append("circle")
        .attr("class", "dot")
        .attr("transform", translateCircle)
        .attr("r", 8);

    setInterval(function () {

        globalData.forEach(function (datum) {
    		var newColor = colorMap[ uidVisitOrder[datum[UID_NAME]] ];
    		var newRad = Number(datum[DIST_NAME]*SCALE);
            console.log("color: ", newColor);
            console.log("radius: ", newRad );
    		console.log("globalData?", globalData);
    		console.log("uid?", datum[UID_NAME]);
    		console.log(uidVisitOrder);
    		console.log("colorMap?", colorMap);

            svg.append("circle")
                .attr("class", "ring")
                .attr("transform", translateCircle(beacon)) // Translate by one beacon, decoupled from globalData
                .attr("r", newRad)
                .style("stroke-width", 3)
                .style("stroke", newColor)
                .transition()
                .ease("linear")
                .duration(2000)
                .style("stroke-opacity", 1e-6)
                .style("stroke-width", 1)
                .style("stroke", newColor)
                .attr("r", newRad )
                .remove();
        })
    }, interval)

    d3.select(self.frameElement).style("height", height + "px");
});

