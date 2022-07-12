# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 
"""
from fastapi import APIRouter
from apps.api.back_end_with_algorithm import v1

router = APIRouter()
router.include_router(v1.router, prefix="/back_end_with_algorithm", tags=["back_end_with_algorithm"])
