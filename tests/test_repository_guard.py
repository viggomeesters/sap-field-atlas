from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def load_guard_module():
    path = Path(__file__).resolve().parents[1] / "scripts" / "validate_repository.py"
    spec = spec_from_file_location("validate_repository", path)
    assert spec and spec.loader
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_repository_guard_main_passes():
    assert load_guard_module().main() == 0
