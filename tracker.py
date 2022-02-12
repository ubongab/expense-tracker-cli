import sys
from prettytable import PrettyTable
import random
from datetime import datetime 
from expense_manager import ExpenseManager  

class MenuItems:
    ''' Display menu items'''

    def __init__(self):
        self.tracker = ExpenseManager()
        self.choices = [1,2,3,4,5,6,7]

    def menu_display(self):
        print('''
        
        Expense Tracker Menu
        ----------------------
        1. Add New Expense
        2. Add New Income
        3. Show all Expenses
        4. Modify Expense
        5. Modify Income
        6. Show all Income
        7. Show Balances
        8. Exit
        
        ''')
    def option_logic(self,opt):
        ''' manage user options '''
        try:
            if int(opt) == 1:
                amount = float(input('Expense Amount: '))
                desc = input('Description? (text): ')
                ct = input('What Category? (text): ')
                self.tracker.add_expense(amount=amount,description=desc, category=ct)

            if int(opt) == 2:
                amount = float(input('Income Amount: '))
                src = input('Income Source? (text): ')
                self.tracker.add_income(amount=amount,income_source=src)

            if int(opt) == 3:
                tb = PrettyTable(['id', 'created', 'modified', 'amount', 'description', 'category'])
                for d in self.tracker.show_expenses():
                    tb.add_row(d.values())
                print(tb)

            if int(opt) == 4:
                id = int(input('Enter expense id: '))
                amt = float(input('Enter NEW expense amount: '))
                new_desc = input('Enter NEW description (or leave blank): ')
                new_cat = input('Enter NEW Category (or leave blank): ')
                self.tracker.modify_expense(id,amt,new_desc, new_cat)

            if int(opt) == 5:
                id = int(input('Enter income id: '))
                amt = float(input('Enter NEW income amount: '))
                new_desc = input('Enter NEW Source (or leave blank): ')
                self.tracker.modify_income(id,amt,new_desc)
            
            if int(opt) == 6:
                tb = PrettyTable(['id', 'created', 'modified', 'amount', 'source'])
                for d in self.tracker.show_income():
                    tb.add_row(d.values())
                print(tb)

            if int(opt) == 7:
                current_balance = self.tracker.show_account()
                print(current_balance)
                tb = PrettyTable(['Total Income', 'Total Expenses','Balance']) 
                tb.add_row(current_balance.values())

                print(tb)

            if int(opt) == 8:
                self.quit()
        except ValueError:
            print('Invalid input. Enter a numeric value')


    def run_app(self):
        ''' Display menu items and react to options'''
        while True:
            self.menu_display()
            opt = input('Enter an option:')
            self.option_logic(opt)

    def quit(self):
        print('Goodbye!')
        sys.exit(0)

if __name__ == '__main__':
    MenuItems().run_app()