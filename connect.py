from textblob import TextBlob
from textblob import Word
import mysql.connector
from difflib import get_close_matches 
from tkinter import * 
from tkinter import ttk
from tkinter.ttk import *
import inflect

win = Tk() 
win.title("NLIDB")    
win.geometry("650x300")  

def replacedata(NlWord):
    NlWord=NlWord.lower()
    NlWord=NlWord.replace(" starts with "," [ ")
    NlWord=NlWord.replace(" ends with "," ] ")
    NlWord=NlWord.replace(" start with "," [ ")
    NlWord=NlWord.replace(" end with "," ] ")
    NlWord=NlWord.replace(" starts as "," [ ")
    NlWord=NlWord.replace(" ends as "," ] ")
    NlWord=NlWord.replace(" start as "," [ ")
    NlWord=NlWord.replace(" end as "," ] ")
    NlWord=NlWord.replace(" with "," ")
    NlWord=NlWord.replace(","," ")
    NlWord=NlWord.replace(" create "," make ")
    NlWord=NlWord.replace(" build "," make ")
    NlWord=NlWord.replace(" fields "," ")
    NlWord=NlWord.replace(" field "," ")
    NlWord=NlWord.replace(" table "," ")
    NlWord=NlWord.replace(" tables "," ")
    NlWord=NlWord.replace(" details of "," ")
    NlWord=NlWord.replace(" detail of "," ")
    NlWord=NlWord.replace(" want "," ")
    NlWord=NlWord.replace(" like "," ")    
    NlWord=NlWord.replace(" i "," ")
    NlWord=NlWord.replace(" is not "," ~ ")
    NlWord=NlWord.replace(" as "," = ")
    NlWord=NlWord.replace(" values "," ")
    NlWord=NlWord.replace(" value "," ")
    NlWord=NlWord.replace(" greater than or equal to"," + ")
    NlWord=NlWord.replace(" more than or equal to"," + ")
    NlWord=NlWord.replace(" less than or equal to"," _ ")
    NlWord=NlWord.replace(" greater than "," > ")
    NlWord=NlWord.replace(" above "," > ")
    NlWord=NlWord.replace(" below "," < ")
    NlWord=NlWord.replace(" more than "," + ")
    NlWord=NlWord.replace(" less than "," < ")
    NlWord=NlWord.replace(" equals "," = ")
    NlWord=NlWord.replace(" equal to "," = ")
    NlWord=NlWord.replace(" not equal to "," ~ ")
    NlWord=NlWord.replace(" manager's name "," manager ")
    NlWord=NlWord.replace(" department name "," name ")
    NlWord=NlWord.replace(" named as "," where name ")
    NlWord=NlWord.replace(" employeed in "," where ")
    NlWord=NlWord.replace(" managed by "," where manager ")
    NlWord=NlWord.replace(" between "," ^ ")
    NlWord=NlWord.replace(" list of ","  ")
    NlWord=NlWord.replace(" to "," place ")
    return(NlWord)
def replaceaggregate(NlWord):
    NlWord=NlWord.replace(" total no of "," count ")
    NlWord=NlWord.replace(" total number of "," count ")
    NlWord=NlWord.replace(" number of "," count ")
    NlWord=NlWord.replace(" no of "," count ")
    NlWord=NlWord.replace(" tally of "," count ")
    NlWord=NlWord.replace(" total of "," sum ")
    NlWord=NlWord.replace(" gross "," sum ")
    NlWord=NlWord.replace(" sum total "," sum ")
    NlWord=NlWord.replace(" grand total "," sum ")
    NlWord=NlWord.replace(" total "," sum ")
    NlWord=NlWord.replace(" aggregate "," sum ")
    NlWord=NlWord.replace(" add "," sum ")
    NlWord=NlWord.replace(" greatest "," max ")
    NlWord=NlWord.replace(" highest "," max ")
    NlWord=NlWord.replace(" biggest "," max ")
    NlWord=NlWord.replace(" largest "," max ")
    NlWord=NlWord.replace(" top "," max ")
    NlWord=NlWord.replace(" topmost "," max ")
    NlWord=NlWord.replace(" lowest "," min ")
    NlWord=NlWord.replace(" bottom "," min ")
    NlWord=NlWord.replace(" base "," min ")
    NlWord=NlWord.replace(" least "," min ")
    NlWord=NlWord.replace(" mean "," avg ")
    NlWord=NlWord.replace(" center "," avg ")
    NlWord=NlWord.replace(" median "," avg ")
    NlWord=NlWord.replace(" mode "," avg ")
    NlWord=NlWord.replace(" middle "," avg ")
    NlWord=NlWord.replace(" standard "," avg ")
    return(NlWord)
