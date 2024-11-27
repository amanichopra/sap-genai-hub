## Using SAP's Generative AI Hub SDK in Python

This track introduces you to the orchestration capabilities of Generative AI Hub using the Python [SDK](https://pypi.org/project/generative-ai-hub-sdk/).

### Prerequisite


1. Follow [this](https://developers.sap.com/tutorials/hcp-create-trial-account..html
) trial to make a BTP trial account and follow [this](https://developers.sap.com/tutorials/appstudio-onboarding..html) tutorial to use Business Application Studio. Create a dev space of type `Full Stack Cloud Application`. Make sure to select the `Docker Image Builder` and `Python Tools` extensions when you create the space.
2. Open up a terminal session at the root of the cloned repository. It is highly suggested to create a virtual Python environment for following along to avoid conflicts with other packages that could be already installed on your system. A virtual environment can be created using `python3 -m venv .venv`. Activate the environment in your current terminal session using `source .venv/bin/activate`. Make sure that all subsequent steps are executed within the context of this newly created virtual environment.
3. Install the [SAP generative AI hub SDK](https://pypi.org/project/generative-ai-hub-sdk/) using pip: `pip install "generative-ai-hub-sdk[all]"`.
4. Download the file `creds.json` that is shared with you and store it in this project directory.

### Exercises

The exercises are comprised of notebooks demonstrating how to use the SAP generative AI hub SDK to interact with the Orchestration Service, enabling you to build AI-driven workflows by combining multiple modules such as templating, large language models (LLM), and content filtering.

- [Exercise 1 - Using LLMs and Embedding Models Directly](./ex1.ipynb)
- [Exercise 2 - Orchestration Templating](./ex2.ipynb)
- [Exercise 3 - Orchestration Content Filtering](./ex3.ipynb)
- [Exercise 4 - Orchestration Chatbot](./ex4.ipynb)
- [Exercise 5 - Building an App Using the Orchestration Service](./ex5.md)

Start the exercises [here](./ex1.ipynb).

### Postman Collections to Use AI Core via API

You can also access Generative AI Hub via API using the Postman collection [here](aicore_postman_collection.json). 