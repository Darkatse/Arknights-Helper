# Arknights Helper-Remix
A QQ bot based on nonebot and mirai/mirai-http-api

## Description
目前功能：公招计算 材料规划 模拟抽卡
## Usage
1. tag 用空格隔开  
e.g. 治疗 先锋

>**Result**\
>【治疗+先锋干员】:桃金娘★4
>
>【先锋干员】:桃金娘★4 清道夫★4 红豆★4 德克萨斯★5 凛冬★5 ★1~★3...4
>
>【治疗】:苏苏洛★4 桃金娘★4 清流★4 白面鸮★5 赫默★5 华法琳★5 临光★5 夜魔★5 末药★4 调香师★4 古米★4 ★1~★3...4



2. @this_bot arkone / arkten  
   模拟单抽/十连抽卡

>抽卡 卡池位于recruit.py 需要手动更新



3. mati/材料 固源岩组 2 异铁组 5  
   刷图计算，命令后加需要刷的材料和个数，均以空格隔开

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
   |      |  tag_processing.py   公招计算
   |      |  TagLogic.py         公招计算接口 
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
### 1. 下载 [mirai](https://github.com/mamoe/mirai) + [mirai-api-http](https://github.com/project-mirai/mirai-api-http)/[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)
[mirai](https://github.com/mamoe/mirai)是当前最潮最in的机器人框架，之后的一切都是基于该框架。如果你还没来得及拥有的话就赶快下载吧！ ~~棒读~~  
或者也可以选择优秀的拓展客户端[go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，拥有许多拓展功能的同时兼容了[Onebot](https://github.com/botuniverse/onebot/blob/master/README.md)  
### 2. Clone 或者下载这个项目
```
git clone https://github.com/Darkatse/Arknights-Helper
```
### 3. 安装[Nonebot](https://github.com/nonebot/nonebot)以及其他依赖
首先安装[Nonebot](https://github.com/nonebot/nonebot)  
可以使用 pip 安装已发布的最新版本：
```
pip install nonebot
```
安装本程序相应的依赖
```
pip install -r akaisora/requirement.txt
```
### 4. 配置反向ws服务端并启动本bot
参考[该链接](https://docs.nonebot.dev/guide/installation.html#cqhttp-%E6%8F%92%E4%BB%B6-%E5%B7%B2%E5%BC%83%E7%94%A8)来配置[mirai-api-http](https://github.com/project-mirai/mirai-api-http)的反向ws服务端，默认配置为 http://127.0.0.1:9090 , 如果遇到端口冲突可以在config.py中修改  
最后启动bot  
```
python bot.py
or
nohup python bot.py >nohup.out 2>&1 & #后台运行
```
enjoy it !
## Acknowledgements
Thanks for nonebot's very detailed instruction.\
https://docs.nonebot.dev/

Thanks for character data from MRFZ-wiki.\
https://prts.wiki/

Thanks for recruitment data from bigfun.\
https://www.bigfun.cn/tools/aktools/hr
