/*                 MENU                 */

function toggleMenu() {
    const menu = document.getElementById('menu');
    const menuIcon = document.querySelector('.menu-icon');
    const closeIcon = document.querySelector('.close-icon');

    if (menu.classList.contains('open')) {
        menu.classList.remove('open');
        menuIcon.style.display = 'block';
        closeIcon.style.display = 'none';
    } else {
        menu.classList.add('open');
        menuIcon.style.display = 'none';
        closeIcon.style.display = 'block';
    }
}


/*                  CARROSSEL                      */


        let slideIndex = 0;

        function showSlides(n) {
            const slides = document.querySelectorAll('.carousel-images img');
            const indicators = document.querySelectorAll('.indicator');
            if (n >= slides.length) slideIndex = 0;
            if (n < 0) slideIndex = slides.length - 1;

            slides.forEach((slide, index) => {
                slide.style.display = (index === slideIndex) ? 'block' : 'none';
            });

            indicators.forEach((indicator, index) => {
                indicator.className = (index === slideIndex) ? 'indicator active' : 'indicator';
            });
        }

        function moveSlide(n) {
            showSlides(slideIndex += n);
        }

        function createIndicators() {
            const slides = document.querySelectorAll('.carousel-images img');
            const indicatorsContainer = document.querySelector('.indicators');
            slides.forEach((_, index) => {
                const div = document.createElement('div');
                div.className = 'indicator';
                div.addEventListener('click', () => {
                    slideIndex = index;
                    showSlides(slideIndex);
                });
                indicatorsContainer.appendChild(div);
            });
        }

        createIndicators();
        showSlides(slideIndex);

        // Auto-slide every 4 seconds
        setInterval(() => {
            moveSlide(1);
        }, 4000);
