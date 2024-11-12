import sqlite3

def dict_factory(cursor, row):
    fields = []
    # Extract column names from cursor description
    for column in cursor.description:
        fields.append(column[0])

    # Create a dictionary where keys are column names and values are row values
    result_dict = {}
    for i in range(len(fields)):
        result_dict[fields[i]] = row[i]

    return result_dict

class HistoryDB:
    def __init__(self, filename):
        #connect to DB file
        self.connection = sqlite3.connect(filename)
        self.connection.row_factory = dict_factory
        #use the connection instance to perform db operations
        #create a cursor instance for the connection
        self.cursor = self.connection.cursor()

    def getAllHistory(self):
        #now that we have an access point we can fetch all on one
        #ONLY applicable use of fetch is folloing a SELECT query
        self.cursor.execute("SELECT * FROM ReadingHistory")
        allHistory = self.cursor.fetchall()
        return allHistory
    
    def getHistory(self, history_id):
        data = [history_id]
        self.cursor.execute("SELECT * FROM ReadingHistory WHERE id = ?", data)
        history = self.cursor.fetchone()
        return history
    
    def createHistory(self,book,auther,review):
        data = [book,auther,review]
        #add a new rollercoaster to our db
        self.cursor.execute("INSERT INTO ReadingHistory(book,auther,review)VALUES(?,?,?)",data)
        self.connection.commit()

    def updateHistory(self, history_id,book,auther,review):
        data = [book,auther,review,history_id]
        print("update data=",data)
        self.cursor.execute("UPDATE ReadingHistory SET book = ?, auther = ?, review = ? WHERE id = ?",data)
        self.connection.commit()

    def deleteHistory(self, history_id):
        data = [history_id]
        print("delete data id=",data)
        self.cursor.execute("DELETE FROM ReadingHistory WHERE id = ?", data)
        self.connection.commit()