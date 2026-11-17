class Patient:
    def __init__(self, name, bill_amount):
        self.name = name
        self.bill_amount = bill_amount

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_bill_amount(self):
        return self.bill_amount

    def set_bill_amount(self, bill_amount):
        self.bill_amount = bill_amount

    def calculate_bill(self):
        return self.bill_amount

    def display_patient_type(self):
        return "Regular Patient"

class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        discount = 0.2
        discounted_amount = self.bill_amount * (1 - discount)
        return discounted_amount

    def display_patient_type(self):
        return "Senior Patient"

class PhilHealthMember(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        discount = 0.15
        discounted_amount = self.bill_amount * (1 - discount)
        return discounted_amount

    def display_patient_type(self):
        return "PhilHealth Member"

regularPatient = Patient("Juan Dela Cruz", 15000)
seniorPatient = SeniorPatient("Maria Santos", 15000)
philHealthMember = PhilHealthMember("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----------------------")
print(f"Patient Name: {regularPatient.get_name()}")
print(f"Patient Type: {regularPatient.display_patient_type()}")
print(f"Original Bill: ₱{regularPatient.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{regularPatient.calculate_bill():,.2f}")
print("-----------------------")
print(f"Patient Name: {seniorPatient.get_name()}")
print(f"Patient Type: {seniorPatient.display_patient_type()}")
print(f"Original Bill: ₱{seniorPatient.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{seniorPatient.calculate_bill():,.2f}")
print("-----------------------")
print(f"Patient Name: {philHealthMember.get_name()}")
print(f"Patient Type: {philHealthMember.display_patient_type()}")
print(f"Original Bill: ₱{philHealthMember.get_bill_amount():,.2f}")
print(f"Final Bill: ₱{philHealthMember.calculate_bill():,.2f}")

