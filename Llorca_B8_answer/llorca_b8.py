import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()
new_col_names = df.columns.str.lower().str.replace(' ', '_')
df.columns = new_col_names

output_df = df[df['visibility_(m)'] > 8.0]

output_df.to_csv('b8_output1.csv', index=False)