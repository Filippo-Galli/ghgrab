#!/usr/bin/env python3
import os
import sys
import subprocess
import urllib.request
import platform
from pathlib import Path


def get_platform_info():
    system = platform.system().lower()
    machine = platform.machine().lower()

    if system == "windows":
        return "win32", "ghgrab-win32.exe", "ghgrab.exe"
    elif system == "darwin":
        if machine in ("arm64", "aarch64"):
            return "darwin-arm64", "ghgrab-darwin-arm64", "ghgrab"
        return "darwin", "ghgrab-darwin", "ghgrab"
    elif system == "linux":
        if machine in ("arm64", "aarch64"):
            return "linux-arm64", "ghgrab-linux-arm64", "ghgrab"
        return "linux", "ghgrab-linux", "ghgrab"
    else:
        raise RuntimeError(f"Unsupported platform: {system}-{machine}")


def download_binary(version: str, bin_dir: Path) -> Path:
    platform_name, remote_name, local_name = get_platform_info()
    url = f"https://github.com/abhixdd/ghgrab/releases/download/v{version}/{remote_name}"
    bin_path = bin_dir / local_name

    print(f"Downloading ghgrab v{version} for {platform_name}...")
    print(f"  URL: {url}")

    try:
        urllib.request.urlretrieve(url, bin_path)
    except Exception as e:
        raise RuntimeError(f"Download failed: {e}")

    # Verify binary size
    size = bin_path.stat().st_size
    if size < 100_000:
        bin_path.unlink(missing_ok=True)
        raise RuntimeError(f"Downloaded file too small ({size} bytes) — not a valid binary")

    if platform.system().lower() != "windows":
        bin_path.chmod(0o755)

    print(f"✓ ghgrab installed to {bin_path}")
    return bin_path


def main():
    # Determine binary location relative to this file
    bin_dir = Path(__file__).parent
    system = platform.system().lower()
    binary_name = "ghgrab.exe" if system == "windows" else "ghgrab"
    binary_path = bin_dir / binary_name

    if not binary_path.exists():
        # Try lazy download on first run
        print(f"Binary not found at {binary_path}. Attempting download...", file=sys.stderr)
        try:
            from importlib.metadata import version as pkg_version
            ver = pkg_version("ghgrab")
        except Exception:
            ver = "0.1.0"
        try:
            download_binary(ver, bin_dir)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            print("Please reinstall: pip install --force-reinstall ghgrab", file=sys.stderr)
            sys.exit(1)

    try:
        result = subprocess.run([str(binary_path)] + sys.argv[1:])
        sys.exit(result.returncode)
    except FileNotFoundError:
        print(f"Error: Binary not found at {binary_path}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(130)


if __name__ == "__main__":
    main()
