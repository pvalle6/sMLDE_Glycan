import glycowork
from glycowork.motif.annotate import get_terminal_structures
print("\nTerminal structures:")
print(get_terminal_structures('GlcA(b1-4)Xyl'))
print(get_terminal_structures('GlcA(b1-3)Xyl(a1-3)GlcA(b1-3)Xyl(a1-3)GlcA(b1-4)Xyl'))
