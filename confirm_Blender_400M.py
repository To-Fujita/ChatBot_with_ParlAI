# Confirm ParlAI Agent for Blender_400M by T. Fujita 2021/08/01

import sys
sys.path.append('./ParlAI-master/')

from parlai.scripts.interactive import Interactive

Interactive.main(
    task= 'blended_skill_talk',
    model_file='zoo:blender/blender_400Mdistill/model',
)

