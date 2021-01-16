import requests,re
from http.cookies import SimpleCookie

#这里填上你登陆时的cookie，下面有讲解如何获取
cookies = '''id3=DACD2C06-965A-4445-9029-20DCFA32d953ea5d483442256-965A-4445-902bca2989f6ac; SESS73302e152; fingerprint_s=0510db5feb41aff108b6801637d882dd; bp_video_offset_277091524=480147102836298343; bp_t_offset_277091524=480147102836298343; PVID=1'''
cookie = SimpleCookie(cookies)
cookies = {coo.key:coo.value for coo in cookie.values()}
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

base_url = 'https://member.bilibili.com/x/h5/data/fan/list?ps=500'


result =  requests.get(base_url,headers=headers,cookies=cookies).json()['data']

follower_count = result['my_follower']

fanNamesList = result['result']

page = 0

f = open("Names.txt","w",encoding='UTF-8')

def getNextPageOfFans(lastFanId):
    global page
    fansNames =[]
    page = page + 1
    print("Getting page " + str(page))

    # fansNames = requests.get(base_url + '&last_id='+lastFanId,headers=headers,cookies=cookies).json()['data']['result']
    # for i in range(0,len(fansNames)):
    #     f.writelines(fansNames[i]["card"]["name"])
    #     print(fansNames[i]["card"]["name"])


    try:
        if(lastFanId):
            fansNames = requests.get(base_url + '&last_id='+lastFanId,headers=headers,cookies=cookies).json()['data']['result']
        else:
            fansNames = requests.get(base_url,headers=headers,cookies=cookies).json()['data']['result']
        for i in range(0,len(fansNames)):
            f.writelines(fansNames[i]["card"]["name"]+'\n')
            print(fansNames[i]["card"]["name"]+'\n')
    except:
        page = page -1
        getNextPageOfFans(lastFanId)

    if(len(fansNames)==0):
        f.close()
        return

    getNextPageOfFans(fansNames[len(fansNames)-1]['mtime_id'])



getNextPageOfFans(False)
