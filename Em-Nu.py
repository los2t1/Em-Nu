from bs4 import BeautifulSoup
import re
import requests

try:
    import requests, os , re 
except MemoryError:
    os.system("pip install requests")
    os.system("pip install BeautifulSoup4")
    os.system("re")
    os.system("pip install os")

    os.system("clear")
#شعار الاداة
print("""""
      
       _..-'(                       )`-.._
                   ./'. '||\\.       (\_/)       .//||` .`\.
                ./'.|'.'||||\\|..    )O O(    ..|//||||`.`|.`\.
             ./'..|'.|| |||||\`````` '`"'` ''''''/||||| ||.`|..`\.
           ./'.||'.|||| ||||||||||||.     .|||||||||||| |||||.`||.`\.
          /'|||'.|||||| ||||||||||||{     }|||||||||||| ||||||.`|||`
         '.|||'.||||||| ||||||||||||{     }|||||||||||| |||||||.`|||.`
        '.||| ||||||||| |/'   ``\||``     ''||/''   `\| ||||||||| |||.`
        |/' \./'     `\./         \!|\   /|!/         \./'     `\./ `\|
        V    V         V          }' `\ /' `{          V         V    V
      Theis tool was programmed by : LOST \ My telegram channel https://t.me/cy1br
                     BTC : bc1q59xyghwlce2ze6tmes6u9m3tmgn5p5473ugeeh
      """)
#اكواد الاداة
allsite = ["https://enghamzasalem.com/",
           "https://www.ionixxtech.com/", "https://sumatosoft.com", "https://4irelabs.com/", "https://www.leewayhertz.com/",
           "https://stackoverflow.com", "https://www.vardot.com/en", "http://www.clickjordan.net/", "https://vtechbd.com/"]
emails = []
tels = []
for l in allsite:
    r = requests.get(l)
    soup = BeautifulSoup(r.content, "html.parser")
    for link in soup.findAll('a', attrs={'href': re.compile("^mailto:")}):
        emails.append(link.get('href'))
    for tel in soup.findAll('a', attrs={'href': re.compile("^tel:")}):
        tels.append(tel.get('href'))
print(emails)
print(tels)