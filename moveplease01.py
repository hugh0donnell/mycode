#!/usr/bin/env python3
'''   blah blah blah comments  '''


import shutil
import os

"""  more comments

comment

comment

"""


def main():
    os.chdir('/home/student/mycode/')
    shutil.move('raynor.obj', 'ceph_storage/')      # comment comment

    xname = input('new name for kerrigan.obj ?  ')
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



main()

