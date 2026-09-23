# Prompt log

บันทึกทุกครั้งที่ใช้ AI กับ repo นี้ เขียนต่อท้ายเรื่อย ๆ ไม่ต้องลบของเก่า

---

## 2569-09-23 คำสั่ง: /tasks

- เครื่องมือ: Copilot ใน Codespaces
- ไฟล์: `specs/001-booking/spec.md`, `specs/001-booking/plan.md`
- ผลลัพธ์: สร้าง `specs/001-booking/tasks.md` จำนวน 18 tasks โดยเรียงตามการพึ่งพา ครอบคลุม AC-BKG-01 ถึง AC-BKG-06 และ Constraint ทั้งหมด
- สิ่งที่ยังรอ: T-13, T-16, T-17 และ T-18 รอ Q-02 เรื่องรูปแบบและวิธีออกหมายเลขคิว จึงไม่มีการเดาคำตอบ
- งานที่ยังไม่ได้ทำ: ยังไม่ได้เริ่มทำ task ใด ๆ ตามคำสั่ง

---

## 2569-09-23 คำสั่ง: /implement T-01

- เครื่องมือ: Copilot ใน Codespaces
- ไฟล์ที่สร้างหรือแก้: `backend/app/db/models.py`, `backend/app/db/session.py`, `backend/app/db/migrations/001_init.py`, `backend/tests/conftest.py`
- ผล test: `pytest` โหลดสำเร็จแต่ยังไม่มี test ที่เก็บได้ (`collected 0 items`); schema check ด้วย SQLite ผ่าน สร้าง `slots`, `bookings`, `audit_logs` และไม่พบ `national_id` ใน `bookings`
- สิ่งที่เกือบต้องเดา: ไม่ได้กำหนดรูปแบบหรือวิธีออก `queue_no` เพราะติด Q-02 จึงสร้างคอลัมน์ nullable ตาม plan เท่านั้น