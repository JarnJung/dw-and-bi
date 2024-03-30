# Building a Data Lake

ใน project นี้จะเป็นการทำ ETL จากข้อมูลดิบ (Raw Data) โดยใช้ Apache Spark ซึ่งเป็นทำการแปลงไฟล์ raw data (.json) ที่อยู่ใน Landing Zone ไปเก็บไว้ใน Clean Zone โดยจะแปลงเป็น structure data และเก็บไว้ในรูปแบบของ csv และ parquet

1. ปรับสิทธิ์การเข้าถึงไฟล์ใน direcotry เพื่อให้เราสามารถสร้างไฟล์ได้จาก Jupyter Lab ให้รันคำสั่งด้านล่างนี้

```sh
sudo chmod 777 .
```

2. Run docker compose

```sh
docker-compose up
```

3. เมื่อเข้ามาใน Jupyter notebook ( ที่ Port 8888 โดยใช้ web browser )

4. เปิดไฟล์ worki/etl_gcs_to_gcs.py

5. ในขั้นตอนนี้เราจะเตรียม variables สำหรับการใช้ Run Code

    5.1 ทำเปลี่ยนค่า SERVICE_ACCOUNT_EMAIL และ KEYFILE_PATH (สำหรับเก็บ keyfile ที่ได้จาก Google Cloud)

    ```sh
    SERVICE_ACCOUNT_EMAIL = "xxxxxxxx@xxxx.iam.gserviceaccount.com"
    KEYFILE_PATH = "path/xxxxxxxxxxxxxx.json"
    ```

    5.2 สร้าง varibales สำหรับเก็บ bucket และ directory path ที่ใช้เก็บไฟล์ใน bucket
    ```sh
    bucket = # bucket name
    landing_zone = # path สำหรับเก็บ Raw data
    cleaned_zone_csv = # path สำหรับเก็บ output ที่เป็น csv
    cleaned_zone_parquet = # path สำหรับเก็บ output ที่เป็น parquet
    events_dir = # path สำหรับเก็บ output events


6. ทำการ Run code ในแต่ละเซลล์ ซึ่งผลลัพธ์ที่ได้จะเป็น structure data เก็บอยู่ใน Clean Zone โดยจะแปลงเป็นไฟล์ในรูปแบบของ csv เก็บไว้ใน cleaned_csv และแปลงเป็นไฟล์ในรูปแบบของ parquet เก็บไว้ใน cleaned_parquet เก็บไว้ใน bucket ที่เราเตรียมไว้ใน GCS 
