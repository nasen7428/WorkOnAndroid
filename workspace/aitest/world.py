#! python

#this is description about how to run the world.
#It better can be use args to define some var.

import sys
import os


def help():
    print """

    -an [num],define how much attribute in this word.
    -sn [aindex] [num],define how much status on this attribute who index is aindex.
    -show [dbfile],show the world about how tu run.
    
    
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

def load(data,filepath):
    #load data from file.


def save(data,filepath):
    #save data to file.


