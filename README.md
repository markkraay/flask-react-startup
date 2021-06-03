# Flask + React Startup Code
## Quick Setup
### Python / Flask
1. Clone this repository
2. ``` cd backend ```... in here, lies the Flask app, the static folder, and templates
3. Setup a Python3 virtual environment. ``` python3 -m venv venv ```
4. Activate the environment ``` . venv/bin/activate ```
5. Pip install the Flask requirements ```pip3 install -r requirements ```
At this point, the Python Flask application is fully functional, but any changes we make in react will not be saved or integrated into our project. We have the initiliaze the React app now.
## Node / React
1. ``` cd frontend ```... in here lies our node configuration files and React files
2. ``` npm install ``` to install the React dependencies
At this point, the React frontend is functioning and able to be compiled to our main app. We can do this by running ``` npm run build ```, which will rebuild our main app in the backend folder. ``` cd backend ``` and rerun the Flask application to see the full functioning page.
## Deployment
When deploying this app, it is suffiecient to just deploy the backend folder. Make sure that all the changes made to the frontend are saved with ``` npm run build ```. 
