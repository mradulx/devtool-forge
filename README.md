# DevTool Forge

> Build the devtool you need without owning the fork you have to maintain.

DevTool Forge is a small, extensible CLI that demonstrates a practical alternative to source-level customization: keep a stable core and add workflow-specific behavior through plugins.

This project is inspired by [“Changing Devtools Is Cheap. Owning Them Isn’t.”](https://lalitm.com/post/changing-devtools-is-cheap-owning-them-isnt/) by Lalit Maganti. The article argues that AI lowers the cost of changing software, but the long-term cost of maintaining personalized forks remains real. A stronger model is a dependable core with well-defined extension points.

## Why this project?

Instead of:

```text
fork → patch → rebase → resolve conflicts → repeat
```

DevTool Forge aims for:

```text
core → plugin → configure → use
```

That makes customization explicit, isolated, testable, and removable.

## Features

- 🔌 Lightweight plugin architecture
- ⚙️ Simple configuration
- 🧩 Built-in example plugins
- 🧪 Unit tests for the extension system
- 🚀 Zero external runtime dependencies
- 🐍 Python 3.10+

## Quick start

```bash
python -m devtool_forge
```

Run with the built-in plugins:

```bash
python -m devtool_forge --demo
```

## Example output

```text
DevTool Forge
─────────────
✓ Focus Mode
✓ Git Changes
✓ TODO Tracker

Active plugins: 3
```

## Project structure

```text
devtool-forge/
├── devtool_forge/
│   ├── __main__.py
│   ├── core.py
│   └── plugins/
│       ├── focus_mode.py
│       ├── git_changes.py
│       └── todo_tracker.py
├── tests/
│   └── test_core.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Design principle

The core should own reliability. Plugins should own personalization.

A plugin can be changed or removed without changing the semantics of the core application. That boundary is the main experiment in this repository.

## Roadmap

- [x] Plugin interface
- [x] Built-in plugins
- [x] CLI demo
- [x] Tests
- [ ] Plugin discovery from installed packages
- [ ] User configuration file
- [ ] Plugin enable/disable commands
- [ ] Optional AI-assisted plugin scaffolding

## Inspiration

Lalit Maganti's article: https://lalitm.com/post/changing-devtools-is-cheap-owning-them-isnt/

The implementation here is an original learning project and does not reproduce the article's text or code.

## License

MIT
