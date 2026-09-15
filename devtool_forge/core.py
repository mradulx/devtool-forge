from dataclasses import dataclass, field
from typing import Protocol


class Plugin(Protocol):
    """Contract implemented by every DevTool Forge plugin."""

    name: str

    def run(self, context: dict) -> str:
        ...


@dataclass
class PluginManager:
    """Keeps the core independent from user-specific behavior."""

    plugins: list[Plugin] = field(default_factory=list)

    def register(self, plugin: Plugin) -> None:
        if any(existing.name == plugin.name for existing in self.plugins):
            raise ValueError(f"Plugin already registered: {plugin.name}")
        self.plugins.append(plugin)

    def run_all(self, context: dict | None = None) -> list[str]:
        context = context or {}
        return [plugin.run(context) for plugin in self.plugins]

    def names(self) -> list[str]:
        return [plugin.name for plugin in self.plugins]
