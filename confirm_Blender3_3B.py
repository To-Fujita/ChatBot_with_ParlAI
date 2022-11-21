# Confirm ParlAI Agent for Blender3_3B by T. Fujita 2022/11/21

from http.client import HTTPConnection
import sys
sys.path.append('./ParlAI-main/')                   # Please set the PATH name according to your environment.

from parlai.scripts.interactive import Interactive

Interactive.main(
    task= 'projects.bb3.tasks.module_level_tasks:MemoryDecisionTeacher',
    model_file='zoo:bb3/bb3_3B/model',
    loglevel= 'debug',
    
)
