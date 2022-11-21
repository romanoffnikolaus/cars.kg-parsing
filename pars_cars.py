import requests
from bs4 import BeautifulSoup
import csv

def write(data):
    with open('cars.csv', 'a') as file:        
        writer = csv.writer(file)
        writer.writerow([data['title'],data['img'],data['price']])




def get_html(url):
    responce = requests.get(url)
    return responce.text

def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    page_list = soup.find('div', class_ = 'pages fl').find_all('a')
    last_page = page_list[-2].text
    return last_page





def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    cars = soup.find('div', class_ = 'catalog-list').find_all('a', class_ = 'catalog-list-item')



    for i in cars:
        try:
            title = i.find('span', class_ = 'catalog-item-caption').text.strip()   #find_all для поиска по элементно
        except:
            title = ''

        try:
            img = i.find('img', class_ = 'catalog-item-cover-img').get('src')
        except:
            img = ''

        try:
            price = i.find('span', class_ = 'catalog-item-price').text
        except:
            price = ''
        
        data = {
            'title': title, 
            'img':img, 
            'price':price
            }
        write(data)



def main():
    url_ = 'https://cars.kg/offers'
    html = get_html(url_)
    number = int(get_total_pages(html))
    page = 1
    while page <= number:
        print(page)
        url_ = f'https://cars.kg/offers/{page}'
        html = get_html(url_)
        number = int(get_total_pages(html))
        if not BeautifulSoup(html, 'lxml').find('div', class_='catalog-list'):
            break
        get_data(html)
        page +=1 
    
    print(number)
    
        

with open('cars.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'img','price'])






main()