# Tasks: จองคิวตรวจสุขภาพ (Booking)

- Feature: จองคิวตรวจสุขภาพ
- Spec ID: SPEC-BKG-001
- อ้างอิง: [plan.md](plan.md)
- วันที่: 2569-09-23
- สรุป: มีทั้งหมด 18 tasks ครอบคลุมงาน backend, frontend, การเชื่อมต่อ และการทดสอบตาม spec
- มี 4 tasks ที่ต้องรอคำตอบ Open Question Q-02 เรื่องรูปแบบและวิธีออกหมายเลขคิว

## รายการ task

### T-01 สร้างตารางและ migration
- รองรับ: CON-TECH-01, DOM-PDPA-01, IF-HIS-01, FR-BKG-04
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-05 และ T-08
- ไฟล์ที่แตะ: `backend/app/db/models.py`, `backend/app/db/session.py`, `backend/app/db/migrations/001_init.py`, `backend/tests/conftest.py`
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: migration สร้างตาราง `slots`, `bookings` และ `audit_logs` ได้ และตาราง `bookings` ไม่มีคอลัมน์เลขบัตรประชาชน
- สถานะ: พร้อมทำ

### T-02 ตรวจผลยืนยันตัวตนก่อนเข้า endpoint
- รองรับ: IF-IDP-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-03, T-05, T-08 และ T-09
- ไฟล์ที่แตะ: `backend/app/auth/idp.py`, `backend/app/main.py`, `backend/tests/test_idp.py`
- ต้องทำหลัง: T-01
- เสร็จเมื่อ: endpoint ที่แตะข้อมูลผู้รับบริการปฏิเสธคำขอที่ไม่มีผลยืนยันตัวตน และยอมรับคำขอที่ยืนยันแล้ว
- สถานะ: พร้อมทำ

### T-03 สร้างบริการค้นหาช่วงเวลาว่าง
- รองรับ: FR-BKG-01, FR-BKG-06, ASM-01, ASM-02
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-04 และ T-15
- ไฟล์ที่แตะ: `backend/app/slots/service.py`, `backend/app/slots/router.py`, `backend/tests/test_slots.py`
- ต้องทำหลัง: T-01, T-02
- เสร็จเมื่อ: `GET /slots` คืนช่วงเวลาภายใน 30 วันพร้อม `remaining` และคำนวณผลใหม่เมื่อเปลี่ยน `package_code`
- สถานะ: พร้อมทำ

### T-04 สร้างหน้าจอเลือกแพ็กเกจและเวลา
- รองรับ: FR-BKG-01, FR-BKG-06
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-12 และ T-14
- ไฟล์ที่แตะ: `frontend/src/pages/SlotPicker.jsx`, `frontend/src/App.jsx`, `frontend/src/api/client.js`, `frontend/src/__tests__/SlotPicker.test.jsx`
- ต้องทำหลัง: ไม่มี
- เสร็จเมื่อ: หน้าจอแสดงช่วงเวลาและที่นั่งคงเหลือจาก API จำลอง และโหลดช่วงเวลาใหม่เมื่อเปลี่ยนแพ็กเกจ
- สถานะ: พร้อมทำ

### T-05 บันทึกการจองและตัดที่นั่งแบบธุรกรรม
- รองรับ: FR-BKG-04, IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-17
- ไฟล์ที่แตะ: `backend/app/booking/service.py`, `backend/app/booking/router.py`, `backend/app/main.py`, `backend/tests/test_booking_create.py`
- ต้องทำหลัง: T-01, T-02, T-03
- เสร็จเมื่อ: `POST /bookings` บันทึก HN และลด `remaining` ในธุรกรรมเดียว โดยไม่เก็บเลขบัตรประชาชน
- สถานะ: พร้อมทำ

### T-06 ป้องกันการจองซ้ำในวันเดียวกัน
- รองรับ: FR-BKG-02, ASM-02
- ตรวจด้วย: AC-BKG-02
- ไฟล์ที่แตะ: `backend/app/booking/service.py`, `backend/app/booking/router.py`, `backend/tests/test_AC_BKG_02.py`
- ต้องทำหลัง: T-05
- เสร็จเมื่อ: `test_AC_BKG_02` ผ่าน โดยคำขอซ้ำถูกปฏิเสธและคืนหมายเลขคิวเดิมเมื่อมีข้อมูลหมายเลขคิวแล้ว
- สถานะ: พร้อมทำ

