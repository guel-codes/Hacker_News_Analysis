#!/usr/bin/env python
# coding: utf-8

# # HACKER NEWS ANALYSIS
# 
# ## Posts we are interested in:
# - Titles that begin with either Ask HN or Show HN
# 
# ## Comparison:
# - Do 'Ask HN' posts or 'Show HN' posts receive more comments on average?
# - Do posts created at a certain time receive more comments on average?

# ## Reading in Dataset
# - We need to import the hacker_news.csv file
# - The dataset was reduced from the full 300,000 rows to 20,000 by removing the submission that did not receive comments

# In[1]:


opened_file = open('hacker_news.csv')

from csv import reader
read_file = reader(opened_file)
hn = list(read_file)
hn_header = hn[0]
hn = hn[1:]
print(hn[0:6])


# ## Columns and Descriptions:
# 
# id: The unique identifier from Hacker News for the post
# 
# title: The title of the post
# 
# url: The URL that the posts links to, if it the post has a URL
# 
# num_points: The number of points the post acquired, calculated as the total -number of upvotes minus the total number of downvotes
# 
# num_comments: The number of comments that were made on the post
# 
# author: The username of the person who submitted the post
# 
# created_at: The date and time at which the post was submitted

# In[2]:


#create 3 empty lists to store separate types of posts
ask_posts = []
show_posts = []
other_posts = []

for post in hn:
    title = post[1]
    #set all post titles to lower case
    title = title.lower()
    if title.startswith("ask hn"):
        ask_posts.append(post)
    elif title.startswith("show hn"):
        show_posts.append(post)
    else:
        other_posts.append(post)
        

        
print(len(ask_posts))
print(len(show_posts))
print(len(other_posts))


# ## Calculate the average amount of comments for the Ask HN and Show HN Posts

# In[23]:


# Find total number of comments in Ask HN posts and assingn to total_ask_comments
total_ask_comments = 0
total_show_comments = 0
for post in ask_posts:
    num_comments = int(post[4])
    total_ask_comments += num_comments
for post in show_posts:
    total_show_comments += int(post[4])
    
    
    # finds the average for 'ask hn' posts that have comments
    avg_ask_comments = total_ask_comments/len(ask_posts)
    
     # finds the average for 'show hn' posts that have comments
    avg_show_comments = total_show_comments/len(show_posts)
    
print("Total Ask HN Posts with Comments: " , total_ask_comments)
print("Average amount of comments for Ask HN Posts : ", avg_ask_comments)    
print("Average amount of comments for Show HN Posts: ", avg_show_comments)


# In[11]:


# Calculate the number of posts made per hour.

import datetime as dt
result_list = []

for post in ask_posts:
    # date_time = post[6]
    # num_comments = int(post[4])
    
    result_list.append([post[6], int(post[4])])
    
counts_by_hour = {}
comments_by_hour = {}
date_format = "%m/%d/%Y %H:%M"
    
for result in result_list:

    date = result[0]
    comment = result[1]
    #extract the hour from the date
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time]= comment
        counts_by_hour[time] = 1
        
comments_by_hour


# In[17]:


#Average number of comments created each our of the day
avg_by_hour = []

for hour in comments_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour] / counts_by_hour[hour]])
    

avg_by_hour



# In[24]:


# Sort the Avg by Hour list in reverse order to show the largest results first

swap_avg_by_hour = []

for avg in avg_by_hour:
    swap_avg_by_hour.append([avg[1], avg[0]])
    
print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse = True)

sorted_swap

print('\n')
print("Top 5 Hours for 'Ask HN' Posts Comments")

for avg, hour in sorted_swap[:5]:
    print("{}: {:.2f} average comments per post".format(
        dt.datetime.strptime(hour, "%H").strftime("%H:%M"), avg))


# # Conclusion
# 
# We analyzed 20,000 posts from the Hacker News dataset and found the average number of comments for 2 types of posts('Ask HN and Show HN').
# 
# We only pulled the top 5 hours for Ask Posts Comments because they had a higher average for comments. I might add the top 5 hours for Show HN posts Comments.
# 
# After a full analysis it is best to post 'Ask HN' posts between 3PM and 8PM. The only time it is advised to post in the morning is within the 2AM hour.
# 
