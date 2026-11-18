# UGC project

- Use concise, straightforward wording.

## STRICT CONSTRAINT — documented execution only

These requirements are mandatory for the coordinator and every subagent. They are not preferences.

1. MUST execute the canonical skill's documented procedure, including initialization and any documented separate API surface, in the specified order. MUST read and follow the current tool documentation required by that procedure.
2. MUST NOT infer that a tool/capability is unavailable because a method, object, binding or namespace is absent from the currently selected surface. MUST complete the documented route for obtaining that capability first.
3. MUST NOT declare a blocker, stop the batch or ask the user to perform the step based on an assumption, incomplete documentation reading or an untried documented route. A blocker requires an actual failed documented step or an explicitly missing required dependency, with concrete evidence recorded in the job: exact step, actual invocation when attempted, verbatim returned error or explicit capability/dependency evidence, and applicable documented recovery result. MUST NOT fabricate an invocation or error.
4. MUST use only the canonical workflow's authorized tools and recovery routes. These constraints do not authorize bypassing tool restrictions, safety/login blocks, authorization limits or higher-priority instructions.
5. MUST advance immediately when the workflow's required evidence is complete. MUST NOT add approval gates, repeat completed checks or substitute a speculative limitation report for the next authorized action.
6. MUST NOT send retrospective self-commentary or excuses, including “I concluded the tool was unavailable too quickly” or equivalent wording. Correct the execution and continue. User-facing progress must state concrete observed results and the next authorized action; report a genuine blocker only with the evidence required above.

## Workflow requirements
- For UGC production or resuming jobs, read `.agents/skills/ugc-workflow/SKILL.md` and follow its linked references. It is the canonical workflow; `config/workflow.json` holds shared settings and each `job.json` holds actual state.
- UGC Video Director v3 in the installed plugin is the creative core. Discover/read it in the session; do not copy it, substitute v4, or treat it as an API. Missing dependencies stop dependent work.
- Handle selected products and batches sequentially. Only one agent controls Chrome at a time. Use Codex browser control through `mcp__cua_repl`, not the old Playwright MCP extension.
- Do not generate, download, upload or schedule duplicates. Existing state must be checked first. No TikTok upload/scheduling, sheet mutation, or new products beyond the user's actual authorization.
- Upload only storyboard.png to Flow. Generate 360p; download 720p. Three generation retries after the initial attempt; stop the whole run and notify on exhaustion. Safety/login blocks stop immediately.
- Product output contains only storyboard.png, <ProductId>.mp4, tiktok_caption.txt and job.json. Keep metadata, prompts, verification and summary in job.json. Working files belong in temp, historical material in archive.
- Content creation requires gpt-6.1-sol with low reasoning effort only, with actual invocation and returned-agent evidence in job.json as specified in director.md. Browser execution requires gpt-6-luna with medium reasoning effort only, with invocation and returned-agent evidence as specified in browser.md. Product preparation model config expresses a preference; config is not proof of tool availability or permission. Use actual current UI and exact ProductId strings. Preserve prior errors, status evidence and authorization limits.
- Archive is historical material, not current instructions. Do not load archived plugin skills as a substitute for the installed v3.

- Follow the canonical workflow and its documented tools/recovery only; do not add steps or API/tool calls beyond it. Required tool documentation and higher-priority rules still apply.
- Apply `.agents/skills/ugc-workflow/references/workflow.md` completion and no-repeat rules to every coordinator and subagent. Required evidence complete means record once and advance; do not add checks, blockers, reviews or approval pauses. Recheck only affected facts with an actual change, conflict, missing required evidence or documented recovery.
- Chrome Downloads is user-preset; do not inspect or change Ask where to save or Location, or request reconfirmation. Check the actual downloaded file as documented.
