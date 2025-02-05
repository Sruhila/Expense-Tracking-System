import mysql.connector
from contextlib import contextmanager
import logging
from logging_setup import setup_logger

logger = setup_logger("db_helper")

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = "localhost",
         user = "root",
        password="root",
         database ="expense_manager"
    )

    # if connection.is_connected():
    #     print("connection Successful")
    # else:
    #     print("Failed in connection")

    cursor = connection.cursor(dictionary = True)
    yield cursor

    if commit:
        connection.commit()

    cursor.close()
    connection.close()

# def fetch_all_records():
#     with get_db_cursor() as cursor:
#         cursor.execute("SELECT * FROM expenses")
#         expenses = cursor.fetchall()
#         return expenses

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s",(expense_date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expenses(expense_date,amount,category,notes):
    logger.info(f"insert_expenses_for_date called with date:{expense_date},amount:{amount},category:{category},notes:{notes}")
    with get_db_cursor(commit =True) as cursor:
        cursor.execute("INSERT INTO expenses(expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
                       (expense_date,amount,category,notes)
                       )

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit =True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s",(expense_date,))

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expenses_summary called with start date:{start_date},end_date:{end_date}")
    with get_db_cursor(commit =True) as cursor:
        cursor.execute('''SELECT category,SUM(amount) as total
                       FROM expenses WHERE expense_date 
                        BETWEEN %s and %s
                        GROUP BY category''',
                       (start_date,end_date))
        data=cursor.fetchall()
        return data

def fetch_monthly_expense_summary():
    logger.info(f"fetch_expense_summary_by_months")
    with get_db_cursor() as cursor:
        cursor.execute('''SELECT month(expense_date) as expense_month, 
               monthname(expense_date) as month_name,
               sum(amount) as total FROM expenses
               GROUP BY expense_month, month_name;
            '''
        )
        data = cursor.fetchall()
    return data
    # logger.info(f"fetch_expenses_summary_by_month called with expense by month")
    #
    # try:
    #     with get_db_cursor() as cursor:
    #
    #         cursor.execute('''SELECT month(expense_date) as expense_month,
    #            monthname(expense_date) as month_name,
    #            sum(amount) as total FROM expenses
    #            GROUP BY expense_month, month_name;''')
    #
    #         expenses_by_month = cursor.fetchall()
    #
    #         if not expenses_by_month:
    #             logger.warning('No expenses found')
    #             return[]
    #
    #     return expenses_by_month
    #
    # except Exception as e:
    #         logger.error(f"Database error: {e}")
    #         return None

if __name__ == "__main__":
    # fetch_all_records()

    # insert_expenses("2024-08-20", "300", "food", "Panipuri")
    # delete_expenses_for_date("2024-08-20")
    # expenses = fetch_expenses_for_date("2024-08-03")
    # data = fetch_expense_summary("2024-08-01","2024-08-05")
    expenses_by_month = fetch_expense_summary_by_month()
    print(expenses_by_month)
    for expenses in expenses_by_month:
        print(expenses)
