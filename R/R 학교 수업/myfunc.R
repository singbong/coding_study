06.
# 한빛 출판 네트워크 사이트의 예제 source 폴더에 파일이 있습니다
monthly_accident <- read.csv(file = "./source/Ch09/도로교통공단_시도_시군구별_월별_교통사고(2018).csv", encoding = 'utf-8')
Sys.setlocale("LC_ALL", "korean")
myds <- aggregate(x = monthly_accident[ monthly_accident[,"시도"] == "서울","발생건수"], by = list("시군구" = monthly_accident[monthly_accident[,"시도"] == "서울",]$시군구), 
                  FUN = sum)
names <- myds$시군구
gc <- geocode(enc2utf8(names))
cen <- c(mean(gc$lon), mean(gc$lat))
df = data.frame(name = names, lon = gc$lon, lat = gc$lat, freq = myds$x)
map <- get_googlemap(center = cen, maptype = "roadmap", zoom = 11)
gmap <- ggmap(map)
gmap + geom_point(data = df, aes(x = lon, y = lat, size = freq), alpha = 0.5, col = "green") + scale_size_continuous(range = c(1, 14)) + 
  geom_text(data = df, aes(x = lon, y = lat), size = 6, label = df$name, col = "steelblue", )
# 글자는 위치 확인용으로 넣었습니다.

07.
myds <- aggregate(x = monthly_accident[monthly_accident[, "시도"] != "세종", "사망자수"],
                  by = list("시도" = monthly_accident[monthly_accident[, "시도"] != "세종",]$시도), 
                  FUN = sum)
names <- myds$시도
gc <- geocode(enc2utf8(names))
cen <- c(mean(gc$lon), mean(gc$lat))
df = data.frame(name = names, lon = gc$lon, lat = gc$lat, freq = myds$x)
map <- get_googlemap(center = cen, maptype = "roadmap", zoom = 7)
gmap <- ggmap(map)

gmap + geom_point(data = df, 
                  aes(x = lon, y = lat, size = freq), alpha = 0.3, col = "black") +
  scale_size_continuous(range = c(1, 14)) 
# 투명도를 .05 로 하면 너무 안보여서 0.3으로 했습니다.
