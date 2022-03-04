import pandas as pd
import sqlalchemy

### df = "Data Frame" - Technically any variable could be used. But, "pandas.read_sql("Table_name",configuration)" make a Data Frame so df. ### Also con = Configuration ###

con = sqlalchemy.create_engine('mysql+pymysql://root:Password123@localhost/puppies')
dfone = pd.read_sql("pups",con)
dftwo = pd.read_sql("owners",con)

#print(dfone)
#print(dftwo)

#cntone = dfone.count()
#print(cntone)
#cnttwo = dfone.count()
#print(cnttwo)


### Number of Records ###

lenone = len(dfone)
print(f"The amount of records in 'pups' table is: {lenone}")
lentwo = len(dftwo)
print(f"The amount of records in 'owners' table is: {lentwo}")

### Number of Columns ###

colpup = len(dfone.columns)
print(f"The number of columns in 'pups' table is: {colpup}")
colown = len(dftwo.columns)
print(f"The number of columns in 'owner' table is: {colown}")

### Group By ###

pupgroup = dfone.groupby(['age'])['age'].count()
print(pupgroup)
