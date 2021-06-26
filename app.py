import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

import datetime as dt
from datetime import datetime
from datetime import date, timedelta

# Data Base setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Flask
app = Flask(__name__)

# Flask Routes
@app.route("/")
def Home():
    """List all available API routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/&lt;start&gt;<br>"
        f"/api/v1.0/&lt;start&gt;/&lt;end&gt;<br>"
    )
# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create session from Python to DB
    session = Session(engine)
    # Defining Last year
    latest_day = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    latest_day = datetime.strptime(latest_day, '%Y-%m-%d')
    strptime_dt = latest_day -timedelta(days=365)
    # Query the last 12 months precipitation
    one_year = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date>=strptime_dt).all()
    session.close()
    # Convert list of tuples into normal list
    prec = []
    for date, prcp in one_year:
        p_dict = {}
        p_dict["Date"] = date
        p_dict["Precipitation"] = prcp
        prec.append(p_dict)
    return jsonify(prec)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
    # Create session from Python to DB
    session = Session(engine)
    # Query list of stations
    stations_list=session.query(Station.station).all()
    session.close()
    # Convert list of tuples into normal list
    stations = list(np.ravel(stations_list))
    return jsonify(stations)






if __name__ == '__main__':
    app.run(debug=True)
