# !/usr/bin adb
import os
from loguru import logger
import time
import re
import sys

filter_devices = ['192.168.1.102:5555', '192.168.1.103:5555', '192.168.1.104:5555', '192.168.1.108:5555',
                  '192.168.1.110:5555', '192.168.1.112:5555', '192.168.1.114:5555', '192.168.1.116:5555',
                  '192.168.1.117:5555', '192.168.1.118:5555', '192.168.1.119:5555', '192.168.1.121:5555',
                  '192.168.1.130:5555','192.168.1.126:5555']

# need_packages = ["com.android.settings", "com.hipu.yidian", "com.jifen.qukan", "com.tencent.news",
#                  "com.sohu.newsclient", "com.sina.weibo", "com.sina.news", "com.ifeng.news2"]
need_packages = ["com.ss.android.article.news","com.UCMobile","com.tencent.reading","com.baidu.searchbox","com.ifeng.news2",
                 "com.netease.newsreader.activity","com.tencent.android.qqdownloader","com.android.chrome"]


need_packages = ["com.ss.android.ugc.aweme"]

# need_packages = ["com.android.settings"]

apks_path = "./apks/"

def reboot_phone(device):
    """
    重启手机
    :param device:
    :return:
    """
    cmd = 'adb -s {device} reboot'.format(device=device)
    return os.popen(cmd)

# 获取所有在线手机的序列号
def get_devices_udid():
    result = os.popen("adb devices")
    lines = result.readlines()
    lnew = lines[1:-1]
    udidlist = []
    for i in range(len(lnew)):
        udid = lnew[i].strip("\n").split("\t")[0]
        udidlist.append(udid)
    return list(set(udidlist).difference(set(filter_devices)))


def call_adb(cmd):
    values = os.popen(cmd).readlines()
    dev = values[0]
    return dev


# 获取手机系统版本号
def get_platforms_version():
    pv_list = []
    devices_udid = get_devices_udid()
    for i in devices_udid:
        cmd = "adb -s " + i + " shell getprop ro.build.version.release"
        pversion = call_adb(cmd).strip("\n")
        pv_list.append(pversion)
    return pv_list


# 获取手机的名字
def get_phonename():
    pname_list = []
    devices_udid = get_devices_udid()
    for i in devices_udid:
        cmd = "adb -s " + i + " shell getprop ro.product.model"
        pversion = call_adb(cmd).strip("\n")
        pname_list.append(pversion)
    return pname_list


# 获取手机安装的apk
def get_phone_apk(devices):
    cmd = "adb -s " + devices + " shell pm list package"
    apk_packages = get_apk(cmd)
    return apk_packages


def get_apk(cmd):
    values = os.popen(cmd).readlines()
    return values


# 根据要导出的app包名，查看APP安装路径
def get_phone_apk_path(devices, packages: list):
    path_list = []
    for package in packages:
        cmd = "adb -s " + devices + " shell pm path {}".format(package)
        get_paths = os.popen(cmd).readline()
        path_list.append(get_paths)
    return path_list

def show():  # <7>
    """
    刷新系统文件
    :return:
    """
    # print(text, end=' ')
    sys.stdout.flush()

# 将手机中的apk下拉到本地文件
def export_phone_apk(devices, app_path, pc_path):
    cmd = "adb -s " + devices + " pull {app_path} {pc_path}".format(app_path=app_path, pc_path=pc_path)
    print(cmd)
    res = os.popen(cmd)
    return res.readline()


# adb安装 apk
def adb_install_apk(devices, apk):
    cmd = "adb -s " + devices + " install {apk}".format(apk=apk)
    res = os.popen(cmd)
    return res.readline()

# 将手机中的apk上传到手机文件
def export_pc_apk(devices, app_path, pc_path):
    cmd = "adb -s " + devices + " push {pc_path} {app_path}".format(app_path=str(app_path), pc_path=str(pc_path))
    print(cmd)
    res = os.popen(cmd)
    return res.readline()


#
def re_sting_title(str):
    # str = re.sub("[$a-zA-Z|\!\%\[\]\,\。\?\'\"\@\.\*\&\、\:\;\$\\\|a-zA-Z$]", "", str)
    str = re.sub("[\!\%\[\]\,\。\?\'\"\@\*\&\、\:\;\$\\\\/]", "", str)
    return str

def start_app2(device, apk_name):
    """
    adb 自动化初始化打开手机apk，root权限
    :param device:
    :param apk_name:
    :return:
    """
    cmd = "adb -s {} shell su -c monkey -p {} 2".format(device, apk_name)
    return os.popen(cmd)

def adb_start_apk(device, apk_name, activity_name=""):
    """
    adb 自动化初始化打开手机apk
    :return:
    """

    result = os.popen("adb -s {device} shell am start {apk_name}/.{activity_name}".
                      format(device=device, apk_name=apk_name, activity_name=activity_name))
    return result
if __name__ == '__main__':
    online_phone = get_devices_udid()
    print(online_phone)
    devices = "192.168.1.112:5555" # online_phone[0]

    ## 获取手机系统版本
    # ss = get_platforms_version()
    # print(ss)
    #
    # # #获取手机的名字
    # print(get_phonename())
    #
    # # 获取手机现有的安装包的
    # print(get_phone_apk(online_phone[0]))

    # 获得手机安装包apk的路径
    result = get_phone_apk_path(devices, need_packages)
    print(result)

    for index, i in enumerate(result):
        if i:
            logger.warning(f"开始下拉 apk: {i}")
            name = i.lstrip("package:")
            # pc_name = need_packages[index] + ".apk"  # re_sting_title(name)
            pc_name = "./apks"
            logger.info(f"name :{name}, pc_name： {pc_name}")
            res = export_phone_apk(devices, name, pc_name)
            logger.info(res)
            show()
            logger.info("开始睡眠30秒")
            time.sleep(30)#需要手动改名字，暂停三十秒
