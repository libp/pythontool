# -*- coding: utf-8 -*-
import csv
import time
import datetime


# csv总结：
#     1、writerow函数执行时，for循环会直接终止掉，如果需要写入，应该把所有需要写入的行准备好，再批量写入
#     2、with open as 支持同时打开多个文件
#     3、如果想相处指定的行，可以使用enumerate方法，通过index判断
#     4、读取指定列  print ([row[0] for row in reader])
#     5、创建csv有元组形式和字典形式，下面使用的是元组形式
#     6、reader是创建一个迭代器，通过函数进行循环调用时，要注意重新初始化
#     7、next(vmreader)   # 如果不需要输出标题，可以next()方法，把迭代器往下挪

def dealcsv():
    """读取虚拟机csv
    """
    newvm = []
    with open(vmpath,'r',newline='') as vmfile:
        vmreader = csv.reader(vmfile)
        next(vmreader)   
        for index,row in enumerate(vmreader):
            try:
                hostname = row[2]
                cpuMax,cpuAvag= searchvm(cpupath,hostname)
                memMax,memAvag = searchvm(memorypath,hostname)
                row[16],row[17],row[18],row[19] = cpuMax,cpuAvag,memMax,memAvag
                suggestion = analyse(row)
                row[20] = suggestion
                newvm.append(row)
            except Exception as e:
                print(str(index) + " row data is exception:" +"please check your csv file")
                print(e)

                break            
    createCsv(newvm)
    

def analyse(row):
    # row = ['WGTRU01_R2', 'GTYYR1DMZ681', 'spszh04wgp02', 'active', 'W2121208', '4', '16', '20', 'UPEL1.0.5', '深圳大湾区智慧出行前置平台-SZHCX', '无感生产环境',
    #  '19.92.9.14', '20.92.9.14', '2405:78c0:20:ec09::e',
    #  '2405:78c0:22:ec09::e', '2021/10/26 2:59', '0.06939999759197235', '0.011608219194676745', '0.9577000141143799', '0.954690047718109', '']
    if(notfindhost(row[16])):
        return "notfindhost"
    if(createtimeless42(row[15])):
        return "createtimeless42"
    if(cpuMaxless005memMaxless010(row[16],row[18])):
        return "cpuMaxless005memMaxless010"
    if(cpuMaxless005memMaxless020(row[16],row[18])):
        return "cpuMaxless005memMaxless020"
    if(cpuMaxless010memMaxless020(row[16],row[18])):
        return "cpuMaxless010memMaxless020"

def judge(row,rule,suggestion):
    """
    #根据cpuMax,cpuAvag,memMax,memAvag 输出建议
    """
    rule =  {'cpuMax': 0.10, 'cpuAvag': 0, 'memMax': 0.20,'memAvag': 0}
    if(float(rule[16]) < rule.cpuMax and float(rule[18]) < rule.memMax):
        return True
    else:
        return False

def cpuMaxless010memMaxless020(cpuMax,memMax):
    """
    #资源消耗低：cpuMax<0.1 && memMax<0.2，建议缩容到1C4G
    """
    if(float(cpuMax) < 0.10 and float(memMax) < 0.20):
        return True
    else:
        return False

def cpuMaxless005memMaxless020(cpuMax,memMax):
    """
    #资源消耗较低：cpuMax<0.1 && memMax<0.2，建议缩容到1C4G
    """
    if(float(cpuMax) < 0.05 and float(memMax) < 0.20):
        return True
    else:
        return False

def cpuMaxless005memMaxless010(cpuMax,memMax):
    """
    #资源消耗极低：cpuMax<0.05 && memMax<0.1，建议缩容到1C2G
    """
    if(float(cpuMax) < 0.05 and float(memMax) < 0.10):
        return True
    else:
        return False

def createtimeless42(created_at):
    """
    #新建服务器：从创建至今，不超过六周（42天），此类服务器暂不做调整建议
    """
    # 先转换为时间数组,然后转换为其他格式
    created_at = time.strptime(created_at, "%Y/%m/%d %H:%M")
    created_at = int(time.mktime(created_at))
    current_at = int(time.mktime(time.localtime()))
    result = (current_at - created_at) // 60 // 60 // 24
    if(result < 42):
        return True
    else:
        return False

def notfindhost(cpuMax):
    """
    #非目标服务器
    """
    if(cpuMax=="notfindhost"):
        return True
    else:
        return False

def createCsv(newvm):
    """
    #创建带时间戳的csv文件
    """
    resultfilepath = vmpath.split('.')[0] + str(time.time()) + '.csv'

    headers = ["zone","availability_zone","hostname","vm_state","phyical_host","vcpus","memory_gb","root_gb","Image",
    "business","Sub-System","ServIPv4","MgmIPv4","ServIPv6","MgmIPv6","created_at","month_cpu_max","month_cpu_avag",
    "month_memory_max","month_memory_avag","suggestion"]

    with open(resultfilepath,'w',newline='') as vmfile:
        vmwriter = csv.writer(vmfile,dialect='excel')
        vmwriter.writerow(headers)
        vmwriter.writerows(newvm)

def searchvm(path:str,hostname:str):
    """读取csv"""
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if hostname in row:
                return row[7],row[9]
        return "notfindhost","notfindhost"


#文件位置
vmpath = r"C:\Users\peng\Desktop\report\vm.csv"
cpupath = r"C:\Users\peng\Desktop\report\cpu.csv"
memorypath = r"C:\Users\peng\Desktop\report\memory.csv"

if __name__ == "__main__":
    dealcsv()
    # analyse()






