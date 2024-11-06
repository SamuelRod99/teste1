num_countries = countries_df.shape # calculei o tamanho da tabela countries_df

continents = countries_df['continent'].unique() #diz cada elemento que esta sendo repetido na coluna continent

total_population = countries_df.population.sum() #soma ta coluna população

country_counts_df = countries_df.groupby('continent')[['location']].count() #conta a quantidade de locais em cada continente

continent_populations_df = countries_df.groupby('continent')[['population']].sum() #mostra a quantidade de população em cada continente

total_tests_missing = covid_data_df.total_tests.isna().sum() #mostra a quantidade de dados faltando (insna) na coluna total testes

combined_df = countries_df.merge (covid_data_df, on='location') #combina as tabelas contries_df e covid data atraves da coluna em comum location

highest_tests_df = combined_df.tests_per_million.nlargest(10) #pega os 10 maiores valores da coluna cases per milion da tabela cmbined

#resumo dos codigos do arquivo
pd.read_csv - Read data from a CSV file into a Pandas DataFrame object
.info() - View basic infomation about rows, columns & data types
.describe() - View statistical information about numeric columns
.columns - Get the list of column names
.shape - Get the number of rows & columns as a tuple


covid_df['new_cases'] #separou a tabela new cases
covid_df['new_cases'][246] #separa o dado numero 246 da coluna new cases

covid_df['new_cases'] - Retrieving columns as a Series using the column name
new_cases[243] - Retrieving values from a Series using an index
covid_df.at[243, 'new_cases'] - Retrieving a single value from a data frame
covid_df.copy() - Creating a deep copy of a data frame
covid_df.loc[243] - Retrieving a row or range of rows of data from the data frame
head, tail, and sample - Retrieving multiple rows of data from the data frame
covid_df.new_tests.first_valid_index - Finding the first non-empty index in a series

high_new_cases = covid_df.new_cases > 1000 # modtra os casos maiores que mil na coluna nwe cases
covid_df.drop(columns=['positive_rate'], inplace=True) # remove a coluna positiv rate, o valor true indica que tem que ser feita na orginal, false para fazer em uma copia

covid_df.new_cases.sum() - Computing the sum of values in a column or series
covid_df[covid_df.new_cases > 1000] - Querying a subset of rows satisfying the chosen criteria using boolean expressions
df['pos_rate'] = df.new_cases/df.new_tests - Adding new columns by combining data from existing columns
covid_df.drop('positive_rate') - Removing one or more columns from the data frame
sort_values - Sorting the rows of a data frame using column values
covid_df.at[172, 'new_cases'] = ... - Replacing a value within the data frame



