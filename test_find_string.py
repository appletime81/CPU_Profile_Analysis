import re

text1 = 'gnb_du_1           | 2605'
text2 = 'gnb_cu_1           | [17/02/2022 10:09:16.573696][SCTP][ERR][ngp_inet.cpp:208]SCTP Socket Bind Failed'



with open('MobaXterm_10.255.174.40_20220217_181140.txt', 'r') as fp:
    lines = fp.readlines()

print(len(text1.split(" ")))

for line in lines:
    if re.findall(r'gnb_du_1           \| \d+', line) and len(line.split(" ")) == 13:

        print(line)

