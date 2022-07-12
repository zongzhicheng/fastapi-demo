# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 
"""
from pydantic import BaseModel
import os


class ProjectConfigs(BaseModel):
    VERSION: str = '0.0.1'
    PROJECT_NAME: str = '基础设施巡检算法平台'
    ENV_MODE: str = "DEV"
    API_PREFIX: str = "/algorithm_platform/api"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    LOG_DIR = "logs"


class DevConfigs(BaseModel):
    """
        开发环境配置文件（外网）
    """
    application: ProjectConfigs = ProjectConfigs(ENV_MODE="DEV")


class ProConfigs(ProjectConfigs):
    """
        开发环境配置文件（内网）
    """
    application: ProjectConfigs = ProjectConfigs(ENV_MODE="PRO")


if __name__ == '__main__':
    pro = ProjectConfigs()
    print(pro.BASE_DIR)
