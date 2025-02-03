import webbrowser

user_term = input("Enter a search term: ")
search_g_url = f"https://www.google.com/search?q={user_term}"

webbrowser.open(search_g_url)