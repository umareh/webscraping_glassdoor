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
    textContent = []
    for x in range(2,10): #goes thorugh the first 10 pages - NEED to finda way to see how many pages are there
        page_link=str(a)+str(x)+str(b)
        print(page_link)
        page_response = requests.get(page_link,timeout=5)
        page_content = BeautifulSoup(page_response.content, "html.parser")
        print(page_content)
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

glassfoor("https://www.glassdoor.co.in/Interview/IMC-Trading-Graduate-Trader-Interview-Questions-EI_IE278100.0,11_KO12,27_IP2.htm?filter.jobTitleFTS=Graduate+Trader")

