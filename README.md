UTEK_2017, Awarded 2nd place out of 30 teams in 2017 Programming competition. Worked in a team of 4.
========
### Overview
Given 6 hours to create an algorithm that would output an optimized route for electric cars. This meant the route with the least distance, required the least amount of time on the road, as well as the route that would minimize the amount of charging stations that a car would need to stop at to recharge.

### The following is a brief summary of the project
#### Part I
*Task: Obtain information of all the electric vehicle charging stations and return the 3 closest stations relative to the location of the car.

*Accomplished in linear time by keeping track of the minimum distance stations and updating those when a lower distance station was found.

#### Part II
*Task: Given a start and end coordinate, return the distance and time to get from start to end.

*Used GoogleMaps API to accomplish this

#### Part III
*Implemented a cache to provide constant look up time for previously inputted coordinates as well as reduce the API calls in part II.

#### Part IV
*Task: Given a start and end coordinate, find the optimal route between the two given:
*A) The vehicle can only travel 480km before recharging
*B) The list of recharging stations we found in Part I

*Implemented a greedy algorithm that chose the next station to go to based on how close it was to the destination (minimizing the the distance from the station to the destination each time).
*Used the Haversine formula to approximate which stations would minize the distance between the car and the destination before making the API call.

#### **Part V**
*Produced a web application that takes user input and displays the results of part IV in an intuitive UI (along with an interactive map using Google Maps API) using pure HTML, CSS, and Flask.
