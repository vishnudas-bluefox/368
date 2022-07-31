// XMLHttpRequest
const request = new XMLHttpRequest()
    // create get request for list all the data from database 
window.onload = function() {
    request.open('GET', 'http://127.0.0.1:8000/api/mothali/list/');
    request.send();

    request.onload = () => {
        if (request.status === 200) {
            const data = JSON.parse(request.response);
            let output = "";
            console.log(data);

            for (const i in data) {
                output += ` 
<div class="post" id="firstpost">
<br>
<input type="hidden" id="pandaid" value="${data[i].id}" onclick="getid()">
<div class="d-flex d-grid gap-2 d-md-block">
  <button class="buttontransperent ms-3" type="button">${data[i].userid}</button>
  <button class="buttontransperent ms-2 id=ffirstpost" type="button" onclick="followed('ffirstpost')">Follow +</button>
</div>
<div class="postp" >
  <p id="pcirstpost">
    <h3 class="title">
    ${data[i].title}
    </h3>
    <p class="content">${data[i].content}</p>
  </p>
</div>
<div class="postbuttons mb-0">
  <div class=" d-flex align-items-center justify-content-center container-fluid" style="height: 50px;">
    <button type="button" style="margin: auto" class=" buttontransperent" onclick="upvote()"><i class="fas fa-arrow-circle-up fa-2x"></i><h3 id="ufirstpost" style="display: inline;margin-left: 5px;"></h3>${data[i].like}</button>
    <button type="button" style="margin: auto" class=" buttontransperent" onclick='downvote()'><i class="fas fa-arrow-circle-down fa-2x"></i><h3 id="dfirstpost" style="display: inline;margin-left: 5px;"></h3>${data[i].dislike}</button>
    <button type="button" style="margin: auto" class=" buttontransperent"data-bs-toggle="collapse" data-bs-target="#airstpost" aria-expanded="false" aria-controls="collapseExample"><i class="far fa-comment fa-2x"></i>${data[i].comments}</button>
    <button type="button" style="margin: auto" class=" buttontransperent"data-bs-toggle="modal" data-bs-target="#options"onclick='postcommentid("firstpost")'><i class="fas fa-ellipsis-v fa-2x"></i></button>
  </div>
</div>
<br>
</div>
<div class="collapse" id="airstpost">
<div class="mx-5 d-flex">
  <textarea class="form-control mb-2 commentarea" placeholder="Leave a comment here" id="cacomment1" style="color:white;" ></textarea>
  <button type="button" style="margin-left:5px;" class="buttontransperent "onclick='postcomment("cacomment1")'><i class="fas fa-paper-plane fa-2x"></i></button>
 </div>
 <div class="comments" id="ccomment1">
  
 </div>
</div>  

`;

            }
            document.getElementById("posts").innerHTML = output;

            // for (const i in data) {
            //     // console.log(data[i])
            //     const title = document.createElement("div.title");
            //     const textnode = document.createTextNode(data[i].title);
            //     title.appendChild(textnode);
            //     document.getElementById("myTable").appendChild(title);
            //     const content = document.createElement("div.content");
            //     const textnode1 = document.createTextNode(data[i].content);
            //     content.appendChild(textnode1);
            //     document.getElementById("myTable").appendChild(content);
            // }
        } else {
            console.log(`error ${request.status}`);
        }

    }

}


// add field 
function addfield() {
    const questions = document.getElementById("questions");
    const question = document.createElement("div.question");
}


function getid() {
    const pandaid = document.getElementById("pandaid").value;
    console.log(pandaid);
    console.log("getid");
}

function upvote() {
    const params = {
        id: document.getElementById("pandaid").value,
    }
    console.log(params);
    request.open('PATCH', 'http://127.0.0.1:8000/api/mothali/newsfeed/upvote/');
    request.setRequestHeader('Content-type', 'application/json');
    request.send(JSON.stringify(params)); // Make sure to stringify
    console.log(params);
}

function downvote() {
    const params = {
        id: document.getElementById("pandaid").value,
    }
    console.log(params);
    request.open('PATCH', 'http://127.0.0.1:8000/api/mothali/newsfeed/downvote/');
    request.setRequestHeader('Content-type', 'application/json');
    request.send(JSON.stringify(params)); // Make sure to stringify
    console.log(params);
}

function editbutton() {
    const params = {
        userid: document.getElementById("pandaid").value,
        title: document.getElementById("feedtitle").value,
        content: document.getElementById("feedcontent").value,
    }

    request.open('PATCH', 'http://127.0.0.1:8000/api/mothali/' + params['userid'] + "/update");
    request.setRequestHeader('Content-type', 'application/json');
    request.send(JSON.stringify(params)); // Make sure to stringify
    console.log(params);

}

function deleteby() {
    // Form fields, see IDs above
    const params = {
        postid: document.getElementById("pandaid").value,

    }
    request.open('DELETE', 'http://127.0.0.1:8000/api/mothali/' + params['postid'] + '/delete/');
    request.setRequestHeader('Content-type', 'application/json');
    request.send(); // Make sure to stringify
    console.log(params);
}

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