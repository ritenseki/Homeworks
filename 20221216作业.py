'''
为监控学校食堂的菜品质量，学校决定监控食堂每天的剩饭剩菜垃圾的产生量，以便从侧面了解学生对菜品的喜爱方向。
请你帮助负责数据统计的老师编写一个程序，根据某月学生们在校吃饭的天数n，和这n天的垃圾处理重量，统计出其中垃圾处理量最少的重量是多少？（要求用循环结构解决该问题）。
输入输出样例：
学生在校吃饭的天数是：3
每天剩饭菜垃圾重量分别是：345
每天剩饭菜垃圾重量分别是：231.6
每天剩饭菜垃圾重量分别是：543
垃圾重量最少的是：231.6
'''
list = []
numOfDays = int(input("学生在校吃饭的天数是："))
for numCount in range(1,numOfDays+1,1):
    list.append(float(input("每天剩饭菜垃圾重量分别是：")))
for i in range(1,len(list)):
    for j in range(0,len(list)-i):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("垃圾重量最少的是："+str(list[0]))