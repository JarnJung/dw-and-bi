# Data Modeling 03
    ในโปรเจ็กต์นี้จะเป็นการทำ ETL ของข้อมูลในรูปแบบของ json ไฟล์ แล้ว สกัดนำเอาข้อมูลที่่ต้องการวิเคราะห์ ไปจัดเก็บไว้ในฐานข้อมูลบนระบบ Cloud โดยเลือกใช้ Google Cloud BigQuery

## โครงสร้างไฟล์ ประกอบด้วย
#### โฟลเดอร์ 02-data-modeling-ii : จัดเก็บไฟล์ code สำหรับ ETL จาก Data files เข้าไปในฐานข้อมูล
    -- requirement.txt
    -- etl_bigquery.py
    -- README.md    
    -- github_events.csv

#### โฟลเดอร์ ../data จัดเก็บ Data files ในรูปแบบของ .json ก่อนการทำ ETL (5 files)

## การทำงาน 
ไฟล์ etl_bigquery.py จะทำการอ่านข้อมูลจาก Data files ทั้งหมดใน Folder ../data/ จากนั้นจะทำสกัดข้อมูลของแต่ละ event จากรูปแบบของ  ๋json โดยจะทำการเก็บข้อมูลของแต่ละ event ตาม column ดังนี้

|column|Data Type|
|:------------|:---------------:|
|id|int|
|type|text|
|repo_id| int
|repo_url| text
|actor_id |int
|login |text
|public| boolean
|created_at |text


แล้วบันทึกไว้ในไฟล์ github_events.csv จากนั้นจะอ่านค่าจาก ไฟล์ github_events.csv แล้วบันทึกไปยัง Google Cloud BigQuery

# Instruction
## Getting Started

```sh
python -m venv ENV                  # สร้าง virtual environment
source ENV/bin/activate              
pip install -r requirements.txt     # ติดตั้ง package ที่จะเป็นสำหรับการ Run Program
```

## Running ETL Scripts

```sh
python etl_bigquery.py    # run script สำหรับการอ่านค่าจาก json files ในโฟล์เดอร์ data ทั้ง 5 ไฟล์ (แล้วเก็บไว้ใน ไฟล์ github_events.csv) แล้วบันทึกค่าแต่ละ row ไปยัง Google Cloud BigQery
```



