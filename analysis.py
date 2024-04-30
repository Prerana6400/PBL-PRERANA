import matplotlib.pyplot as plt

def generate_expense_analysis():
    # Placeholder data for analysis
    categories = ['Food', 'Transportation', 'Shopping', 'Utilities', 'Entertainment']
    expenses = [300, 150, 200, 120, 80]

    # Create a pie chart for expense analysis
    plt.figure(figsize=(8, 8))
    plt.pie(expenses, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expense Analysis')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Save the pie chart as an image
    plt.savefig('expense_analysis.png')

if _name_ == '_main_':
    generate_expense_analysis()
    