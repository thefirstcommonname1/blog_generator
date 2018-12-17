# blog_creator
"""
	- Have a .bk file, and the file creates posts based on what ever is underneath that
	- program reads the .bk file then creates html using it
	- s.code - everything from this till e.code is indented styled into a code like block
	- in order to do that I guess there should be a css file that defines all the styles the html files will have
	- the file should always have a file usually index.html that contains the urls to all the posts
	
	- Updates automatically and creates a new file index.html that collects all other .html files
		generated from the blog_creator
	
	List of commands:
	- new_post creates a file .post.bk extension
	- Later add something like new_blog which creates a directory, this should be implemented when converting this to
	 	a command line tool
"""
import sys
import os

index_template = """
<html>
	<head>
		<link rel="stylesheet" href="styles.css"/>
	</head>
	<body>
		<h1>My blog</h1>
	</body>
</html>
"""

# only create index.html if it doesn't already exist
if not os.path.isfile("index.html"):
	with open("index.html", "w+") as file:
		file.write(index_template[1:])

def parse_and_create_files():
	files = os.listdir(os.getcwd())
	for f in files:
		if ".post.bk" in f:
			name = create_file(f) # would usually just write the code here, but pythons indentation is a pain in the ass
			append_file(name, index_template)

# what a lonely variable
command = sys.argv[1]

def create_file(file_name):
	name = file_name[:file_name.find(".post.bk")]
	with open(file_name, "r+") as file:
		with open(name + ".html", "w+") as html_file: # later have seperate calls based on command gen_all or gen file_name
			bk_text = file.read()
			bk_text = bk_text.replace("s.heading", "<h1>")
			bk_text = bk_text.replace("e.heading", "</h1>")
			bk_text = bk_text.replace("s.text", "<p>")
			bk_text = bk_text.replace("e.text", "</p>")
			html_file.write("<head><link rel=\"stylesheet\" href=\"styles.css\"></head>")
			html_file.write("<body>\n\t")
			html_file.write(bk_text)
			html_file.write("</body>")
	return name

def append_file(name, index_template):
	index = index_template.find("</h1>") + len("</h1>")
	file_to_write = index_template[:index] + "\n<a href={}.html>{}</a>\n".format(name, name[0].upper() + name[1:]) + index_template[index:]
	with open("index.html", "w+") as file:
		file.write(file_to_write[1:])

# used to generate a new .post.bk
if command == "new_post":
	file_name = sys.argv[2]
	with open(file_name.lower() + ".post.bk", "w") as file:
		file.write("s.heading " + file_name + " e.heading\n")

if command == "generate" or command == "gen":
	parse_and_create_files()


