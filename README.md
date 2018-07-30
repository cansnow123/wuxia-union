## 天涯明月刀 DKP数据统计脚本

### 简介
从一开始的EXCEL和宏处理到现在使用Python完成几乎全部任务
这个过程还是比较有趣的
仅用该项目来记录游戏历史及点点滴滴

### 提要

**pytz**限定区域为**Asia/Hong_Kong**是因为人在澳洲，时差会导致当周日期无法和游戏内时间一致漏统数据

### 使用方法

**RewardDelivery**文件夹内的**BangPaiReward.py**和**UnionReward.py**  

分别用于帮派激励发放和联盟激励发放  

**BangPaiReward.py**

在帮派管理界面导出帮派**DKP记录**以及帮派**DKP修改详单**  
权限要求：帮主|副帮|军师  
帮派DKP修改详单导出需要2分钟左右(帮派141人)  
帮派->帮派管理->DKP->导出列表  
![BangPaiDKP](https://raw.githubusercontent.com/heiybb/wuxia-union/master/demopic/BangPaiDKP.png)



**UnionReward.py**

在联盟管理界面导出联盟**DKP记录**以及联盟**DKP修改详单**  
权限要求：联盟龙首|DKP管理员  
联盟DKP修改详单导出需要9分钟左右(联盟550人)  
联盟->联盟管理->DKP->导出列表  
![UnionDKP](https://raw.githubusercontent.com/heiybb/wuxia-union/master/demopic/UnionDKP.png)



**激励发放**

将天刀安装文件夹**DKPData**内的**BangPai_DKP.txt**和**BangPai_DKPFaFangJiLi.txt**复制到与**BangPaiReward.py**/**UnionReward.py**同一目录下  
运行**BangPaiReward.py**或**UnionReward.py**即可  

会生成**BangPai_DKPFaFangJiLi.txt**及**BangPai_DKPFaFangJiLi.txts**分别用于金银箱子发放(相关规则需再文件内自行修改)  

帮派->帮派管理->激励仓库->点击金/银箱子->导入列表->导入列表  
![Reward](https://raw.githubusercontent.com/heiybb/wuxia-union/master/demopic/Reward.png)



以下两文件生成用于DEBUG和查询使用  

**ExcelData.txt**
该文件储存了当前周所有帮派/联盟成员的DKP获取记录 数据格式 分隔符为\t 可直接复制进EXCEL进行额外修改  
数据已排序 默认按照应发金箱子数量降序 其次为委任数量  
![ExcelData](https://raw.githubusercontent.com/heiybb/wuxia-union/master/demopic/ExcelData.png)



**SimDetails.txt**
该文件储存了当前周所有帮派/联盟成员的DKP获取记录 文本格式 方便在DKP事件记录查询  
![SimDetails](https://raw.githubusercontent.com/heiybb/wuxia-union/master/demopic/SimDetails.png)



### LICENSE

Copyright (C) 2016 Heiybb <root@chr.moe>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
