# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import requests
import json


# %%
output = open('data.txt','w')
# output.write("hello")


# %%
i = 0
flag = 0
while True:
    payload = {'scid': 'SAGOVuM3TBO2pbwL', 'ts': str(i) + '000'}
    r = requests.get("https://www.yizhibo.com/live/h5api/get_playback_event", params=payload)
    obj = json.loads(r.text)
    if obj['data']['count']:
        flag = 0
        for item in obj['data']['list']:
            # print(str(item['ts']) + ' ' + item['nickname'] + ':' + item['content'])
            output.write(str(item['ts']) + '\t' + item['nickname'] + ':\t' + item['content'] + '\n')
    else:
        flag += 1
    i += 5
    if i > 20000 or flag > 65:
        break
    
        


# %%
output.close()


# %%


