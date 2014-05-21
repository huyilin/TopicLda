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
    user_ids=[]
    cur.execute("select user_id from UserProfile")
    ids=cur.fetchall()
    for id in ids:
        	user_ids.append(re.findall('\d+',str(id[0]))[0])
    vocab = file('./vocaball.txt').readlines()
    W = len(vocab)
    olda=onlineldauser.OnlineLDA(vocab)
    cur.execute("truncate table User_Topic")
    for user_id in user_ids:
        cur.execute("select tags from UserProfile where user_id=%s",user_id)
        user_tags=cur.fetchone()
        if user_tags!=None:
            user_tags=[user_tags[0]]
            (gamma, bound) = olda.update_lambda(user_tags)
            gamma=str(gamma[0]).strip(' []').replace('\n','')
            gamma=gamma.split()
            gamma_db=''
            for index,value in enumerate(gamma):
                cur.execute("insert into User_Topic(user_id,topic_id,weight) values(%s,%s,%s)",(user_id,str(index),value))        
                if float(value)>0.01:
                    gamma_db+=(str(index)+':'+value+',')
                cur.execute("update UserProfile set user_vector=%s where id=%s",(gamma_db,user_id))
    db.commit()
    db=MySQLdb.Connect(host="localhost",
               user="team06",
               passwd="aiM7chah,d",
               db="randomtrip")
    cur=db.cursor()
#     except:
#         pass
if __name__ == '__main__':
    main()
