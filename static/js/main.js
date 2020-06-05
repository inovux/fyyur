const deleteVenueButton = document.getElementById('delete-venue-button');

if(deleteVenueButton) {
    deleteVenueButton.onclick = function(e) {
        e.preventDefault();

        const venueId = e.target.dataset.id;

        fetch(`/venues/${venueId}`, {
            method: 'DELETE'
        }).then(function(response) {
            console.log(JSON.stringify(response));
            location.href = '/venues';
        })
    }
}