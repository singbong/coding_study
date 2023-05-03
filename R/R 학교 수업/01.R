library(ggplot2)
library(ggmap)

register_google(key = 'AIzaSyDRI065JSqKKXqcmVbZQ7GiNnoKp0dA0ys')

monthly_accident = read.csv(file = "./R/data.csv", encoding = 'cp949')

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
