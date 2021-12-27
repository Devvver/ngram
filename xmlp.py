from sklearn.feature_extraction.text import CountVectorizer
from pymorphy2 import MorphAnalyzer
from newspaper import Article
from newspaper import Config
from newspaper.article import ArticleException
import ssl
from mxml import YaSearch


with open("ini.txt", "r", encoding="utf-8") as f:
    infa = f.readlines()
#    infa= infa.strip("/n")
f.close()
y = YaSearch(infa[0],infa[1])
results = y.search(infa[2], page=1)
if "\n" in y.lem:
    y.lem.remove("\n")
if " " in y.lem:
    y.lem.remove(" ")
#print(y.lem)
ssl._create_default_https_context = ssl._create_unverified_context
urls = []
if results.error is None:
    for result in results.items:
        print(result.url)
        urls.append(result.url)
stop_url1=['wikipedia.org','vk.com','facebook.com','yandex.ru']

clear_urls=[]
clear_urls = [u for u in urls if all(
    s not in u for s in stop_url1
)]
#for fullurl in urls:
#    for iurl in stop_url1:
#        if iurl not in fullurl:
#            clear_urls.append(fullurl)
print("=================================")
print(clear_urls)




stroki = []
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
config = Config()
config.browser_user_agent = user_agent
config.request_timeout = 10
for url in clear_urls:
    article = Article(url,config=config)
    try:
        article.download()
        article.parse()
    except ArticleException:
        continue

#    print(article.text)
    textm = article.text
    textm = textm.replace('\n','')
    stroki.append(textm)
with open("text.txt", "w", encoding='utf-8') as file:
    for kk in stroki:
        file.write(kk)
file.close()

m = MorphAnalyzer()
texts = [z.rstrip() for z in open('text.txt', encoding='utf-8')]
stop_words = [z.rstrip() for z in open('water.txt', encoding='utf-8')]

cvn = CountVectorizer(ngram_range=(2,4), stop_words=stop_words)
words_nf = [' '.join([m.parse(word)[0].normal_form for word in x.split()]) for x in texts]
ngrams = cvn.fit_transform(words_nf)
vb = cvn.vocabulary_
count_values = ngrams.toarray().sum(axis=0)
ngrams ={}
j =1
for ng_count, ng_text in sorted([(count_values[i],k) for k,i in vb.items()], reverse=True):
    ngrams[ng_text] = str(ng_count)
    print(ng_text, ng_count, sep='\t')
    if j>=10:
        break
    else:
        j =j+1



#print(ngrams)
a = []

for k, v in ngrams.items():
    a.append(k+";"+str(v))
kk8=0
# тут какой то ахтунг с циклом
for kk8 in range(len(y.lem)):
    a[kk8]= a[kk8]+";"+y.lem[kk8]
    kk8+1


print(a)
with open(infa[2].strip()+'.csv', 'w', encoding="utf-8") as file:
#    wr = file.write(file, delimiter=';')
    for xxx in range(len(a)-1):
        file.write(a[xxx]+"\n")
file.close()
#    wr.writerows(a)
#info_data = pd.DataFrame.from_dict(ngrams, orient = 'index')
#filename = infa[2].strip()+'.xlsx'
#info_data.to_csv(infa[2].strip()+'.csv')


