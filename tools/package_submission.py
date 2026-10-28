"""Create a minimal submission ZIP using an explicit file allowlist."""

from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def package():
    destination = ROOT.parent / "Ycany-Sanchez-Streamlit-Portfolio.zip"
    required = [ROOT / name for name in ["app.py", "portfolio.py", "requirements.txt", "README.md", "run_app.cmd", ".gitignore", ".streamlit/config.toml"]]
    required.extend(sorted((ROOT / "assets").glob("*.png")))
    required.append(ROOT / "assets/styles.css")
    required.extend(sorted((ROOT / "tests").glob("test_*.py")))
    required.extend([ROOT / "tests/browser-check.cjs", ROOT / ".github/workflows/check.yml", ROOT / "tools/package_submission.py"])
    for file in required:
        if not file.is_file():
            raise FileNotFoundError(f"Missing submission file: {file.relative_to(ROOT)}")
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file in required:
            archive.write(file, file.relative_to(ROOT).as_posix())
    print(f"Created {destination} ({destination.stat().st_size:,} bytes, {len(required)} files)")
    return destination


if __name__ == "__main__":
    package()
