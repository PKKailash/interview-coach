---
name: interview-prep
description: >
  Launches a local video interview coaching tool on the user's laptop. Records practice answers via webcam
  and mic, then analyses: filler words, speaking pace, answer length, rambling, grammar, facial expressions,
  body movement, and gives an overall score with coaching feedback.
  USE THIS SKILL for: interview prep, mock interview, practice answering questions, job interview help,
  camera confidence, video interview coaching, "I have an interview coming up", improve speaking skills,
  presentation skills, how to answer behavioural questions, STAR method coaching.
  Proactively offer when the user is job-hunting or mentions an upcoming interview.
---

# Interview Prep Coach

This skill launches a fully local, browser-based video interview coaching tool on the user's MacBook.
No data leaves the machine — everything runs in the browser using Web Speech API and face-api.js.

## What the tool does

The user opens a localhost URL in their browser. The tool:

1. **Accesses webcam + microphone** via the browser
2. **Generates practice questions** tailored to the role type (marketing, general behavioural, leadership, edtech, or custom)
3. **Lets the user record answers** question by question
4. After each answer, **analyses and scores** on:
   - Speaking pace (target: 120–160 wpm)
   - Filler words (um, uh, like, basically, honestly, etc.) — highlighted live in the transcript
   - Rambling / run-on sentences (flags sentences > 50 words)
   - Answer length (target: 60–120 seconds per question)
   - Grammar issues (double words, run-ons, subject-verb errors)
   - Repetitive vocabulary
   - Facial expression (happiness, confidence, nervousness via face-api.js)
   - Body movement / gesture level
   - Overall score /100 with colour ring
5. Provides **written coaching feedback** per answer with specific, actionable suggestions

## How to launch

When the user wants to use the interview coach, run:

```bash
python3 ~/.claude/skills/interview-prep/scripts/launch_server.py
```

This starts a local server on port 8765 and opens the tool at:
`http://localhost:8765/interview_app.html`

If port 8765 is in use, modify `PORT` in `launch_server.py`.

### Quick one-liner (no server needed — open directly):

```bash
open ~/.claude/skills/interview-prep/scripts/interview_app.html
```

> ⚠️ The direct-open method may restrict microphone/camera access in some browsers. Using the Python server is recommended for full functionality.

## How to coach the user before/after the tool

### Before they record

- Ask which role they're preparing for (role title + company if known)
- Suggest they set up in a quiet, well-lit space, facing the camera at eye level
- Encourage them to have a glass of water nearby
- Remind them to choose the right question type in the app (e.g. "Marketing / Brand / Digital" for a Marketing Coordinator role)

### Reading the feedback with them

After they record an answer and share feedback:

- **Score ≥ 80**: Affirm and point to one specific area for polish
- **Score 60–79**: Focus on the top 2 flagged issues; explain *why* they matter to the interviewer
- **Score < 60**: Prioritise filler words + answer structure first; suggest a re-record immediately

### Common coaching situations

| Issue | Coaching advice |
|---|---|
| High filler words | "Replace 'um' with a silent pause. It sounds confident, not nervous." |
| Too short (< 30s) | "Interviewers want a full story. Use STAR: Situation, Task, Action, Result." |
| Rambling | "One idea per sentence. End on the Result — don't trail off." |
| Nervous expression | "You're having a conversation, not being examined. Take a breath before starting." |
| Flat / neutral expression | "Show genuine enthusiasm for the topic — slight variation in expression reads as engaged." |
| Too fast | "Slow to 130 wpm. Speed reads as anxiety; pace reads as authority." |

## STAR Framework reminder

For behavioural questions ("Tell me about a time…"), coach the user on:

- **S**ituation – set the scene briefly (2–3 sentences)
- **T**ask – what was your specific responsibility?
- **A**ction – what did *you* personally do? (use "I", not "we")
- **R**esult – quantify the outcome if possible

## Session flow suggestion

1. Run 2–3 warm-up questions on "general behavioural"
2. Switch to the specific role type and do 3–4 targeted questions
3. Replay feedback side-by-side for growth comparison
4. End with one full "Tell me about yourself" polished answer

## Technical notes

- The app works entirely in-browser (HTML + JS, no backend required)
- Face detection uses face-api.js from a CDN — requires internet for first load
- Speech recognition uses the browser's built-in Web Speech API (works in Chrome/Edge; Firefox has limited support)
- **Best browser: Google Chrome** (full camera + mic + speech API support)
- No audio or video is recorded or stored — analysis is computed in real time and discarded
