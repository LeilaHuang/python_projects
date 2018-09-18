# 拆分markdown 语句
text = open("lorem.md",'r').read()
frags = text.split('\n')
for f in frags:
    if f == '':
        frags.remove(f)

    if f.startswith('###'):
        print(f + ' is title')

t1 = frags[0]
p1 = frags[1]
t2 = frags[2]
p2 = frags[3]

p1_keywords = []
for i in p1.split():
    if i.startswith('**'):
        clean_word = i.strip('**')
        p1_keywords.append(clean_word)
print(p1_keywords)

p2_links = []
for i in p2.split():
    if i.startswith('['):
        split_words = i.split('](')
        group = (split_words[0][1:],split_words[1][:-2])
        p2_links.append(group)
print(p2_links)
#
content = {}
p1_dict =  {
    'raw':p1,
    'keywords':p1_keywords,
}
content['p1'] = p1_dict
print(content['p1']['keywords'])