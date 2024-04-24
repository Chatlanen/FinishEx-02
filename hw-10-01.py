import pandas as pd
import numpy as np
import random
lst = ['robot'] * 10
lst += ['human'] * 10
#lst += ['anim'] * 2

random.shuffle(lst)

data = pd.DataFrame({'whoAmI':lst})
pdRes = pd.get_dummies(data['whoAmI'])
print(pdRes)

codes, uniqs = pd.factorize(data['whoAmI'], sort=True)

#res = list()
#for n in range (len(codes)):
#    res.append([ codes[n] == n_un for n_un in range(len(uniqs))])

print("=========== 1 способ =================")
res: list[list] = [[ codes[n] == n_un for n_un in range(len(uniqs))] for n in range (len(codes))]
pdRes2 = pd.DataFrame(res, columns=uniqs)
print (pdRes2)
print ('pdRes.equals(pdRes2) = {} '.format (pdRes.equals(pdRes2)))

print("=========== 2 способ =================")
#shape = len(codes), len(uniqs)
res2 = np.zeros(shape=(len(codes), len(uniqs)), dtype=np.dtype(bool), order="F")
res2[np.arange(len(codes)), codes] = 1
pdRes3 = pd.DataFrame(res2, columns=uniqs)

print (pdRes3)
print ('pdRes.equals(pdRes3) = {} '.format (pdRes.equals(pdRes3)))
    
