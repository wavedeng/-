import requests,re
from http.cookies import SimpleCookie

#这里填上你登陆时的cookie，下面有讲解如何获取
cookies = '''_uuid=5DB6F12A-C1A6-4772-45D0-0F82156E57BF99336infoc; buvid3=DACD2C06-965A-4445-9029-20DCFA328434143094infoc; sid=c4aii2qv; CURRENT_FNVAL=80; blackside_state=1; rpdid=|(k)~Rk)JJY)0J'uY|)umumJm; fingerprint3=21d953ea5d483442256bacc0a9f0ddc7; buivd_fp=DACD2C06-965A-4445-9029-20DCFA328434143094infoc; buvid_fp_plain=DACD2C06-965A-4445-9029-20DCFA328434143094infoc; fingerprint=062594a4b2a4559bd304086a123e23a6; LIVE_BUVID=AUTO7416085217882235; dy_spec_agreed=1; buvid_fp=DACD2C06-965A-4445-9029-20DCFA328434143094infoc; bp_t_offset_599021380=478266950833678670; bp_video_offset_599021380=478190904144348234; CURRENT_QUALITY=116; DedeUserID=277091524; DedeUserID__ckMd5=83902bca2989f6ac; SESSDATA=37d37db0%2C1626143982%2C0a9a9*11; bili_jct=1b0ce455aae35b70c45bc5973302e152; fingerprint_s=0510db5feb41aff108b6801637d882dd; bp_video_offset_277091524=480147102836298343; bp_t_offset_277091524=480147102836298343; PVID=1'''
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