function create() {
    // Form fields, see IDs above
    const params = {
        userid: document.querySelector('#userid').value,
        title: document.querySelector('#title').value,
        content: document.querySelector('#content').value,
        media: "medkjshdkia url here",
        like: 0,
        dislike: 0,
        comments: 0,
    }

    const http = new XMLHttpRequest()
    http.open('POST', ' http://127.0.0.1:8000/api/mothali/')
    http.setRequestHeader('Content-type', 'application/json')
    http.send(JSON.stringify(params)) // Make sure to stringify
    http.onload = function() {
        // Do whatever with response
        alert(http.responseText)
    }
    console.log(params);
}