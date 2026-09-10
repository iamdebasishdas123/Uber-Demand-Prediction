# Uber Demand Prediction

## Overview
This project uses the NYC Uber ride dataset provided by the Taxi & Limousine Commission. The open‑source data includes trips from **January 2015**, **January–March 2016**, and additional months.

## Tasks
1. **Clustering Pickup Locations**
	- Group pickup points into regions (clusters) such that the average distance between two points in a cluster is **1–1.5 miles**. This enables drivers to reach the nearest region within 15 minutes.
2. **Demand Forecasting**
	- Predict the demand for upcoming time intervals.

## Approach for Task 1
- Load raw data and clean it (remove outliers and missing values).
- The dataset contains ~10 M records; we use **Dask** instead of pandas for scalable processing.
- Perform mini‑batch **K‑means** clustering on the pickup coordinates and timestamps.
- After experimentation, **30 clusters** provide a good trade‑off between granularity and travel distance.

## Future Work (Task 2)
- Implement time‑series models to forecast demand for the next time interval.