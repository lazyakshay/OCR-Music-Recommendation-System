echo "Downloading HTML from ocremix.org forums..."
python downloadTagHTMLPages.py

echo "Getting song-tag map..."
python getSongTagMap.py > tmp/tempTags

echo "Finding similar songs..."
python getSimilarlyTaggedSongs.py tmp/tempTags

rm tmp/tempTags

echo "Done."
