---
name: ugc-workflow
description: Run or resume this project's UGC product workflow for selected products or a sequential batch, using UGC Video Director v3 for storyboard and video prompts, Google Flow for video, and explicitly authorized TikTok uploads or scheduling.
---

# UGC workflow

Project root: the repository containing this skill (`.agents/skills/ugc-workflow`), `AGENTS.md` and `config/workflow.json`. Resolve it from the skill location, not the shell working directory; `<projectRoot>` below denotes that absolute path. Relative `projectRoot` in config resolves against the repository root. This skill coordinates work; **UGC Video Director v3 is the required creative core**, not an API. Do not duplicate its creative instructions here or silently substitute v4.

1. Read `<projectRoot>/AGENTS.md`, `<projectRoot>/config\workflow.json`, and [workflow.md](references/workflow.md). Resolve the requested product list, batch limit and authorized endpoint before side effects. A batch is sequential, never concurrent browser control.
2. Read each selected `output/<ProductId>/job.json` and the run record. Reconcile existing files and actual external state before generating, downloading, uploading or scheduling again. Completed jobs are skipped unless the user explicitly requests a new version. Preserve test-only restrictions on existing jobs unless the user explicitly changes them.
3. Product preparation: read [sheets.md](references/sheets.md). Store source data in job.json; keep the real product image in temp only.
4. Content creation: read [director.md](references/director.md), then locate and read the installed skill **ugc-video-with-cute-effect-v3** from the **ugc-video-director** plugin in the session's available-skills catalog. Read the image generation skill as required. If v3 or image tools are unavailable, record the blocker and stop dependent work; never claim a storyboard was created from a prompt alone.
5. Flow: read [browser.md](references/browser.md) and [flow.md](references/flow.md) before UI actions. Upload **storyboard.png only**. Create at 360p, download 720p. Check every result. Three retries after the initial attempt means at most four generation attempts; persist counts across sessions. Confirm failure before retrying; pending/unknown is not failed.
6. Only when explicitly authorized for that endpoint, read [tiktok.md](references/tiktok.md) and upload/schedule. Upload alone does not authorize posting. Sheet Done requires a verified Scheduled row. If scheduling succeeded but Sheets failed, resume only the sheet update.
7. Read [state.md](references/state.md) for updates and [recovery.md](references/recovery.md) for failures. Update job and run summaries with actual observations and timezone-aware times; never clear prior errors/retries. On exhausted retries stop the whole run, including a batch, and notify the user.

Permanent product output is exactly `storyboard.png`, `<ProductId>.mp4`, `tiktok_caption.txt`, `job.json` (only files actually produced). Store both prompts, metadata, checks and limitations in job.json. Use `temp/<RunId>/<ProductId>` for working images and screenshots. Clean only the current run's owned temporary files after their required results have been recorded; preserve a screenshot temporarily if it must be shown in the final reply.

Model preferences are in config. The main agent owns coordination and may perform the steps directly; when following the configured split, delegate serially with the actual configured model/effort and record the actual selection. If unavailable, explain the limitation instead of claiming a model was used. Only one agent controls Chrome; finish/release CUA before handing off a tab. No custom agent definitions or recurring automation are required by this skill.

Validation helpers (local files only): `python <projectRoot>/scripts\validate_job.py <job.json>`; `python <projectRoot>/scripts\inspect_video.py <video.mp4>`. These do not validate live UI or authorize external actions. A schema pass is not proof of a successful post.
