# Importing library
from bs4 import BeautifulSoup
# bs4 cannot parse links, so we use urllib to parse the links
from urllib.request import urlopen

# Parsing the webpage 
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/jesus.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Reading the parsed HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
print(type(soup))
# print(soup.prettify())
# .head. specifies only the head tag 
# print(soup.head.prettify())
for child in soup.head.children:
    print(child)