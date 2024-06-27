# 1
college.loc[college['instnm'].str.contains('University of Texas'), 'instnm']

college.loc[college['instnm']=='The University of Texas at Dallas', 'satmtmid']


# 2
total_udgs = college.groupby('stabbr')['ugds'].sum()
total_udgs.nlargest(5).tail(1)

# 3
# code up your answer here
college.isna().sum()/college.shape[0]
college.isna().mean()

# 4
ca = pd.to_numeric(college.loc[college['stabbr']=='CA', 'md_earn_wne_p10'], errors='coerce').dropna()
tx = pd.to_numeric(college.loc[college['stabbr']=='TX', 'md_earn_wne_p10'], errors='coerce').dropna()
ca_n = len(ca)
tx_n = len(tx)
ca_mean = ca.mean()
tx_mean = tx.mean()
ca_var = ca.std() ** 2
ca_var = ca.std() ** 2
tx_var = tx.std() **2

# assuming unequal variance
delta = ca_mean - tx_mean
se = np.sqrt(ca_var / ca_n + tx_var / tx_n)

t_val = delta / se
t_val

# 2-sided two-sample mean test
# - h0 : ca == tx, or delta == 0
# - ha/h1 : ca != tx, or delta !=0

# 2-sided p-value
# using t-distribution  ~~ this validates well with the scipy function
t_df = ca_n + tx_n -2
st.t.sf(abs(t_val), t_df) * 2

# using standard normal
st.norm.sf(abs(t_val)) * 2

# call scipy module function for two sample t-test
st.ttest_ind(ca, tx, equal_var=False)

# 1-sided two-sample mean test
# - h0 : ca > tx, or delta > 0
# - ha/h1 : ca <= tx, or delta <= 0

# calculation is the same
# 1-sided p-value
# using t-distribution
st.t.sf(t_val, t_df)
# using standard normal
st.norm.sf(t_val)

# 5
college['gender'] = np.where(college['menonly']==1, 'menonly',
                             np.where(college['womenonly']==1, 'womenonly', 
                                      np.where(college['menonly'].isna(), 'missing', 
                                               np.where(college['womenonly'].isna(), 'missing','nongenderspecific'))))

college['gender'].value_counts()

df_result = college.groupby('gender').agg({'satmtmid': ['mean','std'],
                                          'satvrmid': ['mean','std']})
df_result.head()

# 6
college.set_index('instnm',inplace=True)

df1 = college.groupby('stabbr')['ugds'].nlargest(3).reset_index()

df2 = college.sort_values(['stabbr','ugds'],ascending=[True,False]).groupby('stabbr').head(3)[['stabbr','ugds']].reset_index()

df1[df1['stabbr']=='VI']

df2[df2['stabbr']=='VI']

# exercise 6 solution
# method 1
college.groupby('stabbr')['ugds'].nlargest(3).reset_index()
# method 2 - will keep the missing
college.sort_values(['stabbr','ugds'],ascending=[True,False]).groupby('stabbr').head(3)

# 7
pd.crosstab(index=emp['gender'], columns=emp['race'], 
            normalize='all').round(3)

# 8
pv3.melt(id_vars='gender', value_vars=['Asian','Black','Hispanic','Native American','White'])