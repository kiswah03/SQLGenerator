from textblob import TextBlob
import nltk
from nltk.corpus import wordnet
import spacy

def fun_connect():
    NlWord="which department does smith manage?"
    #NlWord="how far, how long, how many, how much, how old"
    query=[]
    NlWords = NlWord.split()
    txt = NlWord
    blobs = TextBlob(txt)
    #needwords=[n for n,t in blobs.tags if (t.startswith('N') or t.startswith('W') or t.startswith('JJ') or 
    #t.startswith('V') or t == 'CD')]
    print(blobs.pos_tags)
    #print(needwords)
#fun_connect()

def subjectfinder():  
    nlp = spacy.load('en_core_web_sm')
    sent = "how many hours has smith worked in project p2"
    doc=nlp(sent)
    sub_toks = [tok for tok in doc if (tok.dep_ == "nsubj") ]
    print(sub_toks) 
subjectfinder()

def stopwordsfinder():
    for token in doc:
        if  token.is_stop:
            print (token)
    for token in doc:
        print (token.text, token.tag_, token.head.text, token.dep_)
    for chunk in doc.noun_chunks:
        print (chunk)
    
def most_similar(word):
    nlp = spacy.load('en_core_web_md', parser=False)
    by_similarity = sorted(word.vocab, key=lambda w: word.similarity(w), reverse=True)
    return [w.orth_ for w in by_similarity[:10]]

#most_similar(nlp.vocab[u'dog'])

def similarity_checker():
    nlp = spacy.load('en_core_web_md') 
    print("Enter two space-separated words") 
    words = input() 

    tokens = nlp(words) 
    for token in tokens: 
        print(token.text, token.has_vector, token.vector_norm, token.is_oov) 
    token1, token2 = tokens[0], tokens[1] 
    print("Similarity:", token1.similarity(token2)) 

#similarity_checker()

def pos_tagging():
    nlp = spacy.load("en_core_web_sm") 
    # Process whole documents 
    text = ("list the details of employees salary") 
    doc = nlp(text) 
    # Token and Tag 
    for token in doc: 
        print(token, token.pos_,token.lemma_)
#pos_tagging()

def nltksynonym():
    #text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
    #text.similar('employee')
    dog = wordnet.synset('date_of_birth.n.01')
    print(dog.lemma_names())

#nltksynonym()

def synonymfinder():
    text_word = Word("salary")
    synonyms = set()
    for synset in text_word.synsets:
        for lemma in synset.lemmas():
            synonyms.add(lemma.name())
    print(synonyms)