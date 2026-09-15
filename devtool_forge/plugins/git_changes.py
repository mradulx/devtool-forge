class GitChanges:
    name = "Git Changes"

    def run(self, context: dict) -> str:
        branch = context.get("branch", "main")
        return f"Watching changes on: {branch}"
