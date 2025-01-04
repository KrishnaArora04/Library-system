fetch('/api/members')
    .then(response => response.json())
    .then(data => {
        const container = document.getElementById('members-container');
        container.innerHTML = JSON.stringify(data, null, 2);
    });
