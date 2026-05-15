## Response Section
#### JSON กับ Protocal Buffer
    json รูปแบบข้อมูลเป็น Text-Based สามารถอ่านข้อความได้ มีขนาดข้อมูลใหญ่กว่า เหมาะกับ REST API

        ข้อดี 
            1. อ่านง่าย
            2. ใช้ได้ทุกภาษา
            3. เหมาะกับ REST API
            4. ไม่ต้อง compile schema

        ข้อเสีย    
            1. payload ใหญ่
            2. parse ช้ากว่า เพระาต้องแปลง text เป็น object

    protocal buffer รูปแบบข้อมูลเป็น binary ไม่สามารถอ่านข้อความได้โดยตรง มีขนาดที่เล็กกว่าและเร็วกว่า json เหมาะกับงาน gRPC, Microservice

        ข้อดี
            1. ขนาดเล็กกว่า
            2. เร็วกว่า
            3. strong typing เพราะ schema ชัดเจน

        ข้อเสีย
            1. คนอ่านไม่ได้
            2. ต้องมี schema
            3. frontend ใช้งานยุ่งกว่า

