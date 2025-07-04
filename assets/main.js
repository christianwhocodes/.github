// Initialize AOS when DOM is ready
document.addEventListener("DOMContentLoaded", function () {
  // Add fallback class if AOS fails to load
  if (typeof AOS === "undefined") {
    document.body.classList.add("no-aos");
    console.warn("AOS library failed to load");
    return; // Now this return is valid because we're inside a function
  }

  AOS.init({
    duration: 800,
    easing: "ease-in-out",
    once: true, // Animation happens only once
    offset: 50, // Trigger animations 50px before element is in view
    delay: 0, // Global delay (individual delays still work)
    anchorPlacement: "top-bottom", // When to trigger animations
    disable: function () {
      // Disable AOS on mobile devices for better performance
      return window.innerWidth < 768;
    },
  });

  console.log("AOS initialized successfully");
});

// Refresh AOS on window resize (throttled)
let resizeTimeout;
window.addEventListener("resize", function () {
  clearTimeout(resizeTimeout);
  resizeTimeout = setTimeout(function () {
    if (typeof AOS !== "undefined") {
      AOS.refresh();
    }
  }, 250);
});
