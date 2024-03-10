import time, os
from time import sleep
from shutil import copytree
from psutil import disk_partitions
import ctypes
h = ctypes.windll.LoadLibrary('C:\\Windows\\System32\\user32.dll')

def copy_u_to_computer():
    a = True
    while a:
        sleep(1)
        for item in disk_partitions():
            if 'removable' in item.opts:
                driver, opts = item.device, item.opts
                print('发现U盘', driver)
                if h.MessageBoxW(0, '检测到u盘插入\n是否开始备份', '提示', 1) == 2:
                    break
                a = False
                now_time = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
                now_time1 = now_time.replace(':', '-')
                print(now_time1)
                path = 'E:\\u盘备份\\' + str(now_time1)
                okin = time.time()
                copytree(driver, path)
                print('复制完毕')
                h.MessageBoxW(0, '备份结束\n用时总计:' + str(int(time.time() - okin)) + '秒', '提示', 0)
                break
            else:
                print('没发现可移动优盘')
        a = False


qu_num = len(disk_partitions())
print(qu_num)
while True:
    if len(disk_partitions()) == qu_num:
        print('驱动器个数未改变')
        sleep(3)
    else:
        print('驱动器个数发生改变,准备拷贝优盘的内容')
        qu_num = len(disk_partitions())
        print(qu_num)
        copy_u_to_computer()