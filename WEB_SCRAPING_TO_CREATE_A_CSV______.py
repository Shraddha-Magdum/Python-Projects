import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import time


def get_url(position, location):
    # Generate a url from position and location
    temp = 'https://in.indeed.com/jobs?q={}&l={}'
    url = temp.format(position, location)
    return url


def get_record(result):
    # Extract job data from a single record
    job_title = result.find('div', class_="heading4 color-text-primary singleLineTitle tapItem-gutter").text.replace('\n', '')
    company = result.find('div', class_="heading6 company_location tapItem-gutter").text.replace('\n', '')
    location = result.find('div', class_="companyLocation").text.replace('\n', '')

    salary1 = result.find('span', class_="salary-snippet")

    if salary1:
        salary = salary1.text.replace('\n', '')
    else:
        salary = 'Not Disclosed'

    job_description = result.find('div', class_="job-snippet").text.replace('\n', '')
    postDate = result.find('span', class_="date").text.replace('\n', '')
    today = datetime.today().strftime('%Y-%m-%d')

    record = [job_title, company, location, salary, postDate, today, job_description]

    return record


if __name__ == '__main__':

    # Run the main program routine
    position_ = input("What kind of job you are searching for - Enter job title  ::: ")
    location_ = input("Enter a job location you want ::: ")
    url_ = get_url(position_, location_)

    # extract the job data
    Max = 1
    a = 1
    while a <= Max:
        page = requests.get(url_)
        # print(page)
        soup = BeautifulSoup(page.text, 'html.parser')

        results = soup.find_all('div', class_="slider_container")
        # print(len(results))

        records = []

        for result_ in results:
            record_ = get_record(result_)
            records.append(record_)

        # print(records[0])
        time.sleep(6)
        try:
            url_ = 'https://www.indeed.com ' + soup.find('a', {'aria-label': 'Next'}).get('href')
        except AttributeError:
            break
        a += 1

    # save the job data
    with open("jobs_vacancies.csv", 'w', newline='', encoding='utf8') as f:
        Write = csv.writer(f)
        header = ['Position', 'Company Name', 'Company location', 'Salary', 'postDate', 'today', 'job_description']
        Write.writerow(header)
        Write.writerow(records)
