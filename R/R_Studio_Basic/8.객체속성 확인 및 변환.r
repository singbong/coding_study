#1 객체 속성 정보 확인 class(), typeof()
letters
class(letters)
class(1)
class(2:5)
class(c(3,5,7))

typeof(2:5)
typeof(c(3,5,7))

df = data.frame(aa= 1:3, bb=3:5)
df
class(df)

#2 객체 속성 변환 as.character(), as.numeric(), as.data.frame()

is.numeric(123)
is.numeric("aa")
is.character("aa")
is.character(123)

is.na(123)
is.na("aa")
is.na(NA)
is.na(c(1,3,NA,5))

ls_01 = list(aa= 1:3, bb= 4:6)
ls_01

ls_df_01= as.data.frame(ls_01)
class(ls_df_01)

ls_02 = list(aa= 1:3,
             bb= 4:8)
ls_02             
as.data.frame(ls_02)
