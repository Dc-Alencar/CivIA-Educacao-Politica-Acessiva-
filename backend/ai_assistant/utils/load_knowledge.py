from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

KNOWLEDGE_PATH = BASE_DIR / "knowledge_base"


def load_all_knowledge():

    all_content = ""

    for file_path in KNOWLEDGE_PATH.rglob("*.md"):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            all_content += file.read()

            all_content += "\n\n"

    return all_content