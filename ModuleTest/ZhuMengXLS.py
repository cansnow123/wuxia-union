import datetime
import os
import pytz
import time
import re
import shutil
import xlsxwriter

BaseDKP = 15

tz = pytz.timezone('Asia/Hong_Kong')
hk = datetime.datetime.now(tz)

dates = []
for i in range(0 - hk.weekday(), 9 - hk.weekday()):
    dates.append(hk + datetime.timedelta(days=i))
weekdays = []
for x in range(7):
    weekdays.append(dates[x].strftime("%Y/%m/%d"))
print(weekdays)


def event2dkp(num):
    defaultrw = 0
    # 委任
    if num.wr > 21:
        defaultrw += 3 * BaseDKP
    else:
        defaultrw += (num.wr // 7) * BaseDKP

    if num.zx and num.jh:
        defaultrw += BaseDKP
    else:
        # 醉虾
        defaultrw += num.zx * BaseDKP
        # 血战海河
        defaultrw += num.jh * BaseDKP

    # 帮派战场
    if num.zc == 2:
        defaultrw += num.zc * BaseDKP * 3
    else:
        defaultrw += num.zc * BaseDKP

    # 掠夺
    defaultrw += num.ld * BaseDKP

    # 争锋
    defaultrw += num.zf * BaseDKP * 2
    return defaultrw


def reward(dkp):
    if dkp == 0:
        return 0
    elif dkp >= 8 * BaseDKP:
        return 8
    else:
        return dkp // BaseDKP


def cvl(line):
    # # 删除消耗
    # step1 = re.sub("\s*\d+\s*\d+\s*\d+\s*$", "", line)
    # 删除帮众名后所有内容
    name = re.sub("\s*[\u4e00-\u9fa5]+\s*\d+\s*\d+\s*\d+\s*$", "", line)
    return name


def eventsimp(event):
    simevent = re.sub("的DKP为\d+", "", event)
    return simevent


class SingleRecord:
    def __init__(self):
        self.id = ''  # ID
        self.wr = 0  # 委任
        self.zx = 0  # 醉虾
        self.jh = 0  # 血战海河
        self.zc = 0  # 帮派战场
        self.ld = 0  # 掠夺
        self.zf = 0  # 争锋


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
    TableData.append(newSingleRecord)

with open("ExcelData.txt", 'w', encoding='utf-8') as Simp:
    Simp.write("ID\t委任*10\t醉侠\t血战\t战场\t掠夺\t争锋\tDKP\t箱子\n")
    for ind in TableData:
        Simp.write(str(ind.id) + '\t' + str(ind.wr) + '\t' + str(ind.zx) + '\t'
                   + str(ind.jh) + '\t' + str(ind.zc) + '\t' + str(ind.ld) + '\t' + str(ind.zf) + '\t'
                   + str(event2dkp(ind)) + '\t' + str(reward(event2dkp(ind))) + '\n')

# 逐梦XLSX文件部署
pre_list = []

with open("ExcelData.txt", 'r', encoding='utf-8') as Simp:
    for x in Simp.readlines():
        pre_list.append(x.split('\t'))

# print(pre_list)
workbook = xlsxwriter.Workbook('逐梦.xlsx')
worksheet = workbook.add_worksheet()
ff = workbook.add_format()
ff.set_center_across()
for n in range(len(pre_list)):
    for m in range(len(pre_list[n])):
        if pre_list[n][m].strip().isdigit():
            worksheet.write_number(n, m, int(pre_list[n][m].strip()), ff)
        else:
            worksheet.write(n, m, pre_list[n][m])

workbook.close()
xlsx_file_name = re.sub(r'/', '', str('逐梦' + weekdays[6] + '.xlsx'))
print(xlsx_file_name)

shutil.move('逐梦.xlsx', xlsx_file_name)
shutil.move(xlsx_file_name, 'D:\Git-Source\wuxia-union\天雪初晴-双生逐梦-XLSX')
os.system("explorer D:\Git-Source\wuxia-union\天雪初晴-双生逐梦-XLSX")
