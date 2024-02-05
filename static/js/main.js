/**
* Template Name: Arsha - v4.3.0
* Template URL: https://bootstrapmade.com/arsha-free-bootstrap-html-template-corporate/
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/
(function() {
  "use strict";

  /**
   * Easy selector helper function
   */
  const select = (el, all = false) => {
    el = el.trim()
    if (all) {
      return [...document.querySelectorAll(el)]
    } else {
      return document.querySelector(el)
    }
  }

  /**
   * Easy event listener function
   */
  const on = (type, el, listener, all = false) => {
    let selectEl = select(el, all)
    if (selectEl) {
      if (all) {
        selectEl.forEach(e => e.addEventListener(type, listener))
      } else {
        selectEl.addEventListener(type, listener)
      }
    }
  }

  /**
   * Easy on scroll event listener 
   */
  const onscroll = (el, listener) => {
    el.addEventListener('scroll', listener)
  }

  /**
   * Navbar links active state on scroll
   */
  let navbarlinks = select('#navbar .scrollto', true)
  const navbarlinksActive = () => {
    let position = window.scrollY + 200
    navbarlinks.forEach(navbarlink => {
      if (!navbarlink.hash) return
      let section = select(navbarlink.hash)
      if (!section) return
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        navbarlink.classList.add('active')
      } else {
        navbarlink.classList.remove('active')
      }
    })
  }
  window.addEventListener('load', navbarlinksActive)
  onscroll(document, navbarlinksActive)

  /**
   * Scrolls to an element with header offset
   */
  const scrollto = (el) => {
    let header = select('#header')
    let offset = header.offsetHeight

    let elementPos = select(el).offsetTop
    window.scrollTo({
      top: elementPos - offset,
      behavior: 'smooth'
    })
  }

  /**
   * Toggle .header-scrolled class to #header when page is scrolled
   */
  let selectHeader = select('#header')
  if (selectHeader) {
    const headerScrolled = () => {
      if (window.scrollY > 100) {
        selectHeader.classList.add('header-scrolled')
      } else {
        selectHeader.classList.remove('header-scrolled')
      }
    }
    window.addEventListener('load', headerScrolled)
    onscroll(document, headerScrolled)
  }

  /**
   * Back to top button
   */
  let backtotop = select('.back-to-top')
  if (backtotop) {
    const toggleBacktotop = () => {
      if (window.scrollY > 100) {
        backtotop.classList.add('active')
      } else {
        backtotop.classList.remove('active')
      }
    }
    window.addEventListener('load', toggleBacktotop)
    onscroll(document, toggleBacktotop)
  }

  /**
   * Mobile nav toggle
   */
  on('click', '.mobile-nav-toggle', function(e) {
    select('#navbar').classList.toggle('navbar-mobile')
    this.classList.toggle('bi-list')
    this.classList.toggle('bi-x')
  })

  /**
   * Mobile nav dropdowns activate
   */
  on('click', '.navbar .dropdown > a', function(e) {
    if (select('#navbar').classList.contains('navbar-mobile')) {
      e.preventDefault()
      this.nextElementSibling.classList.toggle('dropdown-active')
    }
  }, true)

  /**
   * Scrool with ofset on links with a class name .scrollto
   */
  on('click', '.scrollto', function(e) {
    if (select(this.hash)) {
      e.preventDefault()

      let navbar = select('#navbar')
      if (navbar.classList.contains('navbar-mobile')) {
        navbar.classList.remove('navbar-mobile')
        let navbarToggle = select('.mobile-nav-toggle')
        navbarToggle.classList.toggle('bi-list')
        navbarToggle.classList.toggle('bi-x')
      }
      scrollto(this.hash)
    }
  }, true)

  /**
   * Scroll with ofset on page load with hash links in the url
   */
  window.addEventListener('load', () => {
    if (window.location.hash) {
      if (select(window.location.hash)) {
        scrollto(window.location.hash)
      }
    }
  });

  /**
   * Preloader
   */
  let preloader = select('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove()
    });
  }

  /**
   * Initiate  glightbox 
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Skills animation
   */
  let skilsContent = select('.skills-content');
  if (skilsContent) {
    new Waypoint({
      element: skilsContent,
      offset: '80%',
      handler: function(direction) {
        let progress = select('.progress .progress-bar', true);
        progress.forEach((el) => {
          el.style.width = el.getAttribute('aria-valuenow') + '%'
        });
      }
    })
  }

  /**
   * Portfolio isotope and filter
   */
  window.addEventListener('load', () => {
    let portfolioContainer = select('.portfolio-container');
    if (portfolioContainer) {
      let portfolioIsotope = new Isotope(portfolioContainer, {
        itemSelector: '.portfolio-item'
      });

      let portfolioFilters = select('#portfolio-flters li', true);

      on('click', '#portfolio-flters li', function(e) {
        e.preventDefault();
        portfolioFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        portfolioIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        portfolioIsotope.on('arrangeComplete', function() {
          AOS.refresh()
        });
      }, true);
    }

  });






  /**
   * blog isotope and filter
   */
  window.addEventListener('load', () => {
    let blogContainer = select('.blog-container');
    if (blogContainer) {
      let blogIsotope = new Isotope(blogContainer, {
        itemSelector: '.blog-item'
      });

      let blogFilters = select('#blog-flters li', true);

      on('click', '#blog-flters li', function(e) {
        e.preventDefault();
        blogFilters.forEach(function(el) {
          el.classList.remove('filter-active');
        });
        this.classList.add('filter-active');

        blogIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        blogIsotope.on('arrangeComplete', function() {
          AOS.refresh()
        });
      }, true);
    }

  });

  /**
   * Initiate blog lightbox
   */
  const blogLightbox = GLightbox({
    selector: '.blog-lightbox',
  });

  /**
   * blog details slider
   */
  new Swiper('.blog-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });

  /**
   * Animation on scroll
   */
  window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: "ease-in-out",
      once: true,
      mirror: false
    });
  });

})()





