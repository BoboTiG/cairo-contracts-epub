import re
from pathlib import Path

# Paths
ROOT = Path(__file__).parent.parent
DOCS = ROOT / "cairo-contracts" / "docs"
OUTPUT_FINAL = ROOT / "output"

# ePub
EPUB_AUTHOR = "OpenZeppelin"
EPUB_FILE = OUTPUT_FINAL / "openzeppelin-contracts-in-cairo-for-starknet.epub"
EPUB_TITLE = (
    "OpenZeppelin Contracts written in Cairo for StarkNet, a decentralized ZK Rollup"
)
TITLE_REGEXP = re.compile(r"<h1>(.+)</h1>")
