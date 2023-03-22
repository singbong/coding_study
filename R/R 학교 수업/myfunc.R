myfunc = function(x,y){
  val.sum = x+y
  val.mul = x*y
  return(list(sum=val.sum, mul=val.mul))
}
mydiv = function(x,y=2){
  result = x/y
  return(result)
}
result= myfunc(5,8)
s= result$sum
m= result$mul
cat('5+8=',s, '\n')   #5,8의 합
cat('5*8=',m,'\n')    #5,8의 곱
