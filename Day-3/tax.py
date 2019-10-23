"""
=================
Calculating tax of Bangladesh (Country in Asia) for a individual person.
=================
Note : Tk is Bangladeshi Currency

- On first upto  Tk. 2 50 000 -> Nil
- On next upto Tk. 4 00 000 -> 10%
- On next upto Tk. 5 00 000 -> 15%
- On next upto Tk. 6 00 000 -> 20%
- On next upto Tk. 30 00 000 -> 25%
- On balance amount 30%

For female taxpayers, senior taxpayers of age 65 years and above, income tax is payable for the

- On first upto  Tk. 3 00 000 -> Nil
- On next upto Tk. 4 00 000 -> 10%
- On next upto Tk. 5 00 000 -> 15%
- On next upto Tk. 6 00 000 -> 20%
- On next upto Tk. 30 00 000 -> 25%
- On balance amount  30%

For 'nil' tax payer
 Minimum tax for any individual assessee living in Dhaka and Chittagong City Corporation area is Tk. 5,000/-.
 Minimum tax for any individual assessee living in other City Corporations area is Tk. 4,000/-.
 Minimum tax for any individual assessee living in any other areas is Tk. 3,000/-.

 Created by IntelliJ IDEA.
 User: Enam
 Date: 10/23/2019
 Time: 12:30 PM
 """

tax = 0.0

gender_dictionary = {
    1: "Male",
    2: "Female"
}
address_dictionary = {
    1: "Dhaka and Chittagong City Corporation area",
    2: "Other city corporation",
    3: "Other areas"
}
minimum_tax_dictionary = {
    address_dictionary[1]: 5000,
    address_dictionary[2]: 4000,
    address_dictionary[3]: 3000,
}
taxable_income = int(input("Enter your yearly income (eg. 350000) : "))  # getting taxable income
gender = int(input("Choose your gender (eg. 2) \n1.Male \n2.Female \n"))
age = int(input("Enter your age : "))
address = int(input("Choose your address (eg. 2)\n1.Dhaka and Chittagong City Corporation area \n2.Other city "
                    "corporation\n3.Other areas\n"))

is_special = True if gender_dictionary[gender] == gender_dictionary[2] else (True if age >= 65 else False)
taxable_threshold = 300000 if is_special else 250000
exceed_taxable = taxable_income - taxable_threshold
print(exceed_taxable)
if taxable_income < taxable_threshold:
    tax = 0.0
elif taxable_threshold <= taxable_income <= 400000:
    tax = (exceed_taxable * 10) / 100
elif 400000 < taxable_income <= 500000:
    tax = (exceed_taxable * 15) / 100
elif 500000 < taxable_income <= 600000:
    tax = (exceed_taxable * 20) / 100
elif 600000 < taxable_income <= 3000000:
    tax = (exceed_taxable * 25) / 100
else:
    tax = (exceed_taxable * 30) / 100

if tax < 5000:
    tax = minimum_tax_dictionary[address_dictionary[address]]

print("Your individual tax as Bangladeshi is : %.2f BDT (Bangladeshi Taka)" % tax)
