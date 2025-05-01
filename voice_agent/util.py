import os 


def load_instruction_from_file(
        filename: str, default_instruction: str = "Default Instruction."
)-> str:
    """Reads instruction from a file relative to this script."""
    instruction = default_instruction
    try:
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, 'r', encoding="utf-8") as f:
            instruction = f.read()
        print(f"Successfully Loaded instruction from {filename}")
    except FileNotFoundError:
        print(f"WARNING: Instruction file not found: {filepath}. Using default instruction.")
    except Exception as e:
        print(f"ERROR: Error reading instruction file {filepath}: {e}. Using default instruction.")
    return instruction