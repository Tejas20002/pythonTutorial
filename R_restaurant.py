import os, sys
from fpdf import FPDF

name = input("Enter the Name:- ")
ph = int(input("Enter the Phone Number:- "))

choice_last = []
qty_last = []
dict_menu = {1: 'Dosa', 2: 'Pani Puri', 3: 'Maggi', 4: 'Ice Cream', 5: 'Coffee', 6: 'Half Tea'}
dict_price = {1: 30, 2: 30, 3: 50, 4: 30, 5: 40, 6: 10}

pdf = FPDF('L', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 14)

print("Menu RDX Hotel")
print("--------------------------------")
for s in dict_menu:
    menu_price = dict_price[s]
    print(f"""{s} {dict_menu[s]}:- {menu_price}""")
print("--------------------------------\n")

while (1):
    try:
        a = input('Do you want to order?(Y/N)')
    except:
        continue
    if (a == 'y' or a == 'Y'):
        try:
            choice = int(input('Enter choice:- '))
        except:
            continue
        if (choice >= 1 and choice <= 6):
            try:
                qty = int(input('How much qty do you need:'))
            except:
                continue

            if (qty >= 1):
                choice_last.append(choice)
                qty_last.append(qty)
                print('\n')

            else:
                print('Invalid order chose! \n')
                continue

        else:
            print('Invalid \n')
            continue

    elif (a == 'n' or a == 'N'):
        pdf.cell(40, 10, 'Rdx Hotel', ln=1)
        pdf.cell(40, 10, 'BILL:', ln=1)
        pdf.cell(40, 10, '------------------------------------------------------------------------------------------------', ln=1)
        total = 0
        length = len(choice_last)

        for i in range(0, length):
            val = choice_last[i]
            bill_print = f"""{i+1} {dict_menu[val]}     |     Qty:- {qty_last[i]}     |     Rs:- {dict_price[val]} per unit"""
            pdf.cell(40,10, bill_print, ln=1)
            pdf.cell(40,10, "------------------------------------------------------------------------------------------------", ln=1)
            total = total + (dict_price[val] * qty_last[i])
        bill_prints = f"Total = Rs. {total}"
        pdf.cell(40, 10, bill_prints, ln=1)
        print('Thank you')
        pdf.output(name+'_'+str(ph)+'.pdf')
        break

    else:
        print("Wrong input \n")
        continue
