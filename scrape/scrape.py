import time
from openai import OpenAI
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

def scrape_job_titles(driver):
    # Locating job title elements
    job_titles_elements = driver.find_elements(By.CSS_SELECTOR, 'span[itemprop="title"]')
    
    # Extracting and printing the job titles
    return [element.text for element in job_titles_elements]

def categorize_job_title(job_title):
    prompt = f"""
    Your task is to categorize a given job title into one of the following broader categories:

    1. Software Engineering and Development
    2. Hardware Engineering and Design
    3. Electrical and Electronics Engineering
    4. Network and Systems Engineering
    5. AI/ML Hardware Engineering
    5. AI/ML Software Engineering
    6. Quality Assurance and Testing
    7. Project/Program Management
    8. Research and Development

    For example, if the job title is 'Software Development Engineer', you would categorize it as 'Software Engineering and Development'.

    Now, please categorize the job title '{job_title}' into the appropriate category from the list above.
    """
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a data analyst helping with an engineering job categorization task. Reply with just the engineering job category nothing else."},
            {"role": "user", "content": prompt}
        ]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


# Base URL pattern of AMD website to scrape
base_url = "https://careers.amd.com/careers-home/jobs?country=United%20States%7CCanada&page={}&categories=Engineering&limit=100"

# Set up Firefox driver
driver = webdriver.Firefox()

# Set up OpenAI Client
client = OpenAI()


all_job_titles = []
page_num = 1

while True:
    # Construct the URL for the current page
    url = base_url.format(page_num)
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Scrape job titles
    new_titles = scrape_job_titles(driver)
    if not new_titles:
        break  # Break the loop if no titles are found

    all_job_titles.extend(new_titles)
    page_num += 1

# Print all job titles
for title in all_job_titles:
    print(title)
print("Number of jobs", len(all_job_titles))

# Close the browser
driver.quit()

# Creating a pandas DataFrame
df = pd.DataFrame(all_job_titles, columns=['Job Title'])

# Categorize each job title
df['Category'] = df['Job Title'].apply(categorize_job_title)

# Save the DataFrame to a CSV file
output_filename = 'job_titles_with_categories.csv'
df.to_csv(output_filename, index=False)
print(f"DataFrame saved to {output_filename}")