# QQ bot-Arknights Helper-Remix
A qq bot based on nonebot and coolq

## Description
目前功能：材料规划 抽卡
## Usage
1. ~~tag list split by space~~
>~~e.g. 近卫 男~~

>**~~Result~~**\
>~~【近卫】:~~
>~~幽灵鲨★5, 因陀罗★5, 杜宾★4, 艾丝黛尔★4, 慕斯★4, 霜叶★4, 缠丸★4, Castle-3★1, ★1~3...1~~
>
>~~【男】:~~
>~~角峰★4, Castle-3★1, ★1~3...6~~
>
>~~【近卫+男】:~~
>~~Castle-3★1~~

2. ~~send a screenshot of tags in game, get result as above~~

3. ~~tell character name~~

## 由于灰机Wiki关闭  tag查询暂不可用

4. @this_bot hello

>tell you some info about this bot

5. @this_bot update_data

>update character data from wiki

## File Structure
```
├─akaisora-bot
   ├─data      Arkplanner数据 删除并重启bot以更新数据
   │  │ formula.json   
   │  └─matrix.json
   ├─akaisora
   │  └─plugins
   │      │  recom_tags.py
   │      │  checklog.py         保存log
   │      │  fuzzname.py         拼音模糊查询
   │      │  material.py         材料规划
   │      │  MaterialPlanning.py 材料规划接口 来自https://github.com/ycremar/ArkPlanner
   │      │  orc_tool.py         图片识别
   │      │  record.py           
   │      │  recruit.py          抽卡
   │      └─ tuchuang.py         图床 用于图片识别
   │  apikeys.py      百度图片识别api
   │  bot.py
   └─ config.py
```

## Install Requirement
```
Python: Python>=3.6.1
Packages:   nonebot>=1.3.0
            numpy>=1.18.1
            sanic>=19.12.2
            scipy>=1.4.1
            Click>=7.0
```

## Usage
### 1. Run Bot
`python bot.py`\
or\
`nohup python bot.py >nohup.out 2>&1 &`
> use `python3 bot.py` for your need

### 2. Get It Work
#### Windows

1. Download [CoolQ](https://cqp.cc/b/news), install it.
> CoolQ Air version is for free but can receive/~send~ image
2. Add CoolQ plugin [CoolQ HTTP API](https://cqhttp.cc/docs/4.10/#/), install it follow the instruction.
3. Run CoolQ and Activate the plugin above.
4. Configure CoolQ HTTP API follow this [instruction](https://none.rclab.tk/guide/getting-started.html#%E9%85%8D%E7%BD%AE-coolq-http-api-%E6%8F%92%E4%BB%B6)
5. Run Bot

#### Linux
Bucause CoolQ has no linux version, but we can run it in docker.
1. Install [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
2. Get and Run Docker CoolQ (with CoolQ HTTP API) image follow this [instruction](https://cqhttp.cc/docs/4.10/#/?id=%E4%BD%BF%E7%94%A8-docker)
3. Run CoolQ and Activate the plugin above.
4. Configure CoolQ HTTP API follow this [instruction](https://none.rclab.tk/guide/getting-started.html#%E9%85%8D%E7%BD%AE-coolq-http-api-%E6%8F%92%E4%BB%B6), note that you should use post_url as 172.17.0.1 instead of 127.0.0.1 because of using Docker.
5. Run Bot

## Acknowledgements
Thanks for nonebot's very detailed instruction.\
https://none.rclab.tk/

Thanks for character data from MRFZ-wiki.\
http://wiki.joyme.com/arknights/%E5%B9%B2%E5%91%98%E6%95%B0%E6%8D%AE%E8%A1%A8
