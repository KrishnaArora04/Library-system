fetch('/api/books')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('books-container');
        container.innerHTML = JSON.stringify(data, null, 2);
    });
