from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import unittest

class UpdateCallqueue(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\webdriver\chromedriver.exe')
        self.driver = webdriver.Chrome(service=s)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_Department_in_Q_Online1(self):
        # Open the web application
        self.driver.get("https://online-web-mauve.vercel.app/")
        # คลิกปุ่ม "เข้าสู่ระบบ"
        open_modal_button = self.driver.find_element(By.ID, "loginNavbar")
        open_modal_button.click()
     
        # ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
        id_input = self.driver.find_element(By.ID, "LoginID_Card")
        password_input = self.driver.find_element(By.ID, "LoginPassword")

        # กรอกข้อมูลใน input field
        id_input.send_keys("7777777777777")
        password_input.send_keys("123456")

        # Wait for the search results to load
        time.sleep(5)

        # คลิกปุ่ม "เข้าสู่ระบบ"
        login_button = self.driver.find_element(By.ID, "Login")
        login_button.click()

        time.sleep(4)

        # ค้นหา <div> โดยใช้ XPath
        div_element = self.driver.find_element(By.XPATH, '//div[contains(text(), "จัดการจองคิว")]')
        div_element.click()

        time.sleep(4)

        # คลิกที่ปุ่ม
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID,"buttonStatus"))
        )
        time.sleep(3)

        # รอให้ปุ่ม "buttonStatus" เป็นคลิกได้
        element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "buttonStatus"))
            )

        # คลิกที่ปุ่ม "buttonStatus"
        element.click()

         # รอเพื่อให้เว็บไซต์ปรับปรุงหน้าหลังจากการคลิก
        time.sleep(3)

        confirm = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='อัพเดต']")

        # คลิกปุ่ม "ตกลง" เป็นยืนยัน
        confirm.click()
        time.sleep(3)

        # คลิกที่ปุ่ม
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID,"buttonStatus"))
        )
        time.sleep(3)

        # รอให้ปุ่ม "buttonStatus" เป็นคลิกได้
        element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "buttonStatus"))
            )

        # คลิกที่ปุ่ม "buttonStatus"
        element.click()

        # รอเพื่อให้เว็บไซต์ปรับปรุงหน้าหลังจากการคลิก
        time.sleep(3)

        confirm = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='อัพเดต']")

        # คลิกปุ่ม "ตกลง" อัพเดตเป็นรับการรักษาแล้ว
        confirm.click()
        time.sleep(3)

         # คลิกที่ปุ่ม
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID,"buttonStatus"))
        )
        time.sleep(3)

        # รอให้ปุ่ม "buttonStatus" เป็นคลิกได้
        element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "buttonStatus"))
            )

        # คลิกที่ปุ่ม "buttonStatus"
        element.click()

        # รอเพื่อให้เว็บไซต์ปรับปรุงหน้าหลังจากการคลิก
        time.sleep(3)

        confirm = self.driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='อัพเดต']")

        # คลิกปุ่ม "ตกลง" อัพเดตเป็นรับการรักษาแล้ว
        confirm.click()
        time.sleep(3)

if __name__ == "__main__":
    unittest.main()