# Cold email generation based on resume using Tune Studio and Streamlit

This repository contains the code for generating cold emails for job posting to hiring managers based on your resume  that uses Tune Studio to integrate LangChain  with the OpenAI API gpt 4-0 model and Streamlit for the front end. 

![image](https://github.com/user-attachments/assets/3756fb7e-c7ca-49a6-9680-bafbd156ca65)



## Running the application

Clone this repository and navigate to the `TUNAI` folder. In this folder, run the following command to create a virtual environment: 

```sh
python -m venv venv
```

Activate the virtual environment with the following command: 

```sh
source venv/bin/activate
```

Inside the virtual environment, install the required dependencies: 

```sh
pip install openai fitz langchain langchain-openai streamlit
```

Start the app by running the following command: 

```sh
streamlit run app.py
```

The StreamLit app will launch in your browser. You can now enter your OpenAI API key and interact with the translator app. 
