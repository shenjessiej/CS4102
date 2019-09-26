# CS4102 Fall 2019 -- Homework 2
#################################
# Collaboration Policy: You are encouraged to collaborate with up to 4 other
# students, but all work submitted must be your own independently written
# solution. List the computing ids of all of your collaborators in the comment
# at the top of your java or python file. Do not seek published or online
# solutions for any assignments. If you use any published or online resources
# (which may not include solutions) when completing this assignment, be sure to
# cite them. Do not submit a solution that you are unable to explain orally to a
# member of the course staff.
#################################
# Your Computing ID: js9fr
# Collaborators:
# Sources: Introduction to Algorithms, Cormen, https://www.geeksforgeeks.org/merge-sort/, https://www.geeksforgeeks.org/reading-writing-text-files-python/
#################################
import math


class ClosestPair:
    def __init__(self):
        return

    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    # This is the method that should set off the computation
    # of closest pair.  It takes as input a list lines of input
    # as strings.  You should parse that input and then call a
    # subroutine that you write to compute the closest pair distance
    # and return that value from this method
    #
    # @return the distance between the closest pair
    def compute(self, file_data):

        points = []

        for line in file_data:
            temptuple = line.split();
            points.append(temptuple)

        fpoints = []
        for item in points:
            fpoints.append([float(item[0]), float(item[1])])

        # sort points according to x coordinate
        # python sort method

        # print fpoints
        fpoints.sort(key=getX)

        if(len(fpoints) == 2):
            return distance(fpoints[0][0], fpoints[0][1], fpoints[1][0], fpoints[1][1])
        # Split the set of points into two equal-sized subsets
        # by a vertical line x=xmid.
        ## find middle by dividing array by len() in half
        ## make two new lists

        middleIndex = len(fpoints) // 2


        left = fpoints[:middleIndex]
        right = fpoints[middleIndex:]

        # Solve the problem recursively in the left and right subsets.
        # This yields the left-side and right-side minimum distances
        # dLmin and dRmin, respectively.

        dLmin, leftArray = computeHelper(left)
        dRmin, rightArray = computeHelper(right)

        # merge leftArray and rightArray
        leftLength = len(leftArray)
        rightLength = len(rightArray)

        i = 0
        j = 0
        mergedArray = []

        while(i < leftLength & j < rightLength):
            if(getY(leftArray[i]) <= getY(rightArray[j])):
                mergedArray.append(leftArray[i])
                i = i + 1
            else:
                mergedArray.append(rightArray[j])
                j = j + 1

        while(i < leftLength):
            mergedArray.append(leftArray[i])
            i = i+1

        while(j < rightLength):
            mergedArray.append(rightArray[j])
            j = j + 1

        mergedArray.sort(key=getY)
        # print mergedArray

        # find the runway points and save into array

        ans = dLmin
        if(dRmin < ans):
            ans = dRmin

        runway = []

        delta = fpoints[middleIndex]
        for x in mergedArray:
            if((x[0] - delta[0] <= ans) & (x[0] - delta[0] >= 0)) | ((delta[0] - x[0] <= ans) & (delta[0] - x[0] >= 0)):
                runway.append(x)
        # print mergedArray
        # print delta[0]
        # print ans
        # print runway

        # compare each point in runway to at most 15 points above it and save the closest distance

        i = 1
        runwayLen = len(runway)
        dLRmin = float('inf')

        for point in runway:
            while(i < (runwayLen) | i <= 15):
                compPoint = runway[i]
                temp = distance(point[0], point[1], compPoint[0], compPoint[1])
                # print compPoint
                # print point
                # print temp
                if temp < dLRmin:
                    dLRmin = temp
                i = i+1

        # The final answer is the minimum among dLmin, dRmin, and dLRmin.

        if(dLRmin < ans):
            ans = dLRmin

        return ans

def getX(elem):
    return elem[0]

def getY(elem):
    return elem[1]

def distance(pt1_x, pt1_y, pt2_x, pt2_y):
    x_dist = pt2_x - pt1_x
    y_dist = pt2_y - pt1_y
    return math.sqrt(math.pow(x_dist,2) + math.pow(y_dist,2))

def computeHelper(arr):

    # base case
    if(len(arr) == 3):
        fpoint = arr[0]
        spoint = arr[1]
        tpoint = arr[2]
        distfs = distance(fpoint[0], fpoint[1], spoint[0], spoint[1])
        distft = distance(fpoint[0], fpoint[1], tpoint[0], tpoint[1])
        distst = distance(spoint[0], spoint[1], tpoint[0], tpoint[1])
        min = distfs
        if(distft < min):
            min = distft
        if(distst < min):
            min = distst
        return min, arr

    if(len(arr) == 2):
        return distance(arr[0][0], arr[0][1], arr[1][0], arr[1][1]), arr

    if(len(arr) == 1):
        return float('inf'), arr


    # recursive call
    middleIndex = len(arr) // 2

    left = arr[:middleIndex]
    right = arr[middleIndex:]
    leftdistance, leftArray = computeHelper(left)
    rightdistance, rightArray = computeHelper(right)

    # re merge, sorting by y
    newarray = []
    leftLength = len(leftArray)
    rightLength = len(rightArray)

    i = 0
    j = 0

    while (i < leftLength & j < rightLength):
        if (getY(leftArray[i]) <= getY(rightArray[j])):
            newarray.append(leftArray[i])
            i = i + 1
        else:
            newarray.append(rightArray[j])
            j = j + 1

    while (i < leftLength):
        newarray.append(leftArray[i])
        i = i + 1

    while (j < rightLength):
        newarray.append(rightArray[j])
        j = j + 1

    #return distance, array

    min = leftdistance
    if(rightdistance < min):
        min = rightdistance
    return min, newarray

