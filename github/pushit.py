#!/usr/bin/env python3
'''

   git commit in one script

'''
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import os

commit_message  = input('Commit comment: ')
working_dir     = '/home/student/mycode'
git_add         = 'git add *'
git_commit      = 'git commit -m "' + commit_message + '"'
git_push        = 'git push origin'

os.chdir(working_dir)
os.system(git_add)
os.system(git_commit)
os.system(git_push)
