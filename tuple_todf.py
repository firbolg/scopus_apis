import pandas as pd

data = [('Pediatrics, Perinatology and Child Health', 'MEDI', 2735),
        ('Orthopedics and Sports Medicine', 'MEDI', 2732),
        ('Anesthesiology and Pain Medicine', 'MEDI',2703),
        ('Medicine (All)', 'MEDI',2700)]

counts = [(2735, 4),(2732,2),(2700,14),(2703,6)]

df1 = pd.DataFrame(data, columns = ['area','abbreviation','code'])

df2 = pd.DataFrame(counts, columns = ['code','total'])

df3 = pd.merge(df1,df2, on='code')

print(df3)
