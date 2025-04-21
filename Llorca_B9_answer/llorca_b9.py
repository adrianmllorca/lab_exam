import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()
new_col_names = df.columns.str.lower().str.replace(' ', '_')
df.columns = new_col_names  

replicates = df['replicate']
interval = df['interval']
count = df['count']

filtered_df = pd.DataFrame({'replicate' : replicates,
                                   'interval' : interval,
                                   'count' : count}).drop_duplicates().sort_values('replicate')

average_count = df.groupby()

# output_df = pd.DataFrame({'replicate_interval' : replicate_interval})

# output_df.to_csv('b9_output1.csv')
filtered_df.to_csv('b9_output1.csv', index=False)