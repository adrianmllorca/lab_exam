import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()

output_df = df[df.Genus == 'Pomacentrus']

output_df.to_csv('b3_output1.csv', index=False)