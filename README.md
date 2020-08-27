# Comparative-Text-Summariser-API

# Introduction

A comparative extractive text summariser implemented in Flask and styled with Bulma CSS. The API will parse text from a webpage and prepare two sets of summaries using the NLTK and Gensim libraries for comparative purposes. 

# Implementation
 
 ### Project Structure
 ```bash
|───static/
│   ├── bulma-0.9.0
│      ├── bulma.sass
│      ├── css
│      ├── sass
|───summariser/
│   ├── __init.py__
│   ├── gensim_summariser.py__
│   ├── nltk_summariser.py__
|───templates/
│   ├── base.html__
│   ├── index.html__
│   ├── results.html__
|───app.py
|───requirements.txt
 ```
 ### Initialise Repository
##### 1. Download or clone this repository

You can either manually download this repository, or clone it with: <br>
```
$ git clone https://github.com/erinzhangyj/Comparative-Text-Summariser-API.git
$ cd Comparative-Text-Summariser-API
```

##### 2. Initialise and activate a `virtualenv`
```
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

##### 3. Install the dependencies
```
$ pip install -r requirements.txt
```

##### 4. Run `app.py ` in your development environment
```
$ python app.py
```

##### 5. Navigate to http://localhost:5000 or  http://127.0.0.1:5000/


# App Screenshots
##### 1. Home page

![Home Page](https://i.imgur.com/xjR2YRA.png))

##### 2. Results page
![Results Page](https://i.imgur.com/7C0No8l.png)


