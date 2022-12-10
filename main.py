import requests
import re


url = "https://stackoverflow.com/questions/22269435/how-to-iterate-through-a-list-of-objects-in-c"
url_1 = "https://vk.com/topic-59372349_29077381"

what_case = 'mail'

if what_case == "mail":
    page = requests.get(url_1)

with open("html.txt", encoding="utf-8", mode = "w+") as file:
    file.write(str(page.text))

pattern_mail = r"\b[\w\.-]+@[\w\.-]+(?:\.[\w]+)+\b"


if what_case == "mail":
    pattern = r"{}".format(pattern_mail)

link_list_1 = re.findall(pattern, str(page.text))


print("Найдено e-mail адресов:",len(link_list_1))
print("\n")
for link_it in range(len(link_list_1)):
    print(link_list_1[link_it])
print("\n")