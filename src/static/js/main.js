(function ($) {
    "use strict";

    // Spinner
    let spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();


    // Initiate the wowjs
    new WOW().init();


    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 45) {
            $('.navbar').addClass('sticky-top shadow-sm');
        } else {
            $('.navbar').removeClass('sticky-top shadow-sm');
        }
    });


    // Dropdown on mouse hover
    const $dropdown = $(".dropdown");
    const $dropdownToggle = $(".dropdown-toggle");
    const $dropdownMenu = $(".dropdown-menu");
    const showClass = "show";

    $(window).on("load resize", function () {
        if (this.matchMedia("(min-width: 992px)").matches) {
            $dropdown.hover(function () {
                const $this = $(this);
                $this.addClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "true");
                $this.find($dropdownMenu).addClass(showClass);
            }, function () {
                const $this = $(this);
                $this.removeClass(showClass);
                $this.find($dropdownToggle).attr("aria-expanded", "false");
                $this.find($dropdownMenu).removeClass(showClass);
            });
        } else {
            $dropdown.off("mouseenter mouseleave");
        }
    });


    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    $(".testimonial-carousel").owlCarousel({
        autoplay: true, smartSpeed: 1000, center: true, margin: 24, dots: true, loop: true, nav: false, responsive: {
            0: {
                items: 1
            }, 768: {
                items: 2
            }, 992: {
                items: 3
            }
        }
    });

})(jQuery);


// my javaScript starts here
async function likeToggle(button, userId, vacationId) {
    const icon = button.querySelector('.icon-heart-custom');
    const likesSpan = button.nextElementSibling.querySelector('.count-likes-value');

    // Determine if the icon is filled or not
    const isLiked = icon.classList.contains('fas'); // If the icon has 'fas', it is filled


    let currentLikesCount = parseInt(likesSpan.textContent);

    try {
        let response;
        if (isLiked) {
            // User is unliking the vacation
            icon.classList.remove('fas', 'liked');
            icon.classList.add('far');
            response = await fetch(`/unlike_vacation/${userId}/${vacationId}/`, {
                method: 'DELETE'
            });
            currentLikesCount--;
        } else {
            // User is liking the vacation
            icon.classList.remove('far');
            icon.classList.add('fas', 'liked');
            response = await fetch(`/like_vacation/${userId}/${vacationId}/`, {
                method: 'POST'
            });
            currentLikesCount++;
        }


        if (!response.ok) {
            throw new Error('Failed to update like status.');
        }
        // Update the displayed like count
        likesSpan.textContent = currentLikesCount;
        console.log('Successfully performed like/unlike operation.');
    } catch (error) {
        console.error('Error in toggleLike:', error.message);
    }
}

function confirmDelete() {
    const ok = confirm("Are you sure ? ")
    if (!ok) {
        event.preventDefault()
    }
}

const errorSpan = document.querySelector(".error");
if (errorSpan) {
    setTimeout(() => {
        errorSpan.parentNode.removeChild(errorSpan);
    }, 4000);
}


const flashMessages = document.querySelector(".flashes.messages");
if (flashMessages) {
    setTimeout(() => {
        flashMessages.parentNode.removeChild(flashMessages);
    }, 3000);
}

const loggingMessages = document.querySelector(".user-login");
if (loggingMessages) {
    setTimeout(() => {
        loggingMessages.parentNode.removeChild(loggingMessages);
    }, 3000);
}


function saveUser() {
    let email = document.getElementById("email").value;
    localStorage.setItem("email", email);
    alert("ok");
}

function previewImage(event) {
    const file = event.target.files[0];
    const fileName = file ? file.name : '';
    const fileReader = new FileReader();

    fileReader.onload = function (e) {
        // Update the src of the current image to show the new image
        const imageElement = document.getElementById('current_image');
        imageElement.src = e.target.result;

        // Update the filename display
        document.getElementById('file_name').textContent = fileName;
    }

    if (file) {
        fileReader.readAsDataURL(file);
    }
}

function previewImageAdded(event) {
    var input = event.target;
    var file = input.files[0];
    var preview = document.getElementById('image_preview');

    // Clear any existing preview
    preview.innerHTML = '';

    if (file) {
        var reader = new FileReader();

        reader.onload = function (e) {
            var img = document.createElement('img');
            img.src = e.target.result;
            img.style.maxWidth = '100%'; // Adjust size as needed
            img.style.maxHeight = '400px'; // Adjust size as needed
            preview.appendChild(img);
        };

        reader.readAsDataURL(file);
    }
}

window.onload = function () {
    // Check the current URL to determine which section to scroll into view
    const url = window.location.href;

    if (/\/vacations\/edit\/\d+/.test(url)) {
        document.getElementById('edit-section').scrollIntoView({behavior: 'smooth'});
    } else if (/\/vacations\/new/.test(url)) {
        document.getElementById('add-section').scrollIntoView({behavior: 'smooth'});
    } else if (url.includes('vacations')) {
        document.getElementById('vacations-section').scrollIntoView({behavior: 'smooth'});
    } else if (url.includes('about')) {
        document.getElementById('about-section').scrollIntoView({behavior: 'smooth'});
    } else if (url.includes('login')) {
        document.getElementById('login-section').scrollIntoView({behavior: 'smooth'});
    } else if (url.includes('register')) {
        document.getElementById('register-section').scrollIntoView({behavior: 'smooth'});
    }
};



