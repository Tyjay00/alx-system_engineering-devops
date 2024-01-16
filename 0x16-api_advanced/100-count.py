#!/usr/bin/python3
"""Script to count the occurrences of specified keywords in the titles of 
   top posts on a Reddit subreddit.
"""
import sys

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    
    # Check if the command-line arguments are provided correctly
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Example: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        # Call the count_words function with subreddit and keyword list
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
