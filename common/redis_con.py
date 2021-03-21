# -*- coding: utf-8 -*-
# 说明: redis连接公共组件

import redis
# from backend import settings

class Redis:
    redisHost = '127.0.0.1'
    redisPort = '6379'

    def __init__(self, host=redisHost, port=redisPort):
        self.__conn = redis.Redis(
            connection_pool=redis.BlockingConnectionPool(max_connections=15, host=host, port=port))

    def __getattr__(self, command):
        def _(*args):
            return getattr(self.__conn, command)(*args)  # 重新组装方法调用
        return _