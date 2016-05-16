#How the code works
Baldomero Vargas
bvarg006@ucr.edu
SID = 861143461

The following code runs as follows

1) function to run the brute force method. This just does a simple for loop
nested in another and returns the shortest distance in a select sort like
algorithm.

2)Divide and Conquer function runs by seperating the list into a left and
right list. Recursivly we find the shortest distance in those subsets and just
use that distance to get a range in the middle. With the middle we compare at
most 7 points because we sort the list in order to just check the nearest 7
points. We check only 7 because we jsut check the surrounding values, so this
allows us to do this shortest distance check in linear time.

Aside from this we use a basic output and distance formula funtion
