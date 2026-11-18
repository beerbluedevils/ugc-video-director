# Execution time and handoffs

## Read once per owner and phase

Coordinator reads AGENTS.md, config, workflow.md and state.md once, plus the selected job/run once. Read only the current phase reference; recovery.md is conditional on an actual failure. The assigned browser agent reads browser.md/sheets.md for preparation and flow.md/tiktok.md for its continuation. The content agent reads director.md, installed Director v3 and ImageGen instructions. Coordinator uses their returned evidence; it does not reread their full phase manuals or repeat their reviews. Tool-mandated documentation still applies. Re-read only changed instructions, missing facts or documented recovery. Batch independent local reads in one call; request bounded fields instead of printing full jobs or all prior runs. Search reservations only for the requested date.

## Two agents, three phase assignments

Invoke the required browser agent once with gpt-6-luna/medium, then the content agent once with gpt-6.2-sol/low, then resume the same browser agent with followup_task. Do not spawn replacement agents or perform model tests. Browser preparation releases CUA before returning Image Ready. Content does not control Chrome. Preserve serial product execution and existing authorizations.

Each assignment supplies projectRoot, runPath, jobPath, tempPath, exact ProductId/variant, endpoint, permissions, procedure paths, existing completion evidence and stopping point in one message. Resolve these absolute paths once. Capture a local clock timestamp immediately before dispatch; capture the returned task handle and result receipt. Missing provider telemetry remains an explicit limitation.

Each agent writes its phase evidence and returns only stage, changed artifact paths, essential observations/limitations, timing and blockers. Merge invocation evidence and run outcome in one local update before the next handoff, using update_job.py validation once. Do not print/read the whole job, ask for bookkeeping confirmation, or perform another creative/UI review. Return immediately when the phase threshold is met. Coordinator may read named missing fields only. Progress messages are not completion gates.

## Download without a blocking event wait

Use flow.md's preset Downloads directory procedure as the primary result path. Capture its existing filenames immediately before the one 720p export click. Do not register or await a download event for this export; do not use the previous 120-second event timeout. After the click, inspect the directory for the new file and unfinished downloads. If pending, yield with a short wait (2–5 seconds) and check the same operation; do not block a tool call for more than 10 seconds merely waiting for a download. Once a new completed MP4 is identifiable and no matching unfinished download remains, inspect it once with the documented inspector and move to the canonical path. Size stability alone is not completion evidence. If multiple new files make identity ambiguous, inspect only the missing identity evidence using the documented UI/filesystem route. Never click download again because a poll is slow. A pending export is not a failed generation. Actual Save As, transport errors and safety blocks retain documented recovery rules.

## Timing in job.json

Start timing when the request begins, before instruction reads; finish after final local persistence. Each agent records timezone-aware local timestamps at existing phase boundaries, in the same updates as phase evidence. Timing is bookkeeping, not a new UI check. Keep `timing` in job.json and a compact total in the run. On resume append a session; never overwrite old measurements or manufacture historical timestamps.

`timing.sessions[]` contains `runId`, `startedAt`, `completedAt`, `phases`, `flowGenerationWaits`, `wallSeconds`, `excludedFlowWaitSeconds`, `countedSeconds`, `targetSeconds: 300`, `targetMet` and `limitations`. A phase contains `name`, `startedAt`, `completedAt`, `elapsedSeconds`, `owner`, and optional `delayReason`. Use phases: instructions_scope, product_preparation, content_handoff, storyboard_prompt, browser_handoff, flow_setup, flow_generation, download_inspection, tiktok_preflight, tiktok_upload, tiktok_form_submit_verify, persistence. Record tool/upload/ImageGen waits within their phase; only Flow generation waits are excluded. Include every attempt's generation wait once; pending intervals stay open until an observed result or a recorded stop. Count coordinator/agent dispatch and idle gaps; do not sum overlapping phase durations to calculate totals.

`wallSeconds = completedAt - startedAt`; `excludedFlowWaitSeconds` is the union of recorded Flow generation intervals clipped to this session; `countedSeconds = wallSeconds - excludedFlowWaitSeconds`. Incomplete timestamps yield null totals with a limitation, never zero. `targetMet` is null for incomplete measurement, otherwise `countedSeconds <= 300`. For an in-progress session report elapsed counted time with its observation time, not a final total. Once persisted, do not reread unchanged evidence just to confirm timing.

For the interval from Video Ready to TikTok upload, record these boundaries as they occur and persist them with the preflight result in `timing.tiktokPreflight`:

| Field | Capture at |
|---|---|
| `videoReadyAt` | The verified video is recorded as ready |
| `browserStartedAt` | The browser agent starts its first TikTok action |
| `postsReadyAt` | The first usable Posts rows or explicit empty state are observed |
| `checksCompletedAt` | The duplicate check and, for scheduling, the slot check are resolved |
| `uploadStartedAt` | The first action to open the upload form |

These boundaries separate handoff time, browser setup/page readiness, Posts and draft checks, and the transition to upload. Reuse the existing observation times. For previously completed checks or steps skipped at an observed stop, record null for unavailable boundaries and note why. Capture identifiable page waits or recoveries as `delayReason` when observed. Persist the upload boundary with the existing upload-start update.

Planning budgets (seconds): instructions/scope 15; product preparation 35; both handoffs and persistence 15; storyboard/prompt including ImageGen 90; Flow setup 30; download/inspection 20; TikTok preflight/upload/form/verification 95. Total 300. These are budgets, not timeouts or reasons to skip required evidence. At a boundary exceeding its budget, record the observed delay reason; continue the authorized operation safely. Final report states actual counted time, excluded Flow wait and the slowest measured phase if the target was missed. Never promise five minutes until measured on a real run.
