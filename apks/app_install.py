import os
from tools import adb_install_apk, get_devices_udid, logger, export_pc_apk, export_phone_apk
from loguru import logger
fileList = os.listdir('./')

divices = get_devices_udid()
if divices:
    device = "192.168.1.116:5555"  # divices[0]
    # os.popen("adb connect {}".format(device))
    # print(device)
    # 向手机内部安装 apk
    for i in fileList:
        try:
            if ".apk" in i:
                logger.info(f"正在安装{i}")
                result = adb_install_apk(device, i)
                logger.info(result)
        except Exception as err:
            logger.error(err)
