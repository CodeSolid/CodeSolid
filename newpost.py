# Note -- python3 only!

from subprocess import call

import sys
import time
import os.path

required_keys = ["Title", "Author", "Date", "Slug"]


settings = {"Author":  "John Lockwood"}

def sluggify(title):
	return title.lower().replace(" ", "_")

def getmeta(settings):
	required_keys = ["Title", "Author", "Date", "Slug"]
	meta = ""
	for key in required_keys:
		meta += key + ": " + settings[key] + "\n"
	optional_tags = ["Excerpt", "Summary", "Category", "Tags"]
	for tag in optional_tags:
		meta += tag + ": \n"
	return meta

def get_filename(slug):
	return "content/" + slug + ".md"

sys.stdout.write("Enter a title for your post: ")
sys.stdout.flush()
settings["Title"] = input()
settings["Slug"] = sluggify(settings["Title"])
settings["Date"] = time.strftime("%Y-%m-%d %H:%M")

filename = get_filename(settings["Slug"])

if (os.path.exists(filename)):
	print("Pick a new title.  File '" + filename + "' exists!")	
	sys.exit(-1)

with open(filename, "w") as article:
	article.write(getmeta(settings))
	article.write("\n\n")

call(["subl", filename])
