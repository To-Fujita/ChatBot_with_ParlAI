# Confirm ParlAI Agent for All_Tasks_mt by T. Fujita 2021/08/01

import sys
sys.path.append('./ParlAI-master/')

from parlai.scripts.interactive import Interactive

Interactive.main(
        model_file='zoo:dodecadialogue/all_tasks_mt/model',
        inference='beam',
        beam_size= 3,
        beam_min_length= 10,
        beam_block_ngram= 3,
        beam_context_block_ngram= 3,
)

