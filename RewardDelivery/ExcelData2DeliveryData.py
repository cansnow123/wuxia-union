import datetime
import os
import pytz
import time
import re
import shutil
import xlsxwriter

tz = pytz.timezone('Asia/Hong_Kong')
hk = datetime.datetime.now(tz)

dates = []
for i in range(0 - hk.weekday(), 9 - hk.weekday()):
    dates.append(hk + datetime.timedelta(days=i))
weekdays = []
for x in range(7):
    weekdays.append(dates[x].strftime("%Y/%m/%d"))
print(weekdays)

BaseDKP = 15

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
    # 删除消耗
    step1 = re.sub("\s*\d+\s*\d+\s*\d+\s*$", "", line)
    # 删除帮众名空白至帮派间空白()包括职位
    step2 = re.sub("\s*(龙首|长老|副龙首|无职位|特需官)\s*", "\t", step1)
    return step2


def event2dkp(num):
    defaultrw = 0
    # 委任
    if num.wr > 21:
        defaultrw += 3 * BaseDKP
    else:
        defaultrw += (num.wr // 7) * BaseDKP
    if num.ga == '万星楼':
        if num.zx and num.jh:
            defaultrw += BaseDKP
        else:
            pass
    else:
        # 醉虾
        defaultrw += num.zx * BaseDKP
        # 血战海河
        defaultrw += num.jh * BaseDKP
    # 帮派战场
    defaultrw += num.zc * BaseDKP
    # 掠夺
    defaultrw += num.ld * BaseDKP
    # 争锋
    defaultrw += num.zf * BaseDKP * 2
    return defaultrw


def rw(dkp):
    if dkp == 0:
        return 0
    elif dkp >= 8 * BaseDKP:
        return 8
    else:
        return dkp//BaseDKP


class ItemRecord:
    def __init__(self):
        self.id = ''  # ID
        self.ga = ''  # 帮派
        self.wr = 0  # 委任
        self.zx = 0  # 醉虾
        self.jh = 0  # 血战海河
        self.zc = 0  # 帮派战场
        self.ld = 0  # 掠夺
        self.zf = 0  # 争锋


UnionNameList = []
with open("LianMeng_DKP.txt", 'r', encoding='utf-8') as LMD:
    for l in LMD.readlines()[3:]:
        UnionNameList.append(cvl(l).split('\t'))

# 格式 ID 帮派
UnionNameDict = {UnionNameList[i][0]: UnionNameList[i][1] for i in range(len(UnionNameList))}
# print(UnionNameDict)
Temp = [[] for x in range(600)]
with open("LianMeng_DKPModifyRecord.txt", 'r', encoding='utf-8') as DKPRecord:
    cot = 0
    for l in DKPRecord.readlines():
        if not l == '\n':
            Temp[cot].append(l)
        else:
            cot = cot + 1
    print("联盟总人数：", cot)
# print(Temp[cot-1]) 最后一人
ItemList = Temp[:cot - 1]

# 联盟DKP记录单周简化版详单写入
with open("SimDetails.txt", 'w', encoding='utf-8') as RecordSimple:
    for preid in ItemList:
        RecordSimple.write(preid[0])
        for x in preid[1:]:
            for d in weekdays:
                if d in x:
                    RecordSimple.write(str(x))

ItemEasy = []
for preid in ItemList:
    newItemRecord = ItemRecord()
    newRecord = ''
    newItemRecord.id = preid[0].split()[0]
    try:
        newItemRecord.ga = UnionNameDict[newItemRecord.id]
    except KeyError:
        print("KeyError: Can't find the key item:" + newItemRecord.id)
        time.sleep(5)
    else:
        pass
    # print(newItemRecord.ga)
    for x in preid[1:]:
        for d in weekdays:
            if d in x:
                newRecord += str(x.split())
                # print(newRecord)
                newItemRecord.wr = newRecord.count('帮派委任')
                newItemRecord.zx = newRecord.count('帮派醉侠')
                newItemRecord.jh = newRecord.count('血战海河')
                newItemRecord.zc = newRecord.count('帮派跨服战场')
                newItemRecord.ld = newRecord.count('掠夺战')
                newItemRecord.zf = newRecord.count('争锋战')
    ItemEasy.append(newItemRecord)

with open("ExcelData.txt", 'w', encoding='utf-8') as Simp:
    Simp.write("ID\t帮派\t委任*10\t醉侠\t血战\t战场\t掠夺\t争锋\tDKP\t箱子\n")
    for ind in ItemEasy:
        Simp.write(str(ind.id) + '\t' + str(ind.ga) + '\t' + str(ind.wr) + '\t' + str(ind.zx) + '\t'
                   + str(ind.jh) + '\t' + str(ind.zc) + '\t' + str(ind.ld) + '\t' + str(ind.zf) + '\t'
                   + str(event2dkp(ind)) + '\t' + str(rw(event2dkp(ind))) + '\n')


# 奖励发放 Template
Template = "发放激励\n领取情况\t帮众\t等级\t职位\t剩余PVP-DKP\t修改PVP-DKP\t剩余PVE-DKP\t修改PVE-DKP\t发放数量\n"
GLFile = "BangPai_DKPFaFangJiLi.txt"
SLFile = "BangPai_DKPFaFangJiLi.txt银"

with open(GLFile, 'w', encoding='utf-8') as init_gf:
    init_gf.write(Template)
with open(SLFile, 'w', encoding='utf-8') as init_sf:
    init_sf.write(Template)

# 激励文件部署
with open("ExcelData.txt", 'r', encoding='utf-8') as Simpw:
    for X in Simpw.readlines()[1:]:
            if int(X.split()[9]) == 0:
                pass
            else:
                # 银箱子
                with open(SLFile, 'a', encoding='utf-8') as SLF:
                    if int(X.split()[9]) == 8:
                        SLF.write("8/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
                    elif int(X.split()[9]) == 7:
                        SLF.write("8/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
                    elif int(X.split()[9]) == 6:
                        SLF.write("8/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
                    elif int(X.split()[9]) == 5:
                        SLF.write("8/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
                    elif int(X.split()[9]) == 4:
                        SLF.write("6/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
                    elif int(X.split()[9]) == 3:
                        SLF.write("6/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
                    elif int(X.split()[9]) == 2:
                        SLF.write("4/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t4" + "\n")
                    else:
                        pass
                # 金箱子
                with open(GLFile, 'a', encoding='utf-8') as JLF:
                    if int(X.split()[9]) == 8:
                        JLF.write("8/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t8" + "\n")
                    elif int(X.split()[9]) == 7:
                        JLF.write("7/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t7" + "\n")
                    elif int(X.split()[9]) == 6:
                        JLF.write("6/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t6" + "\n")
                    elif int(X.split()[9]) == 5:
                        JLF.write("5/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t5" + "\n")
                    elif int(X.split()[9]) == 4:
                        JLF.write("4/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t4" + "\n")
                    elif int(X.split()[9]) == 3:
                        JLF.write("3/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t3" + "\n")
                    elif int(X.split()[9]) == 2:
                        JLF.write("2/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t2" + "\n")
                    elif int(X.split()[9]) == 1:
                        JLF.write("1/8\t" + X.split()[0] + "\t95\tX\t0\t0\t0\t0\t1" + "\n")
                    else:
                        pass

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

worksheet.autofilter(0, 1, 599, 1)
worksheet.filter_column_list('B', ['双生逐梦'])
workbook.close()
xlsx_file_name = re.sub(r'/', '', str('逐梦' + weekdays[6] + '.xlsx'))
print(xlsx_file_name)

shutil.move('逐梦.xlsx', xlsx_file_name)
shutil.move(xlsx_file_name, 'D:\Git-Source\wuxia-union\天雪初晴-双生逐梦-XLSX')
os.system("explorer D:\Git-Source\wuxia-union\天雪初晴-双生逐梦-XLSX")

shutil.copyfile('BangPai_DKPFaFangJiLi.txt', 'D:\Wuxia\天涯明月刀\DKPData\BangPai_DKPFaFangJiLi.txt')
shutil.copyfile('BangPai_DKPFaFangJiLi.txt银', 'D:\Wuxia\天涯明月刀\DKPData\BangPai_DKPFaFangJiLi.txt银')
os.system("explorer D:\Wuxia\天涯明月刀\DKPData")

