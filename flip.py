#flipkart comapny 

from bs4 import BeautifulSoup as bs
import requests
from openpyxl import Workbook
import csv
import re 

link="https://www.flipkart.com/search?q=shoes%20under%20300&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
page=requests.get(link)
print(page)
soup=bs(page.content,'html.parser')
price=soup.find_all('div',class_="_30jeq3")
prices=[]
for i in range(0,len(price)):
        prices.append(price[i].get_text())
print(prices) 

title=soup.find_all('div',class_="_2WkVRV")
titles=[]
for i in range(0,len(title)):
         titles.append(title[i].get_text())
print(titles) 

title1 = soup.find_all('div',string=re.compile("BERSACHE"))
titles1 = []
for i in range(0,len(title1)):
    titles1.append(title1[i].get_text())
print(titles1)

title2 = soup.find_all('div',string=re.compile("199"))
titles2 = []
for i in range(0,len(title2)):
    titles2.append(title2[i].get_text())
print(titles2)

print("===============================================================")

title3 = soup.find_all('div',string=re.compile("Br"))
titles3 = []
for i in range(0,len(title3)):
    titles3.append(title3[i].get_text())
print(titles3)

print("===============================================================")

title4 = soup.find_all('div',string=re.compile("\d"))  # It will print all digits of website 
titles4 = []
for i in range(0,len(title4)):
    titles4.append(title4[i].get_text())
print(titles4)

print("===============================================================")

title5 = soup.find_all('div',string=re.compile("[L-M]")) 
titles5 = []
for i in range(0,len(title5)):
    titles5.append(title5[i].get_text())
print(titles5)

print("===============================================================")

title6 = soup.find_all('div',string=re.compile("^New")) 
titles6 = []
for i in range(0,len(title6)):
    titles6.append(title6[i].get_text())
print(titles6)

print("===============================================================")

title7 = soup.find('div',string=re.compile("Ru.{2}")) 
# titles7 = []
# for i in range(0,len(title7)):
#     titles7.append(title6[i].get_text())
print(title7)
