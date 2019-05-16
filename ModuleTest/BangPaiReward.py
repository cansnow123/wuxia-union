import datetime
import re
from datetime import timedelta
import pytz

GLFile = "BangPai_DKPFaFangJiLi.txt"
# SLFile = "BangPai_DKPFaFangJiLi.txts"

# hk = datetime.datetime.now(pytz.timezone('Asia/Hong_Kong')) - timedelta(days=3)
hk = datetime.datetime.now(pytz.timezone('Asia/Hong_Kong'))

# 计算当前周 周一到周日 日期
dates = []
weekdays = []

for i in range(0 - hk.weekday(), 9 - hk.weekday()):
    dates.append(hk + datetime.timedelta(days=i))

for x in range(7):
    weekdays.append(dates[x].strftime("%Y/%m/%d"))

print(weekdays)

# 小号箱子转移至大号
# 左边大号右边小号
Replace_Dict = [
    ['こ若若や', ['梨花雨落']],
    ['こ奉先や', ['快使用双节棍戳']]
]


def s_tranfer(name):
    for nl in Replace_Dict:
        for sn in nl[1]:
            if sn == name:
                name = nl[0]
            else:
                pass
    return name


def cvl(string):
    # # 删除消耗
    # step1 = re.sub("\s*\d+\s*\d+\s*\d+\s*$", "", line)
    # 删除帮众名后所有内容
    name = re.sub(r'\s*[\u4e00-\u9fa5]+\s*\d+\s*\d+\s*\d+\s*$', '', string)
    return name


