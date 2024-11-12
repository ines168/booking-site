const deleteBtns = document.querySelectorAll('.delete-btn');
for (let i = 0; i<deleteBtns.length; i++) {
    const deleteBtn = deleteBtns[i];
    deleteBtn.onclick = function(e) {
        console.log(e);
        const venue_id = e.target.dataset.id;
        fetch('/venues/'+ venue_id, {
            method: 'DELETE',
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to delete venue');
            }
        })
        .then(data => {
            window.location.reload();
        })
        .catch(error => {
            console.log('fetch failed', error)
        })
    }
}