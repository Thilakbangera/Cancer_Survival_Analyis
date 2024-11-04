To run this Flask application locally, follow these steps:<br>
### Step 1: Set Up Your Environment<br>
1. **Install Flask and Other Required Libraries**<br>
   Make sure you have Python installed, then install the necessary libraries by running:<br>
   pip install Flask pandas lifelines matplotlib<br>
### Step 2: Save Your Files<br>
1. **Create the Project Folder**<br>  
   In your working directory, create a folder (e.g., survival_analysis_app).<br>
2. **Save app.py  (Flask Application)**<br>
   Save your Flask application code in a file named app.py inside the survival_analysis_app folder.<br>
3. **Create a templates Folder**<br>
   Inside survival_analysis_app, create a folder named templates and save the index.html file (HTML template) you just designed into this folder.<br>
### Step 3: Run the Flask Application<br>
1. Open a terminal or command prompt.<br>
2. Navigate to your project folder:<br>
   cd path/to/survival_analysis_app<br>
3. Run the Flask app:<br>
   python app.py<br>
   If everything is set up correctly, Flask should start the server and provide a local URL (usually http://127.0.0.1:5000).<br>
### Step 4: Open the App in Your Browser<br>
1. Open a web browser.<br>
2. Go to http://127.0.0.1:5000 to access your app.<br>
You should see the Kaplan-Meier Survival Analysis interface, where you can enter an age and view the results alongside the graph and its explanation.<br>
