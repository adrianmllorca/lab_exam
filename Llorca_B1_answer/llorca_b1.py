import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv')

df.to_csv('b1_output1.csv')