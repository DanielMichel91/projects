import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the budget data from a CSV file using ';' as the delimiter
budget_df = pd.read_csv("budget.csv", delimiter=";")

# Print the entire DataFrame
print(budget_df)

# Display information about the DataFrame, including data types and non-null counts
print(budget_df.info())

# Filter the DataFrame for rows where 'Description' is 'Salary Mario'

income = sum(budget_df["In"])

# Calculate and print total income
print("Einnahmen =", int(income), "€")
print()

# Filter the DataFrame for rows where 'Out' is greater than 0
filtered_df_out = budget_df.loc[budget_df['Out'] > 0]
sum_out = sum(filtered_df_out["Out"])

# Print the filtered DataFrame
print(filtered_df_out)
print()

# Calculate and print total expenses
print("Ausgaben =", int(sum_out), "€")
print()

# Calculate and print saved money
saved_money = income - sum_out
print("Gespartes Geld =", int(saved_money), "€")
print()

# Create a DataFrame of expenses using rows where 'Out' is greater than 0
budget_df_out = budget_df[budget_df['Out'] > 0]

# Group and sum expenses by category
sum_out_all = budget_df_out.groupby("Category").sum()

# Print the summarized expenses
print(sum_out_all)

# Set seaborn theme
sns.set_theme()

# Create a barplot for expenses per category and save it as an image
barplot_category_out = sns.barplot(data=sum_out_all, x="Out", y=sum_out_all.index)
barplot_category_out.set_title("Ausgaben pro Kategorie")
barplot_category_out.set_xlabel("Höhe der Ausgaben")
barplot_category_out.set_ylabel("Kategorie")
barplot_category_out.figure.savefig('expense_per_category.png', bbox_inches='tight')
barplot_category_out.figure.clf()

# Convert the 'Date' column to datetime
budget_df['Date'] = pd.to_datetime(budget_df['Date'])

# Print the converted 'Date' column
print(budget_df['Date'])
print()

# Group and sum expenses by month
sum_in_months = budget_df.groupby(pd.Grouper(key="Date", freq="1M")).sum()

# Print the summarized expenses by month
print(sum_in_months)
print()

# Create a barplot for expenses per month and save it as an image
barplot_sum_in_months = sns.barplot(data=sum_in_months, x=sum_in_months.index.month_name(), y="Out")
plt.title("Ausgaben pro Monat")
plt.xlabel("Monate")
plt.ylabel("Höhe der Ausgaben")
barplot_sum_in_months.figure.savefig('expense_per_months.png', bbox_inches='tight')
barplot_sum_in_months.figure.clf()