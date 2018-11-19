from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'

#opening connection, grabbing  page
uClent = uReq(my_url)

#put read html code into the variable
page_html = uClent.read()

#close the client
uClent.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"
f.write(headers)

for container in containers:
	brand = "unavailable"
	mex = container.find("div",{"class":"item-info"})
	try:
  		brand  = mex.a.img["title"]	#brand

	except TypeError:
  		print("Brand: not available")
	#brand  = mex.a.img["title"]	#brand
	productName = "unavailable"
	titleContainer =  mex.findAll("a", {"class":"item-title"})
	productName = titleContainer[0].text.strip() #name of graphic card

	shippingPrice = "unavailable"
	try:
		shippingContainer =  mex.findAll("li", {"class":"price-ship"})
		shippingPrice = shippingContainer[0].text.strip() #shipping price
		
	except:
		print("Shipping Price: not available")
	f.write(brand.replace(","," ") + "," + productName.replace(",","|") + "," + shippingPrice + "\n")
f.close()