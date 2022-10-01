"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    # contract type can only be "salary" or "hourly"

    def __init__(self, name, monthly_salary=0, hourly_pay=0, payment_type="salary", hours=0, commission_type="", commission=0, num_contracts=0, pay_per_contract=0):
        self.name = name
        self.payment_type = payment_type
        self.hours = hours
        self.commission_type = commission_type
        self.commission = commission
        self.num_contracts = num_contracts
        self.pay_per_contract = pay_per_contract
        self.hourly_pay = hourly_pay
        self.monthly_salary = monthly_salary
        self.pay = 0

        self.calculate_salary()

    # calculates final salary
    def calculate_salary(self):
        if(self.payment_type == "salary"):
            self.pay += self.monthly_salary
        if self.payment_type == "hourly":
            self.pay += self.hourly_pay * self.hours
        if(self.commission_type == "fixed"):
            self.pay += self.commission
        if self.commission_type == "contracts":
            self.pay += self.num_contracts * self.pay_per_contract
    # Get final salary

    def get_pay(self):
        return self.pay

    def __str__(self):
        finalString = ""
        if(self.payment_type == "salary" and self.commission_type == ""):
            finalString += "{name} works on a monthly salary of {monthly_pay}.".format(
                name=self.name, monthly_pay=self.monthly_salary)

        if(self.payment_type == "hourly" and self.commission_type == ""):
            finalString += "{name} works on a contract of {hours} hours at {hourly_pay}/hour.".format(
                name=self.name, hours=self.hours, hourly_pay=self.hourly_pay)

        if(self.payment_type == "salary" and self.commission_type == "fixed"):
            finalString += "{name} works on a monthly salary of {monthly_pay} and receives a bonus commission of {commission}.".format(
                name=self.name, monthly_pay=self.monthly_salary, commission=self.commission)

        if(self.payment_type == "hourly" and self.commission_type == "fixed"):
            finalString += "{name} works on a contract of {hours} hours at {hourly_pay}/hour and receives a bonus commission of {commission}.".format(
                name=self.name, hours=self.hours, hourly_pay=self.hourly_pay, commission=self.commission)

        if(self.payment_type == "salary" and self.commission_type == "contracts"):
            finalString += "{name} works on on a monthly salary of {monthly_pay} and receives a commission for {num_contracts} contract(s) at {pay_per_contract}/contract.".format(
                name=self.name, monthly_pay=self.monthly_salary, hourly_pay=self.hourly_pay, num_contracts=self.num_contracts, pay_per_contract=self.pay_per_contract)

        if(self.payment_type == "hourly" and self.commission_type == "contracts"):
            finalString += "{name} works on a contract of {hours} hours at {hourly_pay}/hour and receives a commission for {num_contracts} contract(s) at {pay_per_contract}/contract.".format(
                name=self.name, hours=self.hours, hourly_pay=self.hourly_pay, num_contracts=self.num_contracts, pay_per_contract=self.pay_per_contract)

        finalString += "Their total pay is {pay}.".format(pay=self.pay)
        return finalString


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly_salary=4000, commission_type="")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', payment_type="hourly", hourly_pay=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthly_salary=3000,
                 commission_type="contracts", pay_per_contract=200, num_contracts=4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourly_pay=25, payment_type="hourly",
               commission_type="contracts", pay_per_contract=220, num_contracts=3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthly_salary=2000,
                  commission_type="fixed", commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', payment_type="hourly", hours=120,
                 hourly_pay=30, commission_type='fixed', commission=600)


# print(str(billie))
# print(billie.get_pay())
# print(str(charlie))
# print(charlie.get_pay())
# print(str(renee))
# print(renee.get_pay())
# print(str(jan))
# print(jan.get_pay())
# print(str(robbie))
# print(robbie.get_pay())
# print(str(ariel))
# print(ariel.get_pay())
