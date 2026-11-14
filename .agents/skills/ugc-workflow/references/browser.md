# Browser setup

Use mcp__cua_repl only for UI. Read its current documentation; the APIs here are examples, not a substitute. The Chrome profile is Sirawit; discover current browser/tab IDs and element indices. No parallel browser owners.

## 2. เริ่ม session และรับแท็บเดิม

1. อ่าน skill, workflow reference และ config และ `job.json` ของสินค้าที่จะทำก่อนเปิดฟอร์มหรือกดสร้าง
2. เปิดอ่านคำแนะนำล่าสุดของเครื่องมือ browser control ตามข้อกำหนดเริ่มต้นของเครื่องมือ ถ้าต้องดูรายการแอป/เบราว์เซอร์ ใช้ `await cua.getState()` เป็นคำสั่งแรกตามเอกสารเครื่องมือ
3. เลือก Chrome จาก inventory แล้วตั้งชื่อ browser session เช่น `🔎 UGC workflow` ก่อนรับแท็บมาควบคุม ตาม API ที่เครื่องมือประกาศ
4. แสดงรายการแท็บปัจจุบัน เลือกแท็บจากชื่อและ URL จริง ไม่ใช้ tab ID ของ pilot เป็นค่าถาวร
5. รับแท็บเดิมผ่าน `cua.getTab(...)` แล้วอ่าน accessibility state; หากข้อมูลไม่พอ ใช้ DOM snapshot ผ่าน API ของ browser control ที่ประกาศไว้ หรือ screenshot
6. อ่านสถานะหน้าเว็บก่อนกด ใช้ชื่อปุ่ม/label ที่พบจริง หมายเลของค์ประกอบต้องมาจาก state ล่าสุดเท่านั้น หลังทำการกระทำให้อ่าน state ตรวจผล

### หน้าเว็บที่ใช้ใน pilot

- Sheets: [Product Library](https://docs.google.com/spreadsheets/d/1hj97y5gVPzI3pLJLYXAfJmAdxA55nWPYa28IPjZ6pHE/edit?gid=0#gid=0)
- Flow: [โปรเจ็กต์ pilot](https://flow.google.com/project/ef29097b-33be-42cb-8f69-d46337e3d458)
- TikTok: [TikTok Studio](https://www.tiktok.com/tiktokstudio)

หากอยู่ URL ที่ต้องการแล้ว อย่าเปิดซ้ำหรือโหลดใหม่โดยไม่มีเหตุผล โดยเฉพาะหน้าฟอร์มอัปโหลดที่ยังไม่ส่ง

### การส่งแท็บระหว่างตัวควบคุม/agent

- ให้ตัวเดียวควบคุม Chrome ในแต่ละช่วง งานเขียนเนื้อหาที่ไม่แตะเบราว์เซอร์ทำแยกได้
- ถ้าขึ้นว่าแท็บอยู่ใน browser session อื่น ให้เจ้าของเดิมจบงาน CUA ตามข้อกำหนด `completion_summary` และจบเทิร์นเพื่อปล่อยแท็บ ก่อนตัวถัดไปรับต่อ
- การส่งข้อความว่า handoff อย่างเดียวไม่ปล่อยแท็บ ไม่ปิดแท็บของผู้ใช้เพื่อแก้ปัญหานี้
- ไม่ตรึง browser ID หรือ element index จากคู่มือ; ค้นจาก inventory/state ใหม่
