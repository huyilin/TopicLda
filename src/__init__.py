import sys
sys.path.append("/export/home/team06/randomtrip/mysite/random_trip/src/")
import onlineldauser

vocab = file('/export/home/team06/randomtrip/mysite/random_trip/src/vocaball.txt').readlines()
olda=onlineldauser.OnlineLDA(vocab)