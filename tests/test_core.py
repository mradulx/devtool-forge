import pytest

from devtool_forge.core import PluginManager


class ExamplePlugin:
    name = "Example"

    def run(self, context: dict) -> str:
        return context.get("message", "ok")


def test_register_and_run_plugin():
    manager = PluginManager()
    manager.register(ExamplePlugin())

    assert manager.names() == ["Example"]
    assert manager.run_all({"message": "hello"}) == ["hello"]


def test_duplicate_plugin_names_are_rejected():
    manager = PluginManager()
    manager.register(ExamplePlugin())

    with pytest.raises(ValueError, match="already registered"):
        manager.register(ExamplePlugin())
