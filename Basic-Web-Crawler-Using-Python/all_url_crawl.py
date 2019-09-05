
from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as urlReq  


page_url = "https://dmoz-odp.org/"


urlClient = urlReq(page_url)

page_soup = soup(urlClient.read(), "html.parser")
urlClient.close()

links =page_soup.findAll('a')

out_filename = "dmoz_links.csv"

headers = "link\n"

f = open(out_filename, "w")
f.write(headers)
count =0
for link in links:
	if(count <49):

		link_store = link.get('href')
		temp_link =str(link_store)
	
		if(temp_link.find('https')!=-1):
			print("Link :" +str(link_store))
			f.write(str(link_store) +"\n")
		else:
	
			url = "https://dmoz-odp.org"
			print("Link :"+str(url)+str(link_store) )
			f.write(str(url)+str(link_store) +"\n")
		count=count+1

f.close()  

