**TwittyCrawly**

A simple tweet crawler, implemented as part of my Bs.c thesis, which was Automated Sentiment Analysis on Twitter's tweets revolving the general sentiment of twitter users about IranDeal (The landmark Iran nuclear deal coined the JCPOA).

This is just the twitter crawling part of the thesis made public to showcase the effort that was done.

**Methodology**

The collected tweets across the span of 7 days where fed to a MongoDB database. Then the collection was used to aggregate and retrieve relevant documents, while filtering out corrupt and undesired tweets.
Then the corpus of selected tweets where fed into a recurrent neural network to analyse the sentiment of each tweet, and another classifier to detect important words in the tweet.

Feel free to contact me at alirezasadeghi71@gmail.com.
