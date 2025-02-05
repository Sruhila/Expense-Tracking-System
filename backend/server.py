from fastapi import FastAPI,HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app=FastAPI()

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date


@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date:date):
    expenses= db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None :
        raise HTTPException(status_code=500, detail ="Failed to retrive expense summary from database")

    return expenses

@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date:date, expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)

    for expense in expenses:
        db_helper.insert_expenses(expense_date,expense.amount,expense.category,expense.notes)

    return {"message":"Expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range:DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)

    if data is None :
        raise HTTPException(status_code=500, detail ="Failed to retrive expense summary from database")

    total = sum([row['total'] for row in data])

    breakdown={}
    for row in data:
        percentage = (row['total']/total)*100 if total !=0 else 0
        breakdown[row['category']]={
            "total":row['total'],
            "percentage":percentage
        }

    return breakdown

@app.get("/month/")
def get_monthly_summary():
    monthly_summary = db_helper.fetch_monthly_expense_summary()
    if monthly_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly expense summary from the database.")

    return monthly_summary

    # try:
    #     expenses_by_months= db_helper.fetch_expense_summary_by_month()
    #
    #     if expenses_by_months is None :
    #         raise HTTPException(status_code=500, detail ="Failed to retrive expense summary from database")
    #
    #     if not expenses_by_months:  # Handle empty results gracefully
    #         return {"message": "No expenses found"}
    #
    #     return expenses_by_months
    # except Exception as e:
    #     import traceback
    #     error_message = traceback.format_exc()
    #     print(error_message)  # This will show errors in logs
    #     return {"error": str(e)}