from fpdf import FPDF
class TejaHotel:

    def __int__(self):
        print("----------Welcome Teja Hotel----------\n")
        self.name = input("Customer Name: ")
        self.phone = int(input("Customer Phone Number: "))
        self.dict_menu = {1: 'Dosa', 2: 'Pani Puri', 3: 'Maggi', 4: 'Ice Cream', 5: 'Coffee', 6: 'Half Tea'}
        print("\nMenu Teja Hotel")
        self.dict_price = {1: 30, 2: 30, 3: 50, 4: 30, 5: 40, 6: 10}
        for s in self.dict_menu:
            menu_price = self.dict_price[s]
            print(f"""{s}) {self.dict_menu[s]}:- {menu_price}""")
        print("--------------------------------\n")

    def restaurant(self):
        self.__int__()
        choice_last = []
        qty_last = []

        pdf = FPDF('L', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 14)
        while (1):
            order = input('Do you want to order?(Y/N)')
            if (order == 'y' or order == 'Y'):
                choice = int(input('Enter choice:- '))
                if (choice >= 1 and choice <= 6):
                    qty = int(input('How much qty do you need:'))
                    if (qty >= 1):
                        choice_last.append(choice)
                        qty_last.append(qty)
                        print('\n')
                    else:
                        print('Invalid Qty chose! \n')
                        continue
                else:
                    print('Invalid! See the Menu carefully....!\n')
                    continue
            elif (order == 'n' or order == 'N'):
                pdf.cell(40, 10, 'Teja Hotel', ln=1)
                pdf.cell(40, 5, f"Bill Person Name:- {self.name}", ln=1)
                pdf.cell(40, 5, f"Bill Person Phone Number:- {self.phone}", ln=1)
                pdf.cell(40, 10, "", ln=1)
                pdf.cell(40, 5,
                         '------------------------------------------------------------------------------------------------',
                         ln=1)
                total = 0
                length = len(choice_last)
                for i in range(0, length):
                    val = choice_last[i]
                    bill_print = f"""{i + 1} {self.dict_menu[val]}     |     Qty:- {qty_last[i]}     |     Rs:- {self.dict_price[val]} per unit"""
                    pdf.cell(40, 5, bill_print, ln=1)
                    pdf.cell(40, 5,
                             "------------------------------------------------------------------------------------------------",
                             ln=1)
                    total = total + (self.dict_price[val] * qty_last[i])
                pdf.cell(40, 5, f"Total Food Bill= Rs. {total}", ln=1)
                pdf.cell(40, 5, f"Total GST 5%:- {total * 0.05}", ln=1)
                pdf.cell(40, 5, f"Total Amount:- {total + (total * 0.05)}", ln=1)
                pdf.output(self.name + '_' + str(self.phone) + '.pdf')
                break
            else:
                quit()
restaurant = TejaHotel()
restaurant.restaurant()