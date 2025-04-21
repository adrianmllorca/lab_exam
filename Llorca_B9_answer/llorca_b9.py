import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()
new_col_names = df.columns.str.lower().str.replace(' ', '_')
df.columns = new_col_names  

replicates = df['replicate']
interval = df['interval']

replicate_interval = pd.DataFrame({'replicate' : replicates,
                                   'interval' : interval}).drop_duplicates().sort_values('replicate')

# output_df =df.groupby(['replicate', 'interval']).mean()

# output_df = pd.DataFrame({'replicate_interval' : replicate_interval})

# output_df.to_csv('b9_output1.csv')
replicate_interval.to_csv('b9_output1.csv', index=False)