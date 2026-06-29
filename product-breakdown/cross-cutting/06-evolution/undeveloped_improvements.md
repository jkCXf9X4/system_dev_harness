
Im experiencing problems of context rot for long sessions in the subagents

The question is, for subagents can a top agent force context compact or clearing?

An external analysis shows that:
Short answer: No. The task tool provides no mechanism for a parent agent to force context compaction or clearing on a subagent.
Here's the detailed breakdown:
1. No parameters exist for context control
The task tool / SubtaskPartInput type accepts only:
- id (optional)
- type (fixed: "subtask")
- prompt, description, agent
- model (optional)
- command (optional)
There is no reset, compact, clear, prune, truncate, or any context-management parameter.
2. Parent cannot control subagent's context window
The parent has zero control over a subagent's conversation history, context window size, or memory state. Everything about history retention is handled internally by the OpenCode runtime.
3. Where context management does exist (but you can't use it here)
- Session-level compaction — There is a POST /api/session/{id}/compact API endpoint (exposed as session.compact() in the SDK), but that compacts a session, not a subagent, and is not accessible through the task tool.
- Global compaction config — The compaction section in opencode.json controls auto-compaction behavior globally via auto, prune, tail_turns, etc.
- Built-in compaction agent — OpenCode uses this internally; you cannot invoke it on a subagent.
Bottom line
If a subagent's session grows too large with accumulated context, the orchestrator cannot force a reset or compaction. The runtime handles this automatically based on global configuration. The only way to "clear" a subagent's context is to not reuse its session — i.e., launch a fresh subagent with a new task_id (don't pass a previous task_id to resume).

Can we utilize this in directing the sub-agents to start new id if deemed necessary?