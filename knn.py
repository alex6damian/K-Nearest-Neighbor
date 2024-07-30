import math
import knnParser
def euclidian_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def classifyPoint(points, p, k=3):
    '''
    Finds the class of a point p, given a list of points and k
    points is a dictionary like this: {type:(x,y), ..}
    p is our point to classify with coordinates (x,y)
    k is the number of nearest neighbour, default is 3
    '''

    distance=[]

    for type in points: # for each type of point
        for point in points[type]: # each point in the type
            distance.append((euclidian_distance(point,p), type)) # save the distances
            if p == point:
                return type

    distance=sorted(distance)[:k] # save the first k sorted shortest distances

    freq=[0]*len(points) # we will use 2 types

    for d in distance: # for each distance
        for i in range(len(points)): # for each type
            if int(d[1])==int(i): # if the type of the distance is the same as the type we are looking at
                freq[i]+=1 # increase the frequency of that type

    return freq.index(max(freq)) # return the type with the highest frequency

def main():
    # our training points dictionary
    points = knnParser.parseTraining('trainingSet')

    # testing point
    p = (3,3)

    # number of neighbours
    k=3
    print(f'The point {p} is classified as type {classifyPoint(points, p, 3)}')

if __name__ == "__main__":
    main()