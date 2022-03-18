var n = Int(readLine()!)!
var hike = readLine()!
var numValleys = 0
var altitude = 0

for char in hike.characters {
    if(char == "U") {
        if(altitude == -1) {
            numValleys += 1;
        }
        altitude += 1;
    }
    // Step down
    else {
        altitude -= 1;
    }
}

print(numValleys)