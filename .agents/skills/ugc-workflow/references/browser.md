# Browser setup

Follow [execution.md](execution.md) for one-time phase reads, compact handoffs and timing recorded with existing evidence.

Apply [workflow.md — Minimum evidence and mandatory advance](workflow.md#minimum-evidence-and-mandatory-advance) for sufficient evidence and immediate progression. Repeated checks in this procedure use the same recorded observation; they are not new review gates. Inspect again only the named missing, changed or conflicting fact, or the documented recovery condition.

Use mcp__cua_repl only for UI. Read its current documentation; the APIs here are examples, not a substitute. The Chrome profile is Sirawit; discover current browser/tab IDs and element indices. No parallel browser owners.

## 2. เริ่ม session และรับแท็บเดิม

### ใช้เส้นทางปุ่มที่รู้แล้วในทุก session

- อ่านคู่มือ phase หนึ่งครั้ง แล้วใช้เส้นทางนี้ต่อทันที จับคู่ label จริงกับ state ปัจจุบัน ไม่ใช้ element index หรือพิกัดเก่าข้าม session
- Sheets: Tiktok → ช่องชื่อ → ช่วง/เซลล์ → อ่าน clipboard/formula bar ตาม sheets.md
- Flow: โปรเจ็กต์ → ตั้งค่า Video / Omni 1.2 Flash / Elements / 9:16 / 360p / 10 วินาที / x1 → เพิ่มองค์ประกอบ → อัปโหลดสื่อ (เตรียม filechooser ก่อนคลิก) → storyboard.png → เพิ่มไปยังพรอมต์ → videoPrompt → Generate → preview คลิปเดิม → ดาวน์โหลดสื่อ → 720p ตาม flow.md
- TikTok: Upload → Select video → Description → Add link / Product → ค้น ProductId และ apply → เลือกตรง ID → ชื่อสั้น → Add → Settings / When to post / Schedule → วัน เวลา timezone → Reuse OFF / AI-generated ON / Content check lite OFF → Schedule ครั้งเดียว → Posts / Search for post description → อ่านแถวผลลัพธ์ ตาม tiktok.md
- ใช้ state เพื่อจับปุ่มถัดไปและตรวจผลที่จำเป็น เมื่อหลักฐานครบให้ทำขั้นถัดไปทันที ไม่ถาม coordinator ยืนยันปุ่มหรือขออนุมัติขั้นเดิมอีก
- ถ้า label เปลี่ยน ให้หาเฉพาะปุ่มหน้าที่เดียวกันในหน้าปัจจุบัน ถ้าปุ่มหายจริง หลักฐานขัดกัน หรือเกิด error ให้ใช้ recovery ที่ระบุ ไม่สำรวจหน้าอื่นหรืออ่านคู่มือทั้งชุดซ้ำ

1. อ่าน skill, workflow reference และ config และ `job.json` ของสินค้าที่จะทำก่อนเปิดฟอร์มหรือกดสร้าง
2. เปิดอ่านคำแนะนำล่าสุดของเครื่องมือ browser control ตามข้อกำหนดเริ่มต้นของเครื่องมือ ถ้าต้องดูรายการแอป/เบราว์เซอร์ ใช้ `await cua.getState()` เป็นคำสั่งแรกตามเอกสารเครื่องมือ
3. เลือก Chrome จาก inventory แล้วตั้งชื่อ browser session เช่น `🔎 UGC workflow` ก่อนรับแท็บมาควบคุม ตาม API ที่เครื่องมือประกาศ
4. แสดงรายการแท็บปัจจุบัน เลือกแท็บจากชื่อและ URL จริง ไม่ใช้ tab ID ของ pilot เป็นค่าถาวร
5. รับแท็บเดิมผ่าน `cua.getTab(...)` ใช้ initial state ที่เครื่องมือคืนมาได้เลย ไม่เรียก snapshot เพิ่มถ้ามีข้อมูลครบ; หากไม่มี state จึงอ่าน accessibility state; หากข้อมูลไม่พอ ใช้ DOM snapshot ผ่าน API ของ browser control ที่ประกาศไว้ หรือ screenshot
6. อ่านสถานะหน้าเว็บก่อนกด ใช้ชื่อปุ่ม/label ที่พบจริง หมายเลของค์ประกอบต้องมาจาก state ล่าสุดเท่านั้น ใช้ผลที่เครื่องมือคืนจากการกระทำนั้นตรวจผลได้เลย ถ้ายังขาดหลักฐานจึงอ่าน state เพิ่มหนึ่งครั้ง หากหลักฐานครบให้ทำขั้นถัดไปทันที ใช้ DOM หรือ screenshot เพิ่มเฉพาะเมื่อข้อมูลที่จำเป็นยังขาด ห้ามตรวจข้อเท็จจริงเดิมซ้ำเพื่อความมั่นใจ ดู completion rules ใน workflow.md

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

## Required browser model and evidence

Before any production browser control (Sheets, product page, Flow or TikTok), the coordinator invokes one serial browser subagent with collaboration.spawn_agent, task_name="ugc_browser", fork_turns="none", model="gpt-6-luna", reasoning_effort="medium" (Luna 6 Medium). Pass the canonical workflow/config paths, exact product IDs, run/job paths, authorization limits and current stage. Only this agent owns Chrome and calls mcp__cua_repl. The coordinator handles local coordination/state and does not take over production browser actions with another model. Release CUA before any handoff; the content agent must not control Chrome.

Store job.actualModelEffort.browserExecution with model, reasoningEffort, invocationTool, actual invocationArguments, returned agentId/taskName, startedAt, completedAt and resultEvidence tying the agent result to the actual browser steps and UI observations. Preserve the tool response and agent result, not just config values or a self-declared model name. A successful selection proves the requested invocation; it does not expose internal provider telemetry. A model-only test without browser actions is not evidence of production browser execution.

If that exact selection is rejected, retain the error and report the affected step; do not silently substitute the coordinator, another model or effort. For the content handoff, the browser owner records current product facts/reference through the documented product-image procedure, releases CUA as required, then resumes only after the required Sol content result is available. Do not create new products or repeat external actions to obtain model evidence for an already completed job.

## Invocation bookkeeping without a pause

Apply workflow.md's coordinator-owned evidence rule. A returned canonical task name is a valid agent handle; an opaque ID is not additionally required. The coordinator records local dispatch and result-receipt times as startedAt/completedAt with timestampSource, clearly distinguished from provider timestamps. If a historical time was not captured, use null and a limitation rather than asking the agent or inventing a time. Agents return their actual phase result and artifacts without waiting for bookkeeping replies. The coordinator merges invocation evidence after the result and before the next handoff; no second UI or creative review is required. A failed spawn or genuinely absent handle/result still stops dependent work.
