import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()
new_col_names = df.columns.str.lower().str.replace(' ', '_')
df.columns = new_col_names

# max_count = df.groupby('species')['count'].max().sort_values(ascending=False)

# species = df['species'].drop_duplicates()

total_count = df.groupby('species', as_index=True)['count'].sum().sort_values(ascending=False)


output_df = pd.DataFrame({'total_count' : total_count}).iloc[:1]
# output_df = pd.DataFrame({'total_count' : total_count})

output_df.to_csv('b6_output1.csv')
# max_count.to_csv('b6_output1.csv', index=False)
# total_count.to_csv('b6_output1.csv')