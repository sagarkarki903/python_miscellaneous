import requests
from bs4 import BeautifulSoup
import pprint #print pretty

res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

# print(f"{soup.find_all('div')}")
# print(soup.select('.titleline')[0]) #get the first element
headings = soup.select('.titleline')
subtext = soup.select('.subtext')
test = soup.select('.titleline > a')
def create_custom_hn(headings, subtext):
    hn = []
    for index, item in enumerate(headings):
        title = item.getText()
        linkfind = item.find('a')
        links = linkfind.get('href', None) #None here is the default, the second parameter(attribute) exists if there is no href it returns None
        vote = subtext[index].select('.score')
        if len(vote):
            vote_text = vote[0].getText()
            vote_digit = int(vote_text.split()[0])
            if vote_digit > 100:
                hn.append({'vote': vote_text, 'title': title, 'link': links})

    return hn

# print(subtext[0].select('.score'))
# print(subtext[2].select('.score')[0].getText())
pprint.pprint(create_custom_hn(headings, subtext))


