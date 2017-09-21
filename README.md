# databaselib
A simple database module for Python with the option between pickle and csv.

# Installation
Simply download `databaselib.py` and place in the same folder as your Python project.

# Usage
To start you'll need to import the database using:
```python
from databaselib import Database
```

## Creating a Database
You next need to pick between pickle and csv. They both work using the same commands.

```python
db = Database("mydatabase", "csv")
#                   /|\      /|\
#                    |        |
# Filename           /        |
# Provider ('csv' or 'pickle')/
```

# Loading from file

```python
db.load()
```

# Saving to file

```python
db.save()
```

# Add dictionary object to database

```python
db.add({
  "name": "Bob",
  "age": "17",
  "colour": "green"
})
```

# Get all values

```python
db.getall()
```
