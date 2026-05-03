import sys
import webbrowser

class Gorilla:
    def __init__(self):
        self.variables = {}
        self.functions = {}

    def run_line(self, line):
        line = line.strip()
        if not line or line.startswith("//"): return 

        parts = line.split(" ", 1)
        cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ""

        if cmd == "say":
            print(self.eval_expression(args))
        elif cmd == "go_web":
            webbrowser.open(args.strip('"'))
        elif cmd == "set" or cmd == "dictioner":
            if "=" in args:
                name, val = args.split("=", 1)
                self.variables[name.strip()] = self.eval_expression(val.strip())

    def eval_expression(self, expr):
        expr = expr.strip('"')
        return self.variables.get(expr, expr)

    def run_file(self, filename):
        try:
            # إضافة encoding='utf-8' هنا لحل مشكلة UnicodeDecodeError
            with open(filename, 'r', encoding='utf-8') as f:
                for line in f:
                    self.run_line(line)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Runtime Error: {e}")

if __name__ == "__main__":
    interpreter = Gorilla()
    if len(sys.argv) > 1:
        interpreter.run_file(sys.argv[1])
    else:
        print("Gorilla Language v1.0 - Welcome Adam")
        while True:
            try:
                code = input("Gorilla > ")
                if code == "exit": break
                interpreter.run_line(code)
            except EOFError: break