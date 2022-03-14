import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('task_profile_info_ss_nrt_task_3_1_1.csv')
df.plot(kind='bar')
plt.show()