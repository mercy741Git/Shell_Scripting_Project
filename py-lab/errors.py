import json
def load_config(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError as e:
        print(f"{path} not found - using defaults: {e}")
        return {}
    except json.JSONDecodeError as e:
        print(f"bad JSON in {path}: {e}")
        return {}
    finally:
        print("load_config finished")
print(load_config("missing.json"))     # triggers FileNotFoundError branch
open("bad.json","w").write("{not valid")
print(load_config("bad.json"))         # triggers JSONDecodeError branch
#open("good.json","w").write("{id: 1, name: 'test'}")
#open("good.json", "w").write('{"id": 1, "name": "test"}')
#better to use below
with open("good.json", "w") as f:
    json.dump({"id": 1, "name": "test"}, f)
print(load_config("good.json"))        # loads the good config
