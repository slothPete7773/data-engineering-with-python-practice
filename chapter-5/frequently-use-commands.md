# What I learn from Chapter 5? Cleaning, Transforming, and Enriching Data

## Recap of the previous chapter

## Intro of this chapter

This chapter will primary focus on performing exploratory data analysis, or simply speaking, analyzing  data using `Pandas`. 

The chapter will provide ground knowledge of how we can view and analyze data, finding issues within the data, fixing those issues, and filtering out unwanted parts of data.

## Exploring data in `Pandas`

> *`DataFrame.columns`*

***Return: List of columns***

Listing column names of the DataFrame.

---

> *`DataFrame.dtypes`*

***Return: types of each column***

Listing all columns and their type.

---

> *`DataFrame.head() | DataFrame.tail()`*

***Return: A sample of dataframe.***

Give a sameple of the DataFrame from either first-end or last-end of the DataFrame.

---

> *`DataFrame.describe()`*

***Return: DataFrame***

Return a DataFrame of numeric summary of numeric data in the given DataFrame. 

---

> *`DataFrame[<column name>].describe()`*

***Return: Series***

Describe a single column of the dataframe.

---

> *`DataFrame[<column name>].value_counts()`*

- Parameters:
    - normalize: [True, False *(default)*]
        - Statistically normalizing numbers of counting.
    - dropna: [True *(default)*, False]
        - Do not count the null, NaN, whatever. Otherwise the funciton will count them and call them `NaN`.
    - bins: Number of bin(Interval)
        - Create a bin interval for statistical computation(Not often use, maybe).

***Return: Series***

Return a count of each element in the given column of the DataFrame.

---

> *`DataFrame.isnull()`*

***Return: Series***

Return a series of the column from the DataFrame with Boolean value.

Usually combine with other function to get DataFrame's rows which value is NaN only, or the opposite, get DataFrame's rows which value is not Nan only.

**Example**
> *`DataFrame[df[<column name>].isnull()]`* : To get rows that the given column contains NaN only

> *`DataFrame[df[<column name>].isnull()==False]`* : To get rows that the given column does not contain NaN only

> *`DataFrame.where(df[<column name>].isnull())`*

---

> *`DataFrame.isnull().sum()`*

***Return: Series***

Return a serie contain column names and their NaN counts.



## Common setting in Pandas DataFrame

> *`pandas.set_option('<Options>', <Number>)`*

- Options:
    - `'display.max_columns'`
    - `'display.max_rows'`


***Return: None***

Set the maximum of columns or rows show when viewing a DataFrame.



## Viewing and Indexing the DataFrame

> *`DataFrame['<column name>'] | DataFrame['<column name>', '<column name>', ...(more)]`*

***Return: The DataFrame with given columns***

A regular way to viewing the DataFrame

---

> *`DataFrame[<start>:<end>]`*

***Return: Sliced of the DataFrame***

Get the sliced of DataFrame from `start index` till the `end index`.

---

> *`DataFrame.loc[<number of index>]`*

***Return: A serie of a row of the DataFrame***

Get a row of the DataFrame at an exact row.

---

> *`DataFrame.at[<number of index>, '<column name>']`*

***Return: Object | Value***

Just get a value of the given index at the given column

---

> *`DataFrame.where(<Conditional operation against the DataFrame>)`*

> *`DataFrame.where(df['number'] > 123)`*

> *`DataFrame.where(df['user_id'] == 123)`*

> *`DataFrame.where(<Condition 1> and <Condition 2>`*

***Return: DataFrame***

Return the DataFrame with all data but the result DataFrame will replace value that do not meet criteria as `NaN`.

---

> *`DataFrame[<Condition agains DataFrame>`*

> *`DataFrame[<Condition 1> and <Condition 2>`* 

***Return: DataFrame***

Return the DataFrame with only rows that meet the criteria, unlike the `DataFrame.where()` that will contain the whole DataFrame.


## Manipulate the DataFrame

> *`DataFrame.drop(...)`*

> *`DataFrame.drop(index=df[(df['month']=='May')].index,inplace=True)`* : Drop the rows that is May.

- Parameters:
    - columns= ['col name', 'col name', ...]
    - index= [row num, row num, ...]
    - inplace= [True, False] : Specify whether to mutate the original DataFrame or return copy of original.

***Return: DataFrame***

The function will drop the specified rows or columns and return the resulting DataFrame.

---

> *`DataFrame.dropna(...)`*

- Parameters:
    - axis= [0 (on row)(*Default*), 1 (on col)]
    - how= [all (all values are null), any (some values are null)(*default*)]
    - thresh= integer xnumber : at least **n** nulls must meet to drop
    - subset= [colname, colname, ...]
    - inplace= [True, False]

***Return: DataFrame***

The function will drop only rows or columns that contain NaN, other parameters can be provided for more accurate drop.

---

> *`DataFrame.fillna(...)`*

- parameters:
    - value= [(single value) | Dict{'col name': 'value', ...}]
    - method= [None (*default*) | {‘backfill’, ‘bfill’, ‘pad’, ‘ffill’}]
    - axis= [0, 1]
    - inplace= 

***Return: DataFrame | None***

Fill NA/NaN value(s) in columns or rows with the specified value(s)

---

### Creating and modifying columns

> *`df.columns = [col.lower() for col in df.columns]`*

***Return: None***

This code piece is mutating the column names of the DataFrame

---

> *`DataFrame.rename()`*

- parameters:
    - index= Dict-like{'col name': 'value'} | function 
    - column= Dict-like{'col name': 'value'} | function 
    - inplace


***Return: DataFrame | None***

Return a DataFrame that given columns is already renamed 

---

> *`DataFrame['col name'].str.split()`*

- parameters:
    - expand= [True, False (*default*)]

***Return: Mutate***

Write something

---

> *`Pandas.to_datetime(<DataFrame['col name']>, format='<...>')`*

Example

> *`DataFrame['started_at'] = Pandas.to_datetime(df['started_at'], format='%m/%d/%Y %H:%M')`*

- parameters:
    - format= any format you want. -> %m(month) %d(day) %Y(Year) %H(Hour) %M(Minute)

***Return: Mutate the DataFrame attributes***

Just setting the plain text in date format to be the datetime data type.
---

> *`DataFrame.join(...)`*

Example

> *`joint_dataFrame =new.join(other=geo,how='left' lsuffix='_left',rsuffix='_geo_right')`*

- parameters:
    - other= DataFrame to be joined with
    - how= [’left’ (*default*), ‘right’, ‘outer’, ‘inner’] 
    - lsuffix= String | "" by default : The column suffix for left DataFrame
    - rsuffix= String | "" by default : The column suffix for right DataFrame  

***Return: DataFrame***

Join 2 DataFrames as you would do in SQL.

---

> *`Pandas.merge(<left DataFrame>, <right DataFrame>, on='col to be merged on')`*

- parameters: 
    - right
***Return: something***

Write something

---

> *`something`*

***Return: something***

Write something

---

> *`something`*

***Return: something***

Write something
---

> *`something`*

***Return: something***

Write something

---

> *`something`*

***Return: something***

Write something

---

> *`something`*

***Return: something***

Write something

---

> *`something`*

***Return: something***

Write something
---

> *`something`*

***Return: something***

Write something

---

> *`something`*

***Return: something***

Write something

---

> *`something`*

***Return: something***

Write something

---

> *`something`*

***Return: something***

Write something

