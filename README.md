# How should Boston restaurants allocate content creation resources across Instagram, Facebook and Tiktok?
Final Project, MIT 15.072 - Advanced Analytics Edge

<img src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/da01ac57-07de-4f29-9e7d-71ab0b45da63" width="550" />

## Summary

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
The histogram of overall engagement metrics, calculated using `log(number of views + 5 * number of likes + 10 * number of comments + 1)` is shown below. Note that the distribution of Instagram and TikTok are relatively similar, while Facebook has much lower engagement on average.

## Methods

### Classification Model

### Multi-Armed Bandits

## Key Findings

## Web Interface Tool

## Impact - Life Alive Organic Cafe
<img width="837" alt="image" src="https://github.com/jasonjiajs/insta-fb-tiktok-boston-restaurants/assets/90637415/c21ae924-1393-4f21-bb1f-293711f9fd55">


