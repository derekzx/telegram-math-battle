from selenium import webdriver
import time

# Set directory for chromedriver
driver = webdriver.Chrome("./chromedriver.exe")
# Enter your Math Battle URL here
driver.get("")

start = driver.find_element_by_id("button_correct")
start.click()

while True:
    val1 = int(driver.find_element_by_id("task_x").text)
    val2 = int(driver.find_element_by_id("task_y").text)
    op = driver.find_element_by_id("task_op").text
    ans = int(driver.find_element_by_id("task_res").text)
    correct_ans = 0

    if op == "+":
        correct_ans = val1+val2
    elif op == "–":
        correct_ans = val1-val2
    elif op == "×":
        correct_ans = val1*val2
    elif op == "/":
        correct_ans = val1/val2
    
    correct_ans = int(correct_ans)
    if ans == correct_ans:
        button = driver.find_element_by_id("button_correct")
        button.click()
    else:
        button = driver.find_element_by_id("button_wrong")
        button.click()
    
    if int(driver.find_element_by_id("score_value").text) == 130:
        break
    