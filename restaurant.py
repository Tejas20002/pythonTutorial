import os, sys
from fpdf import FPDF, HTMLMixin

if (sys.platform == "linux"):
    osUser = os.getenv('USER')
    pathToAccountData = "/home/" + osUser + "/bills/"
    fileSelectorPath = "/home/" + osUser
else:
    osUser = os.getenv('USERPROFILE')
    pathToAccountData = os.getenv('LOCALAPPDATA') + '\\bills\\'
    fileSelectorPath = osUser + "\\Desktop"
name = input("Enter the name:- ")

lst_choice = []
lst_qty = []
dict_menu = {1: 'Dosa', 2: 'Pani Puri', 3: 'Maggi', 4: 'Ice Cream', 5: 'Coffee', 6: 'Half Tea'}
dict_price = {1: 30, 2: 30, 3: 50, 4: 30, 5: 40, 6: 10}
bill_print = ""

pdf = FPDF('L', 'mm', 'A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

print("Menu Teja Hotel")
print("--------------------------------")
for s in dict_menu:
    menu_price = dict_price[s]
    print(f"""{s} {dict_menu[s]}:- {menu_price}""")
print("--------------------------------\n")

while (1):
    try:
        a = input('Do you want to order?(y/n)')
    except:
        print(f"Oops! {sys.exc_info()[0]} occured.")
        continue
    if (a == 'y' or a == 'Y'):
        try:
            choice = int(input('Enter choice:- '))
        except:
            print(f"Oops! {sys.exc_info()[0]} occured.")
            continue

        if (choice >= 1 and choice <= 6):
            try:
                qty = int(input('How much qty do you need:'))

            except:
                print(f"Oops! {sys.exc_info()[0]} occured.")
                continue

            if (qty >= 1):
                lst_choice.append(choice)
                lst_qty.append(qty)
                print('\n')

            else:
                print('Wrong Input \n')
                continue

        else:
            print('Wrong Input \n')
            continue

    elif (a == 'n' or a == 'N'):
        pdf.cell(40, 10, 'Teja Hotel', 0, 1)
        pdf.cell(40, 10, 'BILL:', 0, 1)
        pdf.cell(40, 10, '------------------------------------------------------------------------------------------------',0,1)
        total = 0
        length = len(lst_choice)

        for i in range(0, length):
            val = lst_choice[i]
            bill_print = f"""{i+1} {dict_menu[val]}          Qty:- {lst_qty[i]}            Rs:- {dict_price[val]} per unit"""
            pdf.cell(40,10, bill_print, 0, 1)
            pdf.cell(40,10, "------------------------------------------------------------------------------------------------",0 ,1)
            total = total + (dict_price[val] * lst_qty[i])
        bill_prints = f"Total = Rs. {total}"
        pdf.cell(40, 10, bill_prints, 0, 1)
        # pdf.cell(40,10, "------------------------------------------------------------------------------------------------",0 ,1)
        print('Thank you')
        # f = open(name+".pdf",'x')
        # f.write(bill_print)
        # f.close()
        pdf.output(name+'.pdf')
        break

    else:
        print("Wrong input \n")
        continue
