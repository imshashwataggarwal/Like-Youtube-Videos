# Script to like youtube videos.
from selenium import webdriver
import sys, pyperclip, time

if len(sys.argv) > 1:
    # Get address from command line.
    url = ' '.join(sys.argv[1:])

else:
    #Get address from clipboard.
    url = pyperclip.paste()

KEY = '.yt-uix-button.yt-uix-button-size-default.yt-uix-button-opacity.yt-uix-button-has-icon.no-icon-markup.like-button-renderer-like-button.like-button-renderer-like-button-unclicked.yt-uix-post-anchor.yt-uix-tooltip'

mail = input('Enter Gmail : ')
password = input('Enter Password: ')

try:
	browser = webdriver.Chrome()
except:
	try:
		browser = webdriver.Firefox()
	except:
		print('Try Installing Chrome or Firefox...')

# Login to YouTube.
browser.get('https://accounts.google.com/ServiceLogin?passive=true&hl=en&service=youtube&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26next%3D%252F%26app%3Ddesktop%26feature%3Dshortcut%26hl%3Den&uilel=3')
time.sleep(3)
try:	
	loginEmail = browser.find_element_by_id('Email')
	loginEmail.send_keys(mail)
	next = browser.find_element_by_id('next')
	next.click()
	time.sleep(3)
	loginPassword = browser.find_element_by_id('Passwd')
	loginPassword.send_keys(password)
	signin = browser.find_element_by_id('signIn')
	signin.click()

except:
	print('Invalid Email')

time.sleep(7)
# Like the Video.
browser.get(url)
time.sleep(5)
try:
	like = browser.find_element_by_css_selector(KEY)
	like.click()	# Like Page
	print('Liked the Video!')
except:
	print('Unable to Like Page :C')
time.sleep(10)
browser.quit()
