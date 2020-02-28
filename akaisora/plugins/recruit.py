from nonebot import on_command, CommandSession
from nonebot.permission import GROUP, PRIVATE_GROUP
import random

from nonebot import logger

# 活动池
class NormalStaffData:
    sixList = ['阿','煌','推进之王','能天使','星熊','闪灵','伊芙利特','银灰','塞雷娅','夜莺','艾雅法拉','陈','安洁莉娜','斯卡蒂','黑','赫拉格','麦哲伦','莫斯提马']
    fiveList =['吽','灰喉','天火','幽灵鲨','芙兰卡','德克萨斯','凛冬','白面鸮','蓝毒','普罗旺斯','雷蛇','临光','红','赫默','夜魔','初雪','华法琳','守林人','狮蝎','真理','白金','陨星','梅尔','可颂','崖心','空','食铁兽','诗怀雅','格劳克斯','星极','送葬人','槐琥','苇草','布洛卡']
    fourList = ['安比尔','深海色','杜宾','白雪','流星','梅','远山','夜烟','蛇屠箱','末药','猎蜂','慕斯','砾','暗索','地灵','调香师','清道夫','霜叶','角峰','古米','缠丸','阿消','红豆','杰西卡','格雷伊','苏苏洛','桃金娘','红云']
    threeList = ['芬','克洛丝','炎熔','米格鲁','芙蓉','卡缇','史都华德','香草','玫兰莎','安赛尔','梓兰','翎羽','空爆','月见夜','斑点','泡普']

    fourListUp = []
    fiveListUp = ['拉普兰德','惊蛰']
    sixListUp = ['刻俄柏']

    # 区间算法
    # 六星：10
    # 五星： 23
    # 四星 22
    # 三星：14
    def singleDrawing(self):
        # 保存随机值,毕竟这是单抽算法
        randomResult = random.randint(1, 10000)
        # 随机值判断
        if randomResult <= 200:
            # 抽到了六星干员.
            randomResult = random.randint(1, 10000)
            # 判断是否抽到了up干员
            if randomResult <= 5000:
                return '【★★★★★★UP!】——' + self.sixListUp[random.randint(0, len(self.sixListUp)-1)]
            else:
                return '【★★★★★★】——' + self.sixList[random.randint(0, len(self.sixList)-1)]
        elif randomResult <= 1000:
            # 抽到了五星干员
            randomResult = random.randint(1, 10000)
            if randomResult <= 5000:
                return '[★★★★★UP!]——' + self.fiveListUp[random.randint(0, len(self.fiveListUp)-1)]
            else:
                return '[★★★★★]——' + self.fiveList[random.randint(0, len(self.fiveList)-1)]
        elif randomResult <= 6000:
            # 抽到了四星干员.
            if randomResult <= 5000:
                return '☆☆☆☆——' + self.fourList[random.randint(0, len(self.fourList)-1)]
            else:
                return '☆☆☆☆UP!——' + self.fourListUp[random.randint(0, len(self.fourListUp)-1)]
            
        else:
            # 抽到了三星干员.
            return '☆☆☆——' + self.threeList[random.randint(0, len(self.threeList)-1)]



@on_command('arkone', aliases=['干员寻访'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def arkRandom(session: CommandSession):
    data = NormalStaffData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '抽到了: ' + data.singleDrawing())


@on_command('arkten', aliases=['十连寻访'], permission=GROUP | PRIVATE_GROUP, only_to_me=False)
async def arkRandomTen(session: CommandSession):
    data = NormalStaffData()
    nickname = session.ctx['sender']['nickname']
    await session.send(nickname + '的十连结果：\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing() + '\n' + data.singleDrawing() + '\n' +
                       data.singleDrawing())
