# _*_ coding: utf-8 _*_
"""
@Author: Zongzc
@Describe: 
"""
import streamlit as st
import pynvml
import time


pynvml.nvmlInit()
gpu_count = pynvml.nvmlDeviceGetCount()
handle = pynvml.nvmlDeviceGetHandleByIndex(0)
meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)

col1, col2, col3 = st.columns(3)
mem_total = meminfo.total / 1024 / 1024
mem_used = meminfo.used / 1024 / 1024

col1.metric(label="GPU Count", value=f"{gpu_count}")
col2.metric(label="GPU Mem Total", value=f"{meminfo.total / 1024 / 1024:.2f}MB",
            delta=f"{(meminfo.total / 1024 / 1024) - mem_total:.2f}MB")
col3.metric(label="GPU Mem Used", value=f"{meminfo.used / 1024 / 1024:.2f}MB",
            delta=f"{(meminfo.used / 1024 / 1024) - mem_used:.2f}MB")
time.sleep(5)
#
# if st.button('Say hello'):
#     st.write('Why hello there')
# else:
#     st.write('Goodbye')
# st.experimental_rerun()
