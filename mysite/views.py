from django.shortcuts import render   # 渲染網頁
from django.http import HttpResponse   # Django用來回應給瀏覽器特定資料的函式
import requests   # 匯入擷取網頁所需要的模組
import json       # 匯入操作JSON格式所需要的模組
from mysite import models  # 從 mysite 的資料夾中的 models.py 匯入所有的類別（資料表）
import random     # 匯入隨機模組

def index(request):
    index = "active"
    mynames = ["高科咖啡因", "有點想睡覺", "今天要吃啥"]
    myname = random.choice(mynames)
    return render(request, "index.html", locals())

def nkustnews(request):
    news = "active"
    datas = models.NKUSTnews.objects.all()
    return render(request, "nkustnews.html", locals())

def phonelist(request, id=-1, country=''):
    add = "active"
    dots = "../../"
    print(str(id) + " " + country)
    if id == -1 and country == '':
        data = models.PhoneModel.objects.all()              #找出所有的手機
    elif country != '':
        maker = models.PhoneMaker.objects.filter(country=country)
        data = models.PhoneModel.objects.filter(maker=maker[0])
        for i in range(1, len(maker)):
            data |= models.PhoneModel.objects.filter(maker=maker[i])
    else:
        maker = models.PhoneMaker.objects.get(id=id)        #找出一個(get)指定的廠牌
        data = models.PhoneModel.objects.filter(maker=maker) #找出一堆(filter)符合的資料
    return render(request, "phonelist.html", locals())

def all_data(request):
    bike = "active"
    # 先把舊資料通通刪除
    models.HBicycleData.objects.all().delete()
    # 要比照all_data函式的程式，把網站上所有的資料都下載解析，放到資料表 (HBicycleData) 裡面
    url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"
    r = requests.get(url)         
    data = json.loads(r.text) 
    date = data['updated_at']    
    bicycle_data = data['retVal'] 
    for item in bicycle_data:
        new_record = models.HBicycleData(
            sna = item['sna'].split("_")[1],
            sbi = int(item['sbi']),
            tot = int(item['tot'])
            )
        new_record.save()

    data = models.HBicycleData.objects.all()
    return render(request, "all.html", locals())

def filtered_data(request):
    bike = "active"
    try:
        num = int(request.GET['num'])
    except:
        print("false")
        searched = False
        return render(request, "filter.html", locals())
    
    # 先把舊資料通通刪除
    models.HBicycleData.objects.all().delete()
    # 要比照all_data函式的程式，把網站上所有的資料都下載解析，放到資料表 (HBicycleData) 裡面
    url = "https://opendata.hccg.gov.tw/OpenDataFileHit.ashx?ID=48DEDBDAC3A31FC6&u=77DFE16E459DFCE3F5CEA2F931E333F7E23D5729EF83D5F20744125E844FB27044F9892E6F09372518441B3BB84260426ADE242A57DFB9E8C9A50C50134F4F47"
    r = requests.get(url)         
    data = json.loads(r.text) 
    date = data['updated_at']    
    bicycle_data = data['retVal'] 
    for item in bicycle_data:
        new_record = models.HBicycleData(
            sna = item['sna'].split("_")[1],
            sbi = int(item['sbi']),
            tot = int(item['tot'])
            )
        new_record.save()

    # 過濾 HBicycleData 裡面的所有記錄，找出其中sbi>=10的站台放到data中

    searched = True
    data = models.HBicycleData.objects.filter(sbi__gte=num)

    return render(request, "filter.html", locals())

def chart(request):
    add = "active"
    data = models.PhoneModel.objects.all()
    return render(request, "chart.html", locals())

def stock300list(request):
    add = "active"
    try:
        cost = int(request.GET['cost'])
        data = models.StockInfo.objects.filter(price__gte=cost).order_by('-price')
        numbers = len(data)
        searched = True
    except:
        searched = False
    return render(request, "stocklist.html", locals())