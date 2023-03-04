# 반복문
#for(객체 in 1차원 벡터){
    #실행코드
#}
for( v in c(1,3,5)){
  print(paste0("v= ",v))
}

for(b in 8:12){
  print(paste0('sample_', sprintf(fmt = '%02d', b), '.csv'))
}

df= data.frame(aa= 1:3,
               bb= 11:13)
df

for( row in 1:nrow(df)){
  df[row, "cc"] = df[row,"aa"] + df[row, "bb"]
  print(df)
  Sys.sleep(2) # 파이썬의 time.sleep 과 같음음
}

df$"dd"= df$bb+ df$aa
df

#조건문 if c언어랑 같음



