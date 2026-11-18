# UGC Video Director v3 integration

Follow [execution.md](execution.md) for one-time phase reads, compact handoffs and timing recorded with existing evidence.

Apply [workflow.md — Minimum evidence and mandatory advance](workflow.md#minimum-evidence-and-mandatory-advance) for sufficient evidence and immediate progression. Repeated checks in this procedure use the same recorded observation; they are not new review gates. Inspect again only the named missing, changed or conflicting fact, or the documented recovery condition.

Discover the installed `ugc-video-with-cute-effect-v3` skill under plugin `ugc-video-director` in the current skill catalog. Read its SKILL.md in full when using it. The verified installed package during setup was version 1.2.7, but its cache path is not a permanent interface; discover again in each new session. Do not edit the plugin during production or use archived copies. If the skill is missing, stop this step and tell the user.

Supply exact product name, selected variant, source-supported facts, intended use and an opened real product reference image. The Director owns the creative process: product analysis, purchase reason, Thai narration/caption, actual storyboard generation and matching English video prompt. Do not replace it with a generic prompt template.

Apply this project's user overrides: 9:16, 10 seconds, five storyboard panels/five full-screen shots, storyboard-only Flow reference, and TikTok output only. Preserve Director v3's continuity, supported claims, no-face POV, narration timing and final still shot requirements. The storyboard's decorative text/stickers must not appear as video overlays; real packaging text remains.

Use the actual image generation tool and its skill; inspect product/variant, hands, five panels and action continuity. Follow Director's correction limit and report unresolved limitations. No video generation when storyboard is missing or unusable.

Save `storyboard.png` and `tiktok_caption.txt` to product output. Store `productMetadata`, `storyboardGenerationPrompt`, `videoPrompt`, narration/analysis as useful and `director: {skillName, pluginName, packageVersion, sourcePath, usedAt}` in job. Captions for other platforms are not separate output files. Temporary real product images are not uploaded into Flow.

## Required content model and evidence

Before creating any new storyboard or prompt, invoke a serial content subagent using collaboration.spawn_agent with task_name="ugc_content", fork_turns="none", model="gpt-6.1-sol", reasoning_effort="low". Pass the product facts, real product reference, user overrides, canonical workflow paths and installed Director v3 skill path. This delegation is explicitly required by this workflow. The content agent reads Director v3 and the image generation skill, creates the storyboard through ImageGen, and supplies both prompts, narration and TikTok caption. Sol 6.1 Low controls the creative work; ImageGen remains the image renderer, not a claim that the image renderer itself is Sol.

Persist job.actualModelEffort.content as an object containing model, reasoningEffort, invocationTool, invocationArguments (the actual model/effort/fork_turns), agentId/taskName returned by the tool, startedAt, completedAt, resultEvidence and artifactPaths. Record the successful spawn response and resulting agent output as evidence, not just copied config values. This proves the requested tool selection and returned result; do not claim access to internal provider execution telemetry. Preserve this evidence for corrections/revisions too. Do not relabel historical direct execution as verified Sol 6.1 Low.

If the tool rejects that exact selection or cannot provide an agent handle/result, record the actual error and stop content-dependent work. Do not silently fall back to the main agent, another model or another effort. Other agents must not rewrite the creative outputs; send creative corrections back to the same required model/effort.

## Invocation bookkeeping without a pause

Apply workflow.md's coordinator-owned evidence rule. A returned canonical task name is a valid agent handle; an opaque ID is not additionally required. The coordinator records local dispatch and result-receipt times as startedAt/completedAt with timestampSource, clearly distinguished from provider timestamps. If a historical time was not captured, use null and a limitation rather than asking the agent or inventing a time. Agents return their actual phase result and artifacts without waiting for bookkeeping replies. The coordinator merges invocation evidence after the result and before the next handoff; no second UI or creative review is required. A failed spawn or genuinely absent handle/result still stops dependent work.
