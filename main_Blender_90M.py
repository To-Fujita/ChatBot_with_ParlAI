# ChatBot with "Blender 90M" by F. Fujita on 2021/08/02

import sys
sys.path.append('./ParlAI-master/')

from parlai.core.params import ParlaiParser
from parlai.core.agents import create_agent, Agent
from parlai.core.worlds import create_task
from parlai.core.script import ParlaiScript, register_script
from parlai.core.opt import Opt
from parlai.core.message import Message
from parlai.utils.misc import load_cands
from typing import Optional
import random
from flask import Flask, render_template, request


agent = ''
human_agent = ''
opt_org = ''
agent_name = 'Blender_90M'

app = Flask(__name__, static_url_path='/static')

@app.route("/")
# Display the HTML
def home():
    return render_template("index_EN.html")

@app.route("/get_Model")
# Set the Agent Name for HTML
def select_Model():
    temp_data = request.args.get('sel_Model')
    return str(agent_name)

@app.route("/get")
# Communicate with HTML
def get_bot_response():
    userText = request.args.get('msg')
    answer = make_answer(userText)
    return answer

# Create the answer
def make_answer(tempText):
    if ('[exit]' in tempText or '[EXIT]' in tempText):
        sys.exit()
    if (tempText == ""):
        tempText = " "
    if (('End' in tempText or 'end' in tempText or 'Terminate' in tempText or 'terminate' in tempText) and ('voice' in tempText and 'input' in tempText)):
        return str('Terminated the voice recognition.')
    else:
        temp_Answer = PatternResponder(tempText)
        return str(temp_Answer)

# ChatBot
class LocalHumanAgent(Agent):
    @classmethod
    def add_cmdline_args(
        cls, parser: ParlaiParser, partial_opt: Optional[Opt] = None
    ) -> ParlaiParser:

        agent = parser.add_argument_group('Local Human Arguments')
        agent.add_argument(
            '-fixedCands',
            '--local-human-candidates-file',
            default=None,
            type=str,
            help='File of label_candidates to send to other agent',
        )
        agent.add_argument(
            '--single_turn',
            type='bool',
            default=False,
            help='If on, assumes single turn episodes.',
        )
        return parser

    def __init__(self, opt, shared=None):
        super().__init__(opt)
        self.id = 'localHuman'
        self.episodeDone = False
        self.finished = False
        self.fixedCands_txt = load_cands(self.opt.get('local_human_candidates_file'))

    def observe(self, msg):
        global text_reply
        text_reply = msg["text"]
        return text_reply

    def act(self):
        global text_send
        reply = Message()
        reply['id'] = self.getID()
        reply_text = text_send
        reply_text = reply_text.replace('\\n', '\n')
        reply['episode_done'] = False
        reply['text'] = reply_text
        return reply

def setup_args(parser=None):
    if parser is None:
        parser = ParlaiParser(
            True, True, 'Interactive chat with a model on the command line'
        )
    parser.add_argument('-d', '--display-examples', type='bool', default=False)
    parser.add_argument(
        '--display-prettify',
        type='bool',
        default=False,
        help='Set to use a prettytable when displaying '
        'examples with text candidates',
    )
    parser.add_argument(
        '--display-add-fields',
        type=str,
        default='',
        help='Display these fields when verbose is off (e.g., "--display-add-fields label_candidates,beam_texts")',
    )
    parser.add_argument(
        '-it',
        '--interactive-task',
        type='bool',
        default=True,
        help='Create interactive version of task',
    )
    parser.add_argument(
        '--outfile',
        type=str,
        default='',
        help='Saves a jsonl file containing all of the task examples and '
        'model replies. Set to the empty string to not save at all',
    )
    parser.add_argument(
        '--save-format',
        type=str,
        default='conversations',
        choices=['conversations', 'parlai'],
        help='Format to save logs in. conversations is a jsonl format, parlai is a text format.',
    )
    parser.set_defaults(interactive_mode=True, task='interactive')
    LocalHumanAgent.add_cmdline_args(parser, partial_opt=None)
    return parser

def interactive(opt):
    global agent
    global human_agent
    global opt_org

    if isinstance(opt, ParlaiParser):
        opt = opt.parse_args()

    agent = create_agent(opt, requireModelExists=True)
    human_agent = LocalHumanAgent(opt)
    world = create_task(opt, [human_agent, agent])
    opt_org = opt

@register_script('interactive', aliases=['i'])
class Interactive(ParlaiScript):
    @classmethod
    def setup_args(cls):
        return setup_args()

    def run(self):
        return interactive(self.opt)


text_send = ''
text_reply = ''
select_no = 0
id_no = ''

def in_out(temp_text):
    global text_send
    global text_reply
    text_send = temp_text
    world = create_task(opt_org, [human_agent, agent])
    world.parley()
    return text_reply

# Create the answer
def PatternResponder(tempText):
    temp_Answer = in_out(str(tempText))
    return temp_Answer

def init():
    Interactive.main(
        task= 'blended_skill_talk',
        model_file='zoo:blender/blender_90M/model',
    )

if __name__ == "__main__":
    random.seed(42)
    init()
    app.run(host='127.0.0.1', port=5000, debug=True)
