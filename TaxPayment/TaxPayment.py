
class Person :
    def __init__(self, id_no):
        self.id_no = id_no
    def pay_tax(self,taxable_income,tax_rate):
        tax = taxable_income * tax_rate
        print('The tax is $ ' +str(tax) )
        return tax
class Businessman(Person):
    def pay_tax(self,taxable_income,business_allowance,tax_rate):
        tax = (taxable_income - business_allowance)* tax_rate
        print('The tax is $ ' +str(tax))
        return tax
class Employee(Person):
    def refund_tax(self,amount):
        print('The amount of refund is $  ' +str(amount))
        return amount

tata_businessman = Businessman('A12233')
tata_tax = tata_businessman.pay_tax(60000,8000,0.3)

alex_self_employed = Person('P68342')
alex_tax = alex_self_employed.pay_tax(40000,0.25)

rituja_employee = Employee('R51097')
rituja_tax = rituja_employee.pay_tax(50000,0.2)
rituja_refund = rituja_employee.refund_tax(2000)