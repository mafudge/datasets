# Data Sets

This repository contains sample data sets used in the courses I teach. Each folder contains a separate data set.

## Clickstream

This data set consists of 3 days of IIS web logs from a sample e-commerce website (nopCommerce).
The data set contains activity of anonymous users browsing products on the website.
With the exception of spiders and robots, the he original IP addresses were replaced with other valid IP's.
Included in the data set is an IP to location CSV (comma separated values) file.

NOTE: The IP addresses in the clickstream data cross reference to the customer data.

## Tweets
This data set contains 6 months of simulated "tweets" about a company named Fudgemart. It can be used in sentiment analysis.  There are two generated data sets of 200 tweets one in json format the other as pipe-delimited.

There is also a python 3 script  `simtweet.py` which can be used to generate additional tweets as desired. This can be useful if you would like to explore real-time scenairos.


NOTE: You can cross-reference these tweets to customers via the survey.csv in customer data.


## Customers
This data set contains base data about customers who have placed orders on an e-commerce website. It also includes a made up survey some of those customers might have filled out.  

- Customer features include Name, Email, Gender, Last IP Address used, City, State, Total Number of Orders, Total Dollar amount of goods purchased, and number of months they have been a customer.  
- Survey features include email, twitter username, marital status, household income, whether or not they own a home, Highest degree of education, and favorite department.


## Exam-Scores

A table of sample examination scores. Includes the following features:

- Class section (same exam issued to 2 different class periods)
- Exam version, A thorough D (4 different version of the same exam)
- Completion Time (time rounded up to nearest 5 minutes for student to complete the exam )
- Made Own Study Guide (whether or not the student made her own study guide to prepare for the exam)
- Did Exam Prep Assignment (whether or not the student completed the exam prep assignment as part of their study)
- Studied in groups (whether or not the student studied in a group)
- Student Score (raw score on the exam out of 30)
- Percentage (same score as a percentage)
- Letter Grade (score translated to a letter grade)

## Funny-Names

A list of fictitious, humorous people's names commonly used in my examples where I need the name of people to complete a dataset example.

## weather
Scraped from weather underground, daily weather data for syracuse, NY. 1998 to present.

# nyc311
NYC 311 service requests on april fools day, 2016.
