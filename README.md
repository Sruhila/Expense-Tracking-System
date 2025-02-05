# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

## Project Output

1. **ADD/UPDATE Module**: https://github.com/Sruhila/Expense-Tracking-System/blob/main/add_update.pdf

   I am retrieving expense data from a MySQL database based on a specific date (e.g., '2024-08-01'). The data includes the amount spent, spending category, and notes explaining the expense. If no expenses are recorded for the selected date, the system returns default values (e.g., Amount: 0.0, Category: 'Shopping', Notes: ' ').

2. **Analytics By Category**: https://github.com/Sruhila/Expense-Tracking-System/blob/main/analytics_by_category.pdf


   For a specified date range (e.g., from '2024-08-01' to '2024-08-05'), I will provide expense analytics in two formats:

   - A bar chart visualizing spending by category to highlight where most money was spent
   - A detailed table showing the breakdown by category, including total amounts and percentages of overall spending

3. **Analytics By Month**: https://github.com/Sruhila/Expense-Tracking-System/blob/main/analytics_by_month.pdf

   I am retrieving all expense data from a MySQL database and aggregating it by month to show the total amount spent per month. I'm visualizing this data using an Altair bar chart, which allows me to customize the bar width and colors.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Sruhila/Expense-Tracking-System.git
   cd expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
