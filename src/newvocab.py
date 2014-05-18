import os

corpus=os.listdir('/home/yilin/workspace/data/vocaball')
i=0
j=0
vocab=list()
stopwords=list()
k=0
with open("/home/yilin/Downloads/wordsstop.txt",'r') as f :
    for line in f:
        stopwords.append(line.split('"')[1])
with open("/home/yilin/workspace/topicmodel/onlineldavb/vocaball.txt",'w') as vocab_write:
    for feature in corpus:
        with open("/home/yilin/workspace/data/vocaball/"+feature,'r') as file:
            i=i+1;
            for line in file:
               if(len(line)>1000):
                   line=line.split(' ')
                   for word in line :
                       if word in vocab or len(word)<=3 or len(word)>30 or 'www' in word or 'http' in word:
                           pass
                       else:
                           vocab.append(word)
                           vocab_write.write(word+'\n')
                           print word
