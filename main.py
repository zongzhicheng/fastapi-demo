# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 
"""
from fastapi import FastAPI, Query, HTTPException
from enum import Enum
from typing import Union
from pydantic import BaseModel
from apps.core.config import Configs


def get_application() -> FastAPI:
    """
    创建 app 应用
    :return:
    """
    application = FastAPI(title=Configs.application.PROJECT_NAME,
                          version=Configs.application.VERSION,
                          docs_url=f"{Configs.application.API_PREFIX}/docs"
                          )

    return application



app = get_application()


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}


# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


"""
    查询参数
"""
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}


# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item


# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item


"""
    请求体
"""


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


# @app.post("/items/")
# async def create_item(item: Item):
#     return item

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price + item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

"""
    额外的校验
"""

# @app.get("/items/")
# async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50)):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results


"""
    处理错误
"""
items = {"foo": "The Foo Wrestlers"}


@app.get(Configs.application.API_PREFIX + "/items/{item_id}")
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item": items[item_id]}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host="127.0.0.1", reload=True, port=8000)
