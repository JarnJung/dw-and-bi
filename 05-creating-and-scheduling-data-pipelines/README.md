# Creating and Scheduling data pipelines

ใน project นี้จะเป็นการทำ Automated ETL โดยให้ใช้ Apache Airflow โดยจะเป็นการ ETL ข้อมูลจากไฟล์ github events แล้ว load ในฐานข้อมูล 

1. Run docker compose

```sh
docker-compose up
```

2. เข้าไปยัง GUI ของ Airflow โดยใช้ port 8080 และ login เข้าไปยัง airflow

3. Run DAG ที่ชื่อว่า 'etl'