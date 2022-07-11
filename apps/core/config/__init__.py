# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 
"""
from apps.core.config.config import DevConfigs, ProConfigs


def get_settings(env: str):
    if env == "DEV":
        return DevConfigs()
    elif env == "PRO":
        return ProConfigs()


Configs = get_settings("DEV")
