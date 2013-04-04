import sys
from selenium import webdriver

driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", webdriver.DesiredCapabilities.FIREFOX)
driver.set_window_size(1680,1050)
with open(sys.argv[1]) as input_file:
    for i, line in enumerate(input_file):
		driver.get(line.rstrip())
		image_name = driver.current_url.replace(sys.argv[2],"").replace('/','-')
		print image_name
		driver.get_screenshot_as_file(sys.argv[3]+image_name+'.jpg')
driver.close()
