import urllib2
import json
print "Give some key words seperated by commas to find the best beer for you"
keysSTR = raw_input()
keysLST = keysSTR.split(',')
url = 'http://api.brewerydb.com/v2/search?q='+'"'+keysSTR+'"'+'&type=beer&key=8a3535c240368c2c188159a51bc481cc&format=json'
html= urllib2.urlopen(url).read()
beers = json.loads(html)
total = int(beers['totalResults'])
data= beers['data']
counter=[]
ctrmax=0
for i in range(0,total):
    try:
     desc = data[i]['description']
     DescriptionLST= desc.split(" ")
     ctr=0
     for m in DescriptionLST :
         for w in keysLST:
          if w == m :
              ctr=ctr+1
     counter.append(ctr)
     if ctr > ctrmax :
         ctrmax=ctr
         maxi=i
         maxid=data[maxi]['id']
         beername = data[maxi]['name']
    except:
        pass

counter.sort(reverse=True)
try:
 if counter[0] != counter[1] :
  print "The beer for you based on the keywords you gave is:", beername
  print "Beer ID: ", maxid
 else:
    print "2 or more beers found with same amount of keywords please be more specific"

except:
     print "No results found"
