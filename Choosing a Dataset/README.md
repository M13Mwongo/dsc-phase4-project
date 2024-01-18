#### Modelling
Data for modelling should be in a long format and the column containing the datetime values set as index. This is necessary because it ensures easier resampling adn data aggregation on various frequencies.
This stage involves using time series forecasting models to analyze the forecasted values and trends. The various time series models include ARIMA, SARIMAX and Prophet models. The SARIMAX handles the seasonlaity well but is usually prone to overfitting. 

As good modelling approach dictates, it is often good practic eto start out with a baseline model with pdq value combinations obtained from the auto-correlation plots. This model at most times has no tuning applied. The subsequent models shouls however have to undergo some tuning so as to avoid the problem of overfitting which is pretty common in most time series models. 

The subsequent model employs the use of the **auto-arima** model to find the best pdq value combinations with the aim of minimizing the **AIC** csores. The lower the **AIC** scores, the better the **ARIMA** model. It is however important to use the **TimeSeriesSplit** as it splits the data into various folds and seeks to find the optimum **AIC** scores within each fold. 

**Challenge**: The values for the best possible combinations may be overwhelming because it requires iterating through every possible combination for each fold and finding the conspicuous values with the lowest scores.

After training the **Auto Regressive models**, we moved on to our third model which is the **Prophet** model which has exhibited great results in the recent past. The Prophet model is the ideal model because of the concept of adjusting the parameters to capture the seasonality in the time series data. 

The zillow data had a major problem regarding home prices when the great 2008 financial crisis happened fueled by the risky mortages given to low income earners. This piled up debt an the bubble burst when th edebt was no longer fiscal and bearable. In future anticipation of such an event, occurring, the Prophet model is ideal and this is due to the easier adjustments of the seasonal component specifically **Seasonality trend, holiday trend** and **Regressors** addition to capture every other external factors driving the target higher or downwards. 

Use of an **ETL** pipeline like method came in handy because of the simplification of feeding any data for prediction provided it has the datetime columns and the target columns. 

**Challenge**: 

* Using the class without splitting the data using the **TimeSeriesSplit** results to a mismatch between the real and forecasted values. This results to a difficulty of evaluating the whole pipleine. It is therefore necessary to go through the documentation [https://facebook.github.io/prophet/docs/non-daily_data.html] which comes in handy and clearly explains how to do forecatsing on various seasons.

* **Time** taken to get the average values of the metrics to evaluate our model is long. This is because of the use ot the **TimeSeriesSplit** which uses a cross-validation kind of approach to get the optimal results. 

The first ETL pipeline chains everything from data ingestion, transforming, training and evaluating the model. It takes in resampled data obtained after transforming the data from wide to long formart. The data is resampled on a monthly basis and contains values of the average house prices for every month. Should the investor like to know the average house values in the near future, the model comes in handy. 

The second **TimeSeriesPipeline** however takes in data filtered from the specific ZipCodes and there forecasted values plotted using the plot function in Prophet. 

**Challenge**: Both pipelines take in quite a lot of time in evaluation of the models. 
The solution here is training the models on free **GPUs** avilable in the cloud so as to minimize the computational power. 

#### <ins>Future Steps</ins>

1. Monitor the models predictions an dscores at production.
2. Deploy both models for easier forecasting.


