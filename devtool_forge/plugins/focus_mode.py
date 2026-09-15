class FocusMode:
    name = "Focus Mode"

    def run(self, context: dict) -> str:
        ignored = context.get("ignored", ["generated files", "imports"])
        return f"Hides: {', '.join(ignored)}"
