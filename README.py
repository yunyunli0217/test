# test

import pandas as pd
c=pd.read_csv("CLIENT_REVENUE2.csv")
w = pd.read_csv("VW_MANAGED2.csv",error_bad_lines=False)
w.drop("party_survey_response_id"  ,axis=1,inplace=True)

df=[w,c]
df=pd.concat(df)
df.shape
