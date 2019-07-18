const markAnswerCorrectLink = document.querySelector('.mark-answer-correct-link');

markAnswerCorrectLink.addEventListener('click', function(event) {
    event.preventDefault();
    fetch(`/answers/${markAnswerCorrectLink.dataset.answerPk}/mark-correct`)
        .then(res => res.json())
        .then(function (data) {
            console.log('data', data)
        })
        .then(function () {
            markAnswerCorrectLink.setAttribute('hidden', true);
        })
});