### T-07 จัดการช่วงเวลาที่เต็มและหาช่วงใกล้เคียง
- รองรับ: FR-BKG-03, ASM-02
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: `backend/app/slots/service.py`, `backend/app/booking/service.py`, `backend/app/booking/router.py`, `backend/tests/test_AC_BKG_03.py`
- ต้องทำหลัง: T-03, T-05
- เสร็จเมื่อ: `test_AC_BKG_03` ผ่าน โดยตอบ 409 พร้อม 3 ช่วงที่ใกล้ที่สุดในวันเดียวกันและวันถัดไป และไม่สร้างการจอง
- สถานะ: พร้อมทำ

### T-08 บันทึก audit log การเข้าถึงข้อมูล
- รองรับ: DOM-PDPA-01
- ตรวจด้วย: AC-BKG-06
- ไฟล์ที่แตะ: `backend/app/audit/middleware.py`, `backend/app/main.py`, `backend/tests/test_AC_BKG_06.py`
- ต้องทำหลัง: T-01, T-02, T-05
- เสร็จเมื่อ: `test_AC_BKG_06` ผ่านและ audit log มีผู้เข้าถึง เวลา และ HN ของผู้รับบริการ
- สถานะ: พร้อมทำ

### T-09 ค้น HN จาก HIS โดยไม่จัดเก็บเลขบัตร
- รองรับ: IF-HIS-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-05
- ไฟล์ที่แตะ: `backend/app/his/client.py`, `backend/app/booking/router.py`, `backend/tests/test_his_lookup.py`
- ต้องทำหลัง: T-02
- เสร็จเมื่อ: `GET /patients/lookup` ส่งเลขบัตรไป HIS และคืน HN โดยเลขบัตรไม่ถูกบันทึกในข้อมูลการจอง
- สถานะ: พร้อมทำ

### T-10 วางคำขอแจ้งเตือนแบบ asynchronous
- รองรับ: IF-NOT-01, FR-BKG-04, FR-BKG-05, ASM-03
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-11 และ T-17
- ไฟล์ที่แตะ: `backend/app/notify/queue.py`, `backend/app/booking/service.py`, `backend/tests/test_notify_queue.py`
- ต้องทำหลัง: T-05
- เสร็จเมื่อ: หลังบันทึกการจอง API วางงานลงคิวและคืนผลโดยไม่รอผลการส่งข้อความ
- สถานะ: พร้อมทำ

### T-11 ส่งซ้ำข้อความที่ล้มเหลวภายในเวลาที่กำหนด
- รองรับ: FR-BKG-05, NFR-REL-02, ASM-03
- ตรวจด้วย: AC-BKG-04
- ไฟล์ที่แตะ: `backend/app/notify/queue.py`, `backend/tests/test_AC_BKG_04.py`
- ต้องทำหลัง: T-10
- เสร็จเมื่อ: `test_AC_BKG_04` ผ่าน โดยการจองยังอยู่และงานส่งซ้ำถูกกำหนดภายใน 5 นาที
- สถานะ: พร้อมทำ

### T-12 สร้างหน้ายืนยันและทางเลือกเมื่อเต็ม
- รองรับ: FR-BKG-03, FR-BKG-04
- ตรวจด้วย: AC-BKG-03
- ไฟล์ที่แตะ: `frontend/src/pages/ConfirmBooking.jsx`, `frontend/src/App.jsx`, `frontend/src/__tests__/AC-BKG-03.test.jsx`
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: `AC-BKG-03.test.jsx` ผ่าน โดย API จำลองตอบ 409 แล้วหน้าจอแสดงข้อความช่วงเวลาเต็มและตัวเลือก 3 รายการ
- สถานะ: พร้อมทำ

### T-13 สร้างหน้าผลการจองและการแจ้งเตือนล้มเหลว
- รองรับ: FR-BKG-04, FR-BKG-05
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ T-17
- ไฟล์ที่แตะ: `frontend/src/pages/BookingResult.jsx`, `frontend/src/App.jsx`, `frontend/src/__tests__/BookingResult.test.jsx`
- ต้องทำหลัง: T-04
- เสร็จเมื่อ: หน้าจอผลการจองแสดงสถานะการจองและเตรียมพื้นที่แสดงหมายเลขคิวจาก API จำลอง
- สถานะ: รอ Q-02

### T-14 ตั้งค่า TLS สำหรับการรับส่งข้อมูล
- รองรับ: NFR-SEC-01
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานพื้นฐานของ NFR-SEC-01
- ไฟล์ที่แตะ: `backend/app/config.py`, `backend/app/main.py`, `frontend/vite.config.js`, `backend/tests/test_transport_security.py`
- ต้องทำหลัง: T-02
- เสร็จเมื่อ: การตั้งค่า deployment/API บังคับใช้ TLS 1.2 ขึ้นไป และมี test ตรวจการตั้งค่าดังกล่าว
- สถานะ: พร้อมทำ

