"""
输入输出样例：
今日运回的垃圾桶数量是（个）：8
垃圾桶1的编号为：1
垃圾桶2的编号为：2
垃圾桶3的编号为：2
垃圾桶4的编号为：4
垃圾桶5的编号为：1
垃圾桶6的编号为：1
垃圾桶7的编号为：3
垃圾桶8的编号为：2
"""
print('瓶装类垃圾桶为1号，其他垃圾桶为2号，纸张回收垃圾桶为3号，有害垃圾桶为4号。')

binList = []
binNum = int(input('今日运回的垃圾桶数量是（个）：'))
tmp = 1
while(tmp != binNum+1):
    try:
        numering=int(input(f'垃圾桶{tmp}的编号为：'))
        if ([1,2,3,4].count(numering)<=0):
            raise ValueError 
    except ValueError:
        print('您输入的数字不代表任何一种垃圾桶的编号，请重新输入。')
    else:
        binList.append(numering)
        tmp += 1
harmfulTrash = 0
no = 0
while (no != binNum):
    while (binList[no] == 4):
        harmfulTrash += 1
        break
    no += 1

print(f"装有害垃圾的垃圾桶的数量为：{harmfulTrash}个")
