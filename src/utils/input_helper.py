from typing import Optional

def get_int_input(prompt: str) -> Optional[int]:
    try:
        val = input(prompt)
        if not val: return None
        return int(val)
    except ValueError:
        print("[!] Invalid integer.")
        return None

def get_float_input(prompt: str) -> Optional[float]:
    try:
        val = input(prompt)
        if not val: return None
        return float(val)
    except ValueError:
        print("[!] Invalid number.")
        return None
