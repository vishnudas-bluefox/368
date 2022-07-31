function addfield() {
    const questions = document.querySelector('.questions');
    const input = document.createElement('input');
    input.type = 'text';
    input.className = 'form-control information';
    input.id = "questions";
    input.placeholder = 'Question';
    questions.appendChild(input);
}

function passalldata() {
    const request = new XMLHttpRequest()
    const params = {
        refernceid: document.querySelector('#refernceid').value,
        fromname: document.querySelector('#fromname').value,
        fromaddress: document.querySelector('#fromaddress').value,
        toname: document.querySelector('#toname').value,
        todesignation: document.querySelector('#todesignation').value,
        toaddress: document.querySelector('#toaddress').value,
        onewordrti: document.querySelector('#onewordrti').value,

    };
    const questions = document.querySelectorAll("#questions");
    const questionsArray = [];
    for (let i = 0; i < questions.length; i++) {
        questionsArray.push(questions[i].value);
    }
    params.questions = questionsArray;

    //pass pdf params to create pdf
    request.open('POST', ' http://127.0.0.1:8000/api/pdf/rtipdf/');
    request.setRequestHeader('Content-type', 'application/json');
    request.send(JSON.stringify(params)); // Make sure to stringify
    console.log(params);
    window.open("file:///home/unknown/Desktop/programs/Miniproject/final/error/firstTestCase/backend/test6.pdf", "_blank");
    return false;
}