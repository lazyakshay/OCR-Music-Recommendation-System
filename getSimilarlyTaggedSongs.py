import sys

taggedSongsFile = None
songsAndTags = {}

def parseArguments():

    if len(sys.argv) < 2:

        print("USAGE: program <taggedSongsFile>")
        exit(-1)

    taggedSongsFileName = sys.argv[1]

    return open(taggedSongsFileName)

def readData(tagFile):

    for line in tagFile:

        tokens = line.strip().split("\t")

        if tokens[1] not in songsAndTags:
 
            songsAndTags[tokens[1]] = [tokens[0]]

        else:

            if tokens[0] not in songsAndTags[tokens[1]]:

                songsAndTags[tokens[1]].append(tokens[0])

# A class to represent a similar song
class SimilarSong:

    name = ""
    sharedTags = []

    def __str__(self):

        return name + ":" + str(sharedTags)

# Returns a map of song to a list with the songs that share at least *threshold* tags with it 
def getMatchesForSongs(songTagMap, threshold):

    # A map of song name (string) to a list of similar songs ([SimilarSong]) 
    similarSongsMap = {}

    for key in songTagMap:

        similarSongsMap[key] = []
        findMatchesForSong(songTagMap, key, similarSongsMap, threshold)

    return similarSongsMap

def findMatchesForSong(songTagMap, songName, similarSongsMap, threshold):

    for key in songTagMap:

        if key == songName:

            continue # we shouldn't compare to ourself

        sharedTags = set(songTagMap[songName]).intersection(songTagMap[key])
        
        if len(sharedTags) < threshold: # they don't share enough tags, so quit

            continue

        entry = SimilarSong()
        entry.name = key
        entry.sharedTags = sharedTags
        similarSongsMap[songName].append(entry)

def getSize(similarSong):

    return len(similarSong.sharedTags)

def trimAllButTop5(similarSongsMap):

    for key in similarSongsMap:

        sortedEntries = sorted(similarSongsMap[key], key=getSize)
        similarSongsMap[key] = sortedEntries[-1 * min(5, len(sortedEntries)):]
        #print('length was: ' + str(len(similarSongsMap[key])))

def outputFiles(similarSongsMap):

    for key in similarSongsMap:

        newFile = open("songRecommendations/" + key.replace("/", "\\"), "w")
        
        #print("length was: " + str(len(similarSongsMap[key]))) 
        for similarSong in similarSongsMap[key]:

            string = ""
            string += similarSong.name + "\t"

            for sharedTag in similarSong.sharedTags:

                string += sharedTag + ","

            string = string[:-1]
            string += "\n"
            newFile.write(string)

def printSongsAndTags(songMap):

    for key in songMap:

        lineString = key + "\t"
        for tag in songMap[key]:

            lineString += tag + "\t"
        
        print(lineString[:-1])        

def getRecommendations():

    taggedSongsFile = parseArguments()
    readData(taggedSongsFile)
    similarSongsMap = getMatchesForSongs(songsAndTags, 1)
    trimAllButTop5(similarSongsMap)
    outputFiles(similarSongsMap)


getRecommendations()
