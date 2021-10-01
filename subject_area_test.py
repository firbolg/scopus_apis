from pybliometrics.scopus import AuthorRetrieval
import pandas as pd

df = pd.read_csv(r'C:\Users\Levi\source\repos\Scopus_API\test_authors.csv')

#for i in df['Scopus_ID']:
    #au = AuthorRetrieval(i)
    #print(au)

print(AuthorRetrieval(6505808971))

