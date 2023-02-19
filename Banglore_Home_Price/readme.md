The /model folder contains the following files:
  1. bangladore_home_prices.ipynb - file containing code implemented in python.
  2. bangladore_home_prices.pickle - a file with a trained model that predicts home prices
  3. bengaluru_house_prices.csv - dataset with information about houses and their prices
  4. columns.json - a file with the names of columns from for the prediction model (bangladore_home_prices.pickle)

  The first three fields are mandatory. They contain information:
   * sqft - area of the apartment.
   * bath - number of bathrooms.
   * bhk - the number of other rooms (bedrooms, halls, kitchens).
   * other parameters are the names of the areas where the apartment is located. Only one of these parameters can be set to 1.