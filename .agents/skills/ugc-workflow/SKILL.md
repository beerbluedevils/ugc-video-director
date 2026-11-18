---
name: ugc-workflow
description: Run or resume this project's UGC product workflow for selected products or a sequential batch, using UGC Video Director v3 for storyboard and video prompts, Google Flow for video, and explicitly authorized TikTok uploads or scheduling.
---

# UGC workflow

Project root: the repository containing this skill (`.agents/skills/ugc-workflow`), `AGENTS.md` and `config/workflow.json`. Resolve it from the skill location, not the shell working directory; `<projectRoot>` below denotes that absolute path. Relative `projectRoot` in config resolves against the repository root. This skill coordinates work; **UGC Video Director v3 is the required creative core**, not an API. Do not duplicate its creative instructions here or silently substitute v4.

## Daily quantity

Users may specify videos per day (for example, “วันละ 2 วิดีโอ”). Default to `config.batch.defaultVideosPerDay` = 3 when omitted. Resolve total selected products and authorized dates separately; an explicit single product remains one video. Apply [workflow.md — Daily quantity](references/workflow.md#daily-quantity) before selecting a batch or scheduling.

## Runtime target

Target at most 300 seconds per video excluding only confirmed Flow generation waits. Follow [execution.md](references/execution.md) for one-time reads, compact agent handoffs, download polling and phase timing. This is a measured target, not permission to omit checks or claim completion.

## Mandatory execution boundary

For every new session, use the known button routes in [browser.md](references/browser.md) and the completion/no-repeat rules in workflow.md. Use workflow.md’s “Minimum evidence and mandatory advance” table as the sufficient completion threshold for every phase. Once its facts are recorded, advance immediately within authorization; agents must not add checks or approval questions. Routine UI actions and invocation bookkeeping must not become coordinator approval pauses.

Execute only the numbered workflow steps and their linked procedures. Do not add a step, prerequisite, blocker, verification, project, tool, or recovery method based on personal judgment. Resolve current UI labels only to perform the documented action. Apply the completion rules in [workflow.md](references/workflow.md#completion-and-no-repeat-rules) to every step; these rules consolidate existing checks and do not add checks. Pass this boundary and the completion rules to both required subagents. A coordinator's uncertainty is not evidence that a completed step must be repeated.

Follow this SKILL.md and its linked references in order. Use only the tools/methods explicitly specified there or required by their linked installed skills and the current documentation of those specified tools. Do not invent extra checks, URL checks, API calls, tool discovery, alternative integrations or recovery steps. Current UI labels may be resolved using the specified browser controls; that is part of the documented step. Tool documentation explains how to execute a listed step; it does not authorize adding unrelated steps. Follow explicit user instructions and higher-priority tool/safety requirements; record an actual tool rejection verbatim in job.errors instead of inventing a blocker. Use only documented recovery paths. If none applies, report the exact failed step and evidence; do not substitute a new workflow.

Chrome Downloads is user-preset: Ask where to save = OFF, Location = config.browser.downloadLocation. Do not open Settings, recheck ON/OFF, change these settings or request reconfirmation. Continue with the documented one-download and file-result checks.

1. Read `<projectRoot>/AGENTS.md`, `<projectRoot>/config\workflow.json`, and [workflow.md](references/workflow.md). Resolve the requested product list, batch limit and authorized endpoint before side effects. A batch is sequential, never concurrent browser control.
2. Read each selected `output/<ProductId>/job.json` and the run record. Reconcile existing files and actual external state before generating, downloading, uploading or scheduling again. Completed jobs are skipped unless the user explicitly requests a new version. Preserve test-only restrictions on existing jobs unless the user explicitly changes them.
3. Product preparation: read [sheets.md](references/sheets.md). Store source data in job.json; keep the real product image in temp only.
4. Content creation: read [director.md](references/director.md), then locate and read the installed skill **ugc-video-with-cute-effect-v3** from the **ugc-video-director** plugin in the session's available-skills catalog. Read the image generation skill as required. If v3 or image tools are unavailable, record the blocker and stop dependent work; never claim a storyboard was created from a prompt alone.
5. Flow: read [browser.md](references/browser.md) and [flow.md](references/flow.md) before UI actions. Upload **storyboard.png only**. Create at 360p, download 720p. Check every result. Three retries after the initial attempt means at most four generation attempts; persist counts across sessions. Confirm failure before retrying; pending/unknown is not failed.
6. Only when explicitly authorized for that endpoint, read [tiktok.md](references/tiktok.md) and upload/schedule. Upload alone does not authorize posting. Sheet Done requires a verified Scheduled row. If scheduling succeeded but Sheets failed, resume only the sheet update.
7. Read [state.md](references/state.md) for updates and [recovery.md](references/recovery.md) for failures. Update job and run summaries with actual observations and timezone-aware times; never clear prior errors/retries. On exhausted retries stop the whole run, including a batch, and notify the user.

Permanent product output is exactly `storyboard.png`, `<ProductId>.mp4`, `tiktok_caption.txt`, `job.json` (only files actually produced). Store both prompts, metadata, checks and limitations in job.json. Use `temp/<RunId>/<ProductId>` for working images and screenshots. Clean only the current run's owned temporary files after their required results have been recorded; preserve a screenshot temporarily if it must be shown in the final reply.

Content model is mandatory: **gpt-6.2-sol / reasoning_effort low only** for product creative analysis, storyboard design/generation instructions, narration, caption and video prompt. Follow the invocation and evidence requirements in [director.md](references/director.md). The main agent coordinates; it must not substitute its own content generation without evidence of the required selection. Browser execution is mandatory: **gpt-6-luna / reasoning_effort medium only**, using the invocation and evidence procedure in [browser.md](references/browser.md). Only productPreparation remains a model preference. Only one agent controls Chrome; finish/release CUA before handing off a tab. No custom agent definitions or recurring automation are required by this skill.

Validation helpers (local files only): `python <projectRoot>/scripts\validate_job.py <job.json>`; `python <projectRoot>/scripts\inspect_video.py <video.mp4>`. These do not validate live UI or authorize external actions. A schema pass is not proof of a successful post.
