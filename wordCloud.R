install.packages("tm")  # for text mining
install.packages("SnowballC") # for text stemming
install.packages("wordcloud") # word-cloud generator 
install.packages("RColorBrewer") # color palettes
# Load
library("tm")
library("SnowballC")
library("RColorBrewer")
library("wordcloud")

install.packages("wordcloud")
library(wordcloud)

result104 <-read.csv("Dobby_wordcount_fake.csv")
# View(result)
# m1 <- as.matrix(result)
# v <- sort(rowSums(result$word), decreasing = TRUE)
# d <- data.frame(word = names(v), freq = v)
# wordcloud(result$word, result$count, min.freq = 1, random.order = F, ordered.colors = F,
#           colors = rainbow(length(row.names(result))))

#png(filename="/Users/young/Documents/碩二課程/text mining/realNews.png",  width = 1500, height = 480)
wordcloud(words = result104$word, freq = result104$count, min.freq =100,
          max.words=200, random.order=FALSE, rot.per=0.35, 
          colors=brewer.pal(8, "Dark2"))
#dev.off()


