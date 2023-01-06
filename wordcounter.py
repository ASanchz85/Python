namef = input('Enter file name: >>> ')
if len(namef) < 1 : namef = 'text.txt'
handle = open(namef)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
q1 = input('Would you like to more words in the list?  (y/n) >>> ')

if q1 == 'y' :
    mwords = int(input('How many ?? >>> '))
    print('Sorted List:\n', sorted([(v,k) for k,v in counts.items()], reverse=True)[:mwords]) #one way of compressing lines
else :
    print('Done! ... exiting ...')
    quit()
    
q2 = input('Would you like to see it in columns?  (y/n) >>> ')

#second way of doing the same
tmp = list()
for k,v in counts.items() :
    new = (v,k)
    tmp.append(new)
tmp = sorted(tmp, reverse=True)

if q2 == 'y' :
    for v,k in tmp[:mwords] :
        print(k,v)
else :
    print('Done! ... exiting ...')
    quit()