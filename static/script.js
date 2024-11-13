const deleteVenueBtns = document.querySelectorAll('.venue-delete');
for (let i = 0; i<deleteVenueBtns.length; i++) {
    const deleteBtn = deleteVenueBtns[i];
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
        .then(() => {
            window.location.reload();
        })
        .catch(error => {
            console.log('fetch failed', error)
        })
    }
}

const deleteArtistBtns = document.querySelectorAll('.artist-delete');
for (let i=0; i<deleteArtistBtns.length; i++) {
    const deleteBtn = deleteArtistBtns[i];
    deleteBtn.onclick = function(e) {
        console.log(e);
        const artist_id = e.target.dataset.id;
        fetch('/artists/'+artist_id, {
            method: 'DELETE',
        })
        .then(response => {
            if(response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to delete artist');
            }
        })
        .then(() => {
            window.location.reload()
        })
        .catch(error => {
            console.log('fetch failed', error)
        })
    }
}