# 删除DKP事件内的2018/07/08 19:09    	时间戳防止后续DKP提取error
def timestampdel(eventlist):
    deleted = []
    for event in eventlist:
        deleted.append(re.sub(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}\s*', '', event))
    return deleted


# 箱子发放计算 根据帮派情况自行调整
# 委任每70                 1个箱子 上限3个
# 醉侠和血战海河州都完成    1个箱子
# 帮派战场完成2场          3个箱子 否则为1个(单场) 0个(0场)
# 掠夺战一次               1个箱子
# 争锋战一个               2个箱子
def rewardcalc(member):
    defaultrw = 0
    # 委任
    if member.wr >= 210:
        defaultrw += 3
    else:
        defaultrw += (member.wr // 70)

    # 醉虾 血战海河
    if member.zx and member.jh:
        defaultrw += 1

    # 帮派战场
    # if member.zc >= 2:
    #    defaultrw += 3
    #else:
        # 1或0
        #defaultrw += member.zc
    defaultrw += member.zc

    # 掠夺
    defaultrw += member.ld

    # 争锋
    defaultrw += member.zf * 2

    if defaultrw >= 8:
        return 8
    else:
        return defaultrw


class SingleRecord:
    def __init__(self):
        self.id = ''  # ID
        self.wr = 0  # 委任数量
        self.zx = 0  # 周六醉侠
        self.jh = 0  # 血战海河
        self.zc = 0  # 帮派战场
        self.ld = 0  # 掠夺战
        self.zf = 0  # 争锋战
        self.zj = 0  # 资金
        self.ys = 0  # 玉石
        self.dkp = 0  # DKP
        self.xz = 0  # 箱子


# 保存帮派DKP详单至 BangPaiDKPList  [['余欢喜','20171201***','20171202***'],[***],[***]]
Temp = [[] for x in range(150)]
with open("BangPai_DKPModifyRecord.txt", 'r', encoding='utf-8') as DKPRecord:
    cot = 0
    for line in DKPRecord.readlines():
        if not line == '\n':
            # 对于DKP事件只保留当周
            if bool(re.search(r'\d{4}/\d{2}/\d{2} \d{2}:\d{2}\s*', line)):
                for d in weekdays:
                    if d in line:
                        Temp[cot].append(line.strip())
            # ID直接append
            else:
                Temp[cot].append(line.strip())
        else:
            cot = cot + 1
    print("帮派总人数：", cot)
# Temp[cot-1] 最后一人
BangPaiDKPList = Temp[:cot - 1]

# 帮派DKP详单简化版写入 只保留当前周的DKP信息
with open("SimDetails.txt", 'w', encoding='utf-8') as RecordSimple:
    for MemberRecord in BangPaiDKPList:
        # [0]为帮派成员ID [1:] 为事件信息
        RecordSimple.write(MemberRecord[0] + '\n')
        for x in MemberRecord[1:]:
            RecordSimple.write(str(x) + '\n')

# 简化为表格格式
TableData = []

for MemberRecord in BangPaiDKPList:
    newSingleRecord = SingleRecord()
    newRecord = ''.join(timestampdel(MemberRecord[1:]))

    newSingleRecord.id = MemberRecord[0]
    newSingleRecord.wr = sum(list(map(int, re.findall(r'(?<=帮派委任（)\d+', newRecord))))
    newSingleRecord.zx = newRecord.count('帮派醉侠')
    newSingleRecord.jh = newRecord.count('血战海河')
    newSingleRecord.zc = newRecord.count('帮派跨服战场')
    newSingleRecord.ld = newRecord.count('掠夺战')
    newSingleRecord.zf = newRecord.count('争锋战')
    newSingleRecord.zj = sum(list(map(int, re.findall(r'(?<=资金（)\d+', newRecord))))
    newSingleRecord.ys = sum(list(map(int, re.findall(r'(?<=玉石（)\d+', newRecord))))
    newSingleRecord.dkp = sum(list(map(int, re.findall(r'(?<=DKP为)\d+', newRecord))))
    newSingleRecord.xz = rewardcalc(newSingleRecord)

    TableData.append(newSingleRecord)

# 优先按箱子数量降序排列其次为委任
# 使数据在EXCEL内美观
TableData.sort(key=lambda member: (member.xz, member.wr), reverse=True)

ExcelTemplate = "ID\t委任\t醉侠\t血战\t战场\t掠夺\t争锋\t资金\t玉石\tDKP\t箱子"

with open("ExcelData.txt", 'w', encoding='utf-8') as Simp:
    Simp.write(ExcelTemplate + '\n')
    for ind in TableData:
        Simp.write(ind.id + '\t'
                   + str(ind.wr) + '\t'
                   + str(ind.zx) + '\t'
                   + str(ind.jh) + '\t'
                   + str(ind.zc) + '\t'
                   + str(ind.ld) + '\t'
                   + str(ind.zf) + '\t'
                   + str(ind.zj) + '\t'
                   + str(ind.ys) + '\t'
                   + str(ind.dkp) + '\t'
                   + str(ind.xz) + '\n')

# 激励文件部署
# 奖励发放 Template 2018/07/30 fix 少了template导致第一位无法被正常读取
JiliTemplate = "发放激励\n领取情况\t帮众\t等级\t职位\t剩余PVP-DKP\t修改PVP-DKP\t剩余PVE-DKP\t修改PVE-DKP\t发放数量\n"

with open(GLFile, 'w', encoding='utf-8') as init_gf:
    init_gf.write(JiliTemplate)

for MemberInTable in TableData:
    if MemberInTable.xz == 0:
        pass
    else:
        # 金箱子
        with open(GLFile, 'a', encoding='utf-8') as JLF:
            if MemberInTable.xz == 8:
                JLF.write("8/8\t" + MemberInTable.id + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
            elif MemberInTable.xz == 7:
                JLF.write("7/8\t" + MemberInTable.id + "\t95\tX\t0\t0\t0\t0\t7" + "\n")
            elif MemberInTable.xz == 6:
                JLF.write("6/8\t" + MemberInTable.id + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
            elif MemberInTable.xz == 5:
                JLF.write("5/8\t" + MemberInTable.id + "\t95\tX\t0\t0\t0\t0\t5" + "\n")
            elif MemberInTable.xz == 4:
                JLF.write("4/8\t" + MemberInTable.id + "\t95\tX\t0\t0\t0\t0\t4" + "\n")
            elif MemberInTable.xz == 3:
                JLF.write("3/8\t" + MemberInTable.id + "\t95\tX\t0\t0\t0\t0\t3" + "\n")
            elif MemberInTable.xz == 2:
                JLF.write("2/8\t" + MemberInTable.id + "\t95\tX\t0\t0\t0\t0\t2" + "\n")
            elif MemberInTable.xz == 1:
                JLF.write("1/8\t" + MemberInTable.id + "\t95\tX\t0\t0\t0\t0\t1" + "\n")
            else:
                pass
