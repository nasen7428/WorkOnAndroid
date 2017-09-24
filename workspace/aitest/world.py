#! python

#this is description about how to run the world.
#It better can be use args to define some var.

import sys
import os


def help():
    print """
    python2 world.py [command] [-type] [args]
    [command] :
       rule-clear
       rule-add :
            [type]:
                -f file
                -a args aid,sid,fas0,fas1,fas2...
       rule-search :
            [type]:
                -f file
                -a args fas0,fas1,fas2..ii

    
    """


def main():



main()




def show_db_data():
    print """
    {
        [aid,sid,a0s,a1s....],
        [aid,sid,a0s,a1s....],
        ...
    }
    """

def show_how_to_writ_db_file():
    #show how to write a db file
    print """
    attrid,stateid,attr0state,attr1state,...
    attrid,stateid,attr0state,attr1state,..
    ....
    
"""




#command : .py rule clear
#clear db ruls...
def clear():
    dbhalper.clear()


#command : .py rule add 
#add new rul into db
def add(aid,sid,fs):
    #aid attribute id
    #sid state id
    #fs [a0s,a1s,a2s,....]
    insdata=(aid,sid,fs)
    #insdata [aid,sid,a0s,a1s,a2s...]
    dbhalper.insert(insdata)



#command : .py rule search
#this func will search rul table and return new state changes
def search(states):
    #search table and find what will change .
    aidsids=dbhalper.search(states)
    #states [fas1,fas2,fas3...]
    #aidsids [(aid,sid),(aid,sid),...]
    #define -1 is not any states.
    #define max states number is MSNUM.
    res=[MSNUM]
    for re in res:
        re=-1
    for aidsid in aidsids:
        res[aidsid[0]]=aidsid[1]
    #create new states 
    return res






