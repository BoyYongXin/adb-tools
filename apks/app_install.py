import os
from tools import adb_install_apk, get_devices_udid, logger, export_pc_apk, export_phone_apk
from loguru import logger

fileList = os.listdir('./')

# divices = get_devices_udid()
# if divices:
#     device = "4676be960404"  # divices[0]
#     os.popen("adb connect {}".format(device))
#     # print(device)
#     # 向手机内部安装 apk
#     for i in fileList:
#         try:
#             if ".apk" in i:
#                 logger.info(f"正在安装{i}")
#                 result = adb_install_apk(device, i)
#                 logger.info(result)
#         except Exception as err:
#             logger.error(err)


tasks = [

    {'serialno': '192.168.1.139:5555', "device": "d85cb9d0", 'target': 'push', 'brand': 'OnePlus',
     'device_id': '869897038829437',
     'bundle_version': 'ONEPLUS A6000', },

    {'serialno': '192.168.1.137:5555', "device": "5a6ab206", 'target': 'push', 'brand': 'OnePlus',
     'device_id': '860746045053615',
     'bundle_version': 'ONEPLUS A6000', },

    {'serialno': '192.168.1.135:5555', "device": "918e2be5", 'target': 'push', 'brand': 'OnePlus',
     'device_id': '867520046084637',
     'bundle_version': 'ONEPLUS A6000', },

    {'serialno': '192.168.1.136:5555', "device": "72ffa539", 'target': 'push', 'brand': 'OnePlus',
     'device_id': '869897033036699',
     'bundle_version': 'ONEPLUS A6000', },
    # #
    {'serialno': '192.168.1.134:5555', "device": "f0e5dc3", 'target': 'push', 'brand': 'OnePlus',
     'device_id': '860746045162895', 'bundle_version': 'ONEPLUS A6000', },

    {'serialno': '192.168.1.138:5555', "device": "b61590ff", 'target': 'push', 'brand': 'OnePlus',
     'device_id': '869897038409016',
     'bundle_version': 'ONEPLUS A6000', },

    {'serialno': '192.168.1.140:5555', "device": "503bb77c", 'target': 'push', 'brand': 'OnePlus',
     'device_id': '860746047030538',
     'bundle_version': 'ONEPLUS A6000', },

    # {'serialno': '192.168.1.116:5555',"device":"bff74003", 'target': 'push', 'brand': 'Xiaomi',
    #  'device_id': '863976045207690',
    #  'bundle_version': 'xiaomi 8', },

    {'serialno': '192.168.1.112:5555', "device": "bff74003", 'target': 'push', 'brand': 'Xiaomi',
     'device_id': '869600042088531',
     'bundle_version': 'xiaomi 8', },

    {'serialno': '192.168.1.117:5555', "device": "75380dff", 'target': 'push', 'brand': 'Xiaomi',
     'device_id': '867252031508194',
     'bundle_version': 'xiaomi 8', },
]
for device in tasks:

    # device_id = "918e2be5"
    device_id = device.get('serialno')
    for i in fileList:
        try:
            if ".apk" in i and "com" not in i:
                # if "qq" or "remin" or "xinhua" or "pengpai" in i:
                logger.info(f"正在安装{i}")
                result = adb_install_apk(device_id, "{}".format(i))
                logger.info(result)
        except Exception as err:
            logger.error(err)
    break