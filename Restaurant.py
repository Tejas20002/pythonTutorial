# import the library that, I have install. Command line to install FPDF library is: pip install fpdf2
from fpdf import FPDF

# create the class of TejaHotel
class TejaHotel:
    # construct the function
    def __int__(self):
        # print message the starting of program
        print("----------Welcome Teja Hotel----------\n")
        # take info of user by input function
        self.name = input("Customer Name: ")
        self.phone = int(input("Customer Phone Number: "))
        # declare the variable and it's value
        self.dict_menu = {1: 'Dosa', 2: 'Pani Puri', 3: 'Maggi', 4: 'Ice Cream', 5: 'Coffee', 6: 'Half Tea'}
        self.dict_price = {1: 30, 2: 30, 3: 50, 4: 30, 5: 40, 6: 10}
        print("\nMenu Teja Hotel")
        # for loop for print the menu in the display
        for s in self.dict_menu:
            menu_price = self.dict_price[s]
            print(f"""{s}) {self.dict_menu[s]}:- {menu_price}""")
        print("--------------------------------\n")

    # define the function of restaurant
    def restaurant(self):
        # call the construct function
        self.__int__()

        # declare the variable
        choice_last = []
        qty_last = []
        # call the fpdf class
        pdf = FPDF('L', 'mm', 'A4')
        # add the page in the pdf
        pdf.add_page()
        # set the font in pdf
        pdf.set_font('Arial', 'B', 14)
        # loop for continue program
        while (1):
            # input for order food or not
            order = input('Do you want to order?(Y/N)')
            # if condition, order value is yes
            if order == 'y' or order == 'Y':
                # input for choice from menu value
                choice = int(input('Enter choice:- '))
                # if condition choice is not less length of the dict_menu and greater than 0
                if choice >= 1 and choice <= 6:
                    # input for qty for person
                    qty = int(input('How much qty do you need:'))
                    # if condition, qty is greater then 0
                    if qty >= 1:
                        # person choice item will append in the dict
                        choice_last.append(choice)
                        qty_last.append(qty)
                        print('\n')
                    else:
                        # invalid qty choose error
                        print('Invalid Qty chose! \n')
                        continue
                else:
                    # invalid menu choose error..
                    print('Invalid! See the Menu carefully....!\n')
                    continue
            # if condition, order value is no
            elif order == 'n' or order == 'N':
                # cell function is for create the line in the pdf
                # pdf.cell(width, height, text, ln=line)
                pdf.cell(40, 10, 'Teja Hotel', ln=1)
                pdf.cell(40, 5, f"Bill Person Name:- {self.name}", ln=1)
                pdf.cell(40, 5, f"Bill Person Phone Number:- {self.phone}", ln=1)
                pdf.cell(40, 10, "", ln=1)
                pdf.cell(40, 5,
                         '------------------------------------------------------------------------------------------------',
                         ln=1)
                total = 0
                # choice_last length
                length = len(choice_last)
                # loop for to calculate the bill of customer
                for i in range(0, length):
                    # val is for store the value of i variable
                    val = choice_last[i]
                    bill_print = f"""{i + 1} {self.dict_menu[val]}     |     Qty:- {qty_last[i]}     |     Rs:- {self.dict_price[val]} per unit"""
                    pdf.cell(40, 5, bill_print, ln=1)
                    pdf.cell(40, 5,
                             "------------------------------------------------------------------------------------------------",
                             ln=1)
                    # total value of bill
                    total = total + (self.dict_price[val] * qty_last[i])
                # total amount of bill
                pdf.cell(40, 5, f"Total Food Bill= Rs. {total}", ln=1)
                pdf.cell(40, 5, f"Total GST 5%:- {total * 0.05}", ln=1)
                pdf.cell(40, 5, f"Total Amount:- {total + (total * 0.05)}", ln=1)
                pdf.output(self.name + '_' + str(self.phone) + '.pdf')
                break
            else:
                # quit the program
                quit()
# create the object of class TejaHotel
restaurant = TejaHotel()
# call the function restaurant of class TejaHotel
restaurant.restaurant()