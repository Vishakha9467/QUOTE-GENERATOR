document.getElementById('quote-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    const category = document.getElementById('category').value.trim();

    const response = await fetch('/get_quote', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ category: category }),
    });

    const data = await response.json();
    document.getElementById('quote').innerText = data.quote;
    document.getElementById('author').innerText = data.author ? `- ${data.author}` : '';
});