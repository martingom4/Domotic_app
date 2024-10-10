document.getElementById('command-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const command = document.getElementById('command-input').value;

    fetch('/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: command })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = `<pre>${JSON.stringify(data.tokens, null, 2)}</pre>`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
