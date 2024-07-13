'''
This Code is coded and Developed by Safeer Abbas.
https://github.com/SafeerAbbas624
https://safeerabbas624.github.io/safeerabbas/


'''

import time
import openai
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Your ChatGPT API Key
openai.organization = ""
openai.api_key = ""
model_engine = "davinci"


# Generate reply from chatGPT
def generate_reply(prompt):
    try:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=30,
            n=1,
            stop=None,
            temperature=0.7,
            frequency_penalty=1,
            presence_penalty=0
        )
        return response['choices'][0]['text']
    except Exception as e:
        print(f"Error generating reply: {e}")
        return None  # Handle the error gracefully


driver = webdriver.Chrome()


# Twitter Login function
def twitter_login(username, password):
    driver.get("https://twitter.com/login")
    time.sleep(15)
    username_field = driver.find_element(By.CSS_SELECTOR, "input[name='text']")
    time.sleep(3)
    username_field.send_keys(username)
    time.sleep(2)
    username_field.send_keys(Keys.RETURN)
    time.sleep(5)
    password_field = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    time.sleep(2)
    password_field.send_keys(password)
    time.sleep(2)
    password_field.send_keys(Keys.RETURN)
    time.sleep(15)


# Twitter reply function to main page
def reply_to_tweets():
    global tweet, total_page_height, browser_window_height, current_position

    for _ in range(1, 15):
        try:
            # Extracting tweets with text fields
            tweet = driver.find_element(By.XPATH,
                                        f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[5]/div/section/div/div/div[{_}]/div/div/article/div/div/div[2]/div[2]/div[2]/div').text
            # Printing Tweets on console
            print(f'this is tweet: {tweet}')
            time.sleep(1)
            timing = driver.find_element(By.XPATH,
                                         f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[5]/div/section/div/div/div[{_}]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[3]/a/time').text
            print(timing)
            if 'm' in timing:
                # Generating replies
                reply = generate_reply(tweet)
                # Printing replies
                print(f"This is the reply from ChatGPT: {reply}")
                time.sleep(2)
                # Finding reply button
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[5]/div/section/div/div/div[{_}]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[1]/div/div").click()
                time.sleep(2)
                # Replying the text generated from chatGPt
                driver.find_element(By.XPATH, "//div[@aria-label='Tweet text']").send_keys(reply)
                time.sleep(10)
                # Clicking reply button
                driver.find_element(By.XPATH, "//span[contains(text(),'Reply')]").click()
                time.sleep(5)

            # Scrolling function below
            total_page_height = driver.execute_script("return document.body.scrollHeight")
            print(f'{total_page_height} this is total page height')
            browser_window_height = driver.get_window_size(windowHandle='current')['height']
            print(f"{browser_window_height} this is browser window height")
            current_position = driver.execute_script('return window.pageYOffset')
            print(f'{current_position} this is current position')

            new = total_page_height - (browser_window_height - 600)
            print(new)
            driver.execute_script(
                f"window.scrollTo({new}, {browser_window_height + current_position});")
            time.sleep(10)
            current_position = driver.execute_script('return window.pageYOffset')
            print(f'{current_position} this is  new current position')
            time.sleep(10)  # It is necessary here to give it some time to load the content

        except:
            # If tweets text will not be found it will scroll down for more tweets and go loop again
            # Scrolling function below
            total_page_height = driver.execute_script("return document.body.scrollHeight")
            print(f'{total_page_height} this is total page height')
            browser_window_height = driver.get_window_size(windowHandle='current')['height']
            print(f"{browser_window_height} this is browser window height")
            current_position = driver.execute_script('return window.pageYOffset')
            print(f'{current_position} this is current position')

            new = total_page_height - (browser_window_height - 600)
            print(new)
            driver.execute_script(
                f"window.scrollTo({new}, {browser_window_height + current_position});")
            time.sleep(10)
            current_position = driver.execute_script('return window.pageYOffset')
            print(f'{current_position} this is  new current position')
            time.sleep(10)  # It is necessary here to give it some time to load the content


def reply_to_tweets_following_page():
    time.sleep(20)
    global tweet, total_page_height, browser_window_height, current_position

    for _ in range(1, 15):
        try:
            # Extracting tweets with text fields
            tweet = driver.find_element(By.XPATH,
                                        f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[5]/div/section/div/div/div[{_}]/div/div/article/div/div/div[2]/div[2]/div[2]/div').text
            # Printing Tweets on console
            print(f'this is tweet: {tweet}')
            time.sleep(1)
            timing = driver.find_element(By.XPATH,
                                         f'/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[5]/div/section/div/div/div[{_}]/div/div/article/div/div/div[2]/div[2]/div[1]/div/div[1]/div/div/div[2]/div/div[3]/a/time').text
            print(timing)
            if 'm' in timing:
                # Generating replies
                reply = generate_reply(tweet)
                # Printing replies
                print(f"This is the reply from ChatGPT: {reply}")
                time.sleep(2)
                # Finding reply button
                driver.find_element(By.XPATH,
                                    f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[5]/div/section/div/div/div[{_}]/div/div/article/div/div/div[2]/div[2]/div[4]/div/div[1]/div/div").click()
                time.sleep(2)
                # Replying the text generated from chatGPt
                driver.find_element(By.XPATH, "//div[@aria-label='Tweet text']").send_keys(reply)
                time.sleep(10)
                # Clicking reply button
                driver.find_element(By.XPATH, "//span[contains(text(),'Reply')]").click()
                time.sleep(5)

            # Scrolling function below
            total_page_height = driver.execute_script("return document.body.scrollHeight")
            print(f'{total_page_height} this is total page height')
            browser_window_height = driver.get_window_size(windowHandle='current')['height']
            print(f"{browser_window_height} this is browser window height")
            current_position = driver.execute_script('return window.pageYOffset')
            print(f'{current_position} this is current position')

            new = total_page_height - (browser_window_height - 600)
            print(new)
            driver.execute_script(
                f"window.scrollTo({new}, {browser_window_height + current_position});")
            time.sleep(10)
            current_position = driver.execute_script('return window.pageYOffset')
            print(f'{current_position} this is  new current position')
            time.sleep(10)  # It is necessary here to give it some time to load the content

        except:
            # If tweets text will not be found it will scroll down for more tweets and go loop again
            # Scrolling function below
            total_page_height = driver.execute_script("return document.body.scrollHeight")
            print(f'{total_page_height} this is total page height')
            browser_window_height = driver.get_window_size(windowHandle='current')['height']
            print(f"{browser_window_height} this is browser window height")
            current_position = driver.execute_script('return window.pageYOffset')
            print(f'{current_position} this is current position')

            new = total_page_height - (browser_window_height - 600)
            print(new)
            driver.execute_script(
                f"window.scrollTo({new}, {browser_window_height + current_position});")
            time.sleep(10)
            current_position = driver.execute_script('return window.pageYOffset')
            print(f'{current_position} this is  new current position')
            time.sleep(10)  # It is necessary here to give it some time to load the content


# Run bot and reply on both pages main timeline page and following page
def run_bot(username, password):
    while True:
        twitter_login(username, password)
        reply_to_tweets()
        # Changing to follower page
        driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div['
                                      '1]/div[2]/nav/div/div[2]/div/div[2]/a').click()
        # Follower tweet reply function call
        reply_to_tweets_following_page()
        # Clicking on Account menu
        driver.find_element(By.XPATH, '//div[@aria-label="Account menu"]').click()
        time.sleep(3)
        # Clicking on Logout button
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div[1]/div').click()
        time.sleep(5)
        # Clicking on Logout button final.
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]/div').click()
        time.sleep(10)
        break


accounts = [
    ('account1', 'password1'),
    ('account2', 'password2'),
]
while True:
    for account in accounts:
        run_bot(*account)
        time.sleep(10)

    time.sleep(120)
