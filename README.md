# Title
The disruptive strategy of the IRA tweets.  

# Abstract
Social media went from exciting to being ingrained in our societies and its influence exceeded the personal sphere to attain even our legal framework and political institutions. The question of regulating social networks is currently a hot topic especially with the rise of the concept of cyber warfare and what that entails in terms of disruption and propaganda. It is therefore very important to study how social media can be used to create narratives and tip the scales into one way or the other. In particular, the Internet Research Agency, a Russian troll factory was accused of interfering in multiple foreign political processes like the the 2016 US presidential elections. We dispose of a dataset of roughly 3 millions tweets spanned between 2012 and 2018 related to accounts of this agency. The aim is to understand what these tweets focus on and how do they adapt with respect to major political and politically divisive events.   

# Research questions
Through this project we want to address the following questions:  
How does the troll tweets activity evolve with respect to the reality?  
Is there a correlation between the stakes of a political/social event (elections, confirmation hearing, shooting..) and the troll activity?  
What are the most discussed topics and do they match the timeline of events?  
How does the degree of intensity of a given sentiment change according to the topic?  
What is the impact of positive and negative tweets on the relevant events?  
Starting from the aforementioned questions we might add new evaluations and studies according to the insights we will get from the data.

# Dataset
The dataset we are using for this project is composed of 2,973,371 tweets from 2,848 Twitter handles distributed in 9 csv files. The twitter handles are linked to the Internet Research Agency, a Russian troll factory accused of interfering in the 2016 US presidential elections. The tweets in the dataset were sent between February 2012 and May 2018 with the vast majority posted from 2015 through 2017.

For each tweet, we have the following attributes:

Header | Definition
---|---------
`external_author_id` | An author account ID from Twitter 
`author` | The handle sending the tweet
`content` | The text of the tweet
`region` | A region classification
`language` | The language of the tweet
`publish_date` | The date and time the tweet was sent
`harvested_date` | The date and time the tweet was collected by Social Studio
`following` | The number of accounts the handle was following at the time of the tweet
`followers` | The number of followers the handle had at the time of the tweet
`updates` | The number of “update actions” on the account that authored the tweet, including tweets, retweets and likes
`post_type` | Indicates if the tweet was a retweet or a quote-tweet
`account_type` | Specific account theme, as coded by Linvill and Warren
`retweet` | A binary indicator of whether or not the tweet is a retweet
`account_category` | General account theme, as coded by Linvill and Warren
`new_june_2018` | A binary indicator of whether the handle was newly listed in June 2018

We are focused on the tweets in English and we may extend to other languages on a later stage. The periods of time we're interested in coincide with major political and major politically devasive events.


# A list of internal milestones up until project milestone 2
Steps up to milestone 2 are:  
Explore data and parse it.    
Filter and preprocess data.    
Perform descriptive analysis on the dataset.  
Check the timeline of major troll tweets activity and align it with major political and social events.  

Later we will focus more on the following:  
Topic extraction, modeling and matching with subsequent events.  
Sentiment analysis on a number of topics.  
Search for correlation between topics, language and perception inferred by the tweets.  

# Questions for TAs
Add here some questions you have for us, in general or project-specific.

# Update for Milestone 2
In milestone, we did the following:
Descriptive analysis of the data.
Investigation of the monthly, daily and hourly IRA tweet activity.
Topic modeling initiation.
Polarity and sentiment analysis initiation.

## Plan for Milestone 3
Reiterate over the topic modeling and sentiment analysis by running on specific time periods.
Topic modeling: investigate results with stemming vs lemmatization
Sentiment analysis: Test different models/architectures to get better results.
Build a classifier to recognize tweets from IRA users vs non-IRA users. To do so, we will need the appropriate non-IRA tweets. We will either filter big twitter datasets or mine our own dataset.
We may extend the classifier to distinguish between IRA accounts and non-IRA accounts.

Develop the story.

