# -*- coding: utf-8 -*-

import os
import ycm_core

cpp_flags = [
    '-Wall',
    '-Wextra',
    '-Werror',
    '-Wno-long-long',
    '-Wno-variadic-macros',
    '-fexceptions',
    '-DNDEBUG',
    '-std=c++11',
    '-x',
    'c++',
    '-I',
    '/usr/include',
    '/usr/local/include',
    '-isystem',
    '/usr/lib/gcc/x86_64-linux-gnu/8/include',
    '-isystem',
    '/usr/include/x86_64-linux-gnu',
    '-isystem',
    '/opt/ros/noetic/include',
    '-isystem',
    '/usr/include/pcl-1.10',
    '-isystem',
    '/usr/include/eigen3',
    '-isystem',
    '/usr/include/c++/9',
    '-isystem',
    '/usr/include/c++/5/bits',
    '-isystem',
    '/home/lingtengqiu/anaconda3/envs/SelfRecon/lib/python3.8/site-packages/torch/include',
    '-isystem',
    '/home/lingtengqiu/anaconda3/envs/SelfRecon/lib/python3.8/site-packages/torch/include/torch/csrc/api/include',
  ]

cuda_flags = [
    '-Wall',
    '-Wextra',
    '-Werror',
    '-Wno-long-long',
    '-Wno-variadic-macros',
    '-fexceptions',
    '-DNDEBUG',
    '-std=c++11',
    '-x',
    'cuda',
    '--cuda-gpu-arch=sm_35',
    '-I',
    '/usr/include',
    '/usr/local/include',
    '-isystem',
    '/usr/lib/gcc/x86_64-linux-gnu/8/include',
    '-isystem',
    '/usr/include/x86_64-linux-gnu',
    '-isystem',
    '/opt/ros/noetic/include',
    '-isystem',
    '/usr/include/pcl-1.10',
    '-isystem',
    '/usr/include/eigen3',
    '-isystem',
    '/usr/include/c++/9',
    '-isystem',
    '/usr/include/c++/5/bits',
    '-isystem',
    '/home/lingtengqiu/anaconda3/envs/SelfRecon/lib/python3.8/site-packages/torch/include',
    '-isystem',
    '/home/lingtengqiu/anaconda3/envs/SelfRecon/lib/python3.8/site-packages/torch/include/torch/csrc/api/include',
  ]


SOURCE_EXTENSIONS = [ '.cpp', '.cxx', '.cc', '.c', '.cu']

def FlagsForFile( filename, **kwargs ):
    if filename.endswith('.cu'):
        return {
                'flags': cuda_flags,
                'do_cache': True,
                }
    else:
        return {
            'flags': cpp_flags,
            'do_cache': True
        }

def PythonSysPath( **kwargs ):
  sys_path = kwargs[ 'sys_path' ]
  sys_path.insert( 1, '/usr/lib/python3/dist-packages' )
  return sys_path
