class TodoTracker:
    name = "TODO Tracker"

    def run(self, context: dict) -> str:
        todos = context.get("todos", 0)
        return f"Open TODOs: {todos}"