### T-15 ทดสอบประสิทธิภาพการค้นหาช่วงเวลา
- รองรับ: NFR-PERF-01, FR-BKG-01
- ตรวจด้วย: AC-BKG-05
- ไฟล์ที่แตะ: `backend/tests/test_AC_BKG_05.py`
- ต้องทำหลัง: T-03
- เสร็จเมื่อ: `test_AC_BKG_05` ยิงคำขอพร้อมกัน 200 รายการแบบย่อส่วนและรายงานค่า p95 เพื่อเทียบเกณฑ์ 2 วินาที
- สถานะ: พร้อมทำ

### T-16 ทดสอบความสำเร็จของผู้ใช้ใหม่
- รองรับ: NFR-USE-01, ASM-05
- ตรวจด้วย: ไม่มี AC ตรง ๆ เป็นงานทดสอบ NFR-USE-01
- ไฟล์ที่แตะ: `docs/srs/`, `frontend/src/__tests__/usability-booking.md`
- ต้องทำหลัง: T-04, T-12, T-13, T-14
- เสร็จเมื่อ: มีผลทดสอบผู้ใช้ใหม่ 10 คนและบันทึกว่าผ่านเกณฑ์ 8 ใน 10 คนภายใน 3 นาทีโดยไม่ขอความช่วยเหลือ
- สถานะ: รอ Q-02

### T-17 กำหนดและออกหมายเลขคิวในการจอง
- รองรับ: FR-BKG-04, FR-BKG-05, FR-BKG-02
- ตรวจด้วย: AC-BKG-01 และ AC-BKG-04
- ไฟล์ที่แตะ: `backend/app/booking/service.py`, `backend/app/booking/router.py`, `backend/tests/test_AC_BKG_01.py`, `backend/tests/test_AC_BKG_04.py`
- ต้องทำหลัง: T-05, T-06, T-10
- เสร็จเมื่อ: หลังทีมตอบ Q-02 แล้ว `test_AC_BKG_01` และส่วนหมายเลขคิวของ `test_AC_BKG_04` ผ่านตามรูปแบบที่อนุมัติ
- สถานะ: รอ Q-02

### T-18 ต่อหน้าจอเข้ากับ API จริง
- รองรับ: FR-BKG-01, FR-BKG-03, FR-BKG-04, FR-BKG-05, IF-IDP-01
- ตรวจด้วย: AC-BKG-01 และ AC-BKG-03
- ไฟล์ที่แตะ: `frontend/src/api/client.js`, `frontend/src/App.jsx`, `frontend/src/pages/SlotPicker.jsx`, `frontend/src/pages/ConfirmBooking.jsx`, `frontend/src/pages/BookingResult.jsx`, `frontend/src/__tests__/integration-booking.test.jsx`
- ต้องทำหลัง: T-03, T-07, T-11, T-12, T-13, T-17
- เสร็จเมื่อ: หน้าจอเรียก API จริงผ่าน `/api` และ flow เลือกเวลา ยืนยัน และแสดงผลทำงานครบตามสัญญา API
- สถานะ: รอ Q-02

## ตารางตรวจความครบ

### Acceptance Criteria

| AC ID | task ที่ตรวจ AC นี้ |
|---|---|
| AC-BKG-01 | T-17 |
| AC-BKG-02 | T-06 |
| AC-BKG-03 | T-07, T-12, T-18 |
| AC-BKG-04 | T-11, T-17 |
| AC-BKG-05 | T-15 |
| AC-BKG-06 | T-08 |

### Constraints

| Constraint ID | task ที่ทำให้เป็นจริง |
|---|---|
| CON-TECH-01 | T-01 |
| DOM-PDPA-01 | T-01, T-08 |
| IF-IDP-01 | T-02, T-18 |
| IF-HIS-01 | T-01, T-09, T-05 |
| IF-NOT-01 | T-10, T-11 |

## สิ่งที่ยังไม่ทำ

- Q-02 หมายเลขคิวรีเซ็ตรายวัน หรือนับต่อเนื่อง และมีรูปแบบอย่างไร (เช่น A001) -> ถามเจ้าหน้าที่เวชระเบียน (ยังไม่ได้คำตอบ)
  - task ที่รอ: T-13, T-16, T-17, T-18