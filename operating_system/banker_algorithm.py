# coding:utf-8

import numpy as np

# 定义算法所需的数据结构
Available = np.array([3, 3, 2])  # 可利用资源向量  假设系统有三类资源 数量分别为 10 5 7
Max = np.array([[7, 5, 3],
                [3, 2, 2],
                [9, 0, 2],
                [2, 2, 2],
                [4, 3, 3],
                ])  # 最大需求矩阵  5个进程 对三类资源 所需的最大数量

Allocation = np.array([[0, 1, 0],
                       [2, 0, 0],
                       [3, 0, 2],
                       [2, 1, 1],
                       [0, 0, 2],
                       ])  # 分配矩阵 系统已分配给进程的资源
Need = np.array([[7, 4, 3],
                 [1, 2, 2],
                 [6, 0, 0],
                 [0, 1, 1],
                 [4, 3, 1]
                 ])  # 需求矩阵  表示每一个进程所需的资源数


def bankerArithmetic(Request_num, Request):
    '''
    1, 检查进程所需资源是否超过系统当前资源值
    2, 检查进程所需资源是否超过其所需值
    '''
    global Available
    global Need
    global Allocation

    if (Request <= Available).all():
        print(Request_num, "Request", Request, "Available", Available)
        if (Request <= Need[Request_num]).all():
            print(Request_num, "Request", Request, "Need", Need[Request_num])
            # 尝试分配
            Available = Available - Request
            Need[Request_num] = Need[Request_num] - Request
            Allocation[Request_num] = Allocation[Request_num] + Request
            print("修改之后：\n", "Available \n", Available, "\nNeed\n", Need, "\nAllocation\n", Allocation)
            safeArithmetic()
            return
    print(Request_num, "请求不成功，你所请求的资源超过系统资源值或所需值\n")


def safeArithmetic():
    '''安全检测算法
    '''
    global Available
    global Need
    global Allocation

    Finish = [False] * 5
    Work = Available.copy()
    SafetyList = []
    flag = True
    while len(SafetyList) != Allocation.shape[0] and flag:
        num = Finish.count(False)
        for i in range(Allocation.shape[0]):
            if Finish[i] == False and (Need[i] <= Work).all():
                Work += Allocation[i]
                Finish[i] = True
                SafetyList.append(i)
                break
        if num - 1 == Finish.count(False):
            flag = True
        else:
            flag = False
    print(SafetyList)
    if False in Finish:
        print(Request_num, "请求 不安全\n")
    else:
        print(Request_num, "请求安全\n")


if __name__ == "__main__":
    Request_num = 1  # 请求进程的序号
    Request = np.array([1, 0, 2])  # 进程所需的资源
    bankerArithmetic(Request_num, Request)

    Request_num = 4
    Request = np.array([3, 3, 0])
    bankerArithmetic(Request_num, Request)

    Request_num = 0
    Request = np.array([0, 2, 0])
    bankerArithmetic(Request_num, Request)