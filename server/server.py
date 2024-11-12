from flask import Flask, request
from history import HistoryDB

app = Flask(__name__)
@app.route("/readinghistory/<int:history_id>", methods=["OPTIONS"])
def handle_cors_options(history_id):
    return "", 204, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type"
        }


@app.route("/readinghistory", methods=["GET"])
def retrieve_history():
    print("path",request.path)
    db = HistoryDB("historydb.db")
    history = db.getAllHistory()
    return history, 200, {"Access-Control-Allow-Origin" : "*"}


@app.route("/readinghistory", methods=["POST"])
def create_history():
    print("The request data is: ", request.form)
    book  = request.form["book"]
    auther  = request.form["auther"]
    review  = request.form["review"]
    db = HistoryDB("historydb.db")
    db.createHistory(book,auther,review)
    return "Created", 201, {"Access-Control-Allow-Origin" : "*"}


@app.route("/readinghistory/<int:history_id>",methods=["PUT"])
def update_history(history_id):
    print("update history with ID ", history_id)
    db = HistoryDB("historydb.db")
    history =db.getHistory(history_id)
    if history:
        book  = request.form["book"]
        auther  = request.form["auther"]
        review  = request.form["review"]
        db.updateHistory(history_id,book,auther,review)
        return "Update",200,{"Access-Control-Allow-Origin" : "*"}
    else:
        return f"Reading History with {history_id} not found",404,{"Access-Control-Allow-Origin" : "*"}

@app.route("/readinghistory/<int:history_id>", methods=["DELETE"])
def delete_history(history_id):
    print("Deleting history with ID:", history_id)
    db = HistoryDB("historydb.db")
    history =db.getHistory(history_id)
    if history:
        db.deleteHistory(history_id)
        return "Deleted", 200, {"Access-Control-Allow-Origin" : "*"}
    else:
        return f"Reading History with {history_id} not found",404,{"Access-Control-Allow-Origin" : "*"}


def run():
    app.run(port=8080)

if __name__ == "__main__":
    run()

