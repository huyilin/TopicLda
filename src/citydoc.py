import sys, urllib2, re, string, time
import os
import subprocess

## To arrange the files 
# whole="/home/yilin/Downloads/OxygenGuide/OxygenGuide_2014-04-12-a/articles"
# corpus=os.listdir(whole)
# for direc in corpus:
#     corpus1=os.listdir(whole+'/'+direc)
#     os.chdir(whole+'/'+direc)
#     for direc1 in corpus1:
#         subprocess.call(("mv "+direc1+" ..").split())
# os.chdir(whole)
# for direc in corpus:
#     subprocess.call(('rm -r '+direc).split())

def get_cities(batchsize,iteration,corpus,target_dir):
    docset=list()
    docnames=list()
    for doc in range(batchsize*iteration,batchsize*(iteration+1)):
        docset.append(open(target_dir+'/'+corpus[doc]).read())
        docnames.append(corpus[doc])
    return (docset, docnames)
    
    


    
    
