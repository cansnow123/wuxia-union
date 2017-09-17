import datetime

today = datetime.date.today()
dates = []
for i in range(0 - today.weekday(), 9 - today.weekday()):
    dates.append(today + datetime.timedelta(days=i))
weekdays = []
for x in range(7):
    weekdays.append(dates[x].strftime("%Y/%m/%d"))
print("本周日期：", weekdays)


class ItemRecord:
    def __init__(self):
        self.id = ''  # ID
        self.wr = 0  # 委任
        self.zx = 0  # 醉虾
        self.jh = 0  # 血战海河
        self.zc = 0  # 帮派战场
        self.ld = 0  # 掠夺
        self.zf = 0  # 争锋


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

# 联盟DKP记录单周简化版详单
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
    newItemRecord.id = preid[0]
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

with open("Simplified.txt", 'w', encoding='utf-8') as Simp:
    Simp.write("ID\t帮派委任\t帮派醉侠\t血战海河\t帮派战场\t掠夺战\t争锋战\n")
    for ind in ItemEasy:
        Simp.write(str(ind.id.split()[0])+'\t'+str(ind.wr)+'\t'+str(ind.zx)+'\t'+str(ind.jh)+'\t'+str(ind.zc)+'\t'+str(ind.ld)+'\t'+str(ind.zf)+'\n')