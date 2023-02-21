
/* 
Week 2 --- World Data Visualisation in p5.js

Task 1 - Load your image into a variable from mapbox

Task 2 - Add a circle on your map at chosen co-ordinates. For example 
// Shanghai : 31.2304 N, 121.4737 E
// Cape Town: 33.9249° S, 18.4241° E
// Havana: 23.1136° N, 82.3666° W

Task 3 - Load the data from the CSV file into p5.js

Task 4 - Use the data to show the location of the earthquakes

Task 5 [Extension] - Update circle size depending on magnitude.   

*/

let mapImg;
let earthquakes;

// Havana: 23.1136° N, 82.3666° W
// Cape Town: 33.9249° S, 18.4241° E
// south & west r neg, north and east r pos
let clat = 0;
let clon = 0;

let lat = 23.1136;
let lon = -82.3666;

// Create the preload function here for loading the image.
function preload() {
  mapImg = loadImage('https://api.mapbox.com/styles/v1/mapbox/dark-v9/static/0,0,1,0/1024x512?access_token=pk.eyJ1IjoibWNjLW9saSIsImEiOiJjbGVlNTl2OHkwZGt5M29wMmd4azVqZ3FhIn0.1EVwO9Y0Thm01MnxgVA4yw');
  
  earthquakes = loadStrings('assets/all_month.csv')
}

function setup() {
  createCanvas(1024, 512);
  
  translate(width/2, height/2);
  imageMode(CENTER);
  image(mapImg, 0, 0);

  let cx = mercX(clon);
  let cy = mercY(clat);

  for (let i = 1; i < earthquakes.length; i++) {
    var data = earthquakes[i].split(/,/);
    lat = data[1];
    lon = data[2];
    
    let x = mercX(lon);
    let y = mercY(lat);

    let mag = data[4];
    
    noStroke();
    fill(200, 50, 0, 50);
    ellipse(x-cx, y-cy, mag*3.5, mag*3.5);
  }  
}

// This function is used to convert longitude co-ordinates from a spherical globe to a "web-mercator" style map
function mercX(lon) {
  let zoom = 1;
  lon = radians(lon);
  let a = (256/PI)*pow(2, zoom);
  let b = lon+PI;
  return a*b;

}

// This function is used to convert latitude co-ordinates from a spherical globe to a "web-mercator" style map
function mercY(lat) {
  let zoom = 1;
  lat = radians(lat);
  let a = (256/PI)*pow(2, zoom);
  let b = tan(PI/4 + lat/2);
  let c = PI - log(b);
  return a*c; 
}


// We will not be using the draw function for this task, but you might want to use it later
// function draw() {
// }
