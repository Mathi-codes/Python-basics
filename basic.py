from bs4 import BeautifulSoup
import requests
url=requests.get("https://www.wired.com/gallery/best-smartwatches/")
soup=BeautifulSoup(url.content,"html.parser")
containers=soup.find_all("div",class_="ProductSummaryBrandAndName-JEiSZ exyoZo")
containers1=soup.find_all("span",class_="ButtonLabel-cjAuJN hzwRuG button__label")
sliced=containers1[0:4]
for name, prices in zip(containers,sliced):
    print(name.text.strip(),":",prices.text.strip())