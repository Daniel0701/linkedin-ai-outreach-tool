# LinkedIn Profile Parser

This project takes in a LinkedIn profile as a **PDF file** and then extracts profile information by using a Python script

# OVERVIEW
# LinkedIn Parser
The script extracts information from a **downloaded LinkedIn PDF** (downloaded from browser i.e. print as a PDF option)  
    - **Name** & **Role**  
    - The **About** Section  
    - The **Experience** Section  
    - The **Education** Section  
The information will be extracted to a **.txt** file that has the sections labeled. 
Look for the **_parsed** tag.

# Outreach Email Generation
The generate_response script will now prompt you for the .txt file containing the information of the LinkedIn profile that was just parsed. Enter the filename of the .txt file, and look for the generate response. 
Look for the ** _email** tag.

# Requirements
Make sure you have Python installed.  
Make sure you have the following package, pdfplumber, installed as well.  
In your cmd prompt, run:  
    **pip install pdfplumber**  
to install the needed package
You will also need the Google Bard API Package
In your cmd prompt, run:  
    **pip install google-generativeai**  
You will also need an API Key to use their AI responses. You can get this for free by following the instructions in this link:  
https://ai.google.dev/tutorials/python_quickstart