def checkaggregate(col):
    agg=["max","min","avg","count","sum"]
    if(col in agg):
        return(True)
    else:
       return(False)
def findmatch(suggest,dbdatas):
    substring=list(n for n in dbdatas if n.lower().find(Word(suggest).lemmatize()) != -1)
    closematches=set(substring+ get_close_matches(suggest, dbdatas))
    closematches=list(closematches)
    print("matches",closematches)
    engine=inflect.engine()
    value=""
    if(len(closematches)>1):
        for n in closematches:
            if(engine.plural(suggest)== n or engine.singular_noun(suggest)== n or suggest==n ):
                value=n
                break
        #if(value==""):
            #print("which table you want to select: ",closematches)
    elif (len(closematches)==1):
            value=closematches[0]
    return(value)
    
def check_tag(str):
    blob2=TextBlob(str)
    #print(blob1.tags)
    if(blob2.tags):
            word=blob2.tags[0][0]
            tag=blob2.tags[0][1]
            if (tag.startswith('N') and str!="~" and str!="=" and str!="+" and str!="_" and str!=">" and str!="<" and str!="^" and str!="[" and str!="]" ):
                str='"'+str+'"'
    return(str)
def fun_connect():
    NlWord=data.get()
    conn=mysql.connector.connect(user="root",password="sahla",host="localhost",database="nliqd")
    conn1=mysql.connector.connect(user="root",password="sahla",host="localhost",database="prjlib")
    mycursor1=conn1.cursor()
    mycursor=conn.cursor()
    engine = inflect.engine()

    wheresyn=['whose','which','where','who']
    #NlWord="send record of name of employee name whose name is hari"
    #NlWord="send me list of employees"
    #NlWord="update age to hari from employee table where name as mani"
    NlWord=replacedata(NlWord)
    NlWord=replaceaggregate(NlWord)
    #print(NlWord)
    txt = NlWord
    blobs = TextBlob(txt)
    syntable=[]
    needwords=[]
    
    NlWords=NlWord.split(" ")
    
    i=0
    while i<len(NlWords):
        blob1=TextBlob(NlWords[i])
        #print(blob1.tags)
        if(blob1.tags):
            word=blob1.tags[0][0]
            tag=blob1.tags[0][1]
            if (tag.startswith('N') or tag.startswith('W') or tag.startswith('JJ') or tag=='VB' or tag == 'CD'):
             needwords.append(word)
        i=i+1
    print(needwords)

    mycursor.execute("select k.keyword from keyword k inner join synonyms s on s.keyword=k.idKeyword where s.word='{}'".format(needwords[0]))
    needwords[0]=','.join(rows[0] for j, rows in enumerate(mycursor))
    
    syntable.append(needwords[0])
    print(needwords)   
    
    whereword=""
    for n in needwords:
        if (n in wheresyn):
            syntable.append("where")
            whereword=n
    #print(whereword)
    print(syntable)

    table=""
    columns=[]
    condition=[]
    query=""
    suggest=""
    whereflag=0
    twonameflag=0
    betwflag=0
    ewithflag=0
    ewithflag=0
    lastcol=""
    cond=""
    colagg=""
    setcond=""

    if(syntable[0] == "select"):
        needwords.remove("select")
        #del needtags[0]
        i=0
        while i<len(needwords):
            suggest=needwords[i]
            if (table == ""):
                mycursor1.execute("show tables")
                dbtables=list(rows[0] for j, rows in enumerate(mycursor1))
                table=findmatch(suggest,dbtables)
                if (table !=""):
                    needwords.remove(suggest)
                    #del needtags[i]
                    i=0
                    continue
            elif(suggest != whereword and whereflag==0):
                if(checkaggregate(suggest) == False):
                    mycursor1.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='{}'".format(table))
                    dbcolumns=list(rows[0] for j, rows in enumerate(mycursor1))
                    col=findmatch(suggest,dbcolumns)
                    if (col!="" and colagg==""): 
                        columns.append(col)
                        needwords.remove(suggest)
                        i=0
                        continue
                    elif(col!="" and colagg!=""):
                        col=colagg+col+")"
                        columns.append(col)
                        needwords.remove(suggest)
                        i=0
                        colagg=""
                        continue
                else:
                    colagg=suggest+"("
                    needwords.remove(suggest)
                    i=0
                    continue
            elif(suggest == whereword):
                needwords=needwords[i:]
                needwords.remove(whereword)
                #del needtags[i]
                whereflag=1
                i=0
                continue
            elif(whereflag==1):
                col=""
                mycursor1.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='{}'".format(table))
                dbcolumns=list(rows[0] for j, rows in enumerate(mycursor1))
                engine=inflect.engine()
                if(engine.plural(suggest) in dbcolumns):
                    col=engine.plural(suggest)
                elif(engine.singular_noun(suggest) in dbcolumns):
                    col=engine.singular_noun(suggest)
                elif(suggest in dbcolumns): col=suggest
                #col=findmatch(suggest,dbcolumns)
                if (col!=""): 
                    if(cond!=""):
                       condition.append(cond)
                    betwflag=0
                    swithflag=0
                    ewithflag=0
                    twonameflag=1
                    lastcol=col
                    cond=""
                    cond+=col
                    needwords.remove(suggest)
                    #del needtags[i]
                    i=0
                    continue
                elif(col=="" and cond!=""):
                    okword=suggest
                    suggest=check_tag(suggest)
                    if(twonameflag==1 and suggest == "~"): cond+="!="
                    elif(twonameflag==1 and suggest == "+"): cond+=">="
                    elif(twonameflag==1 and suggest == "_"): cond+="<="
                    elif(twonameflag==1 and suggest == "^"):
                        cond+=" between " 
                        betwflag=1
                    elif(twonameflag==1 and suggest == "["): 
                        cond+=" like "
                        swithflag=1
                    elif(twonameflag==1 and suggest == "]"): 
                        cond+=" like "
                        ewithflag=1
                    elif(twonameflag==0 and betwflag==1):
                        cond+=suggest+" and "+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and swithflag==1):
                        cond+="{}%".format(suggest)
                    elif(twonameflag==0 and ewithflag==1):
                        cond+="%{}".format(suggest)
                    elif(twonameflag==1  and suggest != "=" and suggest != ">" and suggest != "<"):
                        cond+="="+suggest
                    elif(twonameflag==0 and suggest=="<"):
                        cond+=" and "+lastcol+"<"+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest==">"):
                        cond+=" and "+lastcol+">"+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest=="+"):
                        cond+=" and "+lastcol+">="+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest=="_"):
                        cond+=" and "+lastcol+"<="+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    else: cond+=suggest
                    needwords.remove(okword)
                    #del needtags[i]
                    twonameflag=0
                    i=0
                    continue
            i+=1
        columns=set(columns)
        if(colagg!=""):
            col=colagg+"*)"
            columns.append(col)
        if(table == ""):
            query="There is no such table defined in database..."
        elif(not columns):
            columns=list(columns)
            columns.append("*")
        if(whereflag==1):
           condition.append(cond)
           query="select "+','.join(n for n in columns)+" from "+table+" where "+" and ".join(n for n in condition)
        else:query="select "+','.join(n for n in columns)+" from "+table

    elif(syntable[0] == "delete"):#part for delete statement
        needwords.remove("delete")
        i=0
        while i<len(needwords):
            suggest=needwords[i]
            print(needwords)
            if (table == ""):
                mycursor1.execute("show tables")
                dbtables=list(rows[0] for j, rows in enumerate(mycursor1))
                table=findmatch(suggest,dbtables)
                if (table !=""):
                    needwords.remove(suggest)
                    i=0
                    continue  
            elif(suggest == whereword):
                needwords=needwords[i:]
                needwords.remove(whereword)
                whereflag=1
                i=0
                continue
            elif(whereflag==1):
                col=""
                mycursor1.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='{}'".format(table))
                dbcolumns=list(rows[0] for j, rows in enumerate(mycursor1))
                engine=inflect.engine()
                if(engine.plural(suggest) in dbcolumns):
                    col=engine.plural(suggest)
                elif(engine.singular_noun(suggest) in dbcolumns):
                    col=engine.singular_noun(suggest)
                elif(suggest in dbcolumns): col=suggest
                if (col!=""): 
                    if(cond!=""):
                       condition.append(cond)
                    betwflag=0
                    swithflag=0
                    ewithflag=0
                    twonameflag=1
                    lastcol=col
                    cond=""
                    cond+=col
                    needwords.remove(suggest)
                    i=0
                    continue
                elif(col=="" and cond!=""):
                    okword=suggest
                    suggest=check_tag(suggest)
                    if(twonameflag==1 and suggest == "~"): cond+="!="
                    elif(twonameflag==1 and suggest == "+"): cond+=">="
                    elif(twonameflag==1 and suggest == "_"): cond+="<="
                    elif(twonameflag==1 and suggest == "^"):
                        cond+=" between " 
                        betwflag=1
                    elif(twonameflag==1 and suggest == "["): 
                        cond+=" like "
                        swithflag=1
                    elif(twonameflag==1 and suggest == "]"): 
                        cond+=" like "
                        ewithflag=1
                    elif(twonameflag==0 and betwflag==1):
                        cond+=suggest+" and "+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and swithflag==1):
                        cond+="{}%".format(suggest)
                    elif(twonameflag==0 and ewithflag==1):
                        cond+="%{}".format(suggest)
                    elif(twonameflag==1  and suggest != "=" and suggest != ">" and suggest != "<"):
                        cond+="="+suggest
                    elif(twonameflag==0 and suggest=="<"):
                        cond+=" and "+lastcol+"<"+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest==">"):
                        cond+=" and "+lastcol+">"+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest=="+"):
                        cond+=" and "+lastcol+">="+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest=="_"):
                        cond+=" and "+lastcol+"<="+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    else: cond+=suggest
                    needwords.remove(okword)
                    twonameflag=0
                    i=0
                    continue
            i+=1
        if(table == ""):
            query="There is no such table defined in database..."
            return
        elif(whereflag==1):
           condition.append(cond)
           query="delete from "+table+" where "+" and ".join(n for n in condition)
        else:query="delete from "+table

    elif(syntable[0] == "update"):#place for update statement
        needwords.remove("update")
        i=0
        while i<len(needwords):
            suggest=needwords[i]
            if (table == ""):
                mycursor1.execute("show tables")
                dbtables=list(rows[0] for j, rows in enumerate(mycursor1))
                table=findmatch(suggest,dbtables)
                if (table !=""):
                    needwords.remove(suggest)
                    i=0
                    continue
            elif(suggest == whereword):
                needwords=needwords[i:]
                needwords.remove(whereword)
                whereflag=1
                cond=""
                print(needwords)
                i=0
                continue
            else:
                col=""
                mycursor1.execute("select COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='{}'".format(table))
                dbcolumns=list(rows[0] for j, rows in enumerate(mycursor1))
                engine=inflect.engine()
                if(engine.plural(suggest) in dbcolumns):
                    col=engine.plural(suggest)
                elif(engine.singular_noun(suggest) in dbcolumns):
                    col=engine.singular_noun(suggest)
                elif(suggest in dbcolumns): col=suggest
                if (col!=""): 
                    if(cond!="" and whereflag==1):
                       condition.append(cond)
                    betwflag=0
                    swithflag=0
                    ewithflag=0
                    twonameflag=1
                    lastcol=col
                    cond=""
                    cond+=col
                    needwords.remove(suggest)
                    i=0
                    continue
                elif(col=="" and suggest=="place"):
                    #okword=suggest
                    #suggest=check_tag(suggest)
                    if(cond==lastcol):
                        setcond=lastcol+"="+check_tag(needwords[i+1])
                    else:
                        setcond=lastcol+"="+check_tag(needwords[i+1])
                        condition.append(cond)
                    cond=""
                    setcondflag=1
                    needwords.remove(needwords[i+1])
                    needwords.remove(suggest)
                    i=0
                    continue
                elif(col=="" and cond=="" and setcond!=""):
                    setcond+=check_tag(suggest)
                    needwords.remove(suggest)
                    i=0
                    continue
                elif(col=="" and cond!="" and whereflag==1):
                    if(twonameflag==1 and suggest == "~"): cond+="!="
                    elif(twonameflag==1 and suggest == "+"): cond+=">="
                    elif(twonameflag==1 and suggest == "_"): cond+="<="
                    elif(twonameflag==1 and suggest == "^"):
                        cond+=" between " 
                        betwflag=1
                    elif(twonameflag==1 and suggest == "["): 
                        cond+=" like "
                        swithflag=1
                    elif(twonameflag==1 and suggest == "]"): 
                        cond+=" like "
                        ewithflag=1
                    elif(twonameflag==0 and betwflag==1):
                        cond+=suggest+" and "+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and swithflag==1):
                        cond+='"{}%"'.format(suggest)
                    elif(twonameflag==0 and ewithflag==1):
                        cond+='"%{}"'.format(suggest)
                    elif(twonameflag==1  and suggest != "=" and suggest != ">" and suggest != "<"):
                        cond+="="+check_tag(suggest)
                    elif(twonameflag==0 and suggest=="<"):
                        cond+=" and "+lastcol+"<"+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest==">"):
                        cond+=" and "+lastcol+">"+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest=="+"):
                        cond+=" and "+lastcol+">="+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    elif(twonameflag==0 and suggest=="_"):
                        cond+=" and "+lastcol+"<="+needwords[i+1]
                        needwords.remove(needwords[i+1])
                    else: cond+=check_tag(suggest)
                    needwords.remove(suggest)
                    twonameflag=0
                    i=0
                    continue
            i+=1
        if(table == ""):
            query="There is no such table defined in database..."
            return
        elif(cond!=""):
           condition.append(cond)
           query="update "+table+" set "+setcond+" where "+" and ".join(n for n in condition)
        elif(setcond!=""):
            query="update "+table+" set "+setcond+" where "+" and ".join(n for n in condition)
        else:query="Please rephrase your sentence"
    print(query)
    show(query)
        
