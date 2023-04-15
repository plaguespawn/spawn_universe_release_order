import requests # pip3 install requests
from bs4 import BeautifulSoup # pip3 install beautifulsoup4
from datetime import datetime

# define the URLs to scrape
urls = [
    'https://imagecomics.com/comics/list/series/spawn/releases',
    'https://imagecomics.com/comics/list/series/gunslinger-spawn/releases',
    'https://imagecomics.com/comics/list/series/the-scorched/releases',
    'https://imagecomics.com/comics/list/series/king-spawn-2/releases'
]

# create a list to store the issues
issues = []

# loop through the URLs and scrape the data
for url in urls:
    # make the request and parse the HTML with BeautifulSoup
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # find all the cells containing the issue information
    cells = soup.find_all('div', {'class': 'cell u-mb1'})

    # loop through the cells and extract the data
    for cell in cells:
        #print(cell)
        # extract the issue name and number
        name = cell.find('span').text.strip()

        # extract the release date
        date = cell.find('span', {'class': 'date'}).text.strip()

        # create a dictionary to store the issue information
        issue = {
            'name': name,
            'date': datetime.strptime(date, '%b %d, %Y').date(),
            'url': url
        }

        # append the issue to the list
        issues.append(issue)

# sort the issues by date
sorted_issues = sorted(issues, key=lambda x: x['date'], reverse=False)

# print the sorted issues
for issue in sorted_issues:
    #print(f"{issue['name']} - {issue['date']} - {issue['url']}")
    print(f"{issue['name']} - {issue['date']}")

# Save the output in a file if save_to_file flag is set
save_to_file = True
output_filename = "spawn_universe_release_order.txt"
if save_to_file:
    with open(output_filename, "w") as f:
        for issue in sorted_issues:
            f.write(f"{issue['name']} ({issue['date']})\n")
    print("\n\n\nOutput saved to file '" + output_filename + "'")