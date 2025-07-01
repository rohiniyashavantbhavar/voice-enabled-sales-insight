import pandas as pd

df = pd.read_csv("data.csv")

def process_query(query):
    query = query.lower()

    if "top" in query and "product" in query:
        result = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(3)
        return f"Top products:\n{result.to_string()}"
    
    elif "total" in query and "sales" in query:
        total = df["Sales"].sum()
        return f"Total sales: {total}"
    
    elif "average" in query:
        avg = df.groupby("Product")["Sales"].mean()
        return f"Average sales per product:\n{avg.to_string()}"

    elif "highest" in query and "sales" in query:
        highest = df.groupby("Product")["Sales"].sum().idxmax()
        return f"Product with highest sales: {highest}"
    
    elif "best month" in query:
        month = df.groupby("Month")["Sales"].sum().idxmax()
        return f"Best month for sales: {month}"
    
    elif "revenue by product" in query:
        revenue = df.groupby("Product")["Sales"].sum()
        return f"Revenue by product:\n{revenue.to_string()}"

    elif "revenue by month" in query:
        revenue = df.groupby("Month")["Sales"].sum()
        return f"Revenue by month:\n{revenue.to_string()}"

    elif "improved the most" in query:
        monthly = df.pivot_table(index="Product", columns="Month", values="Sales", aggfunc="sum").fillna(0)
        improved = (monthly.iloc[:, -1] - monthly.iloc[:, -2]).idxmax()
        return f"Product that improved the most this month: {improved}"

    return "Sorry, I couldn't understand your query."
