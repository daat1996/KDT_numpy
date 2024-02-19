import pandas as pd
import numpy as np



df = pd.read_csv('../data/ch2_scores_em.csv', index_col='student number')
print(df.head())