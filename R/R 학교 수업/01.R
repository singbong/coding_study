library(ggmap)
##ggmap::register_google(key = '본인 API 키')##
ggmap::register_google(key = 'AIzaSyDRI065JSqKKXqcmVbZQ7GiNnoKp0dA0ys')

cen = c(127.1568,37.8732)        #경도와 위도 값을 center값으로 직접 입력
map <- get_googlemap(center=cen,
                     zoom = 20,
                     size = c(640,640),
                     maptype = 'satellite') 		# 지도 생성
ggmap(map) 
