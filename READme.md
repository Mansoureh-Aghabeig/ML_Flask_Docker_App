# ML Flask Docker App

This is a Dockerized Flask application that serves a machine learning model. The application provides a simple web interface where users can input data for prediction, and the model returns the results based on the trained machine learning model.

## Project Structure
```bash
ML_Flask_Docker_App/
│
├── app/
│   ├── app.py          # Flask app file
│   ├── model.py        # Script for training and saving the model
│   ├── model.pkl       # Saved model file
│   └── templates/
│       ├── index.html  # Form page
│       └── result.html # Result page
│
├── Dockerfile          # Dockerfile for building the Docker image
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```
## Prerequisites

- Docker installed on your machine.
- Python (if you want to run the application locally without Docker).

## Setup and Installation

### Running the Application with Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/YourUsername/ML_Flask_Docker_App.git
   cd ML_Flask_Docker_App

2.	Build the Docker image:

docker build -t ml-flask-docker-app .


3.	Run the Docker container:

docker run -p 5053:5053 ml-flask-docker-app


4.	Access the application:
   
Open your browser and navigate to http://localhost:5053.

### Running the Application Locally

	1.	Ensure all dependencies are installed:

pip install -r requirements.txt


	2.	Navigate to the app directory:

cd app


	3.	Run the Flask app:

python app.py


	4.	Access the application:
	•	Open your browser and navigate to http://localhost:5053.


## Usage

1. **Home Page**:
   - The home page (`index.html`) contains a form where you can input values for the model’s features.

2. **Prediction**:
   - Once you submit the form, the application processes the input using the trained machine learning model (`model.pkl`) and displays the result on the `result.html` page.

## Project Details

- **Framework**: Flask (Python)
- **Machine Learning Library**: scikit-learn
- **Deployment**: Docker

## Future Improvements

- Add more sophisticated input validation and error handling for the form.
- Deploy the application using a production WSGI server like Gunicorn for better performance.
- Integrate more advanced machine learning models or extend the app to support multiple models.

## License

This project is licensed under the MIT License.
