# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 
"""
from fastapi import FastAPI
from apps.core.log.logger import common_logger
from apps.core.config import Configs
from apps.api.back_end_with_algorithm import router as back_end_with_algorithm_router
import traceback


def get_application() -> FastAPI:
    """
    创建 app 应用
    :return:
    """
    try:
        application = FastAPI(title=Configs.application.PROJECT_NAME,
                              version=Configs.application.VERSION,
                              docs_url=f"{Configs.application.API_PREFIX}/docs"
                              )
        application.include_router(back_end_with_algorithm_router)

        common_logger.info(f"{Configs.application.PROJECT_NAME}已启动")
        common_logger.info(f"当前版本：{Configs.application.VERSION}")
        common_logger.info(f"启动环境：{Configs.application.ENV_MODE}")
        return application

    except:
        common_logger.error(traceback.format_exc())


app = get_application()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host="127.0.0.1", reload=True, port=8000)
