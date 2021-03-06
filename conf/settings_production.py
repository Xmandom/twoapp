# -*- coding: utf-8 -*-
"""
用于正式环境的全局配置
"""
from settings import APP_ID
# ===============================================================================
# 数据库设置, 本地开发数据库设置
# ===============================================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 我们默认用mysql
        'NAME': 'twoapp',                        # 数据库名 (默认与APP_ID相同)
        'USER': 'root',                            # 你的数据库user
        'PASSWORD': 'bk@321',                        # 你的数据库password
        'HOST': '10.105.6.108',                   		   # 数据库HOST
        'PORT': '3306',                        # 默认3306
    },
}
