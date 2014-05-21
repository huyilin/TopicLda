import cPickle, string, numpy, getopt, sys, random, time, re, pprint
import sys
import onlineldauser
import citydoc
import os
import subprocess
import MySQLdb

def main():
    db=MySQLdb.Connect(host="localhost",
                   user="team06",
                   passwd="aiM7chah,d",
                   db="randomtrip")
    cur=db.cursor()
    batchsize = 1
    D = 3.3e6
    K = 100 # number of topics
    documentstoanalyze=1; # number of batches
    user_id='2'
    cur.execute("select tags from UserProfile where id=%s",user_id)
    user_tags=cur.fetchone()
    user_tags=[user_tags[0]]
    print user_tags
    vocab = file('./vocaball.txt').readlines()
    W = len(vocab)
    olda=onlineldauser.OnlineLDA(vocab)
    (gamma, bound) = olda.update_lambda(user_tags)
    (wordids, wordcts) = onlineldauser.parse_doc_list(user_tags, olda._vocab)
    perwordbound = bound * len(user_tags) / (D * sum(map(sum, wordcts)))
    gamma=str(gamma[0]).strip(' []').replace('\n','')
    gamma=gamma.split()
    gamma_db=''
    for index,value in enumerate(gamma):
        if float(value)>0.01:
            gamma_db+=(str(index)+':'+value+',')
    cur.execute("update UserProfile set user_vector=%s where id=%s",(gamma_db,user_id))
    db.commit()
if __name__ == '__main__':
    main()
