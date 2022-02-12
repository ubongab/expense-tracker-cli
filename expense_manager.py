from datetime import datetime 

in_id = 0
class Income:
  def __init__(self,amount:float, income_source:str):
    self.amount = amount
    self.income_source = income_source
    self.created = datetime.today().date()
    self.modified = ''
    global in_id 
    in_id += 1 
    self.income_id = in_id
  
  def __repr__(self):
    return f'Income({self.income_id},{self.created}, {self.amount}, {self.income_source}, {self.created})'

ex_id = 0
class Expenditure:
  ''' defines expenditure data structure'''
  def __init__(self,amount:float, description:str, category:str=''):
    self.amount = amount
    self.description = description
    self.created = datetime.today().date()
    self.category = category
    self.modified = ''
    global ex_id 
    ex_id += 1 
    self.expend_id = ex_id
  
  def __repr__(self):
    return f'Expenditure({self.expend_id}, {self.created}, {self.amount}, {self.description}, {self.created})'

class ExpenseManager:
  ''' Managers the expenditure and income classes'''
  def __init__(self):
    self.expenses = []
    self.incomes = []
    
  def add_income(self, amount:float,income_source=''):
    self.incomes.append(Income(round(amount,2),income_source))
    
  def add_expense(self, amount:float,description='',category=''):
    self.expenses.append(Expenditure(round(amount,2),description,category))

  def show_account(self):
    self.total_income = round(sum([i.amount for i in self.incomes]),2)
    self.total_expenses = round(sum([i.amount for i in self.expenses]),2)
    self.balance = self.total_income - self.total_expenses
    # self.bal = f'Total Income: {self.total_income} \nTotal Expenses: {self.total_expenses} \nBalance: {self.balance}'
    return {'Total Income':self.total_income, 'Total Expenses':self.total_expenses, 'Balance':self.balance}
  
  def show_expenses(self):
    clean_expenses = []
    for e in self.expenses:
      clean_expenses.append( {'id':e.expend_id, 'created':e.created, 'modified':e.modified,'amount':e.amount, 'description':e.description, 'category':e.category,  })
    return clean_expenses

  def show_income(self):
    clean_income = []
    for income in self.incomes:
      clean_income.append( {'id':income.income_id, 'created':income.created, 
      'modified':income.modified,'amount':income.amount,  'source':income.income_source,  })
    return clean_income

  def modify_income(self, id, amount:float,source=''):
      for income in self.incomes:
        if income.income_id == id:
          income.amount = round(amount,2)
          if source != '':
            income.income_source = source
            break
        else:
          print('No such Id in the database')
  
  def modify_expense(self, id, amount:float, description:str='',category:str=''):
        for expend in self.expenses:
          if expend.expend_id == id:
            expend.modified = datetime.today().date()
            expend.amount = round(amount,2)
            if description != '':
              expend.description = description
            if category != '':
              expend.category = category
            break 

# NO NEED FOR NOW    
  def search_expense_by_id(self,id):
    for e in self.expenses:
      if id == e.expend_id:
        return True
    return False

  def search_expense_by_category(self,cat:str):
    found = []
    for e in self.expenses:
      if cat.lower() in e.category:
        found.append(e)
    return found
  

