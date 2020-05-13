from bs4 import BeautifulSoup

# Method for retrieving the DIY recipes from recipes.html
# Returns: ResultSet
def get_diy_list():
	html = open('recipes.html','r',encoding="utf-8")
	soup = BeautifulSoup(html,'html.parser')
	diy = soup.find_all("tr", class_="table-tr-data-rb")
	return diy

# Method for retrieving name of recipe in row
# Params:
	# - Tag row
# Returns: recipe name as str
def get_name(row):
	children = row.contents
	return children[0].div.text

# Method for retrieving the name, sell price, type, materials, and source of recipe
# Params:
	# - Tag row
# Returns: information as str
def get_all(row):
	children = row.contents
	reply = []
	# === basic info ===
	info = children[0].contents
	# name 0
	reply.append(info[0].text)
	#price 1
	reply.append(info[6].strip())
	#type 2
	reply.append(info[7].text)
	
	# === materials === 3
	mats = []
	materials = children[1].contents
	for i in materials:
		mats.append("\t• "+i.text.strip())
	reply.append("\n".join(mats))

	# === source === 4
	reply.append(children[2].text)
	
	return reply

# Method for retrieving url of recipe image
# Params:
	# - Tag row
# Returns: url as str
def get_img_url(row):
	children = row.contents
	img = children[0].contents
	return img[1].get("data-lazy-src").replace(' ','%20') # bandaid