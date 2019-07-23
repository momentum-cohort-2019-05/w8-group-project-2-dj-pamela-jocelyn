const markAnswerCorrectLinks = document.querySelectorAll('.mark-answer-correct-link');

if (markAnswerCorrectLinks) {
    for (let link of markAnswerCorrectLinks) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            fetch(`/answers/${link.dataset.answerPk}/mark-correct`)
                .then(res => res.json())
                .then(function (data) {
                    console.log('data', data);
                })
                .then(function () {
                    link.setAttribute('hidden', true);
                    let correctMessage = document.createElement('span');
                    correctMessage.innerText = 'answer marked as correct';
                    link.parentElement.appendChild(correctMessage);
                });
        });
    }
}


const starAnswerLinks = document.querySelectorAll('.star-answer-link');

if (starAnswerLinks) {
    for (let link of starAnswerLinks) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            fetch(`/answers/${link.dataset.answerPk}/star`)
                .then(res => res.json())
                .then(function (data) {
                    console.log('data', data);
                })
                .then(function () {
                    link.setAttribute('hidden', true);
                    let starMessage = document.createElement('span');
                    starMessage.innerText = 'answer starred';
                    link.parentElement.appendChild(starMessage);
                });
        });
    }
}

const starQuestionLinks = document.querySelectorAll('.star-question-link');

if (starQuestionLinks) {
    for (let link of starQuestionLinks) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            fetch(`/questions/${link.dataset.questionPk}/star`)
                .then(res => res.json())
                .then(function (data) {
                    console.log('data', data);
                })
                .then(function () {
                    link.setAttribute('hidden', true);
                    let starMessage = document.createElement('span');
                    starMessage.innerText = 'question starred';
                    link.parentElement.appendChild(starMessage);
                });
        });
    }
}

const answerInput = document.querySelector('#answer-input');
const answerButton = document.querySelector('#answer-button');
const csrftoken = Cookies.get('csrftoken')
answerButton.addEventListener('click', (e) =>{
    console.log('test')
    fetch(`/questions/${answerInput.dataset.questionPk}/answers/create`,{
        credentials: 'include',
          method: 'POST',
          headers: {
            'X-CSRFToken': csrftoken
          },
          body: JSON.stringify({ 'body': answerInput.value })
        })
    .then(data => data.json())
    .then(json => {
        console.log(json)
        const answerDiv=  document.querySelector('.answer-detail')
        answerDiv.innerHTML += `
        ${ json['user'] }:
        <p>
            ${json['body'] }
        </p>
        
    `
     })
    });