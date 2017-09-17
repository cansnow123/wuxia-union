#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
json_f = 'sum.json'


def process(json_str_line):
    s1 = re.sub("{\"result.*?records\":\[", "", json_str_line)
    s2 = re.sub("\],\"cur.*?hasNextPage\":0\}\}\}","",s1)
    s3 = re.sub("\"rightsBinStr\":\"000000000000000000000000000000000\",|\"imid\":null,\"corpsInfo\":null,\"subChannelId\":0,"
                "\"channelName\":null,|\"sid\":48309424,|\"passport\":null,\"email\":null,"
                "|\"roleCA1\":false,|\"sex\":\d,|,\"majiaUrl\":\"/images/\w*\/*\w*.gif\"", "", s2)
    s4 = re.sub(",\"rightsList\":\[\],\"rightsValue\":0,\"defaultRights\":false", "", s3)
    s5 = re.sub("}{", "},{", s4)
    return s5

with open(json_f, 'r+', encoding='utf-8') as J:
    st_line = J.read()
    a1 = process(st_line)

with open('S.json','w',encoding='utf-8') as K:
    K.write("["+a1.strip()+"]")
