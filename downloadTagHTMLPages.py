import subprocess
import re
import urllib

f = open('topTags')

for line in f:

    numPages = 1
    urllib.urlretrieve("http://ocremix.org/forums/tags.php?tag=" + line.strip(), "html/" + line.strip() + str(numPages))

    webPage = open("html/" + line.strip() + "1")
    contents = webPage.read()
    regex = re.compile(r'Page \d of \d')
    result = regex.search(contents)

    if result == None:

        continue;

    location = (result.start()) + 10   
    numPages = int(contents[location:location+2].strip(" \t[{(<"))
    for i in range(2, numPages + 1):

        urllib.urlretrieve("http://ocremix.org/forums/tags.php?tag=" + line.strip() + "&page=" + str(numPages), filename="html/" + line.strip() + str(i))
