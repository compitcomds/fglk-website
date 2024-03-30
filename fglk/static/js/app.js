    async function fetchData() {
        const url = 'http://localhost:5000/banner_data';
    
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
    document.getElementById('prev').style.backgroundSize = 'cover';
    document.getElementById('prev').style.backgroundPosition = 'center';
    
}


// Function to change banner content at intervals
function startBannerRotation() {
    updateBanner();
    updateNextPrevImages();
    setInterval(nextBanner, 10000); // Change every 10 seconds
}

// Start banner rotation
startBannerRotation();


// Event listeners for the next and previous buttons
document.getElementById('next').addEventListener('click', nextBanner);
document.getElementById('prev').addEventListener('click', prevBanner);
}
fetchData();