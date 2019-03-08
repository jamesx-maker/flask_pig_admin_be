# coding: utf8
'内存中存储种猪信息列表'

from app.models import PigList
from app.common.util import error_logger
from app.common.errorcode import error_code
from app.common.util import asyncFunc

pig_animalnum_list = [] # 种猪种猪号列表，未出栏的
pig_earid_list = [] # 种猪耳标号列表，未出栏的
pig_id_list = [] # 种猪id列表，未出栏的
pig_identity_info_list = [] # [{ pid, animalnum, earid }] 未出栏的

@asyncFunc
def initialize_piglist(animalnum_list = pig_animalnum_list, earid_list = pig_earid_list, id_list = pig_id_list):
    '''
    从数据库中获取数据到内存
    :return:
    '''
    animalnum_list.clear()
    earid_list.clear()
    try:
        res = PigList().get_all()

        for r in res:
            animalnum_list.append(r.animalnum)
            earid_list.append(r.earid)
            id_list.append(r.id)
            pig_identity_info_list.append({
                'animalnum': r.animalnum,
                'earid': r.earid,
                'pid': r.id,
            })

    except Exception as e:
        error_logger(e)
        error_logger(error_code['1100_2001'])

def animalnum_exist(animalnum):
    '''
    检查 animalnum 是否已经存在
    :return:
    '''
    return animalnum in pig_animalnum_list

def earid_exist(earid):
    '''
    检查 earid 是否已经存在
    :return:
    '''
    return earid in pig_earid_list

def pid_exist(pid):
    '''
    检查 pid 是否已经存在
    :return:
    '''
    return pid in pig_id_list

def get_pig_info(param, type='pid'):
    '''
    依据种猪 pid、earid、animalnum 查询种猪信息
    :param param:
    :param type: pid || earid || animalnum
    :return:
    '''

    if type == 'pid':
        for r in pig_identity_info_list:
            if r.get('pid') == param:
                return r
    elif type == 'earid':
        for r in pig_identity_info_list:
            if r.get('earid') == param:
                return r
    else:
        for r in pig_identity_info_list:
            if r.get('animalnum') == param:
                return r
