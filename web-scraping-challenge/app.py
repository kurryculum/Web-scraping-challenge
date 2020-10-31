from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

# Create an instance of Flask
app = Flask(__name__)


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"]= "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_dict = mongo.db.mars.find_one()
    print(mars_dict)
    # Return template and data
    return render_template("index.html", mars=mars_dict)


@app.route("/scrape")
def scrape():
    mars_dict = mongo.db.mars
    mars_data = mission_to_mars.scrape()
    print(mars_data)
    # Update the Mongo database using update and upsert=True
    mars_dict.update({}, mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)