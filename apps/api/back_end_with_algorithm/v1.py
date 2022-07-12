# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 
"""
from fastapi import APIRouter
from typing import Union
from pydantic import BaseModel

router = APIRouter()


class TaskRequest(BaseModel):
    # 任务编号
    task_id: int
    # 输入文件路径
    input_file_path: str
    # 输出文件路径
    output_file_path: str
    # 检测项点列表
    algorithm_list: list


@router.post("/task_request", description="Task Request")
async def task_request(task_req: TaskRequest):
    task_req_dict = task_req.dict()
    return task_req


"""
    处理错误
"""
# items = {"foo": "The Foo Wrestlers"}
#
#
# @app.get(Configs.application.API_PREFIX + "/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"item": items[item_id]}
