# NBA Predicted PPG
Built a ridge regression model to predict each player's PPG for the 2024-2025 season, and then used Flask and sqlite3 to visualize this data in a webpage.

# Cleaning the Data
I gathered data from Basketball Reference for the 2022-2023 and 2023-2024 seasons. I then merged the dataframes so that only players who played in the 22-23 and 23-24 seasons were included. I removed all categorical variables as they weren't going to make an impact in predicting PPG.

# Building the Model
After having my complete dataset and splitting it into training and test data, I built 8 separate regression models and evaluated their training scores based on their RMSE values. The model with the lowest RMSE value was the Ridge Regression model, so I chose to further use it to get my final predictions. I performed a GridSearchCV to identify the best alpha parameter, and was able to lower my RMSE to 2.86. I then used the model on the 23-24 dataset to get PPG predictions for the 24-25 NBA season.

# Flask and sqlite3
I saved the predicted data as a csv file and used DB Browser to create a database containing that data. I then used Flask to build a simple webpage that would output a player's 2023-2024 stats and their predicted PPG for the 2024-2025 season. To connect to the database, I used the sqlite3 API and queried the player using an HTML input field.

# Next Steps
Using advanced statistics when building this type of model would almost certainly create better results in RMSE scores and thus more accurate predictions, so the next step would be to have better data from the outset. 
