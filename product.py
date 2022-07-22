import requests
from bs4 import BeautifulSoup
import gspread

url= "https://www.jumia.com.ng/flash-sales/?flashsale=1658394000&page=12#catalog-listing"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
jumia = "https://www.jumia.com.ng/flash-sales"

first = soup.find("div", class_="-pvs col12")
second = first.find_all("div", class_= "-paxs row _no-g _4cl-3cm-shs")







for i in second:
    a = i.find_all("article", class_="prd _fb _p col c-prd")
    for items in a:
        h3 = items.find("h3")
        price = items.find("div", class_="prc")
        rating = items.find("div" ,class_= "rev")
        if not items.find("div" ,class_= "rev"):
            rating="No Ratings"
        else:
            rating= items.find("div" ,class_= "rev").text.strip()


    
        left = items.find("div", class_="stk")
        link = items.find("a", class_="core").get("href")

        itemss=h3.text.strip()
        pricees = price.text.strip()
        ratingss =rating
        remam = left.text.strip()
        href = jumia + link


        # print(itemss)
        # print(pricees)
        # print(ratingss)
        # print(remam)
        # print(href)
        # print()
        

        pro = {"Items Name":itemss,"Amount":pricees,"Ratings and Review":ratingss,"Stock":remam,"Links":href}
        gc = gspread.service_account(filename='jumia.json')
        sh = gc.open('jumia').sheet1
        sh.append_row([pro["Items Name"],pro["Amount"],pro["Ratings and Review"],pro["Stock"],pro["Links"]])

        


