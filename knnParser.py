def parseTraining(file):

    points = {} # dictionary to save the points

    type = 'none' # type of the point

    with open('trainingSet', 'r') as file:

        for lines in file:

            if 'type' in lines: # if the line contains the word type
                type = lines.split()[1] # save the type
                points[type] = [] # create a list for the type

            else:
                x, y = map(float, lines.split()) # save the coordinates
                points[type].append((x,y)) # save the point

    return points # gives us the points dictoinary