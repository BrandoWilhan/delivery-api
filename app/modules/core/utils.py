import json

FILE_NAME = "pedidos.json"


class JsonIO():
    def __init__(self):
        self.json_name = FILE_NAME
        self.file = None
        self.data = None

    def __read_json(self):
        self.file = open(self.json_name, "r", encoding='utf_8')
        self.data = json.load(self.file)
        self.file.close()

    def write_json(self):
        self.__read_json()
        self.file = open(self.json_name, "w+")
        self.file.write(json.dumps(self.data, ensure_ascii=False, indent=2))
        self.file.close()

    def locate_obj(self, index):
        self.__read_json()
        if(self.data["pedidos"][index-1]["id"] == index):
            return self.data["pedidos"][index-1]
        else:
            return "not found"
        

