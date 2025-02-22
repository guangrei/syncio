# -*-coding:utf8;-*-
from syncio.Task import create_task
from syncio.Multiprocessing import gather
from syncio.Threading import thread_gather

__all__ = ["create_task", "gather", "thread_gather"]
