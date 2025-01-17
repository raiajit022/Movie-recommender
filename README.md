# 🎬 Movie Recommendation System

## 📖 Overview

This project is an advanced movie recommendation system that leverages machine learning algorithms to provide personalized movie suggestions based on user preferences and viewing history. Built with Python and deployed on Heroku, this system aims to enhance the movie selection experience for users by offering tailored recommendations.

## 🚀 Live Demo

Experience the Movie Recommender in action: [Movie Recommender App](https://movierecommend-c0ca8a57785b.herokuapp.com/)

## 🛠️ Technologies Used

- **Python**: Core programming language for the project
- **Jupyter Notebook**: Used for data analysis and model development
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing tools
- **Scikit-learn**: Machine learning library for model building
- **Flask**: Web framework for the application
- **Heroku**: Cloud platform for deploying and managing the application

## 🔍 Features

- **Personalized Recommendations**: Utilizes user preferences to suggest relevant movies
- **Content-Based Filtering**: Recommends movies based on the characteristics of movies that the user has liked in the past
- **Interactive Web Interface**: User-friendly design for easy navigation and movie selection
- **Real-Time Suggestions**: Provides instant movie recommendations based on user input
- **Large Movie Database**: Incorporates a comprehensive dataset of movies for diverse recommendations

## 🛠️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/raiajit022/Movie-recommender.git
   cd Movie-recommender

2. **Set up Python Virtual Environment**
   ```bash
   # For Windows
   python -m venv venv
   .\venv\Scripts\activate

   # For macOS/Linux
   python -m venv venv
   source venv/bin/activate

   ```markdown file="README.md"
...
```

3. **Install Required Dependencies**

```shellscript
pip install -r requirements.txt
```

This will install all necessary Python packages including:

1. numpy
2. pandas
3. scikit-learn
4. flask
5. jupyter
6. matplotlib
7. seaborn



4. **Run the Setup Script**

```shellscript
# For Windows
setup.sh

# For macOS/Linux
sh setup.sh
```

The setup script will:

1. Configure the necessary environment variables
2. Initialize the database
3. Prepare the model files



5. **Start the Application**

```shellscript
python app.py
```

The application will start running on `http://localhost:5000`




## 📦 Dependencies

The project requires the following major dependencies:

- Python 3.7+
- Flask web framework
- Scikit-learn for machine learning
- Pandas for data manipulation
- NumPy for numerical computations
- Jupyter Notebook for data analysis
- Matplotlib and Seaborn for data visualization


## 🗄️ Project Structure

```plaintext
Movie-recommender/
├── .idea/                          # IDE configuration files
├── Data/                          # Dataset directory
│   └── movies_data.csv           # Movie dataset
├── app.py                        # Main Flask application
├── log.py                        # Logging configuration
├── Procfile                      # Heroku deployment config
├── README.md                     # Project documentation
├── requirements.txt              # Python dependencies
├── setup.sh                      # Setup script
└── movie_recommender_system.ipynb # Model development notebook
```

## 🔧 Configuration

The application can be configured using the following environment variables:

- `FLASK_ENV`: Set to 'development' or 'production'
- `PORT`: Port number for the application (default: 5000)
- `DEBUG`: Enable/disable debug mode (default: False)


## 💡 Usage Guide

1. **Access the Application**

1. Open your web browser
2. Navigate to `http://localhost:5000` (local) or the Heroku URL



2. **Browse Movies**

1. View the list of available movies
2. Check movie details including ratings and genres



3. **Get Recommendations**

1. Select a movie you like
2. Click "Get Recommendations"
3. View similar movie suggestions



4. **Filter Results**

1. Filter by genre
2. Sort by rating
3. Sort by release year





## 🚀 Deployment

The application is deployed on Heroku. To deploy your own instance:

1. **Create a Heroku Account**

1. Sign up at [Heroku](https://signup.heroku.com/)



2. **Install Heroku CLI**

```shellscript
# For Windows (using scoop)
scoop install heroku-cli

# For macOS
brew tap heroku/brew && brew install heroku
```


3. **Login to Heroku**

```shellscript
heroku login
```


4. **Create Heroku App**

```shellscript
heroku create your-app-name
```


5. **Deploy Application**

```shellscript
git push heroku main
```


## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Ajit Rai** - *Initial work* - [raiajit022](https://github.com/raiajit022)


## 🙏 Acknowledgments

- Thanks to all contributors who have helped this project grow
- Movie dataset providers
- Open source community for the amazing tools and libraries


## 📞 Support

For support, email [[raiajit022@gmail.com](mailto:raiajit022@gmail.com)] or open an issue on GitHub.

## 🔮 Future Enhancements

- Add user authentication
- Implement collaborative filtering
- Enhance UI/UX
- Add more movie metadata
- Implement real-time recommendations
