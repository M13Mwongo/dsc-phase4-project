# **UNLOCKING REAL ESTATE SUCCESS WITH TIME SERIES MODELLING**

In a bustling cityscape where opportunities arise and markets evolve, a cutting-edge solution is on the horizon for a visionary real estate investment firm – a solution that promises to transcend conventional boundaries and redefine the landscape of strategic decision-making. Welcome to the world of Time Series Modeling, a realm where data becomes the compass for astute investments.

Our journey begins with a challenge posed by a forward-thinking real estate investment firm - BarnaBee & Co.. Faced with the seemingly straightforward question – "What are the top 5 best zip codes for us to invest in?" – the stakes are high, and the road to success is paved with data-driven insights.

<div style='text-align:center'>
  <img src='./images/housing_crash.webp' width='800'/>
</div>

## Introduction

The seemingly simple query concealed intricate nuances - profits or risks, short-term gains or long-term stability? These were all factors to consider when trying to answer the question laid out by BarnaBee and Co. - **_what are the 5 best zip codes to invest in?_** Furthermore, in the pursuit of excellence, the forged metrics aligned with the investment firm’s vision. It wasn’t merely about minimizing mean squared error; it was about orchestrating a delicate balance between risk and profitability. The ROI yield emerged as the guiding star, steering investment decisions with unwavering precision.

These complexities were adeptly navigated, transforming ambiguity into actionable intelligence and truly unearthing the value of real estate.

## Business Understanding

### Problem Statement

Real estate represents a significant portion of most people's wealth, and this is especially true for many homeowners in the United States. A number of factors drive the real estate market including government policies, demographics of the potential buyers,affordability, disparity in housing access, location, cash flows and liquidity as well as the current economic climate. The many variables can make the process tedious for the buyers. Naruto consultants hopes to create a predictive time series model that can help to determine the top five zipcodes in which to invest in.

This forecasting model will help adress the anticipation of any other financial crisis with apt predictive capabilities. The best model shuld capitalize more on the **R2 score** which will be our optmization metric.

### Objectives

1. Investigate and establish the 5 best ZipCodes(Regions) that are the best to invest in that guarantee a good Return on investment.
2. Build a time series regression modell to predict the average house prices in the US and top 5 best performing zipcodes.
3. Investigate impact of the 2008 recession on the housing market per ZipCode(Region).
4. Investigate the growth rates of the real estate industry in Metropolitan areas and Zipcodes.

### Potential Challenges

- Potentially large amounts of missing data with no conclusive reason, forcing assumptions to be made.
- Some trends may be hard to explain due to differences in locale and perceptions of some matters.
- High seasonality caused by the 2008 market crash.

## Data Understanding

## EDA & Data Visualisation

## Feature Engineering

## ARIMA Modelling

## Fine Tunining With Prophet

## Interpreting Results

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

- Using the class without splitting the data using the **TimeSeriesSplit** results to a mismatch between the real and forecasted values. This results to a difficulty of evaluating the whole pipleine. It is therefore necessary to go through the documentation [https://facebook.github.io/prophet/docs/non-daily_data.html] which comes in handy and clearly explains how to do forecatsing on various seasons.

- **Time** taken to get the average values of the metrics to evaluate our model is long. This is because of the use ot the **TimeSeriesSplit** which uses a cross-validation kind of approach to get the optimal results.

The first ETL pipeline chains everything from data ingestion, transforming, training and evaluating the model. It takes in resampled data obtained after transforming the data from wide to long formart. The data is resampled on a monthly basis and contains values of the average house prices for every month. Should the investor like to know the average house values in the near future, the model comes in handy.

The second **TimeSeriesPipeline** however takes in data filtered from the specific ZipCodes and there forecasted values plotted using the plot function in Prophet.

**Challenge**: Both pipelines take in quite a lot of time in evaluation of the models.
The solution here is training the models on free **GPUs** avilable in the cloud so as to minimize the computational power.

#### <ins>Future Steps</ins>

1. Monitor the models predictions an dscores at production.
2. Deploy both models for easier forecasting.
