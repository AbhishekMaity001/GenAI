import os
from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent  # this will form current path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def create_structure():
    # DEFINING FOLDER STRUCTURES
    folders = [
        "knowledge_graph_builder",
        "knowledge_graph_builder/agents",
        "knowledge_graph_builder/tools",
        "knowledge_graph_builder/workflows",
        "knowledge_graph_builder/utils",
        "knowledge_graph_builder/data",
        "knowledge_graph_builder/data/outputs",
    ]

    # DEFINE THE FILES TO BE CREATED IN EACH FOLDER
    files = {
        "knowledge_graph_builder/app.py": "",
        "knowledge_graph_builder/agents/researcher.py": "",
        "knowledge_graph_builder/agents/synthesizer.py": "",
        "knowledge_graph_builder/agents/mapper.py": "",
        "knowledge_graph_builder/tools/serpapi_tool.py": "",
        "knowledge_graph_builder/tools/wikipedia_tool.py": "",
        "knowledge_graph_builder/tools/research_api_tool.py": "",
        "knowledge_graph_builder/workflows/langgraph_router.py": "",
        "knowledge_graph_builder/utils/graphviz_exporter.py": "",
        "knowledge_graph_builder/utils/config.py": "",
        "knowledge_graph_builder/requirements.txt": "",
    }

    print("******************* Creating Folder structures ***************************")

    # CREATE FOLDERS
    res_folders = [os.makedirs(os.path.join(BASE_DIR, folder), exist_ok=True) for folder in folders]
    print("1. Folders created successfully.")

    # CREATE FILES
    for filepath, content in files.items():
        with open(os.path.join(BASE_DIR, filepath), "w") as f:
            f.write(content)
    print("2. Files created successfully.")
    

    print("******************* Folder structures created successfully for the project!! ***************************")

if __name__ == "__main__":
    create_structure()