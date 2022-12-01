from fpdf import FPDF
class hotelfarecal:

    def __init__(self, rt='', s=0, p=0, r=0, t=0, a=1800, name='', address='', rno=101):
        print("\n\n*****WELCOME TO Aanadma HOTEL*****\n")
        self.rt = rt
        self.r = r
        self.t = t
        self.p = p
        self.s = s
        self.a = a
        self.name = name
        self.address = address
        self.rno = rno

    def inputdata(self):
        self.name = input("\nEnter your name:")
        self.address = input("\nEnter your address:")
        print("Your room no.:", self.rno, "\n")

    def restaurentbill(self):

        print("*****RESTAURANT MENU*****")

        print("1.water----->Rs20", "2.tea----->Rs10", "3.breakfast combo--->Rs90", "4.lunch---->Rs110",
              "5.dinner--->Rs150", "6.Exit")

        while (1):

            c = int(input("Enter your choice:"))

            if (c == 1):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 20 * d

            elif (c == 2):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 10 * d

            elif (c == 3):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 90 * d

            elif (c == 4):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 110 * d

            elif (c == 5):
                d = int(input("Enter the quantity:"))
                self.r = self.r + 150 * d

            elif (c == 6):
                break
            else:
                print("Invalid option")

        print("Total food Cost=Rs", self.r, "\n")

    def gamebill(self):
        print("******GAME MENU*******")

        print("1.Table tennis----->Rs60", "2.Bowling----->Rs80", "3.Snooker--->Rs70", "4.Video games---->Rs90",
              "5.Pool--->Rs50==6", "6.Exit")

        while (1):

            g = int(input("Enter your choice:"))

            if (g == 1):
                h = int(input("No. of hours:"))
                self.p = self.p + 60 * h

            elif (g == 2):
                h = int(input("No. of hours:"))
                self.p = self.p + 80 * h

            elif (g == 3):
                h = int(input("No. of hours:"))
                self.p = self.p + 70 * h

            elif (g == 4):
                h = int(input("No. of hours:"))
                self.p = self.p + 90 * h

            elif (g == 5):
                h = int(input("No. of hours:"))
                self.p = self.p + 50 * h
            elif (g == 6):
                break

            else:

                print("Invalid option")

        print("Total Game Bill=Rs", self.p, "\n")

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

def main():
    a = hotelfarecal()

    while (1):
        print("1.Enter Customer Data")
        print("2.Calculate restaurant bill")
        print("3.Calculate gamebill")
        print("4.Show total cost")
        print("5.EXIT")
        b = int(input("\nEnter your choice:"))
        if (b == 1):
            a.inputdata()
        if (b == 2):
            a.restaurentbill()
        if (b == 3):
            a.gamebill()
        if (b == 4):
            a.display()
        if (b == 5):
            quit()
main()

