import requests
import os
import datetime
import time
import traceback
import re


PHONES = ['13402110752', '15098942790', '15039211110', '18611010376']
# PHONES = ['13402110752']


print('==== dingpush begin =====')
print(PHONES)


while True:

    try:

        t = datetime.datetime.now().strftime('%H:%M')
        print(t)

        if t != '11:50':
            time.sleep(55)
            continue

        print('=============================================')

        url = 'http://172.23.43.13:8081/webroot/decision/login'
        data = {"username":"admin","password":"MG3C2eNkwxg/wtJWH5m+3w==","validity":-1,"sliderToken":"","origin":"","encrypted":True}
        r = requests.post(url, json=data)
        token = r.json()['data']['accessToken']

        print(token)

        content =  open('screenshot.js', encoding='utf8').read()
        content = re.sub(r"'value': '....+'", f"'value': '{token}'", content)
        open('screenshot.js', 'w', encoding='utf8').write(content)

        cmd = 'phantomjs.exe screenshot.js'
        print(cmd)
        os.system(cmd)
        print('-----')


        url = 'http://172.23.41.13:9000/message/sendMessageByPhoneAndFile'
        data = {
            'corn': '',
            'date': datetime.datetime.now().strftime('%Y-%m-%d'),
            'fileName': 'card.jpg',
            'msgType': 'image',
            'phones': '|'.join(PHONES),
        }
        f = open('card.jpg','rb')
        files = {'file': f}

        r = requests.post(url, data, files=files)
        f.close()

        print(r.json())

        time.sleep(55)

    except Exception as e:
        traceback.print_exc()
        input()

