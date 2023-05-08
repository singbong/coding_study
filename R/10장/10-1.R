Sys.setenv(JAVA_HOME='C:/Program Files/Java/jre-1.8')
install.packages('koNLP')
install.packages("KoNLP")
library(RColorBrewer)
library(wordcloud)                              
library(RColorBrewer)
library(KoNLP)

text= readLines('./R/10장/mis_document.txt', encoding= 'UTF-8')
buildDictionary(ext_dic = 'woorimalsam')
pla2= brwer.pal(8, 'Dark2')
noun= sapply(text, extractNoun, USE.NAMES=F)
noun
