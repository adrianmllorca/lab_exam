import pandas as pd  # type: ignore

df = pd.read_csv('Exam_Table.csv').dropna()
new_col_names = df.columns.str.lower().str.replace(' ', '_')
df.columns = new_col_names

species = df['species'].drop_duplicates().to_list()

ave_size_est = df.groupby('species')['size_est_(cm)'].mean().to_list()

output_df = pd.DataFrame({'species' : species,
                          'average_size_est_(cm) ' : ave_size_est})

output_df.to_csv('b5_output1.csv', index=False)