# CV Data API
This is a simple Flask application that serves CV data in the form of a JSON API. 

The data is loaded from a separate JSON file, cv_data.json, and is divided into three sections: personal, experience, and education.

# API Endpoints
- /personal: Returns the personal data from the CV
- /experience: Returns all the experience
- /experience/\<year\>: Returns the experience data from the CV from the year
- /experice?year=\<year\>: Returns the experience data from the respective year
- /education: Returns the education data from the CV

### API access:
```shell
curl http://localhost:5000/personal
curl http://localhost:5000/experience/<year>
curl http://localhost:5000/experience?year=<year>
curl http://localhost:5000/education
```

# CLI Commands
You can also access the CV data from the command line using the following commands:

- personal: Prints the personal data from the CV
- experience \<year\>: Prints the experience data from the CV in that year
- education: Prints the education data from the CV

- for cli:
```shell
flask personal
flask experience <year>
flask education
```

# Installation
- Clone the repository
- Create a virtual environment and activate it
- Install the required packages using pip install -r requirements.txt
- Run the application using 
```shell
flask run # --port 8888 --reload
```

# Testing
- To test the CV enpoints you need to run:
```shell
python test_enpoints.py
```
- To test the utils modules you need to run:
```shell
python test_utils.py
```

# Note
Make sure you have cv_data.json file in your directory

License
This project is licensed under the MIT License.