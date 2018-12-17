import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
		'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('summName-7434bb06a932.json', scope)
client = gspread.authorize(creds)

sheet = client.open("summNameDatabase").sheet1

rowdata = ["flabbyfungus07#0944","tankster22"]
index = 1
sheet.insert_row(rowdata, index)
jackname = sheet.row_values(index)
print(jackname)