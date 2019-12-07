def floatRange(lo, hi, stepSize):
    resultList = []
    ele = lo
    while ele <= hi:
        resultList.append(ele)
        ele += stepSize
    return resultList

print floatRange(1.0, 2.0, 0.1)
        
