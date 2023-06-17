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


/*submit 버튼 */
function submitForm() {
    const checkbox = document.getElementById("flexCheckDefault");
    
    if (checkbox.checked) {
        // 체크박스가 체크된 경우
        alert("제출 완료! 메시지가 제출되었습니다.");
    } else {
        // 체크박스가 체크되지 않은 경우
        alert("개인정보 제공에 동의해주세요.");
    }
}




/* 검색 기능 구현*/

const algorithmData = [
    { name: "1,2,3 더하기", page: "./1,2,3 더하기.html" },
    { name: "1로 만들기", page: "./1로 만들기.html" },
    { name: "계단오르기", page: "./계단오르기.html" },
    { name: "계수 정렬", page: "./계수정렬.html" },
    { name: "떡볶이 문제", page: "./떡볶이 문제.html" },
    { name: "버블 정렬", page: "./버블정렬.html" },
    { name: "삽입 정렬", page: "./삽입정렬.html" },
    { name: "선택 정렬", page: "./선택정렬.html" },
    { name: "이진탐색 일반구현", page: "./이진탐색일반구현.html" },
    { name: "이진탐색 재귀구현", page: "./이진탐색재귀구현.html" },
    { name: "퀵 정렬", page: "./퀵정렬.html" },
    { name: "평벙한 배낭", page: "./평범한 배낭.html" },
    { name: "포도주 시식", page: "./포도주 시식.html" },
    { name: "피보나치수 2", page: "./피보나치수 2.html" },
    { name: "bisect 라이브러리", page: "./pages/bisect 라이브러리.html" }
];

  // 검색 인터페이스 요소 가져오기
const searchInput = document.getElementById("searchInput");
const searchResults = document.getElementById("searchResults");

searchInput.addEventListener("input", handleSearch);
searchInput.addEventListener("focus", handleSearch);
document.addEventListener("click", handleClickOutside);

// 검색어 처리 함수
function handleSearch() {
    const searchTerm = searchInput.value.toLowerCase(); // 검색어를 소문자로 변환
    const matchingAlgorithms = algorithmData.filter(
      algorithm => algorithm.name.toLowerCase().includes(searchTerm)
    ); // 검색어와 일치하는 알고리즘 필터링

    // 검색어가 있을 경우에만 검색 결과 표시
    if (searchTerm.length > 0) {
      displaySearchResults(matchingAlgorithms);
    } else {
      hideSearchResults();
    }
}

// 검색 결과 표시 함수
function displaySearchResults(results) {
    // 이전 검색 결과 삭제
    searchResults.innerHTML = "";

    // 검색 결과가 있는지 확인
    if (results.length > 0) {
      // 검색 결과를 순회하며 동적으로 생성하여 표시
      results.forEach(result => {
        const algorithmCard = document.createElement("div");
        algorithmCard.classList.add("searchcard");
        algorithmCard.innerHTML = `
          <h3>${result.name}</h3>
        `;

        // 클릭 이벤트 리스너 추가
        algorithmCard.addEventListener("click", () => {
          // 새 창에서 링크 열기
          window.open(result.page);
        });

        searchResults.appendChild(algorithmCard);
      });
    } else {
      // 일치하는 결과가 없음을 표시
      const noResultsMessage = document.createElement("p");
      noResultsMessage.textContent = "일치하는 결과가 없음";
      searchResults.appendChild(noResultsMessage);
    }

    // 검색 결과 표시
    searchResults.style.display = "block";
}

  // 검색 결과 숨기는 함수
function hideSearchResults() {
    searchResults.innerHTML = "";
    searchResults.style.display = "none";
}

  // 검색 결과 영역 이외 클릭 이벤트 처리 함수
function handleClickOutside(event) {
    if (
        !searchResults.contains(event.target) &&
        event.target !== searchInput
    ) 
    {
      hideSearchResults();
    }
}