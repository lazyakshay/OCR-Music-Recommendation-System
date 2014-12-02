import re
import os

allFileNames = os.listdir("html/")

for fileName in allFileNames:

    f = open("html/" + fileName)

    contents = f.read()

    p = re.compile(r"OCR\d\d\d\d.*'.*'")
    titlesRE = re.compile(r"'.*'")

    results = p.findall(contents)

    for thing in results:

        titles = titlesRE.findall(thing)
        tagName = fileName.rstrip("0987654321")

        print(tagName + "\t" + titles[0].strip('\'').replace("&quot;", "\"").replace("&amp;", "&"))

