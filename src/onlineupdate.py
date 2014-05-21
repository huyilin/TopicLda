#!/usr/bin/python

# onlinewikipedia.py: Demonstrates the use of online VB for LDA to
# analyze a bunch of random Wikipedia articles.
#
# Copyright (C) 2010  Matthew D. Hoffman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import cPickle, string, numpy, getopt, sys, random, time, re, pprint
import sys
import onlineldaupdate
import wikirandom
import citydoc
import os
import subprocess

def main():
    """
    Downloads and analyzes a bunch of random Wikipedia articles using
    online VB for LDA.
    """
    batchsize = 4
#   corpus=os.listdir("/home/yilin/Downloads/OxygenGuide/OxygenGuide_2014-04-12-a/articles")
    target_dir=("/home/yilin/workspace/data/EuroCityStemmed")
#     target_dir=("/home/yilin/workspace/topicmodel/onlineldavb/sample")
    corpus=os.listdir(target_dir)
    D = 3.3e6
    K = 100 # number of topics
    documentstoanalyze=38; # number of batches
    file1=open('../city-lda-vector.txt','w').close()
    file1=open('../city-lda-vector.txt','a')
    vocab = file('./vocaball.txt').readlines()
    W = len(vocab)
    olda=onlineldaupdate.OnlineLDA(vocab)
    for iteration in range(0, documentstoanalyze):
        # Download some articles
#         try:
#           (docset, articlenames)=wikirandom.get_random_wikipedia_articles(batchsize)
        (docset, articlenames) = citydoc.get_cities(batchsize,iteration,corpus,target_dir);
        (gamma, bound) = olda.update_lambda(docset)
        (wordids, wordcts) = onlineldaupdate.parse_doc_list(docset, olda._vocab)
        perwordbound = bound * len(docset) / (D * sum(map(sum, wordcts)))
        print '%d:  rho_t = %f,  held-out perplexity estimate = %f' % \
        (iteration, olda._rhot, numpy.exp(-perwordbound))
        for city,vector in zip(articlenames,gamma):
            file1.write(city+','+str(vector).strip(' []').replace('\n','')+'\n')
#         except:
#             pass
#     subprocess.call('rm -r ./data'.split())
#     subprocess.call('mkdir data'.split())
#     numpy.savetxt('./data/lambda.dat',olda._lambda)
#     numpy.savetxt('./data/K.dat',[olda._K])
#     numpy.savetxt('./data/D.dat',[olda._D])
#     numpy.savetxt('./data/alpha.dat',[olda._alpha])
#     numpy.savetxt('./data/eta.dat',[olda._eta])
#     numpy.savetxt('./data/tau0.dat',[olda._tau0])
#     numpy.savetxt('./data/kappa.dat',[olda._kappa])
#     numpy.savetxt('./data/updatect.dat',[olda._updatect])
#     numpy.savetxt('./data/Elogbeta.dat',olda._Elogbeta)
#     numpy.savetxt('./data/expElogbeta.dat',olda._expElogbeta)
    file1.close()
#     numpy.savetxt('./data/gamma.dat', gamma)

if __name__ == '__main__':
    main()
    

