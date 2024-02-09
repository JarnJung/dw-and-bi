# Data Modeling II
    ในโปรเจ็กต์นี้จะเป็นการทำ ETL ของข้อมูลในรูปแบบของ json ไฟล์ แล้ว สกัดนำเอาข้อมูลที่่ต้องการวิเคราะห์ ไปจัดเก็บไว้ในฐานข้อมูลประเภท NoSQL โดยเลือกใช้ฐานข้อมูล Apache Cassandra เพื่อจัดเก็บข้อมูล

## โครงสร้างไฟล์ ประกอบด้วย
#### โฟลเดอร์ 02-data-modeling-ii : จัดเก็บไฟล์ code สำหรับ ETL จาก Data files เข้าไปในฐานข้อมูล
    -- requirement.txt
    -- docker-compose.yml  
    -- etl.py
    -- README.md    
    -- select_data.py

#### โฟลเดอร์ ../data จัดเก็บ Data files ในรูปแบบของ .json ก่อนการทำ ETL

## การทำงาน 
ไฟล์ etl.py จะทำการอ่านข้อมูลจาก Data files ทั้งหมดใน Folder ../data จากนั้นจะทำสกัดข้อมูลของแต่ละ event จากรูปแบบของ  ๋json โดยจะทำการเก็บข้อมูลของแต่ละ event ตาม column ดังนี้

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

# Instruction
## Getting Started

```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt  # ติดตั้ง package ที่จะเป็นสำหรับการ Run Program
```

## Running Cassandra
```sh
docker-compose up   # run script docker-compose.yml สำหรับการเริ่มใข้งาน Cassandra
```

To shutdown, press Ctrl+C and run:

```sh
docker-compose down   # run script docker-compose.yml สำหรับการหยุดใข้งาน Cassandra
```

## Running ETL Scripts

```sh
python etl.py    # run script สำหรับการอ่านค่าจาก json files แล้วบันทึกค่าใน Cassandrs
```
## Test select data from Cassandra

```sh
python select_data.py   # อ่านค่าที่บันทึกไว้ใน Cassandra
```
