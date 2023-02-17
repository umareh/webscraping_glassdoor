#created by Om Umare
#Glassdoor parser
#things to do -
#   automate input html - done
#   automate max page number
#   able to search different companies and job titles
#   create a UI
#   Name the output file
#Extreme need
#   be able to decipher if its a coding question or probability one
from docx import Document
from bs4 import BeautifulSoup #import bs4 for html data parsing and managment
import requests # to be able to make html requests
from random import randint
from time import sleep
def glassfoor(link):
    for x in range(0,len(link)):
        if link[x:x++3]=="_IP":
            a=link[:x+3]
            b=link[x+4:]
            break
#     return a,b
# a,b=glassfoor("https://www.glassdoor.com/Interview/Susquehanna-International-Group-(SIG)-Assistant-Trader-Interview-Questions-EI_IE24446.0,37_KO38,54_IP3.htm?filter.jobTitleFTS=Assistant+Trader")
# print(a,b)
    textContent = []
    for x in range(30,50): #goes thorugh the first 10 pages - NEED to finda way to see how many pages are there
        page_link=str(a)+str(x)+str(b)
        print(page_link)
        page_response = requests.get(page_link,timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        paragraphs = page_content.ul.find_next_siblings("ul")
        # print(paragraphs)
        paragraphs = page_content.find_all("span", {"class": "d-inline-block mb-sm"})
        for i in range(0,len(paragraphs)):
            textContent.append(paragraphs[i].text)
        #sleep(randint(2,8))
    d= Document()
    for x in range(0,len(textContent)):
        p=d.add_paragraph(textContent[x], style='List Bullet')
        # list_number(d,p,level=0,num=False)
    d.save("test.docx")

# a="https://www.glassdoor.com/Interview/MarketAxess-Software-Developer-Interview-Questions-EI_IE11426.0,11_KO12,30.htm"
# c="https://www.glassdoor.com/Interview/MarketAxess-Software-Developer-Interview-Questions-EI_IE11426.0,11_KO12,30_IP2.htm?filter.jobTitleFTS=Software+Developer"
# b="https://www.glassdoor.com/Interview/Fast-Enterprises-Implementation-Consultant-Interview-Questions-EI_IE241404.0,16_KO17,42_IP1.htm?filter.jobTitleFTS=Implementation+Consultant&filter.offerAccepted=true&filter.offerDeclined=true"







# for i in range(0,2):
#     paragraphs=page_content.find_all("span",{"class":"d-inline-block mb-sm"})[i].text
#     textContent.append(paragraphs)
# print(textContent)

# a="https://www.glassdoor.com/Interview/Fast-Enterprises-Implementation-Consultant-Interview-Questions-EI_IE241404.0,16_KO17,42.htm?filter.jobTitleFTS=Implementation+Consultant&filter.offerAccepted=true&filter.offerDeclined=true"
# b="https://www.glassdoor.com/Interview/Fast-Enterprises-Implementation-Consultant-Interview-Questions-EI_IE241404.0,16_KO17,42_IP2.htm?filter.jobTitleFTS=Implementation+Consultant&filter.offerAccepted=true&filter.offerDeclined=true"
# https://www.glassdoor.com/Interview/Fast-Enterprises-Implementation-Consultant-Interview-Questions-EI_IE241404.0,16_KO17,42_IP3.htm?filter.jobTitleFTS=Implementation+Consultant&filter.offerAccepted=true&filter.offerDeclined=true
# A=[]
# for x in range(0,len(a)):
#     if a[x]!=b[x]:
#         A.append(b[x])
# print("".join(A))
