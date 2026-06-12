from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time
from datetime import datetime

#เปิดเว็บเบราว์เซอร์และเข้าเว็บไซต์
driver = webdriver.Chrome()
driver.get("https://www.lazada.co.th/catalog/?q=หูฟังบลูทูธ")
time.sleep(3)  # รอให้หน้าเว็บโหลด
print("กำลังดึงข้อมูลจากเว็บไซต์...")
#ดึงข้อมูลสินค้าจากหน้าเว็บ
product = driver.find_elements(By.CSS_SELECTOR,".RfADt")
price = driver.find_elements(By.CSS_SELECTOR,".ooOxS")
date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
names = []
prices = []

for i in product[:10]:
    names.append(i.text)
for j in price[:10]:
    prices.append(j.text)

print(f"พบสินค้า {len(names)} วันที่ {date_time}")   
#บันทึกข้อมูลลงไฟล์ Excel
data = {"ชื่อสินค้า": names, "ราคา": prices, "วันที่": date_time}
df = pd.DataFrame(data)
df.to_excel("lazada_price.xlsx", index=False)
print("ข้อมูลสินค้าถูกบันทึกในไฟล์ lazada_price.xlsx")

