import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()
new_col_names = df.columns.str.lower().str.replace(' ', '_')
df.columns = new_col_names

output_df = df[df.Genus == 'Pomacentrus']

output_df.to_csv('b3_output1.csv', index=False)