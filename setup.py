from setuptools import setup, find_packages
from setuptools.command.install import install
from setuptools.command.develop import develop
import os
import sys
import urllib.request
import platform
from pathlib import Path


VERSION = "0.1.0"


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
        print(f"Unsupported platform: {system}-{machine}")
        return None, None, None


def download_binary():
    platform_name, remote_name, local_name = get_platform_info()
    if not platform_name:
        return

    url = f"https://github.com/abhixdd/ghgrab/releases/download/v{VERSION}/{remote_name}"
    bin_dir = Path(__file__).parent / "ghgrab"
    bin_dir.mkdir(parents=True, exist_ok=True)
    bin_path = bin_dir / local_name

    print(f"Downloading ghgrab v{VERSION} binary for {platform_name}...")
    print(f"  URL: {url}")

    try:
        urllib.request.urlretrieve(url, bin_path)

        size = bin_path.stat().st_size
        if size < 100_000:
            bin_path.unlink(missing_ok=True)
            raise RuntimeError(f"Downloaded file too small ({size} bytes) — likely not a valid binary")

        if platform.system().lower() != "windows":
            bin_path.chmod(0o755)

        print(f"✓ Binary downloaded to {bin_path}")
    except Exception as e:
        print(f"Warning: Could not download binary: {e}")
        print("The binary will be downloaded on first use, or you can run:")
        print("  pip install --force-reinstall ghgrab")
        # Don't fail install — __init__.py will retry on first run


class PostInstall(install):
    def run(self):
        install.run(self)
        download_binary()


class PostDevelop(develop):
    def run(self):
        develop.run(self)
        download_binary()


setup(
    name="ghgrab",
    version=VERSION,
    packages=find_packages(),
    package_data={"ghgrab": ["ghgrab", "ghgrab.exe"]},
    include_package_data=True,
    cmdclass={
        "install": PostInstall,
        "develop": PostDevelop,
    },
    zip_safe=False,
)
