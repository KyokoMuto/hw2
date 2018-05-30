def count_score(word):
    return len(word)+2*(word.count('j')+word.count('k')+word.count('x')+word.count('z'))+(word.count('q')+word.count('f')+word.count('h')+word.count('l')+word.count('m')+word.count('p')+word.count('c')+word.count('v')+word.count('w')+word.count('y'))

def long_search(word):
    dict={}
    yfile = open('dict.txt','r')
    line = yfile.readline()
    for i in line:
        data=line.replace('\n','')
        dict[data]=''.join(sorted(data))#nomeaning
        line = yfile.readline()
    yfile.close()
    print(dict[line.replace('\n','')])
    store=[]
    max=0
    for v,t in dict.items():
        if word in t:
            store.append(v)
            if max<count_score(t):
                max=count_score(t)
                max_word=v
    return max_word