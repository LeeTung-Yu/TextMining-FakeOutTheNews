# TextMining-FakeOutTheNews
## This project is created by 2017 NTHU Text Mining class students: Celia Chen, Dobby Yang, Edison Lee, and Thierry Lhee.
In the era of information explosion, the most important thing is to distinguish between truth and fake. Especially, when it comes down to News and information, how to filter out fake News has become a critical issue. Therefore, we want to provide a service that can help identify fake news. 

### You can crawl [Yahoo News](https://www.yahoo.com/news/) using `yahoo_news_crawler.py`
In this python file, we use `selenium` and `BeautifulSoup` package to crawl latest news from Yahoo News Website. 

### After collecting data, please use `news_classification.py`
We use three classification algorithms: Logistic Regression, Decision Tree and Support Vector Machine(SVM). And we try two different feature extraction strategies: count frequency and tf-idf. 

### Also, we use topic analysis method to cluster news in `topicWebsit.R`
The package we use is `lda` in R language. Example output: 
![lda](https://github.com/LeeTung-Yu/TextMining-FakeOutTheNews/blob/master/19125561_1381301311965857_1880614569_o.png)

### For further exploration, use `wordCloud.R` to create Word Cloud for both real news and fake news.
Example: 
![Real news word cloud](https://github.com/LeeTung-Yu/TextMining-FakeOutTheNews/blob/master/real_news.png)
