import twint
import nest_asyncio

nest_asyncio.apply()


def Scrape_Tweets_Of_User():
    c = twint.Config()
    username = input("Enter username : ")
    print()
    print(f"Tweets of {username} : \n")
    c.Username = username
    c.Limit = 1

    # Run
    twint.run.Search(c)


def Scrape_Tweets_Between_Specific_Dates():
    c = twint.Config()
    username = input("Enter username : ")
    c.Username = username

    since = input("Enter the staring date in format (year-month-date)  :::  ")
    until = input("Enter the ending date in format (year-month-date)  :::  ")
    print()
    print(f"Tweets of {username} Between {since} to {until} dates : \n")
    c.Since = since
    c.until = until
    # Run
    twint.run.Search(c)


def Scrape_tweets_for_specific_search():
    c = twint.Config()
    search = input("Enter the word that you want to search ::: ")
    print()
    print(f"Tweets containing {search} word : \n")
    c.Search = search
    c.limit = 20
    twint.run.Search(c)


def Scrape_tweets_contain_media():
    c = twint.Config()
    username = input("Enter username :  ")
    print()
    print(f"Tweets containing media i.e (videos or images or both) of {username}: \n")
    c.Username = username
    c.Media = True
    c.Limit = 1
    twint.run.Search(c)


def Scrape_popular_tweets_of_user():
    c = twint.Config()
    username = input("Enter username : ")
    print()
    print(f"Popular tweets of {username} : \n")
    c.Username = username
    c.Popular_tweets = True
    c.Limit = 1
    twint.run.Search(c)


def Filter_tweets():
    c = twint.Config()
    username = input("Enter username : ")
    c.Username = username
    c.Limit = 1
    min_likes = int(input("Enter minimum Likes ::: "))
    min_Replies = int(input("Enter minimum replies ::: "))
    min_retweets = int(input("Enter minimum retweets :::  "))
    print()
    print(f"Filter tweets based on {min_likes}, {min_retweets} and  {min_Replies} of {username} : \n")
    c.Min_likes = min_likes
    c.Min_replies = min_Replies
    c.Min_retweets = min_retweets

    twint.run.Search(c)


def Scrape_tweets_contain_specific_hashtags():
    c = twint.Config()
    hashTag = input("Enter hashtag :::  ")
    print()
    print(f"Tweets containing {hashTag} : \n")
    c.Search = hashTag
    c.Limit = 1

    twint.run.Search(c)


if __name__ == '__main__':
    print("---------- Scraping twitter without API ----------")
    print()

    while True:
        print("- MENU -")
        print("1. Scrape the tweets of user")
        print("2. Scrape the tweets between specific dates of user")
        print("3. Scrape tweets for specific search given by user")
        print("4. Scrape tweets contain media (images or videos or both)")
        print("5. Scrape Popular tweets of user")
        print("6. Filter tweets based on minimum likes, minimum retweets, and  minimum replies of user")
        print("7. Scrape tweets contain specific hashtags")

        print()

        choice = int(input("Enter choice :::  "))
        print()

        if choice == 1:
            Scrape_Tweets_Of_User()

        elif choice == 2:
            Scrape_Tweets_Between_Specific_Dates()

        elif choice == 3:
            Scrape_tweets_for_specific_search()

        elif choice == 4:
            Scrape_tweets_contain_media()

        elif choice == 5:
            Scrape_popular_tweets_of_user()

        elif choice == 6:
            # Filter tweets based on min likes, min retweets, and min replies
            Filter_tweets()

        elif choice == 7:
            Scrape_tweets_contain_specific_hashtags()

        else:
            print("Invalid input")

        print()
        ch = input("Do you want to scrape the tweets again if yes enter y else n ? ").upper()
        while ch != 'Y' and ch != 'N':
            print()
            ch = input("Invalid input ! Enter again : ").upper()

        print()
        if ch == 'N':
            break
