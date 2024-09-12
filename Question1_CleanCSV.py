import pandas as pd
from statistics import mode 

def Remove_Duplicates():
    #read the csv file
    df = pd.read_csv('CarSharing.csv')

    #code to show how many duplications were removed
    first_count = len(df)
        #the removal od the duplications
    df.drop_duplicates(inplace=True)

    final_count = len(df)
    # total number of duplications calculation 
    duplicates_removed = first_count - final_count

    #save the new df 
    df.to_csv("CarSharing.csv", index=False)
    print(f'{duplicates_removed} duplications were removed from CarSharing.csv')
    return df 


def Clean_Empty_Strings():
    #read csv file
    df = pd.read_csv('CarSharing.csv')    

    #replace the empty strings with null 
    df.replace('', pd.NA, inplace=True)

    # if the null value is in a column that contains objects
    # it will find the mode and replace the null vaue with the modal object
    # NB: in our dataset, we do not have empty strings in the columns with objects 
 
    for col in df.columns:
        if df[col].dtype == 'object':
            Modal_value = mode(df[col].dropna())
            df[col].fillna(Modal_value, inplace=True)
    # if the null value is in a column that contains numerical values (i.e. not objects)
    # it will calculate the average according to the season using .groupby
        else:
            if col != 'season':
                AVG_Values_season = df.groupby('season')[col].mean()
                df[col].fillna(df['season'].map(AVG_Values_season), inplace=True)
    #save to csv file 
    df.to_csv('CarSharing.csv', index=False)
    print(f'Empty Strings have been populated.')
    return df



#Call the function 
Remove_Duplicates() 
Clean_Empty_Strings()