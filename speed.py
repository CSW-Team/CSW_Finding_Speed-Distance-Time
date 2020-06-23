while(True):
    def inputnumber(N):
        while(True):
            try:
                dic = {'1':"거리 시간",'2':"속도 시간",'3':"속도 거리"}
                M = list(map(int,input(dic[N]).split()))
                return M
            except ValueError:
                pass
    def inputpoint(N):
        while(True):
            try:
                dic = {'1':"거리 단위(mm,cm,m,km) 시간 단위(h,m,s)",
                       '2':"속도 단위(mm/h,mm/m,mm/s,cm/h,cm/m,cm/s,m/h,m/m,m/s,km/h,km/m,km/s) 시간 단위(h,m,s)",
                       '3':"속도 단위(mm/h,mm/m,mm/s,cm/h,cm/m,cm/s,m/h,m/m,m/s,km/h,km/m,km/s) 거리 단위(mm,cm,m,km)"
                       }
                L = list(map(str,input(dic[N]).split()))
                return L
            except ValueError:
                pass
    def checktime(L1):
        returnvalue = ""
        check = 0
        for i in range(len(L1)):
            if L1[i] == '/':
                check = 1
            if check == 1:
                returnvalue = returnvalue + L1[i]
        return returnvalue[1:]
    def checkstreet(L1):
        returnvalue = ""
        check = 1
        for i in range(len(L1)):
            if L1[i] == '/':
                check = 0
            if check == 1:
                returnvalue = returnvalue + L1[i]
        return returnvalue
    def one(M1,M2):
        return M1 / M2
    def two(M1,M2,L1,L2):
        dic = {'h':3,'m':2,'s':1}
        point = L2
        if dic[checktime(L1)] > dic[L2]:
            M1 *= (60**(dic[checktime(L1)]-dic[L2]))
        elif dic[checktime(L1)] < dic[L2]:
            M2 *= (60**(dic[L2]-dic[checktime(L1)]))
            point = checktime(L1)
        return M1 * M2,checkstreet(L1),point
    def three(M1,M2,L1,L2):
        dic = {'km':7,'m':4,'cm':2,'mm':1}
        point = L2
        if dic[checkstreet(L1)] > dic[L2]:
            M1 *= (10**(dic[checkstreet(L1)]-dic[L2]))
        elif dic[checkstreet(L1)] < dic[L2]:
            M2 *= (10**(dic[L2]-dic[checkstreet(L1)]))
            point = checkstreet(L1)
        return M2 /M1,point,checktime(L1)
    N = input("선택해주세요. 속도:1,거리:2,시간:3")
    M = inputnumber(N)
    M1,M2 = M[0],M[1]
    L = inputpoint(N)
    L1,L2 = L[0],L[1]
    if N == '1':
        print(str(one(M1,M2))+' '+L2+'/'+L1)
    elif N == '2':
        final = two(M1,M2,L1,L2)
        print(str(final[0])+' '+str(final[1])+'/'+str(final[2]))
    elif N == '3':
        final = three(M1,M2,L1,L2)
        print(str(final[0])+' '+str(final[1])+'/'+str(final[2]))
    C = input("종료하시겠습니까? Y y/N n")
    if C == 'N' or C == 'n':
        break
