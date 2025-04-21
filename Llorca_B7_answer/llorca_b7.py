import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()
new_col_names = df.columns.str.lower().str.replace(' ', '_')
df.columns = new_col_names

observers = df['observer'].unique()

output_df = pd.DataFrame({'observers' : observers})

output_df.to_csv('b7_output1.csv', index=False)