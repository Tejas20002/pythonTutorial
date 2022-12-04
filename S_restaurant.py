# import the library that, I have install. Command line to install FPDF library is: pip install fpdf2
from fpdf import FPDF
# create the class
class hotelfarecal:
    # construct the function
    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1800, name='', address='', rno=101):
        # welcome message
        print("\n\n*****WELCOME TO Aanadma HOTEL*****\n")
        # declaration of variable
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.rno = rno
        # end of variable declaration

    # function for user information
    def inputdata(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your address:")
        print("Your room no.:", self.rno, "\n")

    # function for to calculate the bill of food order
    def restaurentbill(self):
        # display the menu in console
        print("*****RESTAURANT MENU*****")

        print("1.water----->Rs20", "2.tea----->Rs10", "3.breakfast combo--->Rs90", "4.lunch---->Rs110",
              "5.dinner--->Rs150", "6.Exit")
        # start loop
        # continue the program
        while (1):
            # input for choice of order
            c = int(input("Enter your choice:"))
            # here is the condition for choice the food
            if (c == 1):
                # input for annuity of food
                d = int(input("Enter the quantity:"))
                self.r = self.r + 20 * d

            elif (c == 2):
                # input for annuity of food
                d = int(input("Enter the quantity:"))
                self.r = self.r + 10 * d

            elif (c == 3):
                # input for annuity of food
                d = int(input("Enter the quantity:"))
                self.r = self.r + 90 * d

            elif (c == 4):
                # input for annuity of food
                d = int(input("Enter the quantity:"))
                self.r = self.r + 110 * d

            elif (c == 5):
                # input for annuity of food
                d = int(input("Enter the quantity:"))
                self.r = self.r + 150 * d

            elif (c == 6):
                break
            else:
                print("Invalid option")
        # end of loop
        # total food bill amount printed
        print("Total food Cost=Rs", self.r, "\n")

    def gamebill(self):
        # display the game list
        print("******GAME MENU*******")

        print("1.Table tennis----->Rs60", "2.Bowling----->Rs80", "3.Snooker--->Rs70", "4.Video games---->Rs90",
              "5.Pool--->Rs50==6", "6.Exit")
        # loop start
        # continue the program
        while (1):
            # input for select the game
            g = int(input("Enter your choice:"))

            if (g == 1):
                # input for hours of game play
                h = int(input("No. of hours:"))
                self.p = self.p + 60 * h

            elif (g == 2):
                # input for hours of game play
                h = int(input("No. of hours:"))
                self.p = self.p + 80 * h

            elif (g == 3):
                # input for hours of game play
                h = int(input("No. of hours:"))
                self.p = self.p + 70 * h

            elif (g == 4):
                # input for hours of game play
                h = int(input("No. of hours:"))
                self.p = self.p + 90 * h

            elif (g == 5):
                # input for hours of game play
                h = int(input("No. of hours:"))
                self.p = self.p + 50 * h
            elif (g == 6):
                break
            else:
                print("Invalid option")
        # end of loop
        # total bill of game printed
        print("Total Game Bill=Rs", self.p, "\n")

    # function to generate pdf
    def display(self):
        pdf = FPDF('L', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)

        pdf.cell(40, 10, "******HOTEL BILL******", ln=1)
        pdf.cell(40, 10, "Customer details:", ln=1)
        pdf.cell(40, 10, f"Customer name:{self.name}", ln=1)
        pdf.cell(40, 10, f"Customer address:{self.address}", ln=1)
        pdf.cell(40, 10, f"Your Food bill is: {self.r}", ln=1)
        pdf.cell(40, 10, f"Your Game bill is: {self.p}", ln=1)
        self.rt =  self.p + self.r
        pdf.cell(40, 10, f"Your sub total bill is: {self.rt}", ln=1)
        pdf.cell(40, 10, f"Additional Service Charges is {self.a}", ln=1)
        pdf.cell(40, 10, f"Your grandtotal bill is: {self.rt + self.a}", ln=1)
        pdf.output(self.name + '.pdf')
        self.rno += 1

# main function of program
def main():
    # create the object of class
    a = hotelfarecal()

    # loop start
    # continue the program
    while (1):
        print("1.Enter Customer Data")
        print("2.Calculate restaurant bill")
        print("3.Calculate gamebill")
        print("4.Show total cost")
        print("5.EXIT")
        # input for upper option choice
        b = int(input("\nEnter your choice:"))
        if (b == 1):
            # call function collect the information of user
            a.inputdata()
        if (b == 2):
            # call function calculate the restaurant bill
            a.restaurentbill()
        if (b == 3):
            # call function calculate the game bill
            a.gamebill()
        if (b == 4):
            # call function generate the bill in pdf
            a.display()
        if (b == 5):
            # ecit the program
            quit()
    # end of loop
# call the main function
main()

