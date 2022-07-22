import gspread

gc = gspread.service_account(filename='jumia.json')
sh = gc.open('jumia').sheet1

sh.append_row(['Items Name','Amount','Ratings and Review',"Stock","Links"])