import pandas as pd

### NOTE :-    pandas.read_csv() is used to read data from csv files


saad = pd.read_csv(r"C:\Users\Robotics\Desktop\Me\Python_Basics_course\quality_inspection_objects.csv")
print(type(saad))
print(saad)
row = saad.iloc[0]
print(row)


print("################################")

### NOTE :- [dataframe].iterrows() is used to get rows of dataframes

total_pass = 0
total_fail = 0

for index, row in saad.iterrows():
    print( row["Object_Name"])
    print( row["Quality_Score"])
    if row["Quality_Score"] >= 70:
        print (row["Object_Name"] , "    is Pass")
        total_pass = total_pass + 1

    else:
        print (row["Object_Name"] , "    is Fail")
        total_fail = total_fail +1
   
print("Total Pass objects " , total_pass)
print("Total Fail objects ", total_fail)














