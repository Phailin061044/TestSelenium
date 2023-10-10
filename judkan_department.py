from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from selenium.webdriver.support.ui import Select

# ระบุพาธของ ChromeDriver 
chrome_driver_path = "D:/webdriver/chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")

# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# กรอกข้อมูลใน input field
id_input.send_keys("8888888888888")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()
time.sleep(5)

icon = driver.find_element(By.XPATH, '//div[@class="d-flex justify-content-center"]/i[@class="fa-solid fa-calendar-days fs-3 font-bold"]')
icon.click()
time.sleep(5)



# ปุ่มเพิ่มแผนก
button_create_department = driver.find_element(By.ID, "department_create")
button_create_department.click()
time.sleep(5)

# ปุ่มเพิ่มรูป
# หาก input element สำหรับอัปโหลดไฟล์มี ID ให้ใช้ ID ในการระบุ
upload_input = driver.find_element(By.ID, "department_create_image")

file_name = "images.png"
downloads_folder = os.path.expanduser("~\\Downloads")  # หากใช้ Windows
file_path = os.path.join(downloads_folder, file_name)
upload_input.send_keys(file_path)
time.sleep(5)

dapartname_input = driver.find_element(By.ID, "Depart_department_id")
dapartname_input.send_keys("นวดแผนไทย")

time_input = driver.find_element(By.ID, 'Depart_open_time')
time_input.send_keys("10:30")  # เปลี่ยน "12:30" เป็นค่าเวลาที่คุณต้องการทดสอบ
time.sleep(1)

time_input = driver.find_element(By.ID, 'Depart_close_time')
time_input.send_keys("17:30")  # เปลี่ยน "12:30" เป็นค่าเวลาที่คุณต้องการทดสอบ
time.sleep(1)


building_input = driver.find_element(By.ID, "Depart_building")
building_input.send_keys("5")
time.sleep(1)


floor_input = driver.find_element(By.ID, "Depart_floor")
floor_input.send_keys("3")
time.sleep(1)

phone_input = driver.find_element(By.ID, "Depart_department_phone")
phone_input.send_keys("0989698742")
time.sleep(1)

queue_input = driver.find_element(By.ID, "Depart_max_queue_number")
queue_input.send_keys("50")
time.sleep(1)

   # คลิกปุ่ม
button_element = driver.find_element(By.ID, "department_creatSubmit")

        # คลิกปุ่ม
button_element.click()
time.sleep(2)



# ระบุ element ของปุ่ม "ตกลง" ด้วย XPath
confirm_button = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ตกลง']")

# คลิกปุ่ม "ตกลง"
confirm_button.click()
time.sleep(5)


driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อน

# Click on the department dropdown to open it
department_dropdown = driver.find_element(By.ID, "DeselectedDepartment")
department_dropdown.click()

# Find and click the desired department option by its visible text
desired_option_text = "นวดแผนไทย"
option_xpath = f"//div[@id='DeselectedDepartment']//div[contains(text(), '{desired_option_text}')]"
desired_option = driver.find_element(By.XPATH, option_xpath)
desired_option.click()
time.sleep(5)


# รอให้ปุ่ม "แก้ไขแผนก" เป็นแบบคลิกได้
edit_department_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'department_edit')))
# คลิกปุ่ม "แก้ไขแผนก"
edit_department_button.click()
time.sleep(3)  # ควรใช้ WebDriverWait และ expected_conditions ที่นี่ด้วย

# ระบุ input field และคลิกปุ่ม "ตกลง"
floor_input = driver.find_element(By.ID, "Depart_floor")
floor_input.clear()  # เคลียร์ค่าใน input field
time.sleep(3) 
floor_input.send_keys("3")

new_element = driver.find_element(By.ID, "Depart_Creatsebmit")
driver.execute_script("arguments[0].scrollIntoView();", new_element)
time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อนมา

confirm_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "Depart_Creatsebmit")))
confirm_button.click()
time.sleep(3) 

# ปุ่มยืนยันการอัปเดต
button_swal = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
button_swal.click()
time.sleep(5)

driver.execute_script("window.scrollBy(0, -1000);")
time.sleep(2)  # รอสักครู่ให้หน้าเว็บเลื่อน

# Click on the department dropdown to open it
department_dropdown = driver.find_element(By.ID, "DeselectedDepartment")
department_dropdown.click()

# Find and click the desired department option by its visible text
desired_option_text = "นวดแผนไทย"
option_xpath = f"//div[@id='DeselectedDepartment']//div[contains(text(), '{desired_option_text}')]"
desired_option = driver.find_element(By.XPATH, option_xpath)
desired_option.click()
time.sleep(5)


#ลบ
button_Cancel = driver.find_element(By.ID, "department_delete")
button_Cancel.click()
time.sleep(2)


# ปุ่มยืนยันลบ
button_swal = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[6]/button[1]")
button_swal.click()
time.sleep(5)

