import pandas as pd


def calculate_baseball_owners_data(print_data=True):
    # Read data from file
    df = pd.read_csv('baseball_owners_data.csv')

    # How many of each race are represented in this dataset of baseball owners?
    race_count = df['race'].value_counts()

    # What is the average age of baseball owners?
    average_age_owner = round(df['age'].mean() * 100, 1)

    # What percentage of baseball owmers have a Bachelor's degree?
    percentage_bachelors = round(df.loc[df['education'] == 'Bachelors', 'education'].count() / df.shape[0] * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df.loc[~df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round((higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100, 1)
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours]

    rich_percentage = round((num_min_workers.loc[num_min_workers['salary'] == '>50K', 'salary'].count()/len(num_min_workers)) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    country_count = df['native-country'].value_counts() # Total people per country
    rich_country_count = df[df['salary'] == '>50K']['native-country'].value_counts() # Rich people per country
    highest_earning_country = (rich_country_count / country_count * 100).idxmax()
    highest_earning_country_percentage = round((rich_country_count / country_count * 100).loc[highest_earning_country], 1)

    # Identify the most popular industry that MLB owners come from.
    top_IN_industry = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'),'occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of owner:", average_age_owner)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        'highest_earning_country_percentage,
         top_IN_occupation': top_IN_occupation
    }
