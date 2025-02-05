import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_tab
from analytics_by_monthi import analytics_month_tab


st.title("Expense Tracking System")

tab1, tab2, tab3= st.tabs(["Add/Update","Analytics By Category","Analytics By Months"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_month_tab()