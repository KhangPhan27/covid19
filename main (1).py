from sys import stdout
import requests, os,json
import socket
from time import sleep
import os
import time
from datetime import datetime
import pytz
from keep_alive import keep_alive
keep_alive()
os.system('clear')
ip=socket.gethostbyname(socket.gethostname())

os.system('clear')

id='100021668201187'
nd='TÌNH HÌNH COVID 19 VIỆT NAM'
timeh='18'
timem='00'

print('\n')
ck='datr=bfEqY7HBnL1BlQanMtYvlYIZ;sb=bfEqY7P9-nYN-oyfYk5OUPBi;vpd=v1%3B660x360x2;c_user=100087250200164;xs=8%3AjdVKkh7UbDNAJw%3A2%3A1666381846%3A-1%3A-1;m_page_voice=100087250200164;fr=0Y4t7Q8EB37OYvpMu.AWWiKr1mzAGzx4R94MtAy9b22oE.BjKvFt.GF.AAA.0.0.BjWOm1.AWVBjv4zvuQ;m_pixel_ratio=2;wd=360x660;'
while True:
    try:
        get=requests.get(f'https://mbasic.facebook.com/privacy/touch/block/confirm/?bid={id}&ret_cancel&source=profile',headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5','cookie': ck,'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1'}).text
        fb_dtsg=get.split('<input type="hidden" name="fb_dtsg" value="')[1].split('" autocomplete="off" />')[0]
        jazoest=get.split('<input type="hidden" name="jazoest" value="')[1].split('" autocomplete="off" />')[0]
        break
    except:
        print('Cookie sai!!')
os.system('clear')

headers = {
    'authority': 'm.facebook.com',
    'accept': '*/*',
    'accept-language': 'vi,en;q=0.9,vi-VN;q=0.8,fr-FR;q=0.7,fr;q=0.6,en-US;q=0.5',
    # Requests sorts cookies= alphabetically
    'cookie': ck,
    'origin': 'https://m.facebook.com',
    'referer': 'https://www.facebook.com',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
}

params = {
    'icm': '1',
}
#data 1
data = {
    f'ids[{id}]': id,
    'body': nd,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
}
#data
dem=0

while True :
    local = datetime.now()
    tz_VN = pytz.timezone('Asia/Ho_Chi_Minh') 
    datetime_VN = datetime.now(tz_VN)
    datetd=datetime_VN.strftime("%d")
    mtd=datetime_VN.strftime("%m")
    a=datetime_VN.strftime("%H")
    b=datetime_VN.strftime("%M")
    datacv=requests.get('https://api.apify.com/v2/key-value-stores/EaCBL1JNntjR3EakU/records/LATEST?disableRedirect=true').json()
    tc=' Tổng cộng [ Ca nhiễm ' + str(datacv["infected"])+' | Hồi phục: ' + str(datacv["recovered"])+' | Đang điều trị: '+str(datacv["treated"])+ ' | Tử vong: '+str(datacv["died"])+']'
    tk='Trong ngày '+datetd+'/'+mtd+ ' [Ca nhiễm mới: +' + str(datacv["infectedToday"])+' | Hồi phục: +' + str(datacv["recoveredToday"])+' | Đang điều trị: '+str(datacv["treatedToday"])+ ' | Tử vong: +'+str(datacv["diedToday"])+']'
    datacovid = {
    f'ids[{id}]': id,
    'body':  tk,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    }
    datacovidvn = {
    f'ids[{id}]': id,
    'body':  tc,
    'waterfall_source': 'message',
    'fb_dtsg': fb_dtsg,
    'jazoest': jazoest,
    }
    if a==timeh and b==timem and dem==0:
        response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=data)
        response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=datacovidvn)
        response = requests.post('https://m.facebook.com/messages/send/', params=params, headers=headers, data=datacovid)
        print(f' Send Success | {nd}')
        dem=dem+1
	
    if dem!=0 and b!=timem:
        dem=0
    
	

		
		    
		    
	
 
    
    
    