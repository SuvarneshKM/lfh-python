import urllib.request 
from pprint import pprint 
from html_table_parser import HTMLTableParser 
from time import sleep

def create_currency():
    print('Creating forex data ..')
    def url_get_contents(url): 
        req = urllib.request.Request(url=url) 
        f = urllib.request.urlopen(req) 
        return f.read() 

    xhtml = url_get_contents('https://www.mohfw.gov.in/').decode('utf-8') 

    p = HTMLTableParser() 
    p.feed(xhtml) 
    SNo = p.tables[0][2][0]
    State = p.tables[0][2][1]
    Active = p.tables[0][2][2]
    Cured = p.tables[0][2][3]

    print({'S. No.':SNo, 'Name of State / UT':State, 'Active Cases*':Active, 'Cured/Discharged/Migrated*':Cured})
#     Currency.objects.create(
#             gram=gram,
#             today=today,
#             yesterday=yesterday,
#             change=change
#         )
#     sleep(5)


# #some heavy stuff here
# def update_currency():
#     print('Updating forex data ..')
#     def url_get_contents(url): 
#         req = urllib.request.Request(url=url) 
#         f = urllib.request.urlopen(req) 
#         return f.read() 

#     xhtml = url_get_contents('https://www.goodreturns.in/gold-rates/').decode('utf-8') 

#     p = HTMLTableParser() 
#     p.feed(xhtml) 
#     gram = p.tables[0][1][0]
#     today = p.tables[0][1][1]
#     yesterday = p.tables[0][1][2]
#     change = p.tables[0][1][3]

#     print({'gram':gram, 'today':today, 'yesterday':yesterday, 'change':change})
#     Currency.objects.create(
#             gram=gram,
#             today=today,
#             yesterday=yesterday,
#             change=change
#         )
#         find the object by filtering and update all fields
#     Currency.objects.filter(gram=gram).update(**data)

#     sleep(5)

create_currency()
# while True:
#     sleep(15)
#     update_currency()
# import requests
# import json
# from bs4 import BeautifulSoup


# res = requests.get("https://stackoverflow.com/questions")

# soup = BeautifulSoup(res.text, "html.parser")

# questions = soup.select(".question-summary")
# for que in questions:
#     q = que.select_one('.question-hyperlink').getText()
#     vote_count = que.select_one('.vote-count-post').getText()
#     views = que.select_one('.views').attrs['title']
#     tags = [i.getText() for i in (que.select('.post-tag'))]

#     print({'q':q, 'vote_count':vote_count, 'views':views, 'tags':tags})    