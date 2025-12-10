
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
!pip install streamlit
df = pd.read_csv('/content/IndividualAssistanceHousingRegistrantsLargeDisasters (2).csv')

for col in df.columns:
    if df[col].dtype == 'object':
        df[col] = df[col].fillna('Unknown')
    else:
        df[col] = df[col].fillna(df[col].median())

st.title("TSA Eligibility & Repair Amount Dashboard")

st.header("Distribution of Repair Amount")
fig_hist, ax_hist = plt.subplots(figsize=(10,6))
sns.histplot(df['repairAmount'], bins=50, kde=True, ax=ax_hist)
ax_hist.set_xlabel('Repair Amount')
ax_hist.set_ylabel('Count')
ax_hist.set_title('Distribution of Repair Amount')
st.pyplot(fig_hist)
plt.close(fig_hist)

st.header("Repair Amount Across TSA Eligibility")
fig_boxplot, ax_boxplot = plt.subplots(figsize=(10,6))
sns.boxplot(x='tsaEligible', y='repairAmount', data=df, ax=ax_boxplot)
ax_boxplot.set_xlabel('TSA Eligible (0=No, 1=Yes)')
ax_boxplot.set_ylabel('Repair Amount')
ax_boxplot.set_title('Repair Amount Across TSA Eligibility')
st.pyplot(fig_boxplot)
plt.close(fig_boxplot)
