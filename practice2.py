
Banking application scenario:

-bank offers two types of accounts, checking and savings
-both accounts have balance attribute
-checking accounts can have any number of withdrawals, savings accounts maximum of 6 (think of using attributes to code for this)
-savings accounts have 7% interest, checking 2% (once again attribute)
-savings accounts have no overdraft (cannot go below 0) while checking accounts have an overdraft limit set.
-interest can be applied to account via method

-customers are identified by customer ID (6 digit number)
-also have firstname, lastname, age, email attributes
-customers can make account withdrawals as long as they are within aforementioned limits
-customers can have either a checking or savings account, but not both
--all customer info held in a dictionary, where customer ID is key and customer object is value

-2 types of employee: normal and manager
-employees have 6 digit employee IDs, firstname, lastname, age, email,
-they cannot hold accounts
-normal  employees can view customer account info in the dictionary and add a new customer
-manager can switch customer from checking to savings, change customer info, or remove a customer from dictionary
