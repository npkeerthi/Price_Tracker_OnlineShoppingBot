from bs4 import BeautifulSoup
import requests

print(" 🤖 Hello Welcome To Online Price Tracker\n")
press=input("Press 1 if You got your URL with you Else skip :")
if press=="1":
  myurl=input("Paste Your FLipkart Url : ")
else:
  myurl="https://www.flipkart.com/urbanic-cotton-blend-solid-coat/p/itmf17b5c0081c04?pid=CATG5YHBFMWB6WYH&lid=LSTCATG5YHBFMWB6WYHTSEN71&marketplace=FLIPKART&q=urbanic+coat&store=clo%2Fupk%2F6zw%2Fhkw&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&fm=SEARCH&iid=d2beea26-8e9b-471e-8541-60c08053497e.CATG5YHBFMWB6WYH.SEARCH&ppt=sp&ppn=sp&ssid=wuy6m8hotc0000001632338899723&qH=f3a1744ab8c2e697"
# Paste your own url from flipkart; As of now I have Created this only for flipkart products soon I shall Update this selfbot

respnse=requests.get(myurl,headers={"Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"},)
scrapweb=respnse.text

soup=BeautifulSoup(scrapweb,"html.parser")
# print(soup.prettify())

pp=soup.find(class_="_30jeq3 _16Jk6d").getText()
pp_no_symbol=pp.split("₹")[1]
if "," in pp_no_symbol:
  price=pp_no_symbol.split(",")
  price=float(price[0]+(price[1]))
  print(price)
else:
  price=float(pp_no_symbol)
  print(price)

try:
    company=soup.find(class_="G6XhRU").getText()
except:
    print("No Company Name")
product=soup.find(class_="B_NuCI").getText()
try:
    produtname=company+product
except:
    produtname=product
finally:
    print(produtname)

import smtplib

smtp_address="smtp.gmail.com"
mymail="yourmail@gmail.com"
paswd="yourmailpassword"
tomail="recipient@gmail.com"

Buy_Price=1800   #set target

if price < Buy_Price:
    msg=f"{produtname} is now at ₹{price}"

    with smtplib.SMTP(smtp_address ,port=587) as conn_send:
        conn_send.starttls()
        conn_send.login(mymail,password=paswd)
        conn_send.sendmail(
            from_addr=mymail,
            to_addrs=tomail,
            msg=f"Subject: 🛍 FLipkart Price Alert!!!!!! \n\n{msg}\n{myurl}".encode("utf-8") )
        
        
