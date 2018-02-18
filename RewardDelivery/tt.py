# import re
#
# a  = '加密:无+BSSID1:0e:69:6c;ae:10:9a+信号:85%+无线电类型;802.11ac*频道:165+)基本速率(Mbes):612244其他速率(Mbps):9 18 3648 54+:0e:69:6c;d9;0e:17+BSSID 2信号:41%无线电类型:802.11n+频道:6+基本速率(Mbes);114其他速率(Mbes):69121824364854+:0e:69:6C:d9:1f:93+BSSID 3信号:73%+无线电类型:802.11ne频道:114基本速率(Mbps):11+其他速率(Mbes):69121824364854+: 0e:69:6c;ae:10:99BSSID 4信号:99%-无线电类型:802.11n+频道:14基本速率(Mbes):114其他速率(Mbps):69121824364854+1BSSID 5: 0e:69:6C :d9 :1f:94+信号;31%无线电类型:802.11ace频道:153+基本速率(Mbps):612244其他速率(Mbps):918364854+BSSID 6: 0e:69:6C:ae:10:a1.'
#
#
# b = re.match('^\s*([0-9a-fA-F]{2,2}:){5,5}[0-9a-fA-F]{2,2}\s*$', a)
#
# print(b)
import re


def cvl(line):
    # 删除消耗
    step1 = re.sub("\s*\d+\s*\d+\s*\d+\s*$", "", line)
    # 删除帮众名空白至帮派间空白()包括职位
    step2 = re.sub("\s*(龙首|长老|副龙首|无职位|特需官)\s*", "\t", step1)
    return step2


UnionNameList = []
with open("LianMeng_DKP.txt", 'r', encoding='utf-8') as LMD:
    for l in LMD.readlines()[3:]:
        UnionNameList.append(cvl(l).split('\t'))

print(UnionNameList)