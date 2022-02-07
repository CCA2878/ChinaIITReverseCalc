import xlwings as xw

@xw.func
def calcAnnualBonusTax(m):
    '''
    根据财税[2018]164号文进行计算。
    传入参数为扣除个税后的实得金额。
    '''
    r = float(m)
    
    group = [(0.03, 0, float('-inf'), 3000),
        (0.10, 210, 3000, 12000),
        (0.20, 1410, 12000, 25000),
        (0.25, 2660, 25000, 35000),
        (0.30, 4410, 35000, 55000),
        (0.35, 7160, 55000, 80000),
        (0.45, 15160, 80000, float('inf'))]

    for c in group:
        x = (r - c[1])/(1 - c[0])
        if (c[2] < (x/12) <= c[3]):
            return x

