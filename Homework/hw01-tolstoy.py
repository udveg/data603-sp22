#installing useful libraries 
import requests
from bs4 import BeautifulSoup

x = []
res = []
# url of the website
doc = "https://www.gutenberg.org/files/2600/2600-h/2600-h.htm"

# getting response object
res = requests.get(doc)

# Initialize the object with the document
soup = BeautifulSoup(res.content, "html.parser")

# Get the whole body tag
tag = soup.body
#tag
# Print each string recursively
for string in tag.strings:
        #Remove unwanted special characters
        string = string.replace('.', '').replace(',', '').replace('?', '').replace('!', '').replace(';', '').replace(':', '').replace('(', '').replace(')', '').replace('“', '').replace('”', '')
        x = x + string.split()

#Remove duplicates
y = list(set(x))
#print(y)
z=len(y)

print('there are {} unique words in the given book'.format(z))