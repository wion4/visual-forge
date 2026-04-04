---
name: draw
description: Launch visual art workflows — create concept art, establish style guides, or review anatomy
argument-hint: "[create|style|review]"
allowed-tools: ["Bash", "Read", "Write", "Edit", "AskUserQuestion", "Agent"]
---

Launch Visual Forge workflows.

## Modes

- **No arguments / `create`**: Create art using visual-artist agent
- **`style`**: Build or review a visual style guide using style-director agent
- **`review`**: Check character art for anatomy/proportion issues using anatomy-checker agent

## Execution

1. Detect system language: `echo $LANG`
2. Load the visual-forge skill for methodology context
3. Launch the appropriate agent based on the mode
4. All agents work in the user's language
