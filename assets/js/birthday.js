document.addEventListener('DOMContentLoaded', function () {
  // Check if today is May 2nd
  const today = new Date();
  if (today.getMonth() === 4 && today.getDate() === 2) { // Months are 0-indexed
    const wishes = [
      "one of progress and growth",
      "full of new opportunities",
      "blessed with good health",
      "overflowing with creativity",
      "surrounded by love and laughter"
    ];
    const wishesStr = wishes.join(', ');

    const heroContainer = document.querySelector(
      '.hero .container[data-aos="zoom-out"][data-aos-delay="100"]'
    );
    if (heroContainer) {
      heroContainer.innerHTML = `
        <h2>Happy birthday Kevin!</h2>
        <p>May your new year be <span class="typed" data-typed-items="${wishes.join(', ')}"></span><span class="typed-cursor typed-cursor--blink"></span></p>
        <div class="social-links">
          <a href="https://github.com/christianwhocodes/" target="_blank" rel="noopener noreferrer"><i class="bi bi-github"></i></a>
          <a href="https://www.linkedin.com/in/christianwhocodes" target="_blank" rel="noopener noreferrer"><i class="bi bi-linkedin"></i></a>
        </div>
      `;

      // Re-initialize Typed.js for the new element
      if (window.Typed) {
        new Typed(heroContainer.querySelector('.typed'), {
          strings: wishes,
          typeSpeed: 50,
          backSpeed: 30,
          backDelay: 1500,
          loop: true
        });
      }
    }
  }
});