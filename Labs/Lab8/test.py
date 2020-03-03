import pandas

excel_df = pandas.read_excel("manga_data.xlsx")
# print(excel_df)
# print(excel_df["title"])
# print(excel_df["title"][3])
# for column in excel_df:
#     print(column)
# print(excel_df.iterrows())  # What does the word iter here imply?
# print(type(excel_df.iterrows()))  # Does this load everything into memory?
for index, row in excel_df.iterrows():
    print(row["title"])  # what gets printed? What type is it? What elements
    # does it
#     # have?
#     print(type(row[1]))  # can this value be unpacked like a dictionary?
