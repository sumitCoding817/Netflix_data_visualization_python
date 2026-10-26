import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Netflix_Data_Visualization/netflix_titles.csv")
#clean data
df=df.dropna(subset=['type','release_year','rating','country','duration'])

type_counts=df['type'].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_counts.index,type_counts.values,color=['skyblue','orange'])
plt.title('Number of Movies vs TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel("Counts")
plt.tight_layout()
plt.savefig('Netflix_Data_Visualization/movies_vs_tvshows.png')

## rating

rating_counts=df['rating'].value_counts()
plt.figure(figsize=(8,6))
plt.pie(rating_counts.values,labels=rating_counts.index,autopct='%1.1f%%',startangle=90)
plt.title("Percentage of Content Rating")
plt.tight_layout()
plt.savefig("Netflix_Data_Visualization/content_rating_pie.png")
# plt.show()

##Distribute of movie using histogram

movie_df=df[df['type']=='Movie'].copy()
movie_df['duration_int']=movie_df['duration'].str.replace('min','').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_df['duration_int'],bins=30,color='purple',edgecolor='black')
plt.title("Distribute of Movie Duration")
plt.xlabel("Duration(Mins)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("Netflix_Data_Visualization/movie_duration_histogram.png")
# plt.show()

## realse year vs number of shows

release_counts=df['release_year'].value_counts().sort_index()
plt.figure(figsize=(10,6))
plt.scatter(release_counts.index,release_counts.values,color='red')
plt.title('Release Year Vs Number of Shows')
plt.xlabel('Release Year')
plt.ylabel('Number of Shows')
plt.tight_layout()
plt.savefig('Netflix_Data_Visualization/release_year_scatter.png')
# plt.show()

##country count top of 10

country_count=df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index,country_count.values,color='teal')
plt.title('Top 10 Countries by Number of Shows')
plt.xlabel('Number of Shows')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig('Netflix_Data_Visualization/top_10_Countries.png')
# plt.show()

## content by year ,subplot

content_by_year=df.groupby(['release_year','type']).size().unstack().fillna(0)
fig,ax=plt.subplots(1,2,figsize=(12,5))

#First subplots : movies
ax[0].plot(content_by_year.index,content_by_year['Movie'],color='blue')
ax[0].set_title('Movies Released Per Year')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Number Of Movies')

## Second subplot : Tv shows
ax[1].plot(content_by_year.index,content_by_year['TV Show'], color='orange')
ax[1].set_title('TV Shows Per Year')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Number of TV Shows')

fig.suptitle('Comparison of Movies and TV Shows Released Over Year')

plt.tight_layout()
plt.savefig('Netflix_Data_Visualization/movies_tv_comparison.png')
# plt.show()
