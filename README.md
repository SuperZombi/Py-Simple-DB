# My Data Base

## Load:
```python
from DataBase import DataBase

mydb = DataBase("simple.bd")
mydb_unique = DataBase("unique.bd", unique="user")
```

You can use a database in which the unique key will be a number, or specify your own name for the unique key, which will need to be transmitted

## Add row:
This command automatically saves the state of the database.
```python
mydb.add(name="Hello", last_name="world", gender="male") # any values
mydb_unique.add(user="User1", name="Hello world", gender="male") # any values
#               ^ unique key
```
Make sure you are passing in a unique key for the appropriate database. <br>
As in this example, the unique key is the "user" argument specified during initialization.


## Find:
Returns the id of the first matched element, or an array of ids.
```python
id_first = mydb.get(name="Hello")               # 0
id_array = mydb.get(gender="male", all=True)    # [0...]
```
```python
id_first_unique = mydb_unique.get(gender="male")            # "User1"
id_array_unique = mydb_unique.get(gender="male", all=True)  # ["User1"...]
```

## Get row:
Returns value by key.
```python
mydb.get_by_id(id_first)               # {"name": "Hello", "last_name": "world", "gender": "male"}
mydb_unique.get_by_id(id_first_unique) # {"name": "Hello world", "gender": "male"}
```

## Delete row:
This command automatically saves the state of the database.
```python
mydb.delete(id_first)
mydb_unique.delete(id_first_unique)
```

## Save:
```python
mydb.save()
```

## Data:
```python
mydb.data
```
Allows you to get the whole database.
