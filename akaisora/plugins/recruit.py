from nonebot import on_command, CommandSession
from nonebot.permission import GROUP, PRIVATE_GROUP
import random

from nonebot import logger

# 活动池
class NormalStaffData:
    sixList = ['能天使','推进之王','伊芙利特','艾雅法拉','安洁莉娜','闪灵','夜莺','星熊','塞雷娅','银灰','斯卡蒂','陈','黑','赫拉格','麦哲伦','莫斯提马','煌','阿','刻俄柏','风笛','傀影','温蒂','早露','铃兰','棘刺','森蚺','史尔特尔','瑕光','泥岩','山','空弦','嵯峨','异客','凯尔希','卡涅利安','帕拉斯']
    fiveList =['白面鸮','凛冬','德克萨斯','芙兰卡','拉普兰德','幽灵鲨','蓝毒','白金','陨星','天火','梅尔','赫默','华法琳','临光','红','雷蛇','可颂','普罗旺斯','守林人','崖心','初雪','真理','空','狮蝎','食铁兽','夜魔','诗怀雅','格劳克斯','星极','送葬人','槐琥','苇草','布洛卡','灰喉','吽','惊蛰','慑沙','巫恋','极境','石棉','月禾','莱恩哈特','断崖','蜜蜡','贾维','安哲拉','燧石','四月','奥斯塔','絮雨','卡夫卡','爱丽丝','乌有','熔泉','赤冬','绮良']
    fourList = ['夜烟','远山','杰西卡','流星','白雪','清道夫','红豆','杜宾','缠丸','霜叶','慕斯','砾','暗索','末药','调香师','角峰','蛇屠箱','古米','深海色','地灵','阿消','猎蜂','格雷伊','苏苏洛','桃金娘','红云','梅','安比尔','宴','刻刀','波登可','卡达','孑','酸糖','芳汀','泡泡','杰克','松果','豆苗','深靛']
    threeList = ['芬','香草','翎羽','玫兰莎','卡缇','米格鲁','克洛丝','炎熔','芙蓉','安赛尔','史都华德','梓兰','空爆','月见夜','斑点','泡普卡']

    fourListUp = []
    fiveListUp = ['红','幽灵鲨']
    sixListUp = ['帕拉斯']

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
                #有可能没有四星UP
                try:
                    return '☆☆☆☆UP!——' + self.fourListUp[random.randint(0, len(self.fourListUp)-1)]
                except:
                    return '☆☆☆☆——' + self.fourList[random.randint(0, len(self.fourList)-1)]
            
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
