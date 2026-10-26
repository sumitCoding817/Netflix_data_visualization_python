Netflix Data Visualization using Python
A beginner-friendly exploratory data analysis (EDA) project that uses Pandas to clean and summarize Netflix-style catalog data and Matplotlib to create six visualizations.
Dataset note: The included netflix_titles.csv is a synthetic sample dataset for testing, not an official or current Netflix catalog. Do not interpret the charts as real Netflix business statistics.

Project overview
This project explores:
1. Movies vs TV Shows: Counts by content type (bar chart).
2. Content ratings: Distribution of audience ratings (pie chart).
3. Movie duration: Distribution of movie runtimes in minutes (histogram).
4. Release year: Number of titles by original release year (scatter plot).
5. Top 10 countries: Countries with the most listed titles (horizontal bar chart).
6. Movies vs TV Shows over time: Separate release-year trends (two subplots).
release_year means the title's original release year, not the year it was added to Netflix.
Tech stack
- Python 3
- Pandas
- Matplotlib
Folder structure
Netflix-Data-Visualization/
├── netflix_data_visualization.py
├── netflix_titles.csv
├── README.md
├── movies_vs_tvshows.png
├── content_rating_pie.png
├── movie_duration_histogram.png
├── release_year_scatter.png
├── top10_Countries.png
└── movies_tv_comparison.png
The PNG files are created when you run the script. The exact filenames depend on the plt.savefig(...) statements in your code.
Getting started
1. Clone your repository and enter the project directory:
   git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
   cd YOUR_REPOSITORY
   Replace the placeholders with your actual GitHub username and repository name.
2. Install dependencies:
   pip install pandas matplotlib
3. Keep netflix_titles.csv in the same folder as the Python script. Make sure the script reads the exact filename:
   df = pd.read_csv("netflix_titles.csv")
4. Run:
   python netflix_data_visualization.py
5. View the charts in the project folder. The script also displays charts using plt.show() where included.
Important code checks
If you are using the original draft of the script, correct these lines before running:
# Pie chart: labels must be passed by keyword
plt.pie(rating_counts.values, labels=rating_counts.index,
        autopct='%1.1f%%', startangle=90)

# Column names are case-sensitive
country_count = df['country'].value_counts().head(10)

# Content types in the CSV are singular
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')

# Figure title
fig.suptitle('Comparison of Movies and TV Shows Released Over Years')
For country analysis, some titles may list multiple countries in one field. To count each listed country separately, use:
country_count = (
    df['country'].str.split(',').explode().str.strip()
    .value_counts().head(10)
)
Dataset fields used
Column	Meaning
type	Movie or TV Show
rating	Content maturity rating
duration	Movie runtime or number of TV seasons
release_year	Original release year
country	Listed production country or countries


The sample CSV contains 800 records and 12 columns. It is intended for practicing data cleaning, grouping, and visualization.
Skills demonstrated
- Reading and cleaning CSV data with Pandas
- Handling missing values with dropna()
- Filtering rows and converting data types
- Aggregating with value_counts() and groupby()
- Building bar, pie, histogram, scatter, and subplot visualizations
- Exporting plots as PNG files
Future improvements
- Replace synthetic data with a properly sourced, real Netflix catalog snapshot.
- Add more robust handling of missing values and malformed durations.
- Build an interactive dashboard using Streamlit or Plotly.
- Add tests and a requirements.txt file.
Disclaimer
This is an independent educational project and is not affiliated with or endorsed by Netflix.
