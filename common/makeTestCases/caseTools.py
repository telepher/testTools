"""
 * @description: TODO 
 * @author ChenDong
 * @date 2024/8/19 下午5:09
 * @version 1.0
"""
import copy
import re


class dataMaker(object):
    def equalsMake(self):
        res = []
        namelist, usefullist = [], []
        tmp1, tmp2, tmp3 = [], [], []
        # T = input()
        # F = input()
        # n = None
        # while n == None:
        #     try:
        #         n = int(input())
        #     except Exception as e:
        #         print('输入有误，请重新输入')
        # for i in range(n):
        #     name = input()
        #     namelist.append(name)
        #     useful = input().split(' ')
        #     useless = input().split(' ')
        #     usefullist.append(useful)
        #     for i in useless:
        #         res.append(f'输入{name}{i}')
        T = input('请输入成功的预期结果')
        F = input('请输入失败的预期结果')
        n = None
        while n == None:
            try:
                n = int(input('请输入类型数量：'))
            except Exception as e:
                print('输入有误，请重新输入')
        for i in range(n):
            name = input('请输入类型的名字：')
            namelist.append(name)
            useful = input('请输入有效等价类：').split(' ')
            useless = input('请输入无效等价类：').split(' ')
            usefullist.append(useful)
            for i in useless:
                res.append(f'输入{name}{i}')

        for i in range(len(namelist)):
            tmp1, tmp3 = [], []
            for j in usefullist[i]:
                tmp1.append(f'{namelist[i]}{j}、')
            if not tmp2:
                tmp2 = copy.deepcopy(tmp1)
                continue
            for j in tmp1:
                for k in tmp2:
                    tmp3.append(k + j)
            tmp2 = copy.deepcopy(tmp3)

        for i in range(len(tmp2)):
            tmp2[i] = '输入' + tmp2[i][:-1] + f',{T}'

        for i in range(len(res)):
            res[i] = res[i] + f',{F}'
        return tmp2 + res

    def boundaryMake(self):
        res = []
        namelist, usefullist = [], []
        tmp1, tmp2, tmp3 = [], [], []
        T = input('请输入成功的预期结果')
        F = input('请输入失败的预期结果')
        n = None
        while n == None:
            try:
                n = int(input('请输入类型数量：'))
            except Exception as e:
                print('输入有误，请重新输入')
        for i in range(n):
            st = float()
            name = str()
            a2b = str()
            while not st and not name and not a2b:
                st = input('请输入精确度')
                name = input('请输入类型的名字：')
                namelist.append(name)
                a2b = input(f'请输入{name}的边界区间 [a-b]/(a-b]/[a-b)/(a-b)').strip()
                if (a2b.startswith('[') and a2b.endswith(']') or a2b.startswith('(') and a2b.endswith(')')
                        and a2b.startswith('[') and a2b.endswith(')') or a2b.startswith('(') and a2b.endswith(']')):
                    a = a2b[0]
                    a2b = re.sub('[^/d/.]', ' ', a2b).strip().split(' ')
                    b = a2b[1]
                    if a > b:
                        a, b = b, a
                    elif a == b:
                        print('边界相等，想清楚再输入A')
                        continue
                else:
                    print('输入有误，想清楚再输入B')
                    continue
        pass