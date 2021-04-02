$( document ).ready(function() {
$('.testi').owlCarousel({
    items: 3,
    margin: 10,
    lazyLoad: true,
    dots: true,
    autoPlay: true,
    autoPlayTimeout: 3000,
    responsive: {
        0: {
            items: 1,
        },
        800: {
            items: 2,
        },
        1000: {
            items: 3,
        }
    }
});


(function () {
    var $gallery = new SimpleLightbox('.row .col-md-4  a', {});
})();


// Initialize and add the map


const items = document.querySelectorAll(".accordion-item h2");

function toggleAccordion() {
    const itemToggle = this.getAttribute('aria-expanded');

    for (i = 0; i < items.length; i++) {
        items[i].setAttribute('aria-expanded', 'false');
    }

    if (itemToggle == 'false') {
        this.setAttribute('aria-expanded', 'true');
    }
}

items.forEach(item => item.addEventListener('click', toggleAccordion));

$('body').scrollspy({ target: '#mainNav' })
});


function initMap() {
    // The location of Uluru
    const uluru = { lat: -25.344, lng: 131.036 };
    // The map, centered at Uluru
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 4,
        center: uluru,
    });
    // The marker, positioned at Uluru
    const marker = new google.maps.Marker({
        position: uluru,
        map: map,
    });
}