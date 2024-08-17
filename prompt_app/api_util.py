# prompt_generator/api_utils.py
import requests

def get_wordpress_posts(api_url='http://your-wordpress-site.com/wp-json/wp/v2/posts'):
    """
    Fetches posts from the WordPress REST API.

    Args:
        api_url (str): The base URL of your WordPress REST API.

    Returns:
        list: A list of post data (dictionaries), or None if an error occurs.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching WordPress posts: {e}")
        return None 