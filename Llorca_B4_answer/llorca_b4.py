import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()
new_col_names = df.columns.str.lower().str.replace(' ', '_')
df.columns = new_col_names

# sci_names = df['scientific_name'].drop_duplicates().to_list()

# total_count = df.groupby('scientific_name')['count'].sum().to_list()

total_count = df.groupby('scientific_name', as_index=True)['count'].sum()

output_df = pd.DataFrame({'total_count' : total_count})

output_df.to_csv('b4_output1.csv')