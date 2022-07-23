// XMLHttpRequest
const request = new XMLHttpRequest()
    // create get request for list all the data from database 
function getAllData() {
    request.open('GET', 'http://127.0.0.1:8000/api/mothali/list/');
    request.send();

    request.onload = () => {
        if (request.status === 200) {
            const data = JSON.parse(request.response);
            console.log(data);
        } else {
            console.log(`error ${request.status}`);
        }

    }

}
// Create post request to create data 
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

    request.open('POST', ' http://127.0.0.1:8000/api/mothali/');
    request.setRequestHeader('Content-type', 'application/json');
    request.send(JSON.stringify(params)); // Make sure to stringify
    console.log(params);
}


// fetch single data 
function getData() {
    const id = document.querySelector('#feedid').value;
    request.open('GET', 'http://127.0.0.1:8000/api/mothali/' + id + '/');
    request.send();

    request.onload = () => {
        if (request.status === 200) {
            const data = JSON.parse(request.response);
            console.log(data);
        } else {
            console.log(`error ${request.status}`);
        }

    }

}

// update the current data available 

function updatebyid() {
    const postid = document.querySelector('#postid').value;
    // Form fields, see IDs above
    const params = {
        title: document.querySelector('#updatetitle').value,
        content: document.querySelector('#updatecontent').value,
    }
    request.open('PATCH', 'http://127.0.0.1:8000/api/mothali/' + postid + '/update/');
    request.setRequestHeader('Content-type', 'application/json');
    request.send(JSON.stringify(params)); // Make sure to stringify
    console.log(params);
}
// delete the content by id 
function deleteby() {
    // Form fields, see IDs above
    const params = {
        postid: document.querySelector('#deletefeedid').value,
    }
    request.open('DELETE', 'http://127.0.0.1:8000/api/mothali/' + params['postid'] + '/delete/');
    request.setRequestHeader('Content-type', 'application/json');
    request.send(); // Make sure to stringify
    console.log(params);
}


// fetch api for get data

// fetch('http://127.0.0.1:8000/api/mothali/list/')
//     .then(response => {
//         return response.json();
//     }).then(json => {
//         console.log(json);
//     }).catch(error => {
//             console.log(error);
//         } // error
//     );