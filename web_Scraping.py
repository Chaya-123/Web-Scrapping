import requests
from bs4 import BeautifulSoup
import pandas as pd
import contents
    



page_num=int(input("Enter page numbers:"))
dbname=input("Enter database name:")


scraped_hotel_list=[]
contents.connect(dbname)
scraped_hotel_list=[]
for num in range(1,page_num):
    url="https://www.tripadvisor.in/Hotels-g297628-"+"oa"+str(30*(page_num-1))+"-Bengaluru_Bangalore_District_Karnataka-Hotels.html"
    
    print("GET Request for:",url)
    req=requests.get(url)
    content=req.content
    soup=BeautifulSoup(content,"html.parser")
    all_hotels=soup.find_all("div",{"class":"prw_rup prw_meta_hsx_responsive_listing ui_section listItem"})
    
    #hotel_features=[]
    for hotel in all_hotels:
        hotel_dict={}
        
        hotel_dict["hotel_name"]=hotel.find("a",{"class":"property_title prominent"}).text
            
        hotel_dict["hotel_reviews_count"]=hotel.find("a",{"class":"review_count"}).text
        #combine feature1 and feature2
    
        #hotel_features=[hotel_features1,hotel_features2]
        hotel_dict["hotel_features"]=hotel.find("span",{"class":"text"}).text
        
        
        try:
            hotel_dict["hotel_price"]=hotel.find("div",{"class":"price__resizeWatch"}).text
            
        except AttributeError:
            hotel_dict["hotel_price"]=hotel.find("div",{"class":"price-wrap"}).text
            
        scraped_hotel_list.append(hotel_dict)
        
    
        contents.insert_into_table(dbname,tuple(hotel_dict.values()))
    
dataFrame=pd.DataFrame(scraped_hotel_list)
print("Creating CSV file...")
dataFrame.to_csv("tripadvisor1.csv")
contents.get_Hotel_info(dbname)
