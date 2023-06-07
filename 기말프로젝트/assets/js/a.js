/*네비게이션 bar 불러오기*/

fetch('../pages/navbar.html')
    .then(response => response.text())
    .then(data => {
    document.getElementById('navbar-container').innerHTML = data;
    })
    .catch(error => {
    console.error('네비게이션 바를 가져오는 동안 오류가 발생했습니다:', error);
});

/*탑 섹션 불러오기*/
fetch('../pages/top.html')
    .then(response => response.text())
    .then(data => {
    document.getElementById('top').innerHTML = data;
    })
    .catch(error => {
    console.error('탑 섹션을 가져오는 동안 오류가 발생했습니다:', error);
});

/*footer 불러오기*/
fetch('../pages/footer-clone.html')
    .then(response => response.text())
    .then(data => {
    document.getElementById('footer-clone').innerHTML = data;
    })
    .catch(error => {
    console.error('footer을 가져오는 동안 오류가 발생했습니다:', error);
});


/*슬라이드 효과*/
const slickSlide1 = jQuery('#slick-slide-1')

if(slickSlide1) {
    slickSlide1.slick({
        dots: true,
        arrows: true,
        slidesToShow: 3,
        slideToScroll: 1,
        autoplay: false,
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