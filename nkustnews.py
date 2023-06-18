import os
import django
import requests                 #擷取網頁用的模組
from bs4 import BeautifulSoup   #剖析網頁用的模組
import time                     #時間模組，可以用它來暫停一小段時間
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_final.settings')
django.setup()
from mysite import models

models.NKUSTnews.objects.all().delete()
urls = "https://www.nkust.edu.tw/p/403-1000-1363-{}.php?Lang=zh-tw"
for page in range(1, 54):
    url = urls.format(page)
    html = requests.get(url).text
    sel = "#pageptlist > div > div > div > div.d-txt > div.mtitle > a"
    sel2 = "#pageptlist > div > div > div > div.d-txt > div.mtitle > i"
    soup = BeautifulSoup(html, "html.parser")

    dates = soup.select(sel2)
    titles = soup.select(sel)
    for i in range(len(titles)):
        new_record = models.NKUSTnews(
            date = dates[i].text.strip(),
            title = titles[i].text.strip(),
            url = titles[i].get("href").strip()
        )
        new_record.save()
    print("Page:{}".format(page))
    time.sleep(3)
print("Done")