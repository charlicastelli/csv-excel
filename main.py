import pandas as pd
 

arquivo = pd.read_csv('nomearquivo.CSV')

myfile = pd.ExcelWriter('nome.xlsx')
arquivo.to_excel(myfile, index = False)
myfile.save()