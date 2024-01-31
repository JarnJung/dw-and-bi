# Data Modeling I

## โครงสร้างไฟล์ ประกอบด้วย
#### โฟลเดอร์ 01-data-modeling-i : จัดเก็บไฟล์ code สำหรับสร้างตารางในฐานข้อมูล และ สำหรับ ETL จาก Data files เข้าไปในฐานข้อมูล
    -- docker-compose.yml
    -- create_table.py
    -- etl.py
#### โฟลเดอร์ data จัดเก็บ Data files ในรูปแบบของ .json ก่อนการทำ ETL

## โครงสร้างฐานข้อมูล
#### ฐานข้อมูลประกอบด้วย ตาราง 2 ตาราง
#### Table : 'actors'

|Attribute|Data Type|
|:------------|:---------------:|
|id|int|
|login|text|

#### Table : 'events'

| Attribute | Data Type  |
| :------------ |:---------------:|
| id | int |
| type | text |
| actor_id (FK) | int |
| respo | text |
| create_at | text |

## การทำงาน 
    - ไฟล์ etl.py จะทำการอ่านข้อมูลจาก Data files ทั้งหมดใน Folder data จากนั้นจะทำสกัดข้อมูลของแต่ละ event โดยจะทำการเก็บข้อมูลของ Attribute ตามตารางของ actors และ events

## Getting Started

```sh
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

### Prerequisite when install psycopg2 package

For Debian/Ubuntu users:

```sh
sudo apt install -y libpq-dev
```

For Mac users:

```sh
brew install postgresql
```

## Running Postgres

```sh
docker-compose up
```

To shutdown, press Ctrl+C and run:

```sh
docker-compose down
```

## Running ETL Scripts

```sh
python create_tables.py
python etl.py
```
