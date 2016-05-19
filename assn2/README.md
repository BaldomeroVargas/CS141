#CS141 Assignment 2

How it runs: 

1) Begin with reading the contents of the file and storing it in a 2D array of Decimals/Floats. 
2) Use a nested loop to itterate through the 2d array of decimals/float and perform the seam calculation algorithm. The previously defined point class used inthe first assignment is used to store for each pixel the x = energy value, y = lowest seam. The algorithm is as follows 2darray[i][j].y =2adarray[i][j].x + min(2darray[i-1][j-1].y + 2darray[i-1][j].y,grid[i-1][j+1].y) with bound checking on the left most and rightmost columns as well as the top row. So as this algorithm goes it stores the seam values in the (y) component of each pixel or cell in the 2darray. 
3)Once the algorithm is finished we check the bottom row for the minimum y value, this represents our minimum seam and we send that to the output file.
4) After we now know the current row and column of the minimum seam and we use this as our starting point and REVERSE the above algorithm except this time we compare the (y) values above the cell like the algorithm and return the (x) value of the smallest (y) value returned. (aka return the energy level of the smallest seam returned in the trace back algorithm)
5) As we trace back variables are used the store the energy value to send to the file, the row and column positions. 

