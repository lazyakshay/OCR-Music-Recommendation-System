import sys
import os
import operator

songsAndTags = {}

def parseArguments():

    if len(sys.argv) < 2:

        print("USAGE: program <recommendation directory>")
        exit(-1)

    return sys.argv[1]

# returns a map of songs to lists of SimilarSong objects
def readData(recommendationDirectory):

    files = os.listdir(recommendationDirectory)
    allSongs = {}

    for file in files:

        recommendationFile = open(recommendationDirectory + "/" + file)

        for line in recommendationFile:

            tokens = line.split("\t")
            allSongs[tokens[0]] = tokens[1]

    return allSongs

def outputData(top5RecommendationMap):

    for key in top5RecommendationMap:

        newFile = open("top5Recommendations/" + key, "w")
        string = top5RecommendationMap[key]
        newFile.write(string)

def getRecommendations():

    recommendationDirectory = parseArguments()
    sortedRecommendationList = readData(recommendationDirectory)
    outputData(sortedRecommendationList)

getRecommendations()
