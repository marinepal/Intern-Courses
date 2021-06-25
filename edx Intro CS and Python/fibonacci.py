from time import time
import sys
from time import time

from pyinstrument import Profiler

sys.setrecursionlimit(1500)
p = Profiler()


def fibRecursive(n: int) -> int:
    if n <= 2:
        return 1
    return fibRecursive(n - 1) + fibRecursive(n - 2)


def fibDict(n: int, fibValuesDict={1: 1, 2: 1}) -> int:
    if n in fibValuesDict:
        return fibValuesDict[n]
    fibValuesDict[n] = fibDict(n - 1, fibValuesDict) + fibDict(n - 2, fibValuesDict)
    return fibValuesDict[n]


def fibList(n: int, fibValuesList: list) -> int:
    if fibValuesList[n] != 0:
        return fibValuesList[n]
    else:
        fibValuesList[n] = fibList(n - 1, fibValuesList) + fibList(n - 2, fibValuesList)
        return fibValuesList[n]


FIB_NUMBER = 500
# print(fibRecursive(FIB_NUMBER))
p.start()
now = time()
initialList = [0] * (FIB_NUMBER + 1)  # np.zeros(FIB_NUMBER + 1)
initialList[1], initialList[2] = 1, 1
fibList(FIB_NUMBER, initialList)
print(time() - now)
p.stop()
# print(p.output_text())
now = time()
p.start()
fibDict(FIB_NUMBER)
print(time() - now)
p.stop()
# print(p.output_text())
