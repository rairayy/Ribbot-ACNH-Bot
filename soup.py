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
	# name
	reply.append("**Item Name: "+info[0].text+"**")
	#price
	reply.append("Sell Price: "+info[6].strip())
	#type
	reply.append("Item Type: "+info[7].text)
	
	# === materials ===
	reply.append("Materials Needed:")
	materials = children[1].contents
	for i in materials:
		reply.append("\t• "+i.text.strip())
	
	# === source ===
	reply.append("Source: "+children[2].text)
	
	return "\n".join(reply)

# Method for retrieving url of recipe image
# Params:
	# - Tag row
# Returns: url as str
def get_img_url(row):
	children = row.contents
	img = children[0].contents
	return img[1].get("data-lazy-src").replace(' ','%20') # bandaid