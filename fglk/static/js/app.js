    async function fetchData() {
        const url = '/banner_data';
    
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            
            const data = await response.json();
            console.log(data); // Log the fetched data to the console
            
            // You can perform further operations with the data here
            startBannerRotation(data); // Pass the fetched data to the rotation function
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
        }
    }  
function startBannerRotation(data)
    {
        let currentIndex = 0;
// Function to update banner content
function updateBanner() {
    document.getElementById('banner-img').src = data[currentIndex]['img-link'];
    document.getElementById('banner-text').innerHTML = '<p>' + data[currentIndex]['text'] + '</p>';
    document.getElementById('banner-heading').innerHTML='<h3>' + data[currentIndex]['heading'] + '</h3>';
    document.getElementById('banner-button-link2').href = data[currentIndex]['button-link2'];
    document.getElementById('banner-button-link2').textContent = data[currentIndex]['button-text'];
    document.querySelector('.banner-tags').innerHTML = '';

    // Loop through tags in current data item and append them
    data[currentIndex]['tags'].forEach(tag => {
        let tagElement = document.createElement('div');
        tagElement.classList.add('tag');
        tagElement.textContent = tag;
        document.querySelector('.banner-tags').appendChild(tagElement);
    });
    updateDotNavigation();
}

// Function to update dot navigation
function updateDotNavigation() {
    const dotContainer = document.getElementById('dot-container');
    dotContainer.innerHTML = '';
    for (let i = 0; i < data.length; i++) {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        if (i === currentIndex) {
            dot.classList.add('active-dot');
        }
        dot.onclick = function() {
            currentIndex = i;
            updateBanner();
            updateNextPrevImages();
        
        };
        dotContainer.appendChild(dot);
    }
}

// Function to change to the next banner content
function nextBanner() {
    currentIndex = (currentIndex + 1) % data.length;
    updateBanner();
    updateNextPrevImages();
}

// Function to change to the previous banner content
function prevBanner() {
    currentIndex = (currentIndex - 1 + data.length) % data.length;
    updateBanner();
    updateNextPrevImages();
}

// Function to update the images for next and previous buttons
function updateNextPrevImages() {
    const nextIndex = (currentIndex + 1) % data.length;
    const prevIndex = (currentIndex - 1 + data.length) % data.length;
    
    document.getElementById('next').style.backgroundImage = `url('${data[nextIndex]['img-link']}')`;
    document.getElementById('prev').style.backgroundImage = `url('${data[prevIndex]['img-link']}')`;

    // Center and fit the background image inside the div
    document.getElementById('next').style.backgroundSize = 'cover';
    document.getElementById('next').style.backgroundPosition = 'center';
    document.getElementById('next').style.alignItems= 'center';
    document.getElementById('next').style.justifyContent="space-between";

    document.getElementById('prev').style.backgroundSize = 'cover';
    document.getElementById('prev').style.backgroundPosition = 'center';
    document.getElementById('prev').style.alignItems= 'center';
    document.getElementById('prev').style.justifyContent="space-between";

    // document.getElementById('next').style.borderRadius = '50px'; // Adjust the value as needed
    // doc  ument.getElementById('prev').style.borderRadius = '50px'; // Adjust the value as needed
}

// Function to change banner content at intervals
function startBannerRotation() {
    updateBanner();
    updateNextPrevImages();
    setInterval(nextBanner, 3000); // Change every 10 seconds
}

// Start banner rotation
startBannerRotation();
// Event listeners for the next and previous buttons
document.getElementById('next').addEventListener('click', nextBanner);
document.getElementById('prev').addEventListener('click', prevBanner);
}
fetchData();

// video
document.addEventListener("DOMContentLoaded", function () {
    var videos = document.querySelectorAll(".video");
    var muteToggles = document.querySelectorAll(".mute-toggle");

    // Mute all videos by default
    videos.forEach(function(video) {
        video.muted = true;
    });

    muteToggles.forEach(function (muteToggle, index) {
        muteToggle.addEventListener("click", function () {
            if (videos[index].muted) {
                videos[index].muted = false;
                muteToggle.querySelector('.muted-icon').style.display = 'none';
                muteToggle.querySelector('.unmuted-icon').style.display = 'inline';
            } else {
                videos[index].muted = true;
                muteToggle.querySelector('.muted-icon').style.display = 'inline';
                muteToggle.querySelector('.unmuted-icon').style.display = 'none';
            }
        });
    });

    videos.forEach(function (video, index) {
        video.addEventListener("mouseenter", function () {
            video.play();
        });

        video.addEventListener("mouseleave", function () {
            video.pause();
        });
    });
});

window.onload = function () {
    // Check if Swiper library is available
    if (typeof Swiper !== 'undefined') {
        // Swiper library is available
        var mySwiper = new Swiper('.top-course .swiper-container', {
            slidesPerView: 4,
            spaceBetween: 30,
            loop: true,
            autoplay: {
                delay: 3000,
                disableOnInteraction: false,
            },
            pagination: {
                el: '.swiper-pagination',
                clickable: true,
            },
        });

        // Add event listeners to pause and resume autoplay
        var swiperContainer = document.querySelector('.top-course .swiper-container');
        swiperContainer.addEventListener('mouseenter', function () {
            mySwiper.autoplay.stop();
        });

        swiperContainer.addEventListener('mouseleave', function () {
            mySwiper.autoplay.start();
        });
    } else {
        // Swiper library is not available
        console.error('Swiper library is not loaded.');
    }
};

// screen size to 100%
  document.addEventListener("DOMContentLoaded", function() {
    if (window.innerWidth < window.innerHeight) {
      var originalZoom = 1;
      document.body.style.zoom = originalZoom;
      window.onresize = function() {
        document.body.style.zoom = originalZoom;
      };
    }
  });