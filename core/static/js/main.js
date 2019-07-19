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