window.addEventListener('DOMContentLoaded', () => {
  const coursesContainer = document.querySelector('.courses-container');
  const coursesFilters = document.querySelectorAll('#courses-filters li');
  const coursesIsotope = new Isotope(coursesContainer, {
    itemSelector: '.course-item'
  });

  coursesFilters.forEach(filter => {
    filter.addEventListener('click', function() {
      coursesFilters.forEach(f => {
        f.classList.remove('filtercourses-active');
        f.classList.remove('filter-active'); // Remove 'filter-active' from all filters
      });
      this.classList.add('filtercourses-active');
      const filterValue = this.getAttribute('data-filter');
      coursesIsotope.arrange({ filter: filterValue });
    });
  });

  new Swiper('.courses-details-slider', {
    speed: 400,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    }
  });
});



// Initialize Swiper with the custom class name


new Swiper('.custom-swiper', {
  slidesPerView: 3,
  spaceBetween: 20, // Adjust the space between images as needed
  loop: true, // Enable looping if needed
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
    pagination: {
    el: '.swiper-pagination',
    clickable: true,
  },
});



// In counterAnimation.js
const counters = document.querySelectorAll('.counter');

const options = {
  root: null,
  rootMargin: '0px',
  threshold: 0.5,
};



const startCounting = (entries, observer) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const countUp = (current, end, duration, id) => {
        const increment = end / duration;
        const timer = setInterval(() => {
          current += increment;
          document.getElementById(id).textContent = Math.floor(current);
          if (current >= end) {
            clearInterval(timer);
            document.getElementById(id).textContent = end;
          }
        }, 3); // Change the interval duration as needed for the speed of counting
      };

      const target = +entry.target.getAttribute('data-target');
      const id = entry.target.querySelector('span').id;
      countUp(0, target, 1000, id); // Change the duration of the count animation
      observer.unobserve(entry.target);
    }
  });
};

const observer = new IntersectionObserver(startCounting, options);
counters.forEach((counter) => observer.observe(counter));






// Importing the debounce function from lodash
const { debounce } = _;

// Your existing counter functions

const debouncedStartCounter = debounce(startCounter, 500);
const debouncedStartCoffeeCounter = debounce(startCoffeeCounter, 500);

// Triggering the counters on scroll with a debounce
window.addEventListener('scroll', () => {
  debouncedStartCounter();
  debouncedStartCoffeeCounter();
});

/*

// Counter for number of years
 const experienceCounter = document.getElementById('count_experience');

function countYears() {
  const startDate = new Date('2009-01-01');
  const currentDate = new Date();
  const differenceInYears = currentDate.getFullYear() - startDate.getFullYear();
  return differenceInYears;
}

function startCounter() {
  let count = 0;
  const target = countYears();

  const timer = setInterval(() => {
    count++;
    experienceCounter.textContent = count;
    if (count === target) {
      clearInterval(timer);
    }
  }, 300); // Adjust the interval to change the speed of counting
}

startCounter();


const coffeeCounter = document.getElementById('count_coffee');

function countCoffee() {
  const startDate = new Date('2023-01-01'); // Replace with the actual start date
  const currentDate = new Date();
  const differenceInDays = Math.floor((currentDate - startDate) / (1000 * 60 * 60 * 24));
  const cupsPerDay = 4;

  return 21350 + differenceInDays * cupsPerDay;
}

function startCoffeeCounter() {
  const target = countCoffee();
  const duration = 3000; // Duration in milliseconds (4 seconds)
  const frames = 100;
  const increment = Math.ceil(target / frames);

  let count = 0;
  let currentCount = 0;
  const timer = setInterval(() => {
    count += increment;
    currentCount++;

    if (currentCount === frames) {
      clearInterval(timer);
      count = target;
    }

    coffeeCounter.textContent = count;
  }, duration / frames);
}

startCoffeeCounter();
*/
