const deleteVenueButton = document.getElementById('delete-venue-button');
const deleteArtistButton = document.getElementById('delete-artist-button');

if(deleteVenueButton) {
    deleteVenueButton.onclick = function(e) {
        e.preventDefault();

        const venueId = e.target.dataset.id;

        fetch(`/venues/${venueId}`, {
            method: 'DELETE'
        }).then(function(response) {
            location.href = '/venues';
        })
    }
}

if(deleteArtistButton) {
    deleteArtistButton.onclick = function(e) {
        e.preventDefault();

        const artistId = e.target.dataset.id;

        fetch(`/artists/${artistId}`, {
            method: 'DELETE'
        }).then(function(response) {
            location.href = '/artists';
        })
    }
}