#fun_connect()

def show(query):
    resultquery.configure(text="")
    resultquery.configure(text=query)
    if(query != "There is no such table defined in database..."):
        conn=mysql.connector.connect(user="root",password="sahla",host="localhost",database="prjlib")
        mycursor=conn.cursor()
        mycursor.execute(query)
        num_fields = len(mycursor.description)
        field_names = [i[0] for i in mycursor.description] 
        print(field_names,num_fields)
        records = mycursor.fetchall()
        records = [list(i) for i in records]
        print(records)
        cols=['col1','col2']
        listBox = ttk.Treeview(win, columns=field_names, show='headings') 
        listBox.grid(row=3, column=0, columnspan=4)   
        for n in field_names:
            listBox.heading(n, text=n)

        for n in records:
            listBox.insert("", "end", values=n)


#creating label  
label1 = Label(win, text = "Enter request").grid(row=0, column=0)
data = Entry(win,width = 70)
data.grid(row = 0, column = 1)  

#creating button  
sbmitbtn = Button(win, text = "Submit", width=15, command=fun_connect).grid(row = 1, column = 1)  
global resultquery
#resultquery=Label(root,text="")
resultquery = Label(win, text = "The resulting query is shown here")
resultquery.grid(row = 2, column = 1)
#label = Label(scores, text="High Scores", font=("Arial",30)).grid(row=0, columnspan=3)


#showScores = Button(scores, text="Show scores", width=15, command=show).grid(row=4, column=0)
#closeButton = Button(scores, text="Close", width=15, command=exit).grid(row=4, column=1)

win.mainloop()