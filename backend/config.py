import os
from pathlib import Path

def get_api_key():
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if api_key:
        return api_key.strip()

    root_dir = Path(__file__).resolve().parent.parent
    env_candidates = [
        root_dir / ".env",
        root_dir / ".env.local",
        root_dir / "backend" / ".env",
        root_dir / "backend" / ".env.local",
    ]

    for env_path in env_candidates:
        if not env_path.exists():
            continue
        try:
            for raw_line in env_path.read_text(encoding="utf-8").splitlines():
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    continue
                key, value = line.split("=", 1)
                if key.strip() != "DEEPSEEK_API_KEY":
                    continue
                value = value.strip().strip('"').strip("'")
                if value:
                    return value
        except Exception:
            continue

    return None
