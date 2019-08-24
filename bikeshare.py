import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the name of the city you would like to analyze: ").lower()
    while city not in ["chicago", "new york city", "washington"]:
        print("This city is not available. Please check the spelling or enter another city")
        city = input("Enter the name of the city you would like to analyze: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter the name of the month to filter by, or enter 'all' to apply no month filter: ").lower()
    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        print("Please enter another month")
        month = input("Enter the name of the month to filter by, or enter 'all' to apply no month filter: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day of the week or enter 'all' to apply no day filter: ").lower()
    while day not in["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]:
        print("Please enter a day of the week (e.g. Monday) or input 'all'")
        day = input("Enter the day of the week or enter 'all' to apply no day filter: ").lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('The most popular month to travel is:', popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]

    print('The most common day of the week to travel is: ', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_time = df['hour'].mode()[0]

    print('The most common start hour is: ', popular_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df.loc[:,"Start Station"].mode()[0]

    print('The most commonly used start station is: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df.loc[:,"End Station"].mode()[0]

    print('The most commonly used end station is: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start_end'] = df["Start Station"] +" to " + df["End Station"]
    popular_start_end = df['start_end'].mode()[0]

    print('The most frequently combined start and end station of trip is: ', popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df.loc[:,"Trip Duration"].sum()
    print('Total travel time (seconds): ', total_travel_time,
            '\nTotal travel time (minutes): ', total_travel_time/60,
            '\nTotal travel time (hours): ', total_travel_time/60/60)

    # TO DO: display mean travel time
    mean_travel_time = df.loc[:,"Trip Duration"].mean()
    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types, '\n')

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
    except:
        print('Sorry, no gender data is available for this city')
    else:
        print(gender, '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode())
    except:
       print('Sorry, no year of birth data is available for this city')
    else:
        print('Years of birth \nEarliest year of birth: ', earliest_birth, '\nMost recent year of birth: ', recent_birth, '\nMost common year of birth: ', common_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# TO DO: Give visibility of raw data
    raw_data = input('\nWould you like to see the first 5 rows of raw data? Enter yes or no. \n')
    i = 0
    while raw_data.lower() == 'yes':
        print(df[(5*i):((i + 1)*5)])
        new_question = input('\nWould you like to see the next 5 rows of raw data? Enter yes or no. \n')
        if new_question.lower() == 'yes':
            i += 1
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
