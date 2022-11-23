# ChatBot_with_ParlAI

## 1. Description
This is a chat bot based on the ParlAI by Facebook. You can talk to some chat bots by keyboard and/or voice.  
If you want to enjoy conversation in Japanese, please check "[ChatBot_with_GPT-2_Rinna](https://github.com/To-Fujita/ChatBot_with_GPT-2_Rinna)". The [Japanese_ChatBot_with_ParlAI](https://github.com/To-Fujita/Japanese_ChatBot_with_ParlAI) is also available.

## 2. Operational Environment
- Windows 10 64-bit
- Visual Studio Code (VS Code)
- Python 3.9.4 64-bit
- Browser: Microsoft Edge or Google Chrome

## 3. Demo
![ChatBot_000](https://to-fujita.github.io/Images/ChatBot_000.gif "Images for ChatBot")

## 4. Details
I have confirmed these Python Scripts on the above conditions only. I will show you below how to execute the Python scripts. 
### 4-1. Preparation
(a) Download & unzip the files  
Please download following files and put these unzipped folders under the system path passed.
- [ParlAI](https://github.com/facebookresearch/parlai): A framework for training and evaluating AI models on a variety of openly available dialogue datasets.
- ChatBot_with_ParlAI: Please download from above "Code". 
  
(b) Install some libraries to your Python  
Please install following libraries to your Python system.
- Pytorch: pip install torch
- ParlAI: pip install parlai
- Python-Aiml: pip install python-aiml or pip install aiml
- Flask: pip install Flask

### 4-2. Confirm to work some agents/models in ParlAI
If you finished the preparation above, please confirm to work some agents/models in ParlAI. 
After open the "ChatBot_with_ParlAI" folder, please open the each following files with VS Code.
- confirm_Alice.py: The ALICE bot is a strong rule-based bot uing AIML.
- confirm_All_Tasks_mt.py: One of Dodeca models in Zoo, please refer to [Model Zoo](https://parl.ai/docs/zoo.html)
- confirm_Blender_90M.py: Blended Skill Talk models in Zoo, please refer to [Model Zoo](https://parl.ai/docs/zoo.html)
- confirm_Blender_400M.py: Large size of Blended Skill Talk models in Zoo.
- confirm_Blender3_3B.py: Large size of BlenderBot 3 model in zoo. (This is very very slow responce. It takes about 10 minutes to reply.)

At the VS Code, click the "Run" and the "Start Debugging" or the "Run Without Debugging" with one by one. 
Wait a few minutes, and after display "Enter Your Message: " at the terminal, you can talk with agent in terminal.  
If these scripts are not working well, please check your setting for system path and/or check your Python environment. You can set for your system path in each files.  
If you want to try the other agents/models in ParlAI, please refer to [Standard Agents in ParlAI Document](https://parl.ai/docs/agents_list.html).  

### 4-3. Try to talk with the chat bot
The Chat Bot programs are as follows. 
- main_Alice.py
- main_All_Tasks_mt.py
- main_Blender_90M.py
- main_Blender_400M.py
- main_Blender3_3B.py (This is very very slow responce. It takes about 10 minutes to reply.)

Please open the one of above files by the VS Code, then click the "Run" and the "Start Debugging" or the "Run Without Debugging". 
Wait a few minutes, it will be displayed "* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)" at the Terminal. 
Then, after open the Browser, please input "http://127.0.0.1:5000". You can talk with each agent by keybord and/or voice.  
  
This Chat Bot is created in following concepts.
- The human interface is given in HTML and Javascript.
- The answer from the chat bot is created in Python.

In this time, I used the "Dialog Element" in HTML. The Safari and the FireFox are not supported for the Dialog Element, yet. Then, it is not working well by the Safari and the Firefox.
Please enjoy the communication with the chat bot on the Microsoft Edge or the Google Chrome.

## 5. History
2021/5/5: Upload first version.  
2022/11 21: Add the files "confirm_Blender3_3B.py" and "main_Blender3_3B.py".  

## 6. Reference
- [Facebookresearch/ParlAI](https://github.com/facebookresearch/parlai)
- [Visual Studio Code](https://azure.microsoft.com/en-us/products/visual-studio-code/)
- [Python](https://www.python.org/)
- [ChatBot_with_GPT-2_Rinna](https://github.com/To-Fujita/ChatBot_with_GPT-2_Rinna)
- [Japanese_ChatBot_with_ParlAI](https://github.com/To-Fujita/Japanese_ChatBot_with_ParlAI)

## 7. License
- Programs: MIT
- All of the images: Please confirm to each author.

## 8. Author
[T. Fujita](https://github.com/To-Fujita)
