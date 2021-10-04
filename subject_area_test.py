import pandas as pd
from pybliometrics.scopus import AuthorSearch, AuthorRetrieval

df = pd.read_csv(r'C:\Users\dolanl\Projects\Scopus_API\a_test.csv')

#pd.set_option('display.max_columns', None)
#df_names['Scopus_ID'] = df_names.apply(AuthorSearch('AUTHLAST(Faculty Last Name[])' and 'AUTHFIRST(Faculty First Name[])'))

#find_auth = AuthorSearch('AUTHLAST(Hardacker) and AUTHFIRST(Doris)')

#print(find_auth)

#au = AuthorRetrieval(6505808971)
#for index, row in df.iterrows():
    #au = AuthorSearch('AUTHLAST(' + row['Faculty Last Name'] + ') and AUTHFIRST(' + row['Faculty First Name'] + ')')
#print(au)    

au_list = [6505808971,6506552389,6602261254]

def get_info(scopus_id):
    au = AuthorRetrieval(scopus_id)
    df1 = pd.DataFrame(au.affiliation_current)
    #df2 = pd.DataFrame(au.affiliation_history)
    df3 = pd.DataFrame(au.subject_areas)
    frames = [df1, df3]
    df_all = pd.concat(frames)

    return df_all

au = AuthorRetrieval(6505808971)

#print('Citations: ', au.citation_count, 'Documents: ', au.document_count, 'h-index: ', au.h_index, 'ORCID: ', au.orcid, 
#'Publication Range: ', au.publication_range)
#test = get_info(6505808971)

#test.to_csv(r'C:\Users\dolanl\Projects\Scopus_API\test2.csv')
#print(au.get_coauthors())
#au = AuthorRetrieval(6602261254, view='ENHANCED')
#coauthors = pd.DataFrame(au.get_coauthors())
#docs = pd.DataFrame(au.get_documents(refresh=7)


docs = pd.DataFrame(au.get_documents())

docs.to_csv(r'C:\Users\dolanl\Projects\Scopus_API\docs2.csv')
 
    #pd.set_option('display.max_columns', None)
    

