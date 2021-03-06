<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
<body>
<h1>Climate Analysis and Exploration</h1> 
<br>
<p>Use Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database of Honolulu, Hawaii.</p>
<p>Two datasets were provided:</p>
<ol>
    <li>Measurement. This table contains data for precipitation, weather stations, temperature observations and dates.</li>
    <li>Station. This table contains data for station id, elevation, name, longitude and latitude.</li>
</ol>
<h2>Precipitation Analysis</h2>
<br>
<p>This graph shows the precipitation data in Honolulu, Hawaii from 24.August.2016 to 23.August.2017</p>
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/Precipitation_Graph.png">
<br>
<h2>Station Analysis</h2>
<p>This histogram shows the temperature observations for weather station USC00519281 in Honolulu, Hawaii from 24.August.2016 to 23.August.2017</p>
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/Temperature_Histogram.png">
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/Temp_stats_for_station_USC00519281.png">
<br>
<h2>Temperature Analysis</h2>
<h3>Trip from 06.August.2017 to 14.August.2017</h3>
<br>
<p>The following images show the minimum, the average and the maximum temperature for the choosen dates for a trip.</p>
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/Trip_Avg_Temp.png">
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/Trip_Avg_Temp_DF.png">
<br>
<p>The following images show the daily normals for the same trip.</p>
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/Daily_Normals_Aug_2017.png">
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/Daily_Normals_DF.png">
<br>
<h2>Is there a meaningful difference between the temperature in, for example, June and December?</h2>
<p>The following plot shows the average temperatures for June and December at all stations across all available years in the dataset.</p>
<p>According to the calculated p-value, the difference in the temperature means is not statistically significant.</p>
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/Jun_Dec_Temp.png">
<br>
<img src="https://github.com/uldom/SQLAlchemy_Challenge/blob/main/Images/ttest_pvalue.png">
</body>
</html>

