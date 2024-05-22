const swiper = new Swiper('.swiper-container', {
    // Optional parameters
    direction: 'horizontal',
    loop: true,
    effect: 'fade', // Use fade effect
    speed: 800, // Transition speed

    // If we need pagination
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
        dynamicBullets: true,
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    scrollbar: {
        el: '.swiper-scrollbar',
        hide: true,
    },

    autoplay: {
        delay: 3000, // Reduced delay for faster transition
        disableOnInteraction: false,
    },

    // Add parallax effect
    parallax: true,

    // Add keyboard control
    keyboard: {
        enabled: true,
    },

    // Add mousewheel control
    mousewheel: {
        invert: false,
    },
});