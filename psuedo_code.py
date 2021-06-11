#open the file with tweets
from collections import Counter
lis=[]
with open('filename.txt') as f:
    #save tweets with stripping the newline character
    tweets = [line.rstrip() for line in f]
for tweet in tweets:
    #create a dict of the count of words in each tweet
    lis.append(dict((Counter(tweet.split()))))
#given slur words
slur_words = []
count=[]
#getting count of slur words in each tweet
for i in range(len(lis)):
    dic=dict()
    for word in slur_words:
        if word in lis[i]:
            dic[word]=lis[i].get(word)
    count.append(dic)
res=[]
for i in count:
    value = i.values()
    #list with total count of slur words in each tweet - which indicates the level of profanity of each tweet 
    res.append(sum(value))
for tweet,cnt in zip(tweets,res):
        #we can set a threshold - say for example if a tweet has more than x racial slurs we say its profane 
        if cnt > 1:
            print(tweet +" is profane")