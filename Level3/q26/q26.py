for i in range(0, 1000000):
   k = i * 3438478 + 193127 # 3438478で割って193127余る
   if k % 1584891 == 32134: # 1584891で割って32134余る
       print(k)
       break