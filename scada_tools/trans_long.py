# coding=utf-8

import string



record_mask = 0xffffffff
column_mask = 0xffff
area_mask=0xff

def key_to_id(input):
    str=''
    item=input.split(' ')
    table_id=long(item[0])
    if(len(item)==3):
        column_id=long(item[1])
        record_id=int(item[2])
        id=table_id<<48|column_id<<32|record_id
        str=repr(long(id))
        return str
    elif(len(item)==4):
        area_id=long(item[1])
        column_id=long(item[2])
        record_id=int(item[3])
        id=table_id<<48|area_id<<24|column_id<<32|record_id
        str=repr(long(id))
        return str
    elif(len(item)==1):
        str='不带area\n'+id_to_key(input)
        str+='\n\n'+'带area\n'+area_id_to_key(input)
        return str

def id_to_key(key):
    key=long(key)
    record_id=key&record_mask
    column_id=(key>>32) & column_mask
    table_id=key>>48
    str=''
    str='record:'+repr(int(record_id))+'\n'\
        +'column:'+repr(int(column_id))+'\n'+'table:'+repr(int(table_id))
    id_str=repr(int(table_id))+' '+'0'+' '+repr(int(record_id))
    id_str=key_to_id(id_str)
    str+='\n'+id_str
    return str

def area_id_to_key(key):
    key=long(key)
    record_id=key&0xffffff
    column_id=(key>>32) & area_mask
    area_id=(key>>24) & area_mask
    table_id=key>>48
    str=''
    str='record:'+repr(int(record_id))+'\n'\
        +'column:'+repr(int(column_id))+'\n'\
        +'area:'+repr(int(area_id))+'\n'\
        +'table:'+repr(int(table_id))
    id_str=repr(int(table_id))+' '+'0'+' '+repr(int(record_id))
    id_str=key_to_id(id_str)
    str+='\n'+id_str
    return str
    