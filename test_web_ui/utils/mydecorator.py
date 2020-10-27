# -*- coding:utf-8 -*-
# author:zhangjie
# datetime:2020/10/27 12:19



def rerun_failer_step(func):
    '''
    用于定位步骤的失败重试
    '''
    rang_times = 4
    def wapper(*args, **kwargs):
        for _ in range(rang_times):
            try:
                func(*args, **kwargs)
                break
            except:
                continue
        else:
            raise RuntimeError(f"当前重复 {rang_times} 次操作失败，请查看日志处理！！！")
    return wapper




