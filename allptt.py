import requests
from bs4 import BeautifulSoup

while page<=5972:	
	link = requests.get('https://www.ptt.cc/bbs/Food/index'+str(page)+'.html')
	soup = BeautifulSoup(link.text, 'lxml').select('.r-ent')

	for entry in soup :
		try :
			title = entry.find('a').text
			url = entry.find('a').get('href', None)
			
			if '食記' in title and '台中' in title:
				print("標題 : ", title)
				print("超連結 : ", url)
				print()
				#sql.sql_save(title, url, 3)
		except :
			pass
	page+=1