from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

KNOWLEDGE_PATH = BASE_DIR / "knowledge_base"

# Funcão que carrega os dados dos arquivo na pasta knowledge_base
def load_all_knowledge(module_id, topic_id):

    topic_path = (

        KNOWLEDGE_PATH

        / "modules"

        / f"module_{module_id}"

        / f"topic_{topic_id}.md"
    )

    if not topic_path.exists():

        return ""

    with open(
        topic_path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()