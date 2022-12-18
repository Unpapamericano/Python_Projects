Welcome to the budget tracker project!

This project is a simple Python class that allows users to track their expenses and create a visual chart of their spending habits. The Category class represents a category of expenses and allows users to deposit and withdraw funds, as well as transfer funds to other categories.

To use the Category class, create an instance of it and pass in a description for the category. You can then use the following methods to manage the category's funds:

deposit(amount, description): Adds the specified amount to the category's balance, with an optional description for the transaction.
withdraw(amount, description): Removes the specified amount from the category's balance, with an optional description for the transaction. Returns True if the withdrawal is successful, False if the category does not have sufficient funds.
transfer(amount, category_instance): Transfers the specified amount from the current category to the provided category_instance, with a description for the transaction in both categories. Returns True if the transfer is successful, False if the current category does not have sufficient funds.
get_balance(): Returns the current balance of the category.
check_funds(amount): Returns True if the category has sufficient funds to cover the specified amount, False otherwise.
The create_spend_chart(categories) function takes in a list of Category instances and returns a string representing a visual chart of the spending habits for each category. The chart displays the percentage of the total spent in each category, with 10% increments.

We hope this budget tracker helps you keep track of your expenses and make informed financial decisions.
