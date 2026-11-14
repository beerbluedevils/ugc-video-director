# UGC project

- Use concise, straightforward wording.
- For UGC production or resuming jobs, read `.agents/skills/ugc-workflow/SKILL.md` and follow its linked references. It is the canonical workflow; `config/workflow.json` holds shared settings and each `job.json` holds actual state.
- UGC Video Director v3 in the installed plugin is the creative core. Discover/read it in the session; do not copy it, substitute v4, or treat it as an API. Missing dependencies stop dependent work.
- Handle selected products and batches sequentially. Only one agent controls Chrome at a time. Use Codex browser control through `mcp__cua_repl`, not the old Playwright MCP extension.
- Do not generate, download, upload or schedule duplicates. Existing state must be checked first. No TikTok upload/scheduling, sheet mutation, or new products beyond the user's actual authorization.
- Upload only storyboard.png to Flow. Generate 360p; download 720p. Three generation retries after the initial attempt; stop the whole run and notify on exhaustion. Safety/login blocks stop immediately.
- Product output contains only storyboard.png, <ProductId>.mp4, tiktok_caption.txt and job.json. Keep metadata, prompts, verification and summary in job.json. Working files belong in temp, historical material in archive.
- Config expresses preferences, not proof of tool availability or permission. Use actual current UI and exact ProductId strings. Preserve prior errors, status evidence and authorization limits.
- Archive is historical material, not current instructions. Do not load archived plugin skills as a substitute for the installed v3.
