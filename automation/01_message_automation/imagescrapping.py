from bs4 import BeautifulSoup
import requests
import os 

url ="https://ncit.edu.np/albums"

#Get the HTMLcontent
response = requests.get(url)
soup =BeautifulSoup(response.text, 'html.parser')
#parsethe html content

#find image tag
image_tags =soup.find_all('img')

#imagesource
os.mkdir('images')
i=1

for img_tags in image_tags:
    image_source_link = img_tags['src']

    print(f"IMAGE_SOURCE LINK : {image_source_link}")
    image_data = requests.get(image_source_link).content

    with open(f'images/image_{i}.jpg','wb') as file:
        file.write(image_data)
    i+=1    