# 🎬 Movies Recomendation System - Machine Learning Operations (MLOps) 🍿

Welcome to the Movies Recomendation System 

This repository contains a full stack Data Scientist process:


🌟 **Features**
- Detailed Jupyter notebook for seamless visualization
- Step-by-step ETL process
- Exploratory Data Analysis and insights discovery
- API Development
- ML Model movies-recomendation-system
- Deploy


📚 **Contents**
1. **Data Engineering**: Collecting and transforming de data

- **ETL (Extraction, Transformation and Loading)**
    * Data Types
    * Missing Values
    * Unnesting data from columns in the dataset
    * Cleaning Data for future use
    * Loading Data in a structured format



- **Developing API**: 6 API functions with FastAPI 

    * **cantidad_filmaciones_mes(Mes)**: One month is entered in Spanish language. Returns the number of movies that were released in the month queried in the entire dataset
    * **cantidad_filmaciones_dia(Dia)**: One day of the week is entered in Spanish. Returns the number of movies that were released on the day queried in the entire dataset
    * **score_titulo(titulo_de_la_filmación)**: The title of a film is entered and returns the title, the year of release and the score.
    * **votos_titulo(titulo_de_la_filmación)**: The title of a film is entered and returns the title, the number of votes and the average value of the votes. The movie must have at least 2000 ratings.
    * **get_actor(nombre_actor)**: The name of an actor is entered and returns the success of the same measured through the return. In addition, the number of films in which he has participated and the average return.
    * **get_director(nombre_director)**: The name of a director is entered and the success of the director measured through the return returns. In addition, you will need to return the name of each movie with the release date, individual return, cost and profit of it.


2. **Machine Learning**: Analyze and Model Training

- **EDA (Exploratory Data Analysis)**
   - Knowing the Data Set
   - Missing Values
   - Comparative Analysis with Graphics
   - Outliers
   - Word Clouds


- **Movies Recomendation System**: Model implemented with an API function
    - recomendacion(titulo): It enters the name of a movie and recommends similar ones in a list of 5 values.


3. **Deployment**: The model is deployed in render.com
    - Try the system [Here - Movies Recomendation System](https://movies-c2m9.onrender.com)


🔍 **Quick Access**

- Visualize ETL process in the interactive [`ETL.ipynb`](./ETL.ipynb) notebook.
- Visualize EDA process in the interactive [`EDA.ipynb`](./EDA.ipynb) notebook.
- Visualize API Functions and ML Model in the [`MAIN.PY`](./main.py)


🔗 **Get the Data**
Download the original dataset [here](https://drive.google.com/drive/folders/11MyTm7s9wJAn1San9m4-EqG7ZNbuURtk?usp=drive_link).


## Video Explanation

To better understand the functionality and workflow of the project, an explanatory video has been prepared. This video provides a detailed walkthrough of the project, explaining each step and demonstrating the features and capabilities of the Movies Recommendation Project.

## Setup in your local machine

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

Clone the repository to your local machine using the following command:

```shell
git clone https://github.com/HugoSalazarS/movies.git
```

### 2. Navigate to the Project Directory

Navigate to the project directory using the following command:

```shell
cd movies
```
### 3. Create a Virtual Environment

Create a virtual environment for the project using the following command:

```shell
python virtualenv env
```

### 4. Activate the Virtual Environment

Activate the virtual environment using the appropriate command based on your operating system:

- For Windows:
```shell
env\Scripts\activate
```
- For macOS/Linux::
```shell
source env/bin/activate
```

### 5. Install Dependencies

Install the project dependencies from the requirements.txt file using the following command:

```shell
pip install -r requirements.txt
```

### 6. Run the Project

To try the FastAPI Functions directly, run the following command:

```shell
uvicorn main:app --host 0.0.0.0 --port 10000 --reload
```

Enter the following address in your web browser: "http://0.0.0.0:10000". From this interface, you can test the functions.