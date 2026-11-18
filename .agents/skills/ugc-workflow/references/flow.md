# Flow generation and download

Apply [workflow.md — Minimum evidence and mandatory advance](workflow.md#minimum-evidence-and-mandatory-advance) for sufficient evidence and immediate progression. Repeated checks in this procedure use the same recorded observation; they are not new review gates. Inspect again only the named missing, changed or conflicting fact, or the documented recovery condition.

Read browser.md first. Settings come from config; explicit project rules below remain mandatory. Do not regenerate Video Ready jobs or download an existing verified file again unless the user requests a test.

## 6. Google Flow — ตั้งค่าและแนบภาพ

### เส้นทางปุ่มที่พบ

1. เลือกแท็บโปรเจ็กต์ Flow ตรวจว่ามีงานเดิมค้าง/คลิปที่สร้างไว้แล้วหรือไม่ก่อนสร้างเพิ่ม
   - ถ้าเป็นงานสินค้านี้ให้ resume ตาม job ห้ามสร้างซ้ำ ถ้าแท็บเป็นงานสินค้าอื่นและ job ไม่มีโปรเจ็กต์ของงานนี้ ให้ใช้ New project ใน UI หนึ่งครั้ง บันทึก URL/เหตุผลแล้วทำต่อ ไม่ถาม coordinator เรื่องการเลือกนี้ ไม่สร้างโปรเจ็กต์เพิ่มเมื่อมีของงานนี้แล้ว
2. บนหน้าคลังโปรเจ็กต์ ใช้ช่อง **คุณต้องการสร้างอะไร** สำหรับ prompt
3. กดปุ่มตั้งค่าข้างช่อง prompt ซึ่งใน accessibility เคยชื่อ **ทริกเกอร์การตั้งค่า** และแสดงข้อความประมาณ `วิดีโอ · 360p · 10 วินาที` กับ `x1`
4. เปิด panel แล้วเลือก/ตรวจ:
   - Video mode
   - Model: **Omni 1.2 Flash** ซึ่งใช้จริงใน pilot
   - Reference mode: **Elements / องค์ประกอบ**
   - Aspect ratio: **9:16**
   - Generation resolution: **360p**
   - Duration: **10 วินาที**
   - Outputs: **x1**
5. อ่านค่าที่เลือกจริงจาก panel หลังแก้ ไม่ถือว่าค่าเดิมตรงตามคู่มือ และไม่เปลี่ยนโมเดลหรือเสียเครดิตสร้างหลายคลิปโดยเงียบ ๆ หากตัวเลือกไม่ตรงให้บันทึกข้อจำกัด

### แนบไฟล์และ prompt — วิธีหลักที่ทดสอบผ่าน

1. ใช้หลักฐาน Storyboard Ready และ path ที่ content agent ส่งมาเป็นผลตรวจว่า `storyboard.png` มีอยู่และเปิดได้ ไม่เปิดตรวจภาพซ้ำเพราะ handoff; ตรวจเพิ่มเฉพาะเมื่อไฟล์หาย/เปลี่ยนหรือหลักฐานขัดกัน รับแท็บจาก inventory ล่าสุด อ่านเอกสาร `file-uploads` ตามข้อกำหนดเครื่องมือก่อนอัปโหลด
2. กด **เพิ่มองค์ประกอบลงในช่องพรอมต์** แล้วอ่านเมนูปัจจุบัน รอบทดสอบพบปุ่ม **อัปโหลดสื่อ**
3. **เตรียมรอ filechooser ก่อนกดปุ่มอัปโหลดในคำสั่งเดียวกัน** แล้วใช้ chooser.setFiles ด้วย absolute path ไม่กดเปิด native dialog ไว้ก่อนแล้วค่อยรอ event ไม่ใช้ locator.setInputFiles ซึ่ง API นี้ไม่ได้ประกาศ

```javascript
const chooserPromise = tab.playwright.waitForEvent('filechooser', { timeout: 10000 });
await tab.playwright.getByRole('button', { name: 'อัปโหลดสื่อ', exact: true }).click();
const chooser = await chooserPromise;
await chooser.setFiles([storyboardAbsolutePath]);
await tab.getAXState();
```

`storyboardAbsolutePath` ต้องเป็น absolute path ของ output/<ProductId>/storyboard.png ใน project root นี้ ไม่ใช่ placeholder ที่ส่งตรงเข้า API ตัวแปร tab ต้องเป็นแท็บที่รับมาจริง และชื่อปุ่มต้องตรง state ล่าสุด หากใช้ input[type=file] ให้ตรวจ DOM ว่ามีจริงก่อนใช้

4. รอ progress ของ storyboard หาย รอบทดสอบเห็น 0% → 37% → การ์ดรูปภาพสำเร็จ จากนั้นเลือก storyboard ที่เพิ่งอัปโหลด แล้วกด **เพิ่มไปยังพรอมต์** ตรวจว่ามี Elements chip รูปเดียวและไม่มีรูปสินค้า การอยู่ในคลังอย่างเดียวไม่พอ
5. หาก chooser timeout ให้ตรวจ state และ native window inventory ก่อน ห้ามกดอัปโหลดซ้ำขณะมี dialog เดิม หากมี Open dialog ค้าง ให้ยกเลิกด้วย UI ที่รองรับแล้วเริ่ม flow ใหม่หนึ่งครั้ง ไม่เดาพิกัดหรือสลับไปติดตั้ง Playwright Extension
6. หาก setFiles ล้มเหลว ให้อ่าน `chrome-file-upload-troubleshooting` และแจ้งข้อความตามเอกสาร สำหรับ Chrome ให้ผู้ใช้เปิด chrome://extensions → Details ของ ChatGPT browser extension → เปิด **Allow access to file URLs** ตาม [คู่มือ](https://developers.openai.com/codex/app/chrome-extension#upload-files) แล้วทดสอบใหม่ ห้ามอ้างว่าสำเร็จเมื่อยังไม่เห็นรูปพร้อม
7. ใส่ `job.json.videoPrompt` ใช้ผลการกรอก prompt และค่าที่อ่านจาก settings ก่อนหน้าเป็นหลักฐาน ไม่เปิด panel ตรวจค่าเดิมซ้ำ แล้วกดเริ่มสร้างตามขอบเขตที่ได้รับอนุญาต การทดสอบอัปโหลดอย่างเดียวไม่กด Generate
8. การ timeout ของ chooser/upload ไม่ใช่ generation retry; บันทึก `fileHandlingVerification` แยกใน job.json

### ตรวจผลการสร้างและ retry

1. อ่าน `generationAttempts` และ `retryCount` ใน job.json ก่อนเริ่มหรือรับช่วงงาน ใช้ผลตรวจ card/คลิปเดิมจาก preflight ในข้อ 6 หากยังไม่มีการสร้างหรือหลักฐานเปลี่ยนแปลง ไม่ตรวจ preflight ซ้ำก่อน Generate
2. บันทึก stage `Generating`, project URL, attempt และเวลาเริ่มจริงทุกครั้ง รอบแรกคือ attempt 1; retry ได้อีกสูงสุด 3 ครั้ง (attempt 2–4) ใช้ยอดสะสมเดิม ไม่เริ่มนับใหม่เมื่อเปลี่ยน session
3. ตรวจ progress/error ของ card เดิมเป็นระยะ หากยัง Pending/Generating หรือ 0% ให้รอและตรวจใหม่ ไม่กดสร้างซ้ำและไม่นับการตรวจสถานะเป็น retry
4. เมื่อ card เปลี่ยนเป็นภาพปก เปิด preview ของคลิปเดิม ตรวจ timeline thumbnail, ระยะเวลารวม **00:10:00** และเล่นได้จริง จึงบันทึกผล attempt เป็น `Completed` และไปดาวน์โหลด 720p; ยังไม่ตั้ง job.stage เป็น Completed เพราะงานยังไม่ถึงปลายทาง ภาพปกหรือ badge `360P` อย่างเดียวไม่ยืนยันความสำเร็จ
5. หาก preview ยังแสดง **00:00:00** ให้ตรวจ progress/error ใหม่ หากจำเป็นปิดแล้วเปิด preview เดิมเมื่อไม่มี unsaved edit ห้ามสรุปล้มเหลวจากเวลาโหลดอย่างเดียว หากยังระบุผลไม่ได้ ให้บันทึกสถานะไม่ชัดเจนและแจ้งผู้ใช้ก่อนสร้างเพิ่ม
6. เมื่อมีหลักฐานชัดว่า Failed/Error ให้บันทึกผลล้มเหลว เวลา ข้อความผิดพลาดและหลักฐานลง `generationAttempts` พร้อมอัปเดต `retryCount` ก่อนพิจารณารอบถัดไป
7. ถ้ายังใช้ retry ไม่ครบ 3 ครั้ง ให้ตรวจอีกครั้งว่าไม่มีงานเดิมกำลังสร้างหรือคลิปสำเร็จ แล้ว retry หนึ่งครั้งด้วย **storyboard.png เท่านั้น** และ prompt/ค่าที่กำหนดเดิม ตรวจ Elements chip พร้อมก่อนกด และกลับไปตรวจผลตามข้อ 3–6 ไม่ส่งหลายรอบพร้อมกัน
8. หาก retry ครั้งที่ 3 ยังล้มเหลว (รวมรอบแรกเป็น 4 attempts) ให้บันทึก stage `Generation Failed`, `retryCount: 3` และข้อผิดพลาดล่าสุด หยุด workflow ไม่ดาวน์โหลด/อัปโหลด/ตั้งเวลา/แก้ชีตหรือเริ่มสินค้าถัดไป แจ้งผู้ใช้พร้อม ProductId, project URL, จำนวน attempts/retries และสาเหตุที่ตรวจพบ
9. CAPTCHA/ล็อกอิน/ข้อจำกัดความปลอดภัยเป็นข้อยกเว้น: หยุดและแจ้งผู้ใช้ทันที ไม่ retry เพื่อข้ามข้อจำกัด แม้ยังใช้โควตาไม่ครบ

เมื่อ preview ของคลิปเดิมเล่นได้และ timeline รวม 10 วินาที ให้จบการตรวจ generation และไปดาวน์โหลดทันที ไม่เปิด preview หรืออ่าน card เดิมซ้ำเพื่อยืนยันความสำเร็จอีก การตรวจภาพ/เสียงตามข้อ 7 ยังทำตามขอบเขตเดิม

## 7. Flow — ดาวน์โหลด 720p และตรวจไฟล์

1. ในหน้า edit ของคลิปเดิมที่พร้อม กดไอคอนดาวน์โหลดด้านบนขวา ชื่อ accessibility ดาวน์โหลดสื่อ
2. เมนูที่พบจริง:
   - 270p GIF ภาพเคลื่อนไหว
   - 360p ขนาดดั้งเดิม
   - **720p เพิ่มความละเอียดแล้ว** (Upscaled/Enhanced)
3. เลือก 720p ของคลิปเดิม ไม่เลือก 360p Original และไม่ถือว่า badge 360P บน editor คือความละเอียดไฟล์ส่งออก
4. ใช้ค่า Downloads ที่ผู้ใช้ preset ไว้แล้ว: Ask where to save = OFF และ Location = config.browser.downloadLocation ห้ามเปิด Settings ตรวจ ON/OFF ซ้ำ เปลี่ยนค่า หรือขอผู้ใช้ยืนยันซ้ำ บันทึกแหล่งค่าเป็น user-preset โดยไม่อ้างว่าได้ตรวจ UI และอ่านรายการไฟล์เดิมในโฟลเดอร์ก่อนดาวน์โหลด
5. เลือกดาวน์โหลด 720p หนึ่งครั้ง แล้วตรวจโฟลเดอร์ที่ preset ว่ามีไฟล์ใหม่ ไม่หยิบ MP4 เก่าจากรายการก่อนหน้า ใช้ filesystem polling ตาม [execution.md](execution.md#download-without-a-blocking-event-wait) โดยไม่รอ download event/timeout 120 วินาที บันทึกเวลา download_inspection ตั้งแต่เริ่ม export จนตรวจไฟล์เสร็จ
6. ตรวจว่าไม่มีไฟล์ .crdownload ขนาดคงที่ และเป็นวิดีโอจริง หาก Save As ปรากฏจริง ให้บันทึกผลและจัดการ dialog ตาม UI/คำสั่งเครื่องมือที่รองรับ หากทำต่อไม่ได้ให้รายงาน dialog ที่ค้าง ห้ามกดดาวน์โหลดซ้ำหรือย้อนกลับไปตรวจ/เปลี่ยน Downloads settings
7. ย้ายไฟล์ใหม่เป็น <projectRoot>/output\<ProductId>\<ProductId>.mp4 เมื่อยืนยันแล้วเท่านั้น; ถ้ามีไฟล์เป้าหมายอยู่ ให้ตรวจของเดิมก่อน ไม่สร้างสำเนาทดสอบใน output และห้ามเขียนทับโดยไม่ตรวจ



After download inspect real dimensions/duration/audio metadata using the documented inspector when available; record actual unavailability as a limitation otherwise. Reuse the visual observations collected in the Flow preview. Record supported audio findings or explicitly mark narration unverified; do not add full playback, frame extraction or transcription as a completion gate. Record all findings/limits in job.videoInspection. Download label alone does not prove file resolution. Never overwrite an existing primary video without checking it. A test copy belongs in temp, not output.
