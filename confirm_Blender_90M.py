# Confirm ParlAI Agent for Blender_90M by T. Fujita 2021/08/01

import sys
#sys.path.append('./ParlAI-master/')
sys.path.append('./ParlAI-main/')                   # Please set the PATH name according to your environment.

from parlai.scripts.interactive import Interactive

Interactive.main(
    task= 'blended_skill_talk',
    model_file='zoo:blender/blender_90M/model',
)

