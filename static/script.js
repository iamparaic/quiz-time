document.getElementById('quiz-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const formData = new FormData(event.target);
    const userAnswers = {};
    formData.forEach((value, key) => {
        userAnswers[key] = value;
    });
    fetch('/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userAnswers)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = `You scored ${data.score} out of ${data.total}`;
    });
});
