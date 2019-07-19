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