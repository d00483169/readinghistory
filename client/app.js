console.log("connected")

let historyWrapper = document.querySelector("#history-review-wapper");
console.log("wapper",historyWrapper)
let inputBookName = document.querySelector("#input-book-name");
let inputAutherName = document.querySelector("#input-auther-name");
let inputReview = document.querySelector("#input-review");
let saveReviewButton = document.querySelector("#save-review-button");
let editId = null;


function saveReviewOnServer() {
    console.log("save button clicked");
    let data = "book=" + encodeURIComponent(inputBookName.value);
    data += "&auther=" + encodeURIComponent(inputAutherName.value);
    data += "&review=" + encodeURIComponent(inputReview.value);
    console.log("d",data)
    let method = "POST";
    let URL = "http://localhost:8080/readinghistory";
    if(editId){
        method = "PUT";
        URL = "http://localhost:8080/readinghistory/"+editId;
    }
    fetch(URL, {
        method: method,
        body: data,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    }).then(function(response){
        console.log("new review saved!", response)
        historyWrapper.textContent = "";
        loadHistoryFromServer()
    })
    document.getElementById("hide").style.display = "none";
    document.getElementById("add-review-button").style.display = "block";
}

function addReadingHistory(data){
    console.log("data",data)
    let bookName = document.createElement("h3");
    bookName.textContent = '"'+data.book+'"';
    bookName.style.fontStyle = "italic"; 
    let autherName = document.createElement("p");
    autherName.textContent = data.auther;
    let bookReview = document.createElement("p");
    bookReview.textContent = data.review;
    let editButton = document.createElement("button")
    editButton.textContent = "Edit";
    editButton.classList.add("edit-delete-button");
    let deleteButton = document.createElement("button")
    deleteButton.textContent = "Delete";
    deleteButton.classList.add("edit-delete-button");
    let historySeparater = document.createElement("hr");
    historyWrapper.appendChild(bookName);
    historyWrapper.appendChild(autherName);
    historyWrapper.appendChild(bookReview);
    historyWrapper.appendChild(editButton);
    historyWrapper.appendChild(deleteButton);
    historyWrapper.appendChild(historySeparater);

    editButton.onclick = function () {
        console.log("edit-button clicked");
        console.log("history id: ",data.id)
        document.getElementById("hide").style.display = "block";
        document.getElementById("add-review-button").style.display = "none";
        inputBookName.value = data.book;
        inputAutherName.value = data.auther;
        inputReview.value = data.review;
        editId = data.id;
    }
    deleteButton.onclick = function () {
        console.log("delete-button clicked");
        if (confirm("Are you sure to delete this history?")){
            console.log("history id: ",data.id)
            editId = data.id;
            let method = "DELETE";
            let URL = "http://localhost:8080/readinghistory/"+editId;
            console.log("d",data)
            fetch(URL, {
                method: method
            }).then(function(response){
                console.log("history deleted", response)
                historyWrapper.textContent = "";
                loadHistoryFromServer()
            })
        }
    }
}

function loadHistoryFromServer() {
    fetch("http://localhost:8080/readinghistory")
        .then(function(response){
            response.json()
                .then(function(data){
                    console.log("from server",data);
                    let readingHistory = data;
                    readingHistory.forEach(addReadingHistory)
                })
        })
}


let addBookButton = document.querySelector("#add-review-button");
function addNewBook(){
    console.log("add-button clicked");
    document.getElementById("hide").style.display = "block";
    document.getElementById("add-review-button").style.display = "none";
}

addBookButton.onclick = addNewBook;
saveReviewButton.onclick = saveReviewOnServer;

loadHistoryFromServer()