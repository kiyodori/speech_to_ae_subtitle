import json

ENOUGH_CONTENT_LENGTH = 24

class AeScriptConverter:
    def make_script(self):
        script = self.convert()
        self.export(script)

    def convert(self):
        json = self.load_json()
        start_time = ''
        end_time = ''
        content = []
        contents = []

        # for index, item in enumerate(json):
        #     start_time = item['start_time']
        #     content.append(item['alternatives'][0]['content'])
        #     if enough_content_length(content):
        #         end_time = item['end_time']
        #         add_contents(start_time, content, end_time)
        #         content = []
        #         break

        print(start_time)
        print(end_time)
        print(content)
        return 1

    def export(self, script):
        print(1)

    def load_json(self):
        file = open("test.json", "r")
        line = file.read()
        file.close
        return json.loads(line)["results"]["items"]

    # def add_contents(start_time, content, end_time):

    def enough_content_length(content):
        len(content) >= ENOUGH_CONTENT_LENGTH

ae_script_converter = AeScriptConverter()
ae_script_converter.make_script()
