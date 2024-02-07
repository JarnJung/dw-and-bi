# Data Modeling II

## โครงสร้างไฟล์ ประกอบด้วย
#### โฟลเดอร์ 02-data-modeling-ii : จัดเก็บไฟล์ code สำหรับสร้างตารางในฐานข้อมูล และ สำหรับ ETL จาก Data files เข้าไปในฐานข้อมูล
    -- docker-compose.yml  
    -- etl.py
    -- README.md
    -- requirement.txt

#### โฟลเดอร์ ../data จัดเก็บ Data files ในรูปแบบของ .json ก่อนการทำ ETL

## การทำงาน 
ไฟล์ etl.py จะทำการอ่านข้อมูลจาก Data files ทั้งหมดใน Folder ../data จากนั้นจะทำสกัดข้อมูลของแต่ละ event โดยจะทำการเก็บข้อมูลของแต่ละ event ตาม attribute ดังนี้

|Attribute|Data Type|
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
