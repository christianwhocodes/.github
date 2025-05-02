document.addEventListener('DOMContentLoaded', function () {
  fetch('https://worldtimeapi.org/api/timezone/Africa/Nairobi')
    .then(response => response.json())
    .then(data => {
      const currentDate = new Date(data.datetime); // ISO string
      const month = currentDate.getUTCMonth(); // 0-indexed
      const day = currentDate.getUTCDate();

      if (month === 4 && day === 2) {
        fetchBirthdayWishes();
      }
    })
    .catch(error => {
      console.error('Could not fetch time from API. Falling back to local time.', error);

      const today = new Date();
      if (today.getMonth() === 4 && today.getDate() === 2) {
        fetchBirthdayWishes();
      }
    });
});

const defaultWishes = [
  "one of progress and growth",
  "blessed with good health",
  "surrounded by love and laughter"
];

function fetchBirthdayWishes() {
  const url = 'https://api.sheety.co/a21bb8ea00f0c35e5ebded3afded8fab/2025May2KevinsBirthday/formResponses1';

  fetch(url)
    .then((response) => response.json())
    .then(json => {
      // Extract wishes from the responses
      const formResponses = json.formResponses1;

      if (formResponses && formResponses.length > 0) {
        // Extract the wishes from "May your new year be..." column
        const wishes = formResponses.map(response => {
          // The column name in your sheet is "May your new year be..."
          // Sheety might transform this to camelCase or keep it as is with spaces
          const wishText = response.mayYourNewYearBe || response['May your new year be...'];
          return wishText;
        }).filter(wish => wish); // Filter out any undefined/empty wishes

        // Combine wishes, using defaults if no form submissions exist
        const allWishes = wishes.length > 0 ? [...defaultWishes, ...wishes] : defaultWishes;

        // Update the hero container with birthday message
        updateHeroWithWishes(allWishes);
      } else {
        // Use default wishes if no responses were found
        updateHeroWithWishes(defaultWishes);
      }
    })
    .catch(error => {
      console.error('Error fetching wishes:', error);
      // Fallback to default wishes in case of an error
      updateHeroWithWishes(defaultWishes);
    });
}

function updateHeroWithWishes(wishes) {
  const heroContainer = document.querySelector(
    '.hero .container[data-aos="zoom-out"][data-aos-delay="100"]'
  );

  if (heroContainer) {
    heroContainer.innerHTML = `
      <h2>Happy birthday Kevin!</h2>
      <p>May your new year be <span class="typed" data-typed-items="${wishes.join(', ')}"></span><span class="typed-cursor typed-cursor--blink"></span></p>
      <div class="social-links">
        <a href="https://github.com/christianwhocodes/" target="_blank" rel="noopener noreferrer"><i class="bi bi-github"></i></a>
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