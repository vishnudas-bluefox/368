function createfeed() {
    // Form fields, see IDs above
    // for random id 
    let s4 = () => {
            return Math.floor((1 + Math.random()) * 0x10000)
                .toString(16)
                .substring(1);
        }
        // random id ends 
        // call the params 
    const params = {
        userid: s4(),
        title: document.getElementById("feedtitle").value,
        content: document.getElementById("feedcontent").value,
        media: "medkjshdkia url here",
        like: 0,
        dislike: 0,
        comments: 0,
    }

    request.open('PATCH', 'http://127.0.0.1:8000/api/mothali/' + postid + '/update/');
    request.setRequestHeader('Content-type', 'application/json');
    request.send(JSON.stringify(params)); // Make sure to stringify
    console.log(params);

}

// // for upvoting the post 
// function upvote() {
//     const orginalid = document.getElementById("originalid").value;
//     console.log(orginalid);
// }