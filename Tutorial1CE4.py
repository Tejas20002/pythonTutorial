import pdfkit
import pandas as pd
data = pd.read_csv('./data.csv')
rowcount  = 0
for row in open("./data.csv"):
    pdfkit.from_url(data.url[rowcount],data.name[rowcount]+".pdf")
    rowcount+=1

# for i in range(rows):
#     for j in range(columns):
#         data.loc[i, columnHeaders[j]] = self.ui.tableWidget.item(i, j).text()
# pdfkit.from_url('https://pyfpdf.readthedocs.io/en/latest/index.html#installation','yepe.pdf') 