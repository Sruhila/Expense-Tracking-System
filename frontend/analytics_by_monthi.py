import streamlit as st
from datetime import datetime
import requests
from click import option
import pandas as pd
import altair as alt
from unicodedata import category

API_URL = "http://localhost:8000"

def analytics_month_tab():
    # col1,col2 = st.columns(2)
    # with col1:
    #
    # with col2:
    #     end_date = st.date_input("End Date", datetime(2024, 8, 5))
    response = requests.get(f"{API_URL}/month")
    if response.status_code== 200:
        monthly_expenses = response.json()
        # st.write(monthly_expenses)
    else:
        st.error("Failed to retrieve expenses")
    # st.write(response)
    data={
        "expense_month": [expense_month["expense_month"] for expense_month in monthly_expenses],
        "month_name": [month_name["month_name"] for month_name in monthly_expenses],
        "total": [total["total"] for total in monthly_expenses]
    }
    # st.write(data)
    df=pd.DataFrame(data)
    df_chart = df.set_index("expense_month")

    # Create Altair bar chart
    chart = (
        alt.Chart(df)
        .mark_bar(size=50, color="White")  # Change bar color
        .encode(
            x=alt.X(
                "month_name:N",
                title="Month",
                axis=alt.Axis(labelColor="lightgray", titleColor="White", gridColor="gray")  # X-axis color settings
            ),
            y=alt.Y(
                "total:Q",
                title="Total Expenses",
                axis=alt.Axis(labelColor="lightgray", titleColor="White", gridColor="gray")  # Y-axis color settings
            ),
            tooltip=["month_name", "total"],
        )
    ).properties(
        title=alt.TitleParams("Expense Breakdown By Month", anchor="middle", color="White", fontSize=25)  # Title color
    )

    # st.title("Expense Breakdown By Month")

    st.altair_chart(chart,use_container_width=True)

    # 🎨 **Custom Table Styling**
    styled_df = df.style.set_properties(**{
        'background-color': 'lightgray',  # Table background color
        'color': 'black',  # Text color
        'border-color': 'black'  # Border color
    }).set_table_styles(
        [{'selector': 'th', 'props': [('background-color', 'darkblue'), ('color', 'white')]}]  # Column headers styling
    )

    # Display Styled Table
    st.write("### Monthly Expenses Data Table", unsafe_allow_html=True)
    st.dataframe(styled_df)

    # st.table(df_chart)
