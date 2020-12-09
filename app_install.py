import os
from tools import adb_install_apk, get_devices_udid, logger, export_pc_apk, export_phone_apk
from settings import tasks, need_packages

# 将特殊的两个app ，放入制定文件
for i in tasks:
    device = i.get('serialno')
    os.popen("adb connect {device}".format(device=device))

    # 安装Frida-server
    # s = export_pc_apk(device, "/data/local/tmp/", "frida-server-arm64")
    s1 = export_pc_apk(device, "/sdcard/", "com.hipu.yidian.apk")
    s2 = export_pc_apk(device, "/sdcard/", "com.netease.newsreader.apk")
    continue
