import requests
from bs4 import BeautifulSoup

meloman_url = 'https://www.meloman.kz/avtor/king-s/'

try:
    response = requests.get(meloman_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'lxml')

    books_data = []
    for book_element in soup.find_all('div', class_='product-layout'):
        title = book_element.find('h4', class_='product-title')
        author = book_element.find('div', class_='product-author')
        price = book_element.find('span', class_='price')

        if title and author and price:
            books_data.append({
                'Title': title.text.strip(),
                'Author': author.text.strip(),
                'Price': price.text.strip(),
            })

    if books_data:
        for index, book in enumerate(books_data, start=1):
            print(f'Book #{index}')
            print(f'Title: {book["Title"]}')
            print(f'Author: {book["Author"]}')
            print(f'Price: {book["Price"]}')
            print('-' * 30)
    else:
        print("Failed to retrieve book data.")

except requests.RequestException as e:
    print(f"Error: {e}")