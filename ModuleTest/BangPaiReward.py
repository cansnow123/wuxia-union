import datetime
import os
import pytz
import re
import shutil

import xlsxwriter

GLFile = "BangPai_DKPFaFangJiLi.txt"
SLFile = "BangPai_DKPFaFangJiLi.txts"

# Past File Clean
if os.path.isfile(GLFile):
    os.system("del BangPai_DKPFaFangJiLi.txt")
if os.path.isfile(SLFile):
    os.system("del BangPai_DKPFaFangJiLi.txts")

tz = pytz.timezone('Asia/Hong_Kong')
hk = datetime.datetime.now(tz)

dates = []
for i in range(0 - hk.weekday(), 9 - hk.weekday()):
    dates.append(hk + datetime.timedelta(days=i))
weekdays = []
for x in range(7):
    weekdays.append(dates[x].strftime("%Y/%m/%d"))
print(weekdays)

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


def cvl(line):
    # # 删除消耗
    # step1 = re.sub("\s*\d+\s*\d+\s*\d+\s*$", "", line)
    # 删除帮众名后所有内容
    name = re.sub("\s*[\u4e00-\u9fa5]+\s*\d+\s*\d+\s*\d+\s*$", "", line)
    return name


def eventsimp(event):
    simevent = re.sub("的DKP为\d+", "", event)
    return simevent


