# Confirm ParlAI Agent for Alice by T. Fujita 2021/08/01

import sys
sys.path.append('./ParlAI-master/')
sys.path.append('./ParlAI-main/')

from parlai.scripts.interactive import Interactive

Interactive.main(model='alice')
