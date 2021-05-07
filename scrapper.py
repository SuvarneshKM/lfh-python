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

#hai
create_currency()
