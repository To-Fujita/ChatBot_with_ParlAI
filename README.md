# ChatBot_with_ParlAI

## 1. Description
This is a chat bot based on the ParlAI by Facebook. You can communicate to some chat bots by keyboard and/or voice.

## 2. Operational Environment
- Windows 10 64-bit
- Visual Studio Code (VS Code)
- Python 3.9.4 64-bit
- Browser: Microsoft Edge or Google Chrome

## 3. Demo
![ChatBot_000](https://to-fujita.github.io/Images/ChatBot_000.gif "Images for ChatBot")

## 4. Details
I have confirmed these Python Scripts on the above conditions only. I will show you below how to execute the P`ython scripts. 
### 4-1. Preparation
(a) Download & unzip the files
- [ParlAI](https://github.com/facebookresearch/parlai): A framework for training and evaluating AI models on a variety of openly available dialogue datasets.
- ChatBot_with_ParlAI: Please download from above "Code".  
Please put these unzipped folders under the system pass passed.   
  
(b) Install some files to your Python
- ParlAI: pip install parlai
- Python-Aiml: pip install python-aiml
- Flask: pip install Flask

### 4-2. Confirm to work some agents/models in ParlAI
If you finished the preparation above, please confirm to work some agents/models in ParlAI.  
After open the "ChatBot_with_ParlAI" folder, please open the each following files with VS Code.
- confirm_Alice.py
- confirm_All_Tasks_mt.py
- confirm_Blender_90M.py
- confirm_Blender_400M.py
Then, Click the "Run" and the "Start Debugging" or the "Run Without Debugging" with one by one.  
If these scripts are not working, please check your setting for system pass. You can set for your system pass in each files.  
If you want to try the other agents/models in ParlAI, please refer to [Standard Agents in ParlAI Document](https://parl.ai/docs/agents_list.html).  

### 4-3. Try to communicate with the chat bot

## 5. Reference
- [Facebookresearch/ParlAI](https://github.com/facebookresearch/parlai)
- [Visual Studio Code](https://azure.microsoft.com/en-us/products/visual-studio-code/)
- [Python](https://www.python.org/)

## 6. License
MIT

## 7. Author
[T. Fujita](https://github.com/To-Fujita)
