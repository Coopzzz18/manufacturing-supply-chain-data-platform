import subprocess
import sys
from pathlib import Path
from logger import logger

SCRIPTS_DIR = Path(__file__).resolve().parent

scripts = [
    "generate_shipments.py",
    "generate_production.py",
    "generate_inventory.py",
    "pipeline.py",
    "export_views.py",
]

print("=" * 50)
print("MANUFACTURING DATA PLATFORM")
print("=" * 50)

logger.info("Pipeline started.")

for script_name in scripts:
    script_path = SCRIPTS_DIR / script_name

    print(f"\nRunning {script_name}...")

    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")

    subprocess.run(
        [sys.executable, str(script_path)],
        check=True,
    )

    logger.info(f"{script_name} completed successfully.")

print("\nAll processes completed successfully!")
logger.info("Pipeline finished successfully.")