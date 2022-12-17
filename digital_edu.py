import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv('train.csv')
df = df.fillna(-1)
df.drop(["bdate", "has_photo","relation", "followers_count", "graduation","langs","occupation_type","occupation_name"], axis = 1, inplace = True)
df.info()

wooman = 0 
mujik = 0
est = 0
ne_est = 0
def est_telephone(row):
    global est, ne_est
    if row['has_mobile'] == 1 and row["result"] == 1:
        est += 1
    if row['has_mobile'] == 1 and row["result"] == 0:
        ne_est += 1
    return False

df.apply(est_telephone, axis = 1)
a = pd.Series(data = [est, ne_est],
index = ["есть", "нету"])
a.plot(kind = 'barh')
plt.show()

def mujiki_or_wooman(row):
    global mujik, wooman
    if row['sex'] == 1 and row['result'] == 1:
        mujik += 1
    if row['sex'] == 2 and row['result'] == 1:
        wooman += 1
    return False
df.apply(mujiki_or_wooman, axis = 1)
a = pd.Series(data = [mujik, wooman],
index = ["мужик", "вумен"])
a.plot(kind = 'barh')
plt.show()