# 箱子发放计算 根据帮派情况自行调整
def rewardcalc(member):
    defaultrw = 0
    # 委任
    if member.wr > 21:
        defaultrw += 3
    else:
        defaultrw += (member.wr // 7)

    # 醉虾 血战海河
    if member.zx and member.jh:
        defaultrw += 1

    # 帮派战场
    if member.zc == 2:
        defaultrw += 3
    else:
        # 1或0
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
        self.xz = 0  # 箱子


# 保存帮派名单至 BangPaiNameList
BangPaiNameList = []
with open("BangPai_DKP.txt", 'r', encoding='utf-8') as LMD:
    for l in LMD.readlines()[3:]:
        BangPaiNameList.append(cvl(l))

# 保存帮派DKP详单至 BangPaiDKPList  [['余欢喜','20171201***','20171202***'],[***],[***]]
Temp = [[] for x in range(150)]
with open("BangPai_DKPModifyRecord.txt", 'r', encoding='utf-8') as DKPRecord:
    cot = 0
    for l in DKPRecord.readlines():
        if not l == '\n':
            Temp[cot].append(eventsimp(l.strip()))
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
            for d in weekdays:
                if d in x:
                    RecordSimple.write(eventsimp(str(x)) + '\n')

# 简化为表格格式
TableData = []

for MemberRecord in BangPaiDKPList:
    newSingleRecord = SingleRecord()
    newSingleRecord.id = MemberRecord[0]
    newRecord = ''

    for x in MemberRecord[1:]:
        for d in weekdays:
            if d in x:
                newRecord += x
                # print(newRecord)
    newSingleRecord.wr = newRecord.count('帮派委任')
    newSingleRecord.zx = newRecord.count('帮派醉侠')
    newSingleRecord.jh = newRecord.count('血战海河')
    newSingleRecord.zc = newRecord.count('帮派跨服战场')
    newSingleRecord.ld = newRecord.count('掠夺战')
    newSingleRecord.zf = newRecord.count('争锋战')
    newSingleRecord.xz = rewardcalc(newSingleRecord)
    TableData.append(newSingleRecord)

# 优先按箱子数量降序排列其次为委任
# 使数据在EXCEL内美观
TableData.sort(key=lambda member: (member.xz, member.wr), reverse=True)

with open("ExcelData.txt", 'w', encoding='utf-8') as Simp:
    Simp.write("ID\t委任*10\t醉侠\t血战\t战场\t掠夺\t争锋\t箱子\n")
    for ind in TableData:
        Simp.write(str(ind.id) + '\t'
                   + str(ind.wr) + '\t'
                   + str(ind.zx) + '\t'
                   + str(ind.jh) + '\t'
                   + str(ind.zc) + '\t'
                   + str(ind.ld) + '\t'
                   + str(ind.zf) + '\t'
                   + str(ind.xz) + '\n')

# 激励文件部署
# 奖励发放 Template 2018/07/30 fix 少了template导致第一位无法被正常读取
Template = "发放激励\n领取情况\t帮众\t等级\t职位\t剩余PVP-DKP\t修改PVP-DKP\t剩余PVE-DKP\t修改PVE-DKP\t发放数量\n"

with open(GLFile, 'w', encoding='utf-8') as init_gf:
    init_gf.write(Template)
with open(SLFile, 'w', encoding='utf-8') as init_sf:
    init_sf.write(Template)

with open("ExcelData.txt", 'r', encoding='utf-8') as Simpw:
    for X in Simpw.readlines()[1:]:
        if int(X.split()[7]) == 0:
            pass
        else:
            # 银箱子
            with open(SLFile, 'a', encoding='utf-8') as SLF:
                if int(X.split()[7]) == 8:
                    SLF.write("8/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
                elif int(X.split()[7]) == 7:
                    SLF.write("8/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
                elif int(X.split()[7]) == 6:
                    SLF.write("6/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
                elif int(X.split()[7]) == 5:
                    SLF.write("5/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t5" + "\n")
                elif int(X.split()[7]) == 4:
                    SLF.write("4/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t4" + "\n")
                elif int(X.split()[7]) == 3:
                    SLF.write("3/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t3" + "\n")
                elif int(X.split()[7]) == 2:
                    SLF.write("2/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t2" + "\n")
                else:
                    pass
            # 金箱子
            with open(GLFile, 'a', encoding='utf-8') as JLF:
                if int(X.split()[7]) == 8:
                    JLF.write("8/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
                elif int(X.split()[7]) == 7:
                    JLF.write("7/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t7" + "\n")
                elif int(X.split()[7]) == 6:
                    JLF.write("6/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
                elif int(X.split()[7]) == 5:
                    JLF.write("5/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t5" + "\n")
                elif int(X.split()[7]) == 4:
                    JLF.write("4/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t4" + "\n")
                elif int(X.split()[7]) == 3:
                    JLF.write("3/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t3" + "\n")
                elif int(X.split()[7]) == 2:
                    JLF.write("2/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t2" + "\n")
                elif int(X.split()[7]) == 1:
                    JLF.write("1/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t1" + "\n")
                else:
                    pass

# 根据帮派情况自行调整 可注释或删除
pre_list = []
zm = 1

with open("ExcelData.txt", 'r', encoding='utf-8') as Simp:
    for x in Simp.readlines():
        pre_list.append(x.split('\t'))
        if "余欢喜" in x.split('\t'):
            zm = 0

if zm:
    workbook = xlsxwriter.Workbook('逐梦.xlsx')
    worksheet = workbook.add_worksheet()
    for n in range(len(pre_list)):
        for m in range(len(pre_list[n])):
            if pre_list[n][m].strip().isdigit():
                worksheet.write_memberber(n, m, int(pre_list[n][m].strip()))
            else:
                worksheet.write(n, m, pre_list[n][m])

    workbook.close()

    xlsx_file_name = re.sub(r'/', '', str('逐梦' + weekdays[6] + '.xlsx'))
    print(xlsx_file_name)

    shutil.move('逐梦.xlsx', xlsx_file_name)
    shutil.move(xlsx_file_name, 'D:\Git-Source\wuxia-union\天雪初晴-双生逐梦-XLSX')
    os.system("explorer D:\Git-Source\wuxia-union\天雪初晴-双生逐梦-XLSX")
else:
    shutil.copyfile('BangPai_DKPFaFangJiLi.txt', 'D:\Wuxia\天涯明月刀\DKPData\BangPai_DKPFaFangJiLi.txt')
    shutil.copyfile('BangPai_DKPFaFangJiLi.txts', 'D:\Wuxia\天涯明月刀\DKPData\BangPai_DKPFaFangJiLi.txts')
