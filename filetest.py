import pandas as pd

# load the excel file NOTE: the file path
xls_file = pd.ExcelFile('20170602_02.xlsx')

#全部工作表名稱 資料型態為 list
xlsit = xls_file.sheet_names

#工作表數量
xls_len = len(xls_file.sheet_names)



for le in xlsit:

    xls_df = xls_file.parse(le)

    ss = xls_df.__str__()

    #print(len(ss.index()))

    file = open(le+'.txt', 'w', encoding='UTF-8')
    file.write(str(ss))
    file.close()












'''
# print out the sheets this excel file have
print(xls_file.sheet_names)
# parse the first sheet into dataframe
xls_df = xls_file.parse(xls_file.sheet_names[0])

# 印出前五筆資料
print(xls_df.head(n=54))
# 印出Dataframe的Header
print(xls_df.columns.values)
# 印出Dataframe的資料數量
print(xls_df.size)
# 印出Dataframe的維度
print(xls_df.shape)
# 印出Dataframe的資料筆數
print(len(xls_df))
'''
'''
for row in range(0, 5):
    print(xls_df.loc[row]
          #xls_df.loc[row, 'Code_ID'],
          #xls_df.loc[row, 'Content'],
          #xls_df.loc[row, 'Description']
    )
'''