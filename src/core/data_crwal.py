import requests
from bs4 import BeautifulSoup


def generate_data():
    url = 'https://realpython.github.io/fake-jobs/'
    resp = requests.get(url, verify=False)

    if resp.status_code == 200:
        content = resp.content
        soup = BeautifulSoup(content, 'html.parser')
        job_elements = soup.find_all("div", class_="card-content")
        for item in job_elements:
            title_element = item.find("h2", class_="title")
            company_element = item.find("h3", class_="company")
            location_element = item.find("p", class_="location")
            print(title_element.text.strip())
            print(company_element.text.strip())
            print(location_element.text.strip())
            print('hmmmmmmmmm')
    else:
        print('Failed to retrieve the page')


generate_data()
