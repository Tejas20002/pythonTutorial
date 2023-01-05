import pdfkit
import pandas as pd
# for windows users uncomment line
# conf = pdfkit.configuration(wkhtmltopdf='PATH_OF_WKHTMLTOPDF_APP_FILE')
data = pd.read_csv('./data.csv')
rowcount  = 0
for row in open("./data.csv"):
    pdfkit.from_url(data.url[rowcount],data.name[rowcount]+".pdf") # add the "configuration = config" for window users
    rowcount+=1