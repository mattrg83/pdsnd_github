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
    
    # Acceptable cities defined
    cities = ['chicago', 'new york city', 'washington']
    
    # Gather selected city from input, while loop handles invalid names and repeats until actual name is typed
    city = input("Enter a city name (chicago, new york city, or washington): ").lower()
    while city not in cities:
        city = input("Invalid, please enter a city name (chicago, new york city, or washington): ")
    
    # print selected city, convert new york city to file name
    print("City selected is: " + city)
    if city == "new york city":
        city = city.replace(" ", "_")
    
    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    # Define acceptable month entries
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all']
    
    # Gather selected month from input, while loop handles invalid entries
    month = input("Enter a month of the year (january, february, march, ...), or 'all' for no filter: ")
    while month not in months:
        month = input("Invalid, please enter a month of the year (january, february, march, ...), or 'all' for no filter: ")

    # print selected month, convert to integer value for date range selection, if statement handles the 'all' option
    print("Month selected is: " + month)
    if month != "all":
        month = months.index(month) + 1
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    # Define acceptable day entries
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    
    # Gather day from input, while loop handles invalid entries
    day = input("Enter a day of the week (monday, tuesday, wednesday, ...), or 'all' for no filter: ")
    while day not in days:
        day = input("Invalid, please enter a day of the week (monday, tuesday, wednesday, ...), or 'all' for no filter: ")

    # print selected day, convert to integer for 'day of week' selection if not all
    print("Day selected is: " + day)
    if day != "all":
        day = days.index(day)
    
    
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
    
    # Import csv and convert dates to datetime format
    df = pd.read_csv('./' + city + '.csv')
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # filter by month if 'all' is not selected
    if month != "all":
        month_filter = df['Start Time'].map(lambda x: x.month) == month
        df = df[month_filter]
        
        # Check if filter created an empty data set, exit program if it did.
        if df.empty: 
            print("There is no data for the selected month!")
            exit()
    
    # filter by day of week if 'all' is not selected
    if day != "all":
        day_filter = df['Start Time'].map(lambda x: x.dayofweek) == day
        df = df[day_filter]
        
        # Check if filter created an empty data set, exit program if it did.
        if df.empty: 
            print("There is data for this month, but not your selected day of the week!")
            exit()
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    # List of months for applying name to the number found
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    
    # create new column of month numbers from 'Start Time'
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    
    # find the most common month using mode, extract only the number associated
    common_month = df['month'].mode().loc[0]
    
    # Print most common month
    print("The most common month of travel is: ", months[common_month - 1])
    
    # TO DO: display the most common day of week
    
    # List of days for applying name to the number found
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    # create new column of month numbers from 'Start Time'
    df['day_of_week'] = pd.DatetimeIndex(df['Start Time']).dayofweek
    
    # find the most common day using mode, extract only the number associated
    common_day = df['day_of_week'].mode().loc[0]
    
    # Print most common day of the week
    print("The most common day of the week of travel is: ", days[common_day])

    
    
    # TO DO: display the most common start hour
    
    # create a new column for hour of travel
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour
    
    # find the most common hour using mode, extract only the hour
    common_hour = df['hour'].mode().loc[0]
    
    # Print the most common hour of travel
    print("The most common hour to travel is: ", common_hour)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    # use mode to find most common start station and display with print
    common_start_station = df['Start Station'].mode().loc[0]
    print("The most commonly used start station is: ", common_start_station)

    
    
    # TO DO: display most commonly used end station
    
    # use mode to find most common end station and display with print
    common_end_station = df['End Station'].mode().loc[0]
    print("The most commonly used end station is: ", common_end_station)

    
    
    # TO DO: display most frequent combination of start station and end station trip
    
    # Create start station and end station combined column
    df['station_combination'] = "Start: " + df['Start Station'] + " " + "| End: " + df['End Station']
    
    # use mode to find most frequent
    common_combination = df['station_combination'].mode().loc[0]
    print("The most common start station and end station combination is: ", common_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    # TO DO: display total travel time
    
    # calculate total time using sum and display with print
    total_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_time)

    
    # TO DO: display mean travel time
    
    # calculate mean travel time and display with print
    mean_time = df['Trip Duration'].mean()
    print("The average travel time is: ", mean_time)

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    # use value_counts to display user types and print
    user_type_counts = df['User Type'].value_counts()
    print("The user type counts are: ")
    print(user_type_counts)
    
    
    # TO DO: Display counts of gender
    
    # use value_counts to display gender types and print
    # use of if and else to check if the Gender column is available
    if 'Gender' in df.columns:
        user_gender_counts = df['Gender'].value_counts()
        print("\nThe user gender counts are: ")
        print(user_gender_counts)
    else:
        print("\nNo gender data is available for this data set.")

    
    # TO DO: Display earliest, most recent, and most common year of birth
    
    # use value_counts to display gender types and print
    # use of if and else to check if the Gender column is available
    if 'Birth Year' in df.columns:
        print("\nThe earliest birth year of a user in this range is: ", int(df['Birth Year'].min()))
        print("The most recent birth year of a user in this range is: ", int(df['Birth Year'].max()))
        print("The most common birth year of a user in this range is: ", int(df['Birth Year'].mode().loc[0]))
    else:
        print("\nNo Birth Year data is available for this data set.")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def raw_data(df):    
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue? Enter yes or no\n")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()