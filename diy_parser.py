from bs4 import BeautifulSoup
import re

# Method for retrieving the tools from the AC Wiki
# Returns: list of lists
def get_diy(filename,table_class,type):
	html = open(filename,'r',encoding="utf-8")
	bs = BeautifulSoup(html,'html.parser')
	table = bs.find("table",  {"class" :table_class})
	tr = table.find_all("tr")
	tools = []
	for row in tr :
		tool = []
		cols = row.find_all("td")
		if( len(cols) > 0 ):
			# 0 name
			tool.append(re.sub('x[0-9]+','',cols[0].text).strip())
			# 1 img
			img_link = cols[1].find('a')
			if( img_link != None ):
				tool.append(img_link['href'].replace(' ','%20'))
			else:
				tool.append('')
			# 2 materials
			tool.append(['• '+s.group() for s in re.finditer('(x[0-9]+[ A-Za-z]+[^x0-9])|([0-9]+x[ A-Za-z]+)',cols[2].text.strip())])
			# 3 size
			size_link = cols[3].find('a')
			if( size_link != None ):
				tool.append(size_link['href'].replace(' ','%20'))
			else:
				tool.append('')
			# 4 src
			tool.append(cols[4].text.strip())
			# 5 sell
			tool.append(cols[5].text.strip())
			# 6 tools
			tool.append(type)
			tools.append(tool)
	return tools


def get_diy_masterlist():
	diy_master = []
	diy_master.extend(get_diy('html/recipes/tools.html','sortable','Tool'))
	diy_master.extend(get_diy('html/recipes/housewares.html','sortable','Houseware'))
	diy_master.extend(get_diy('html/recipes/equipment.html','sortable','Equipment'))
	diy_master.extend(get_diy('html/recipes/misc.html','sortable','Miscellaneous'))
	diy_master.extend(get_diy('html/recipes/wall.html','sortable','Wall Mounted'))
	diy_master.extend(get_diy('html/recipes/rug-wall-floor.html','sortable','Wallpaper, Rug, Flooring'))
	diy_master.extend(get_diy('html/recipes/other.html','sortable','Other'))
	return diy_master