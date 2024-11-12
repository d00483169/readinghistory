# My Project

## Resource

**Reading History**

Attributes:

* book (string)
* auther (string)
* review (string)
* rating (integer)
* date (integer)

## Schema

```sql
CREATE TABLE ReadingHistory (
id INTEGER PRIMARY KEY,
book TEXT,
auther TEXT,
review TEXT,
rating INTEGER,
date INTEGER);
```

## REST Endpoints

Name                           | Method | Path
-------------------------------|--------|------------------
Retrieve reading history       | GET    | /readinghistory
Retrieve reading history       | GET    | /readinghistory/*\<id\>*
Create reading history         | POST   | /readinghistory
Update reading history         | PUT    | /readinghistory/*\<id\>*
Delete reading history         | DELETE | /readinghistory/*\<id\>*