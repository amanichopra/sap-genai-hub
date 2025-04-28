## Using SAP's Generative AI Hub SDK in Python

This track introduces you to the orchestration capabilities of Generative AI Hub using the Python [SDK](https://pypi.org/project/generative-ai-hub-sdk/). More documentation is provided [here](https://help.sap.com/doc/generative-ai-hub-sdk/CLOUD/en-US/index.html).

### Prerequisites if Running Notebooks on SAP BAS Environment


1. Follow [this](https://developers.sap.com/tutorials/hcp-create-trial-account..html
) trial to make a BTP trial account. Once you have set up an account, follow [this](https://developers.sap.com/tutorials/appstudio-onboarding..html) tutorial to use Business Application Studio. After step 5, on this tutorial, you are ready to create a dev space. Click `Create Dev Space` and give it a name like `dev`, assign the type `Full Stack Cloud Application`, and select the `Docker Image Builder` and `Python Tools` extensions when you create the space. It takes a few minutes for the dev space to start running, but once it's running you can click the name of the space to open the application.
2. Open up a terminal session by clicking the "hamburger"-shaped icon in the top left corner, hovering over terminal, and then clicking new terminal like shown in [this](./assets/new_terminal.png) picture. In the terminal type `python3 --version`, click enter, and ensure you see `Python 3.12` as the output. If you don't see this, go back to step 1 and make sure you followed the instructions correctly.
3. On the left side, click the folder icon (below the "hamburger"-shaped icon) and select `Open Folder` as shown [here](./assets/open_folder.png). You will see a path at the top like `/home/user`. Simple click enter as shown [here](./assets/folder_path.png). Shortly, a new window will popup with this folder set as the workspace context.
4. Now clone this repo by typing `git clone https://github.com/amanichopra/sap-genai-hub.git`. Then type `cd sap-genai-hub` in the same terminal. 
5. It is highly suggested to create a virtual Python environment for following along to avoid conflicts with other packages that could be already installed on your system. You can create a virtual environment by typing `python3 -m venv .venv`. Activate the environment in your current terminal session using `source .venv/bin/activate`. Make sure that all subsequent steps are executed within the context of this newly created virtual environment.
6. Install the [SAP generative AI hub SDK](https://pypi.org/project/generative-ai-hub-sdk/) using pip: `pip install "generative-ai-hub-sdk[all]"`. At this point, your terminal should look like [this](./assets/terminal_commands.png) if you followed the above steps correctly.
7. Right click on the `sap-genai-hub` folder and click new file like shown [here](./assets/create_new_file.png). Name this file `creds.json` and click enter. Now, click the Google Drive link (5th item shared in Prashant's email), and open the file called `creds.json`. Copy these contents and paste them into the `creds.json` file you just created in Business Application Studio. These have the credentials needed to access the generative AI models we will use in the below exercises. 
8. Finally, you must assign the Python interpreter from your newly created virtual environment to Business Application Studio. Open folder called `./sap/genai-hub/.venv/bin` in the file explorer and right click on the `python` executable. Then click `Copy Path` like shown [here](./assets/copy_interpreter_path.png). Now click `Command+Shift+P` on Mac or `Control+Shift+P` on Windows and select `Python: Select Interpreter` from the [dropdown](./assets/select_interpreter.png). Then click `Enter interpreter path...`, paste the path you just copied, and click enter.

### Prerequisites if Running Notebooks on Google Colab
1. Ensure to have a Google account. You can register [here](https://support.google.com/mail/answer/56256?hl=en).
2. Open the Google Colab links in the top of each notebook.


### Exercises

The exercises are comprised of notebooks demonstrating how to use the SAP generative AI hub SDK to interact with the Orchestration Service, enabling you to build AI-driven workflows by combining multiple modules such as templating, large language models (LLM), and content filtering.

To complete the first exercise, you must click `ex1.ipynb` on the file explorer. On the top right of this notebook, slick the button titled `Select Kernel` and select `.venv` from the dropdown as shown [here](./assets/select_kernel.png) (ignore this if running in Colab; the kernel is preset). At this point, you are ready to run the code cells in the notebook. Make sure to run each cell sequentially. You can run a cell by "play" button on the left of the cell like shown [here](./assets/execute_cell.png). You can learn more about using Jupyter notebooks [here](https://www.dataquest.io/blog/jupyter-notebook-tutorial/). Once you finish running all the cells, you can move on to the remaining exercises as shown below. 

- [Exercise 1 - Using LLMs and Embedding Models Directly Through Native APIs](./native_llm_clients.ipynb)
- [Exercise 2 - Orchestration Templating](./orchestration_templating.ipynb)
- [Exercise 3 - Orchestration Content Filtering](./orchestration_content_filtering.ipynb)
- [Exercise 4 - Orchestration Chatbot](./orchestration_chatbot.ipynb)
- [Exercise 5 - Building an App Using the Orchestration Service](./orchestration_app/README.md)
- [Exercise 6 - Building a RAG Pipeline, and Making Use of Orchestration's Grounding Module](./RAG.ipynb)
- [Exercise 7 - Building Agents Using Langgraph and Generative AI Hub](./agents.ipynb)

Start the exercises [here](./native_llm_clients.ipynb).

### Postman Collections to Use AI Core via API

You can also access Generative AI Hub via API using the Postman collection [here](aicore_postman_collection.json). 