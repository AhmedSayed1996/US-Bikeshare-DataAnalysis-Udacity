import pandas as pd
import numpy as np
import time

CITY_DATA = {'chicago':'chicago.csv','new york':'new_york_city.csv','washington':'washington.csv'}

def load_data():
    """
    Loads data for the specified city and filter it by month & day if applicable.
    args :
        none
    Returns:
        df : pandas DataFrame containing city data which may be filtered as applied
    """
    print('\nHello! Let\'s explore some US bikeshare data!\n')

    city=input("sellect a city [chicago],[washington],[new york] \n").lower()
    while city not in ['chicago','washington','new york']:
        print('there is an error in input !!!')
        city=input("sellect a city [chicago],[washington],[new york] \n").lower()

    # load city data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    filter_type = input('what do you want to fillter by [month], [day] , [both] or [non] ? \n')
    while filter_type.lower() not in ['month','day','both','non'] :
        print('there is an error in input !!!')
        filter_type = input('what do you want to fillter by [month], [day] , [both] or [non] ? \n')

    if filter_type.lower() == 'month':
        print('Available months', df['month'].unique())
        months = df['month'].unique()
        month =input('what month you want to filter by  ? ').title()
        while month not in months:
            print('ther is error in input !!!')
            month =input('what month you want to filter by  ? ').title()
        day='non'

    elif filter_type.lower() == 'day':
        print('Available days',df['day_of_week'].unique())
        days= df['day_of_week'].unique()
        day = input('what day you want to filter by ? ').title()
        while day not in days :
            print('ther is error in input !!!')
            day = input('what day you want to filter by ? ').title()
        month="non"

    elif filter_type.lower() == 'both':
        print('Available months', df['month'].unique())
        print('Available days',df['day_of_week'].unique())
        months = df['month'].unique()
        month =input('what month you want to filter by  ? ').title()
        while month not in months:
            print('ther is error in input !!!')
            month =input('what month you want to filter by  ? ').title()
        days= df['day_of_week'].unique()
        day = input('what day you want to filter by ? ').title()
        while day not in days :
            print('there is an error in input !!!')
            day = input('what day you want to filter by ? ').title()

    else :
        month = 'non'
        day = 'non'

    # filter by month if applicable to create the new dataframe
    if month != 'non':
        df =  df[df['month'] == month]

    # filter by day of week if applicable to create the new dataframe
    if day != 'non':
        df = df[df['day_of_week']==day]

    return df ,city



def showlist(df):
    repeat=input("do you want to see the first five raws of data? [yes],[no]\n").lower()
    while repeat != 'yes'and repeat !='no':
        print('there is an error in input !!!')
        repeat=input("do you want to see the first five raws of data? [yes],[no]\n").lower()

    while repeat=='yes':
         for i in range(10):
            if repeat=='yes':
                print(df.iloc[i*5:(i*5)+5,:])
                repeat=input("do you want to see the next five raws of data? [yes],[no]\n").lower()
                while repeat != 'yes'and repeat!='no':
                    print('ther is error in input !!!')
                    repeat=input("do you want to see the next five raws of data? [yes],[no]\n").lower()

            else:
                break



def time_stats(df):
    """     Displays statistics on the most frequent times of travel.    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if len(df['month'].unique()) != 1 :
        print("\nthe most common month is ",df['month'].mode()[0],'with count of ',(df["month"]==df['month'].mode()[0]).sum())

    # display the most common day of week
    if len(df['day_of_week'].unique()) != 1 :
        print("\nthe most common day of week is ",df['day_of_week'].mode()[0],'with count of ',(df["day_of_week"]==df['day_of_week'].mode()[0]).sum())

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("\nthe most common start hour is",df['hour'].mode()[0],'with count of ',(df["hour"]==df['hour'].mode()[0]).sum())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """      Displays statistics on the most popular stations and trip.     """
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("\nthe most common used start station is ",df['Start Station'].mode()[0],'with count of ',(df["Start Station"]==df['Start Station'].mode()[0]).sum())

    # display most commonly used end station
    print("\nthe most common used end station is ",df['End Station'].mode()[0],'with count of ',(df["End Station"]==df['End Station'].mode()[0]).sum())

    # display most frequent combination of start station and end station trip
    df['combination_of_station']=df['Start Station']+" To "+df['End Station']
    print("\nthe most common used combination_of_station is ",df['combination_of_station'].mode()[0],'with count of ',(df["combination_of_station"]==df['combination_of_station'].mode()[0]).sum())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """      Displays statistics on the total and average trip duration.    """
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("\nthe total trave time is ",df['Trip Duration'].sum(),"seconds")

    # display mean travel time
    print("\nthe average  travel time is ",df['Trip Duration'].mean(),"seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """      Displays statistics on bikeshare users.      """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('count of users type \n\n',df['User Type'].value_counts(),'\n')

    # Display counts of gender
    if city != "washington" :
        print('count of users Gender \n\n',df['Gender'].value_counts(),'\n')

    # Display earliest, most recent, and most common year of birth
    if city != "washington" :
        print('the earliest year of birth is  ',df['Birth Year'].min(),'\n')
        print('the most recent year of birth is  ',df['Birth Year'].max(),'\n')
        print('the common year of birth is  ',df['Birth Year'].mode()[0],'\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        df , city = load_data()
        showlist(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart != 'yes'and restart!='no':
            print('ther is error in input !!!')
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()

        if restart.lower() == 'no':
            print('Thank you for your time \n and I hope you will share the experience with us again ')
            break

if __name__ == "__main__":
	main()
