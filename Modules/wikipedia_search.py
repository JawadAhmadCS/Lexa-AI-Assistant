import requests

def wiki_search(query):
    try:
        # Wikipedia API URL
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        data = response.json()  # Parse JSON response
        if 'extract' in data:
            summary = data['extract']
            print(f"Wikipedia summary for '{query}':\n{data['extract']}")
            qa_dict[query] = summary  # Store in qa_dict
            save_qa_data(qa_file_path, qa_dict)  # Save updated qa_dict
            #print(qa_dict)
        else:
            print(f"No summary found for '{query}' on Wikipedia.")

    except requests.exceptions.RequestException as e:
        print(f"Network error: Unable to fetch data from Wikipedia for '{query}'.\nError: {e}")

    except ValueError as e:
        print(f"Data processing error: Could not decode JSON response.\nError: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#wiki_search("SRK")