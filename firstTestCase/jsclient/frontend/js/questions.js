// XMLHttpRequest
const request = new XMLHttpRequest()
    // create get request for list all the data from database 
window.onload = function() {
    request.open('GET', 'http://127.0.0.1:8000/api/mothali/questions/list/');
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
<div class="d-flex d-grid gap-2 d-md-block">
  <button class="buttontransperent ms-3" type="button">${data[i].userid}</button>
  <button class="buttontransperent ms-2 id=ffirstpost" type="button" onclick="followed('ffirstpost')">Follow +</button>
</div>
<div class="postp" >
  <p id="pcirstpost">
    <h3 class="title">
    ${data[i].subject}
    </h3>
    <p class="content">${data[i].description}</p>
  </p>
</div>
<div class="postbuttons mb-0">
  <div class=" d-flex align-items-center justify-content-center container-fluid" style="height: 50px;">
    <button type="button" style="margin: auto" class=" buttontransperent" id="upvotethepost" onclick='upvote()'><i class="fas fa-arrow-circle-up fa-2x"></i><h3 id="ufirstpost" style="display: inline;margin-left: 5px;"></h3>${data[i].like}</button>
    <button type="button" style="margin: auto" class=" buttontransperent" onclick='downvote()'><i class="fas fa-arrow-circle-down fa-2x"></i><h3 id="dfirstpost" style="display: inline;margin-left: 5px;"></h3>${data[i].dislike}</button>
    <button type="button" style="margin: auto" class=" buttontransperent"data-bs-toggle="collapse" data-bs-target="#airstpost" aria-expanded="false" aria-controls="collapseExample"><i class="far fa-comment fa-2x"></i>${data[i].answers}</button>
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