#!/usr/bin/python3
"""Module for fetching and processing posts from JSONPlaceholder API"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder API and prints their titles.
    Prints the status code of the response and if successful,
    prints all post titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder API and saves them to a CSV file.
    If the request is successful, creates a CSV file with post data
    including id, title, and body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts = response.json()
        
        # Create list of dictionaries with only required fields
        structured_posts = [
            {
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            }
            for post in posts
        ]
        
        # Write to CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_posts)
