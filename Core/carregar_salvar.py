import json

def carregar_json(data):
  with open(f"{data}", "r", encoding="utf-8") as arq:
    return = json.load(arq)

def salvar(data, name_path):
  with open(f"{nome_path}", "w", encoding="utf-8") as arq:
    json.dump(data, arq, indent=4)
