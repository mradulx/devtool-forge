import argparse

from .core import PluginManager
from .plugins.focus_mode import FocusMode
from .plugins.git_changes import GitChanges
from .plugins.todo_tracker import TodoTracker


def build_manager() -> PluginManager:
    manager = PluginManager()
    manager.register(FocusMode())
    manager.register(GitChanges())
    manager.register(TodoTracker())
    return manager


def main() -> None:
    parser = argparse.ArgumentParser(description="A tiny plugin-first developer tool.")
    parser.add_argument("--demo", action="store_true", help="run the built-in plugin demo")
    args = parser.parse_args()

    manager = build_manager()
    print("DevTool Forge")
    print("─────────────")

    for name in manager.names():
        print(f"✓ {name}")

    if args.demo:
        print("\nPlugin details")
        for result in manager.run_all({"branch": "main", "todos": 3}):
            print(f"• {result}")

    print(f"\nActive plugins: {len(manager.plugins)}")


if __name__ == "__main__":
    main()
