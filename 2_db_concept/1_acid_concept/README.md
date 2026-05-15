## Response Section
#### Atomicity คือ transaction ต้องสำเร็จทั้งหมดหรือ ไม่ทำเลย หากขั้นตอนใดล้มเหลวต้อง rollback ทั้งหมด

#### Consistency ข้อมูลต่้องคงความถูกต้องก่อนและหลัง transaction ตามกฎของระบบ

#### Isolation คือ Transaction หลายตัวที่ทำงานพร้อมกันไม่รบกวนกัน และทำให้ผลลัพธ์เหมือนกับการรันทีละ Transaction เพื่อป้องกันปัญหาข้อมูลไม่ถูกต้องจากการเข้าถึงพร้อมกัน

#### Durability เมื่อ commit แล้วข้อมูลต้องถูกบันทึกถาวร แม้ระบบล่ม ข้อมูลก็ไม่หาย

#### Backend :
    1. จัดการ transaction (begin , commit , rollback)
    2. ควบคุม business logic
    3. ป้องกัน race condition และ concurrent access
    4. กำหนด isolation level

#### Frontend :
    1. ตรวจสอบข้อมูลเบื้องต้น
    2. ป้องกันการกดซ้ำ
    3. แสดง loading state
    4. ส่ง request อย่างถูกต้อง
