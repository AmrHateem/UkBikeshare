import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



def check_input(input_str,input_type): #to ensure that the user typed a string
  
    while True:
        input_user=input(input_str)
        try:
            if input_user in ['chicago','new york city','washington'] and input_type == 1:
                break
            elif input_user in ['january', 'february', 'march', 'april', 'may', 'june','all'] and input_type == 2:
                break
            elif input_user in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and input_type == 3:
                break
            else:
                if input_type == 1:
                    print("Invalid entry, please try again")
                if input_type == 2:
                    print("Invalid entry, please try again")
                if input_type == 3:
                    print("Invalid entry, please try again")
        except ValueError:
            print("Sorry, the input you placed is wrong")
    return input_user

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_input("Which city you would like to analyze? chicago, new york city or washington?",1)
    # get user input for month (all, january, february, ... , june)
    month = check_input("Which month you would like to analyze? you can choose all if you want to!", 2)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_input("which day you would like to analyze? or all days?", 3)
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

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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
    most_common_month = df['month'].value_counts().idxmax() #short note, i used idmax function to get maximum value in the series
    print("The most common month is :", most_common_month)

      # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", most_common_day_of_week)

   # TO DO: display the most common start hour

    most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

   # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)
    
# TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print("Total travel timeis :", total_travel)
    


    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Average travel time :", mean_travel)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #user counts
    user_counts = df['User Type'].value_counts()
    print("Counts of User Types", user_counts)
    if city != 'washington':
        # gender counts
        
        print('Gender Counts:')
        print(df['Gender'].value_counts())
        
        #earliest, most recent, and most common year of birth
        
        common_year = df['Birth Year'].mode()[0]
        print('Common Year Of Birth:',common_year)
        
        recent_year = df['Birth Year'].max()
        print('Recent Year Of Birth:',recent_year)
        
        earliest_year = df['Birth Year'].min()
        print('Earliest Year Of Birth:',earliest_year)
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1    #extracting raw data
    while True:
        raw = input('Would you like to check on any raw data? type yes or no!')
        if raw.lower() == 'yes':
            print(df[x:x+5])
            x = x+5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
