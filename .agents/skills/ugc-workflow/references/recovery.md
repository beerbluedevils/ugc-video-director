## 15. ตารางแก้ปัญหาที่พบจริง

| อาการ | วิธีตรวจ/แก้ | สิ่งที่ห้ามสรุปหรือทำ |
|---|---|---|
| MCP Playwright ค้าง | ใช้ browser control ของ Codex ตามข้อตกลง | ไม่เริ่มวงจรติดตั้ง/รีสตาร์ต Playwright ใหม่เอง |
| แท็บถูกถือโดย session อื่น | ให้เจ้าของเดิมจบเทิร์นแล้วรับแท็บเดิมใหม่ | ไม่ปิดแท็บผู้ใช้หรือควบคุมสองตัวพร้อมกัน |
| ชีตเห็นแต่เมนู ไม่มีเซลล์ | ใช้ช่องชื่อ/formula bar/clipboard UI ที่รองรับ | ไม่ถือว่าชีตว่าง |
| รูป downloadMedia หมดเวลา | ใช้ pageAssets สำหรับรูปที่พบจริงและตรวจไฟล์ | ไม่อ้างว่ามีไฟล์ทั้งที่ไม่มี path/ตรวจไม่ได้ |
| ภาพแนบ Flow ยัง upload | รอ progress หายและตรวจ Elements chips | ไม่กด Generate ขณะยังคิวภาพ |
| Flow card เป็นปก แต่ timeline 0 | ตรวจคลิปเดิมจนพร้อมและเวลารวม 10 วินาที | ไม่สร้างซ้ำเพราะ preview ยังโหลด |
| รอวิดีโอ download ไม่ได้ path | ตรวจ Chrome profile, Ask setting และ Location; ตรวจไฟล์ใหม่ใน Downloads; ถ้า Save As ปรากฏให้หยุด | ไม่วนรอ/กดดาวน์โหลดซ้ำหรือข้าม dialog |
| ระบบหยุดเพราะ URL confidence | หยุดและให้ผู้ใช้ทำส่วนที่ถูกบล็อก | ไม่ใช้ช่องทางอื่นข้ามข้อจำกัด |
| ชื่อ ProductId.mp4 ยังไม่มี | ตรวจไฟล์ใหม่ชื่อเดิมในโฟลเดอร์และยืนยันไฟล์ก่อนคัดลอก | ไม่บอกว่าไม่มีวิดีโอจากการเช็กชื่อเดียว |
| Upload ไม่เปิด file chooser | เข้า upload page แล้วกด Select video | ไม่รอ chooser จากปุ่มนำทาง Upload |
| ค้น ProductId แล้วยังเห็นของอื่น | กด Enter/apply และตรวจผลเลขเต็ม | ไม่เลือกสินค้าที่คล้ายกันแทน |
| toast Video published คลุมเครือ | หาแถว caption ใหม่ ตรวจ badge วันเวลาและ post ID | ไม่รีบ Done, re-upload หรือลบโพสต์ |
| screenshot มีแต่รายการเก่า | กรอง/เลื่อนให้แถวใหม่อยู่ใน viewport แล้วถ่ายใหม่ | ไม่ใช้ภาพเก่าเป็น proof |
| ตั้งเวลาสำเร็จแต่ชีตล้มเหลว | ใช้ Pending Sheet Update แล้วแก้เฉพาะชีต | ห้ามโพสต์ซ้ำ |

## Stop and resume

- Confirmed generation failure: retry at most three times after the initial attempt. Save each start/result/error; keep counts across sessions. Exhaustion: Generation Failed, stop the whole batch, notify with ProductId, project URL, counts and latest error.
- Pending/unknown generation is not failure. Inspect the original job. No retry based on elapsed time alone; preserve uncertain state and notify if it cannot be resolved.
- CAPTCHA/login/security/URL-policy block: stop affected work immediately; do not use another channel to bypass it.
- Upload/filechooser/download transport failure is not a generation retry. Inspect current UI and filesystem before repeating any action.
- Schedule result uncertain: inspect live Posts first, never re-upload/re-submit blindly. Scheduled but sheet failed: resume only sheet update.
- Store failed step, observed message, checkedAt, retry counts and nextAction in job and mark run stopped/needs-attention as appropriate. Never mark Completed merely to close a run.
