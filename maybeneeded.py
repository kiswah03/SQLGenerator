
import spacy
from difflib import get_close_matches
from spacy import displacy

#syntable=','.join(str(rows[0]) for j, rows in enumerate(mycursor) if rows[1]==n)

"""for n in needwords: 
        tempword= ','.join(row[0] for row in syntable if row[1]==n)
        if(tempword != ''): query.append(tempword)
    print(query)"""
    
    
"""substring=list(n for n in dbtables if suggest in n == True)
    closematches=set(closematches+substring)
    print(substring)"""
'''tables=["date_of_birth","dateofbirth","dob"]
substring=list(n for n in tables if n.lower().find("date_of_birth") != -1)
print(substring)
closematches=set(get_close_matches("date_of_birth", tables))
print(closematches)'''

#needwords.remove(','.join(row[1] for row in syntable))
#query.append(','.join(row[0] for row in syntable))
#print(query)

nlp = spacy.load('en_core_web_sm') 
about_interest_text = ('which all employees worked 5 hours in project p2')
about_interest_doc = nlp(about_interest_text)
displacy.serve(about_interest_doc, style='dep')
#entities=[(i, i.label_, i.label) for i in about_interest_doc.ents]
print(entities)

# synonym finder in close match function
elif (len(closematches)== 0):
        text_word = Word(suggest)
        synonyms = set()
        for synset in text_word.synsets:
            for lemma in synset.lemmas():
                synonyms.add(lemma.name())
        synonyms.remove(suggest)
        for t in dbdatas:
            for n in synonyms:
                if(engine.singular_noun(t)== n or t==n):
                    value=t
                    break
            if(value != ""):
                break

#mycursor.execute("select k.keyword , s.word from synonyms s inner join keyword k on s.keyword=k.idkeyword where s.keyword=3 and word in {}".format(tuple(needwords[1:])))
    #syntable=list(mycursor.fetchall())
    #syntable = [list(i) for i in syntable]
    #print(syntable)
    #for row in syntable:
        #needwords=[row[0] if n==row[1] else n for n in needwords]

    spcharacter=[n for n in NlWord if(n=="~" or n=="=" or n=="+" or n=="_" or n==">" or n=="<" or n=="^" or n=="[" or n=="]")]
    print(spcharacter,"spcharacter")
    needwords=[n for n,t in blobs.tags if (t.startswith('N') or t.startswith('W') or t.startswith('JJ') or 
    t=='VB' or t == 'CD' or n=="~" or n=="=" or n=="+" or n=="_" or n==">" or n=="<" or n=="^" or n=="[" or n=="]")]
    # to split special character
    i=0
    specialcharacter=["~","=","+","_",">","<","^","[","]"]
    spcharacter=[]
    spindex=[]
    while i<len(NlWords):
        if(NlWords[i] in specialcharacter):
            spcharacter.append(NlWords[i])
            spindex.append(i)
        i+=1
    
#old needwords
    #spcharacter=[n for n in NlWord if(n=="~" or n=="=" or n=="+" or n=="_" or n==">" or n=="<" or n=="^" or n=="[" or n=="]")]
    #print(spcharacter,"spcharacter")
    #needwords=[n for n,t in blobs.tags if (t.startswith('N') or t.startswith('W') or t.startswith('JJ') or 
    #t=='VB' or t == 'CD' or n=="~" or n=="=" or n=="+" or n=="_" or n==">" or n=="<" or n=="^" or n=="[" or n=="]")]
    
#old connection statement
   #mycursor.execute("select k.keyword , s.word from synonyms s inner join keyword k on s.keyword=k.idkeyword where s.keyword=1 and word='{}'".format(needwords[0]))