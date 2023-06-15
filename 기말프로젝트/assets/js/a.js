/*슬라이드 효과*/
const slickSlide1 = jQuery('#slick-slide-1')

if(slickSlide1) {
    slickSlide1.slick({
        dots: true,
        arrows: true,
        slidesToShow: 3,
        slideToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    })
}

const slickSlide2 = jQuery('#slick-slide-2')

if(slickSlide2) {
    slickSlide2.slick({
        dots: true,
        arrows: true,
        slidesToShow: 3,
        slideToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    })
}

const slickSlide3 = jQuery('#slick-slide-3')

if(slickSlide3) {
    slickSlide3.slick({
        dots: true,
        arrows: true,
        slidesToShow: 3,
        slideToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        responsive: [
            {
                breakpoint: 768,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 576,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    })
}