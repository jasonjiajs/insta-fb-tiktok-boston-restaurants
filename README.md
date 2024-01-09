# How should Boston restaurants allocate content creation resources across Instagram, Facebook and Tiktok?
Final Project, MIT 15.072 - Advanced Analytics Edge <br>
Team Members: [Jason Jia](https://www.linkedin.com/in/jasonjiajs/), [Stephanie Sha](www.linkedin.com/in/ousha/), [Maria Besedovskaya](https://www.linkedin.com/in/mariabesedovskaya/), [Pavena Vongkhammi](https://www.linkedin.com/in/pavena-vongkhammi/)

<img src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/da01ac57-07de-4f29-9e7d-71ab0b45da63" width="550" />

## Summary
Boston restaurants targeting younger audiences can significantly improve overall social media engagement by spending a lot more time creating content on TikTok relative to Instagram and Facebook. [Life Alive Organic Cafe](https://www.lifealive.com/) expressed strong interest in our project, and we are currently discussing ideas for future collaboration. We are in the midst of signing an NDA, and plan to start in Spring 2024.

## Problem and Motivation
Deciding how to allocate content creation resources (e.g. time, effort, number of posts) across different social media channels is critical to the success of a business. But:

- Most small firms cannot afford to hire marketing analysts or marketing agencies. Even if they can, they might not have enough internal data for analysis.
- BigTechs have excellent performance measurement systems, but only within their ecosystem. Firms do not know how they should split marketing spend across social media platforms.
- Not as much research has been done on short-form videos, which are relatively recent compared to TV, newspapers and search. However, they are becoming one of the most important channels for businesses, which are both content creators and advertisers.

Since restaurants heavily use social media to promote their menu offerings, we want to explore how Boston restaurants should allocate content creation resources (e.g. time, effort, number of posts) across Instagram, Facebook and TikTok.

## Data

### Engagement metrics dataset

We manually collected data for 96 restaurants in Boston. 100% of the restaurants have an Instagram account, 96% have a Facebook account, and 49% have a TikTok account. We obtain social media metrics (number of likes, views, comments, followers) for Instagram, Facebook and Tiktok over 6 months (April 2023 - September 2023) and group the restaurants into 3-4 equal classes (quantiles) based on their metrics for each period.

### Overall engagement
The histogram of overall engagement, defined as `log(number of views + 5 * number of likes + 10 * number of comments + 1)` is shown below. Note that the distribution of Instagram and TikTok are relatively similar, while Facebook has much lower engagement on average.

![image](https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/54c0e76e-6ac1-4afb-9858-c507dff90610)

## Methods

### Classification Model
- We used ensembles (CatBoost, XGBoost) to predict the next month's class for each restaurant. We developed a model to forecast each social media metric across Instagram, Facebook, and TikTok. The CatBoost model performs well on our dataset: our results show 70-80% AUC for Instagram, 72-88% AUC for Facebook, and 60-72% AUC for TikTok.

<img width="416" alt="image" src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/5ad4b66b-1636-4936-adff-6e50d86b1473">

- For the baseline, we used Time Series based models: Random Walk (the metric for the next month is approximately equal to the metric in the last month), ARIMA (the future metric can be predicted as the linear combination of its past values) and VAR (the future metric is dependant on the past values of the same and other metrics). Because of the short time series for each variable and overall consistency of the metrics over time, the Random Walk model works the best. To obtain the AUC we used the q-cut to group the metric values and define whether the predictions fall in the same group as the real values. The ensemble models outperform the baseline by 17%.

### Multi-Armed Bandits
We used epsilon-greedy Multi-Armed Bandits to get a recommendation of the share of content creation resources restaurants should put into each social media platform. The model seeks to optimize overall engagement. We compare the best epsilon-greedy bandit out of a range of epsilons against a baseline where restaurants spend 60% of their time on Instagram, 30% of their time on Facebook and 10% of their time on Tiktok. We used this baseline because it is a good approximation of the relative amount of content appearing in each social media platform.

## Key Findings

1. Overall engagement can be significantly improved by 30%, on average.

![](https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/96e85824-c839-4647-af27-09be41f0e0c9)

2. Restaurants should consider using TikTok a lot more. The epsilon-greedy bandit recommends spending 152% more resources on Tiktok, 16% less resources on Instagram and 18% less resources on Facebook relative to baseline, on average. This gives an average optimal distribution of resources of 50.2% on Instagram, 24.6% on Facebook and 25.2% on Tiktok.

![](https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/2e1cfd3c-29e9-4483-9b36-c3042b740a35)

3. Restaurants should try out different social media platforms. The optimal strategy typically gives ε between 0.1 to 0.2, which means restaurants should diversify and use multiple marketing channels.

![](https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/04f13d11-49e1-4f61-8cc8-59710d779412)

## Web Interface Tool
We also developed a Streamlit-based front-end that enables restaurants to assess their social media follower count in comparison to similar establishments in the Boston region. The platform also allows restaurants to upload their social media engagement statistics which are then fed into our models to predict the restaurant's social media engagement for the upcoming month, and generate a recommendation of how the restaurant should spend its time across the 3 different platforms.

<img width="612" alt="image" src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/3007d3f8-312f-47d8-93c2-c8795cffb06e">

## Case Study - Life Alive Organic Cafe
While the estimated 30% improvement in overall engagement is promising, not all restaurants are likely to unlock the full benefits by increasing content creation efforts on TikTok. This could be because the restaurant's customer base might not use TikTok regularly (e.g. older audience) and/or creating video content on TikTok might be a challenge (e.g. because it takes more time than images or text). However, for restaurants that target younger audiences and are already creating video content, but have limited activity on TikTok, shifting resources towards TikTok is likely to significantly improve overall engagement.

[Life Alive Organic Cafe](https://www.lifealive.com/), a Boston-based cafe is a perfect example of a restaurant who will benefit from our recommendations. It specializes in organic, plant-based food with vegan and vegetarian options, and is especially popular amongst the younger demographic.

<img width="837" alt="image" src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/c21ae924-1393-4f21-bb1f-293711f9fd55">

It is also highly active on social media, with a dedicated marketing team which uploads content on a daily basis. 

![image](https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/aa7f925a-f015-46cb-bbc9-b242cc50bfc0)

However, while it has established a significant presence on Instagram with 28.3K followers and Facebook with 13K followers, it has made little impact on TikTok with only 390 followers. 

<img src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/4d72fa9f-f501-49e2-83f7-f71051352e08" width="600" />
<img src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/88f3f2d6-4507-4c9e-a4aa-ac1745578430" width="600" /> 
<img src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/7229468d-9eea-4774-adcf-9768ff17d865" width="600" />

## Impact - Life Alive Organic Cafe
We pitched our recommendations to Kaitlyn Mailly, the social media coordinator of Life Alive Organic Cafe. She expressed strong interest in our project as her marketing team is also considering ramping up activity on Tiktok relative to Instagram and Facebook, which currently serve as their main social media channels. We are currently discussing how we can further collaborate, and are in the midst of signing an NDA.
