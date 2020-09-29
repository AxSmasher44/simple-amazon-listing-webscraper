import requests
from bs4 import BeautifulSoup
from csv import DictWriter

"""WARNING:Don't send requests continuously!!!
    Only works for amazon india"""

def amazon_scraper(item):
    if " " in item:
        url_item = item.split(" ")
        url_string = "+".join(url_item)
        URL = "https://www.amazon.in/s?k="+url_string+"&ref=nb_sb_noss_2"
    else:
        URL = "https://www.amazon.in/s?k="+item+"&ref=nb_sb_noss_2" 
    
    all_items = []
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.find_all("div", class_="sg-col-inner")
    for product in products:
        all_items.append({
            "Name":product.find("span", class_="a-size-medium a-color-base a-text-normal").get_text(),
            "Price":product.find("span", class_="a-offscreen").get_text()
        })
    return all_items
print(amazon_scraper("apple watch"))
def product_listings_to_csv(product):
    item_dict = amazon_scraper(product)
    with open(product+".csv", "w", newline="", encoding="UTF-8") as file:
        headers = ["Name", "Price"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for item in item_dict:
            csv_writer.writerow(item) 


