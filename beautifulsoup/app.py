# import requests
# #the website URL
# url_link = "https://www.webforefront.com/django/formfieldtypesandvalidation.html"
# result = requests.get(url_link).text
# print(result)

from bs4 import BeautifulSoup
#import requests library
import requests
#the website URL
url_link = "https://www.webforefront.com/django/formfieldtypesandvalidation.html"
result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")

res = doc.find(class_ = "card-text text-justify")
print(res)
for ele in res:
  print(res.find("p"))

# f = open("doc.html", "a")
# f.write(doc.prettify())
# f.close()
