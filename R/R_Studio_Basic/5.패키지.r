#library() 함수 대신 :: 기호 활용하여 특정 패키지의 함수 또는 데이터 사용 가능
#cran.r-project.org/ 에 접속해서 패키지 카테고리에서 다운로드 가능

library("data.table")

#R 내부 다운로드 및 설치
#install.packages() 함수를 사용 / 패키지 제거는 remove.packages()
install.packages("abc.zip", repos = NULL, type = "source") #( 파일이름 or 경로,  )
devtools::install_github()
remotes::install_github()
install.packages()

#data.table::
?mean #base 패키지의 함수 임 을 알 수 있음

library("dplyr")
?merge
