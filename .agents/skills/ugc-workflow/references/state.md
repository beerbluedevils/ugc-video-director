# State, output and maintenance

Schema: `<projectRoot>/schemas\job.schema.json`. Shared config: `<projectRoot>/config\workflow.json`. Config is not authorization. Use a new run record for each user request; preserve job history across runs. New jobs start at Preparing with empty generationAttempts and retryCount 0.

Stages: Preparing → Image Ready → Storyboard Ready → Generating → Video Ready → TikTok Uploading → TikTok Uploaded (only if observed) → TikTok Scheduling → Scheduled — Pending Sheet Update → Completed. Generation Failed and Blocked are explicit terminal/attention states for a run; resuming requires resolving the blocker and respecting remaining retries.

Write job before a generation attempt with attempt number/start time, and after with result/completion time/error. retryCount counts attempts started after the initial attempt, not status polls. Atomic update helper: `python <projectRoot>/scripts\update_job.py <job.json> --patch-file <patch.json>`; patch is a top-level replacement per supplied key, preserves other keys, validates before atomic replace. For history arrays supply the complete retained array, never only the newest entry. Create patch files in temp; the helper does not make external state true.

Existing legacy jobs may have no structured generationAttempts even though a video exists. That means history was not recorded, not that zero attempts occurred. Do not generate again or invent attempt details to fill the gap; reconcile actual assets first. A new generation version requires an explicit new-version request and a separately identified history; never reset counters in an existing generation sequence.

Store current fields and observations, including stage, productId string, workflowVersion, updatedAt with timezone, productMetadata, prompts, Flow project/asset, paths, actual model/effort, generationAttempts, retryCount, videoInspection, verification, errors, summary and optional TikTok/sheet details. Keep unknown/not-checked explicit. Retain legacy fields when migrating; do not reinterpret old successes as current test results.

Only four permanent product files: storyboard.png, <ProductId>.mp4, tiktok_caption.txt, job.json. Missing unfinished assets stay absent. Canonical output paths remain stable. Work images/screenshots/reports go under temp/<RunId>/<ProductId>; record findings in job before cleaning owned temp. Do not delete arbitrary Downloads or other runs. Legacy supporting files live in archive and are linked from legacyArtifacts when needed.

Inspect metadata with inspect_video.py when ffprobe or imageio_ffmpeg is available. It reports metadata only, not visual fidelity or speech correctness. Record actual visual/audio checks separately. Validate jobs before side effects and after writing. Use Git for maintained instructions/config/scripts, excluding output, runs, temp, archive and local tool dependencies. No credentials in config or source control.

Verified history: PID-047 / ProductId 1731411374901070843 was Scheduled for 2026-11-15 17:00 +07:00, post 7708003835293306132, sheet row 49 Done. Do not repeat. ProductId 1729583039542102625 is test-only Video Ready; no TikTok or sheet writes authorized by that historical test. Its storyboard upload and automatic 720p download passed in Sirawit on 2026-11-14, same SHA-256 as the original. Luna medium, multi-item batch recovery and unattended recurring runs have not been verified end to end. Use live state for all future schedule choices.

The existing local tools/python library is not bundled. Install requirements.txt in the Python environment or provide ffprobe. Historical job/output/archive files are not bundled; never infer that an empty local output means a product has never been scheduled. Reconcile live Posts and Sheets before starting.
