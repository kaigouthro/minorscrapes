

Skip to main content

On this page

# DuckDB

> DuckDB is an in-process SQL OLAP database management system.

Load a `DuckDB` query with one document per row.

[code]
```python




    #!pip install duckdb  
    


```
[/code]


[code]
```python




    from langchain.document_loaders import DuckDBLoader  
    


```
[/code]


[code]
```python




    Team,Payroll  
    Nationals,81.34  
    Reds,82.20  
    


```
[/code]


[code]
```python




        Writing example.csv  
    


```
[/code]


[code]
```python




    loader = DuckDBLoader("SELECT * FROM read_csv_auto('example.csv')")  
      
    data = loader.load()  
    


```
[/code]


[code]
```python




    print(data)  
    


```
[/code]


[code]
```python




        [Document(page_content='Team: Nationals\nPayroll: 81.34', metadata={}), Document(page_content='Team: Reds\nPayroll: 82.2', metadata={})]  
    


```
[/code]


## Specifying Which Columns are Content vs Metadata​

[code]
```python




    loader = DuckDBLoader(  
        "SELECT * FROM read_csv_auto('example.csv')",  
        page_content_columns=["Team"],  
        metadata_columns=["Payroll"],  
    )  
      
    data = loader.load()  
    


```
[/code]


[code]
```python




    print(data)  
    


```
[/code]


[code]
```python




        [Document(page_content='Team: Nationals', metadata={'Payroll': 81.34}), Document(page_content='Team: Reds', metadata={'Payroll': 82.2})]  
    


```
[/code]


## Adding Source to Metadata​

[code]
```python




    loader = DuckDBLoader(  
        "SELECT Team, Payroll, Team As source FROM read_csv_auto('example.csv')",  
        metadata_columns=["source"],  
    )  
      
    data = loader.load()  
    


```
[/code]


[code]
```python




    print(data)  
    


```
[/code]


[code]
```python




        [Document(page_content='Team: Nationals\nPayroll: 81.34\nsource: Nationals', metadata={'source': 'Nationals'}), Document(page_content='Team: Reds\nPayroll: 82.2\nsource: Reds', metadata={'source': 'Reds'})]  
    


```
[/code]


