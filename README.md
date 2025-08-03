# Flask Note-Taking Web Application by Qier

แอปพลิเคชันสำหรับจดบันทึกอย่างง่าย สร้างขึ้นด้วย Flask และ PostgreSQL ผู้ใช้สามารถสร้าง, แก้ไข, ลบโน้ต และจัดระเบียบด้วยแท็ก (Tags) ได้

## Features (คุณสมบัติ)

* **จัดการโน้ต (CRUD for Notes):** สร้าง, อ่าน, อัปเดต และลบโน้ต
* **จัดการแท็ก (CRUD for Tags):** สร้าง, อ่าน, อัปเดต และลบแท็ก
* **ระบบแท็ก:** หนึ่งโน้ตสามารถมีได้หลายแท็ก
* **กรองตามแท็ก:** สามารถดูโน้ตทั้งหมดที่เกี่ยวข้องกับแท็กที่เลือกได้
* **หน้าตาเรียบง่าย:** ออกแบบโดยใช้ Bootstrap

## Technologies Used (เทคโนโลยีที่ใช้)

* **Backend:** Python, Flask, SQLAlchemy
* **Frontend:** HTML, Jinja2, Bootstrap 5
* **Database:** PostgreSQL
* **Containerization:** Docker, Docker Compose
* **Forms:** Flask-WTF, WTForms-SQLAlchemy

## Setup and Installation (การติดตั้งและตั้งค่า)

ทำตามขั้นตอนต่อไปนี้เพื่อรันโปรเจกต์บนเครื่องของคุณ

1.  **Clone the repository:**
    ```bash
    # vvv LINK HAS BEEN CORRECTED vvv
    git clone [https://github.com/xhier2547/PSUNOTE_QIER.git](https://github.com/xhier2547/PSUNOTE_QIER.git)
    cd PSUNOTE_QIER
    ```

2.  **Start Database Service:**
    ใช้ Docker Compose เพื่อเริ่มการทำงานของฐานข้อมูล PostgreSQL
    ```bash
    docker compose up -d
    ```

3.  **Create and Activate Virtual Environment:**
    สร้างและเปิดใช้งานสภาพแวดล้อมเสมือนของ Python
    ```bash
    # สร้าง venv
    python -m venv venv

    # เปิดใช้งาน venv (Windows)
    .\venv\Scripts\activate

    # เปิดใช้งาน venv (macOS/Linux)
    source venv/bin/activate
    ```

4.  **Install Dependencies:**
    ติดตั้งแพ็คเกจ Python ทั้งหมดที่โปรเจกต์ต้องการ
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the Application:**
    สั่งให้แอปพลิเคชัน Flask เริ่มทำงาน
    ```bash
    python noteapp.py
    ```

6.  **Access the Application:**
    เปิดเว็บเบราว์เซอร์แล้วไปที่ `http://127.0.0.1:5000`

## 📖 Usage (วิธีใช้งาน)

* **หน้าแรก:** แสดงโน้ตทั้งหมด
* **สร้างโน้ต:** คลิกปุ่ม "Create" เพื่อเพิ่มโน้ตใหม่ สามารถเพิ่มแท็กได้โดยการพิมพ์ชื่อแท็กลงในช่อง "Tag" คั่นด้วยเครื่องหมายจุลภาค (`,`)
* **จัดการโน้ต:** ใช้ปุ่ม "Edit" และ "Delete" ที่อยู่บนการ์ดของแต่ละโน้ต
* **ดูตามแท็ก:** คลิกที่ชื่อแท็กเพื่อดูโน้ตทั้งหมดที่มีแท็กนั้นๆ และสามารถแก้ไขหรือลบแท็กได้จากหน้านี้


**QIER**