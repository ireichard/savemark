import os
import sys
import praw
from praw.util.token_manager import FileTokenManager


def main():
    """
    Entry point
    """
    if not os.path.exists('refresh_token.txt'):
        f = open('refresh_token.txt', 'x')
        f.close()
        print('Please fill in required information in \'refresh_token.txt\'')
        sys.exit()
    if not os.path.exists('bot.txt'):
        f2 = open('bot.txt', 'x')
        f2.close()
        print('Please fill in required information in \'bot.txt\'')
        sys.exit()
    # Authenticate to Reddit
    refresh_token_manager = FileTokenManager(
        'refresh_token.txt')  # Refer to praw documentation for obtaining a refresh token from reddit here: https://praw.readthedocs.io/en/latest/getting_started/authentication.html
    reddit = praw.Reddit(token_manager=refresh_token_manager,
                         user_agent=open('bot.txt', 'r').read())  # Get bot token
    links = reddit.user.me().saved(limit=5)
    result = []
    for link in links:
        if link.subreddit == 'ProgrammerHumor':
            result.append(link)
    print("answers: " + str(result))


if __name__ == '__main__':
    main()
