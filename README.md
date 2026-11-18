# UGC Video Director Workflow

Workflow สำหรับเลือกสินค้า → UGC Video Director v3 → Google Flow → TikTok ทำได้ทั้งรายการเดียวและ batch ทีละสินค้า

## โครงสร้าง

```text
.agents/skills/ugc-workflow/
  SKILL.md
  agents/openai.yaml
  references/
    workflow.md
    director.md
    browser.md
    sheets.md
    flow.md
    tiktok.md
    recovery.md
    state.md
AGENTS.md
config/workflow.json
schemas/job.schema.json
scripts/
  validate_job.py
  update_job.py
  inspect_video.py
requirements.txt
```

- `AGENTS.md` เป็นกติกาของ repo และชี้ไปยัง skill หลัก
- `ugc-workflow` คุมลำดับงาน เรียก **ugc-video-with-cute-effect-v3 จาก plugin ugc-video-director ที่ติดตั้ง** เพื่อสร้าง storyboard และ video prompt ไม่คัดลอก skill v3 มาซ้ำใน repo นี้
- `config/workflow.json` เก็บค่าร่วมและโมเดลที่ต้องการ ตรวจบัญชี ชีต Chrome profile และ download location ให้ตรงเครื่องก่อนใช้ ค่า config ไม่ใช่การอนุญาตโพสต์
- `schemas` และ `scripts` ใช้ตรวจ/อัปเดต job และอ่าน metadata วิดีโอ ไม่แทนการตรวจผลจริงใน UI
- `ugc-automation-workflow.md` และ `browser-runbook.md` เป็นลิงก์ทางเข้าจากชื่อไฟล์เดิม ไม่ใช่คู่มือซ้ำอีกชุด

## เริ่มใช้งาน

1. เปิด repo นี้เป็น workspace ใน Codex และอ่าน `AGENTS.md`
2. ต้องมี UGC Video Director v3, เครื่องมือสร้างภาพ และ browser control `mcp__cua_repl` พร้อม Chrome ที่ล็อกอินบริการที่เกี่ยวข้อง หาก dependency ไม่พร้อมให้หยุดขั้นที่ต้องใช้ ไม่เปลี่ยนเป็น v4 อัตโนมัติ
3. ติดตั้งตัวช่วยท้องถิ่นด้วย `python -m pip install -r requirements.txt` เมื่อจะใช้สคริปต์ตรวจ job/วิดีโอ หากมี ffprobe จะใช้ก่อน imageio-ffmpeg
4. เรียก `$ugc-workflow` หาก session ค้นพบ project skill แล้ว หรือสั่งให้อ่าน `.agents/skills/ugc-workflow/SKILL.md` โดยตรง

ตัวอย่างรายการเดียว:

```text
ใช้ $ugc-workflow ทำ PID ที่ฉันระบุ ตั้งแต่เตรียมสินค้าไปจนถึง
อัปโหลดและตั้งเวลา TikTok พร้อมอัปเดตชีต Done หลังยืนยัน Scheduled
ตรวจงานเดิมก่อนและทำต่อเฉพาะขั้นที่ยังไม่เสร็จ
```

ตัวอย่าง batch:

```text
ใช้ $ugc-workflow ทำ 3 รายการแรกที่เป็น In Progress ในแท็บ Tiktok
สร้างและดาวน์โหลด 720p เท่านั้น ไม่อัปโหลด TikTok และไม่แก้ชีต
```

## ข้อกำหนดสำคัญ

- Flow อัปโหลดเฉพาะ storyboard.png; สร้าง 360p / 10 วินาที / 9:16 / x1 แล้วดาวน์โหลด 720p
- รอ filechooser ก่อนคลิก upload แล้วใช้ setFiles ด้วย absolute path ตรวจ upload สำเร็จและ Elements chip
- ตรวจผลการสร้างทุกครั้ง retry เฉพาะงานที่ยืนยันว่าล้มเหลว อีกไม่เกิน 3 ครั้งหลังรอบแรก หากยังล้มเหลวให้หยุดทั้ง batch และแจ้งผู้ใช้
- ตรวจ Ask where to save = OFF และ download location ของโปรไฟล์ปัจจุบัน หาก Save As ปรากฏให้หยุด ไม่กดดาวน์โหลดซ้ำ
- TikTok ต้องได้รับอนุญาตตามปลายทางจริง เวลาเลือกจาก 11:00 / 14:00 / 17:00 Asia/Bangkok โดยตรวจเวลาว่างจริง
- Reuse OFF / AI-generated ON / Content check lite OFF; Sheet Done ต้องมีแถว Scheduled ที่ตรวจยืนยันแล้ว

## ข้อมูลขณะรัน

repo root คือ project root ของสำเนานี้ ไม่ชี้กลับไปใช้ output ของโฟลเดอร์แม่โดยอัตโนมัติ

สร้างตามความจำเป็นในเครื่องและไม่ติดตามด้วย Git:

- `output/<ProductId>/`: storyboard.png, <ProductId>.mp4, tiktok_caption.txt, job.json เท่านั้น
- `runs/<RunId>.json`: ขอบเขตและสรุปแต่ละรอบ
- `temp/<RunId>/<ProductId>/`: ไฟล์ทำงานชั่วคราว
- `archive/`: ประวัติท้องถิ่นถ้ามี

**ไม่ได้คัดลอก output, runs, temp, archive หรือไลบรารีที่ติดตั้งไว้จากโปรเจกต์เดิม** ประวัติงานเดิมยังอยู่ใน `D:\ugc` ดังนั้นอย่าถือว่าไม่มี job ใน repo นี้แล้วทำสินค้าเดิมซ้ำ ต้องตรวจชีต/Posts หรือรับช่วง job เดิมอย่างตั้งใจก่อนเริ่ม

Skill ส่วนตัวที่ติดตั้งไว้เดิมยังชี้ไปโปรเจกต์เดิม การจัด repo รอบนี้ไม่เปลี่ยนการเชื่อมต่อนั้น หากใช้สำเนา repo ให้เปิด workspace นี้และระบุ skill path นี้เพื่อเลือกให้ถูก

## ตรวจสอบท้องถิ่น

```text
python scripts/validate_job.py output/<ProductId>/job.json
python scripts/inspect_video.py output/<ProductId>/<ProductId>.mp4
python scripts/update_job.py output/<ProductId>/job.json --patch-file temp/patch.json
```

ทั้งสอง job เดิมและขั้นตอน upload/download เคยตรวจในเครื่องแล้ว แต่ repo นี้ไม่ได้แนบประวัติ/หลักฐานเหล่านั้น และยังไม่รับรอง batch หรือ Luna medium แบบครบกระบวนการ ข้อความนี้บอกขอบเขตการทดสอบในอดีต ไม่ใช่เงื่อนไขให้หยุดถามหรือทดสอบโมเดลเพิ่ม งานปัจจุบันใช้ Luna medium ตาม workflow และทำต่อทันทีเมื่อหลักฐานครบ
