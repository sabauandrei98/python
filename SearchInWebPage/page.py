import time
import datetime
import os
from urllib.request import urlopen

'''
This program was mainly made to search for the prices in a web pages on Black Friday
When the websites changes the price of an article for a small amount of time the program
detects this change and plays a song to announg the user.

For instance:
Lets say we are looking for an Iphone 7 which now is $500 (for example)
We copy the url link of the Iphone 7 search (ex: www.onlineshop.com/articles/iphone7)

Now the program will search on that page all the prices once every X second
In this interval it may find the normal place ex: $500 or it may find the new price (which only leasts for 1-2 mins)
If the price is very low : ex $20 the program will announce the user and the user will buy the article

IMPORTANT:
AFTER STARTING THE PROGRAM, DELETE ALL THE .TXT FILES IN THE PROJECT
'''

#SAVE THE PAGE CODE (the code of the page is useful in case you want to find the price format ex : <art-price> $570 </art-price>)
def writeToFile(html):
    f1 = open('siteCode.txt', 'w+')
    f1.write(str(html))
    f1.close()

#SAVE THE PRICES AT EACH ITERATION (an optional raport)
def raportData(price):
    f1 = open('raportData.txt', 'a')
    f1.write(str(datetime.datetime.now().time()) + " price -> " + price + '\n')
    f1.close()

#CHECKS IF IN THE PAGE EXIST A DESIRED PRICE
def checkPrice(price): 
    #MAXIMUM ACCEPTABLE PRICE
    wantedPrice = 1

    result = ""

    #Price may contain '.' or ',' ex: 2.999
    for x in price:
        if x >= '0' and x <= '9':
            result += x;

    intPrice = int(result)

    #START THE SONG AND SAVE THE PRICE IN TEXT FILE
    if (intPrice < wantedPrice):
        os.system(r"song.mp3")
        f1 = open('winPrice.txt', 'a')
        f1.write(str(datetime.datetime.now().time()) + " price -> " + result + '\n')
        f1.close()

#SEARCH FOR PRICES IN PAGE
def executeSearch(searchTag, separator, pageCode):

    index = 0
    while index != -1:
        index = pageCode.find(searchTag, index + 1)
        if index != -1:
            price = ""
            for i in range(index + len(searchTag), len(pageCode)):
                if pageCode[i] != separator:
                    price += str(pageCode[i])
                else:
                    checkPrice(price)
					
                    #optional
                    raportData(price)
                    break

def start():
    #CONSTANTS

    #REFRESH TIME (SECONDS)
    refreshIntervalSeconds = 10

    '''
    Let's say we have the page code and we don't know how to extract the prices
    We find an article and try to find out in which format it appears EX: <article-price> $505 </article-price>
    all prices will start after <article-price> and will end before </article-price> (This is just an instance, for a better understanding)
    '''
    searchTag = "<article-price>"

    '''
    We do not need all the tag in the separator because after we find the place where the price starts in the code
    We know that a price has the following format: <currency>(number).(floating_point) ex: $57.12  $500
    So it is enough to read the number until we reach the separator which will be "</article-price>"
    And we only need the first character of it because it is not a number
    And now we are looking to separate all the values (prices) which starts at "<article-price>" and end at "<"
    '''
    separator = "<"

    #SEARCH EVERY refreshIntervalSeconds
    while True:
        html = urlopen("http://codeforces.com")
        pageCode = str(html.read())

        executeSearch(searchTag, separator, pageCode)
        time.sleep(refreshIntervalSeconds)

        #optional
        writeToFile(pageCode)

start()

