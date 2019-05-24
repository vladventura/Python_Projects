class Notepad:

    brain = list()

    def read_file(self):
        try:
            with open("save.txt", "rt") as file:
                print("File opened to read")
                for line in file.readlines():
                    self.brain.append(line.replace("\n", ""))
                print("Read loop exited")
            print("Message(s) read")
        except FileNotFoundError:
            print("File wasn't there, so I'll make a new one")
            f = open("save.txt", "wt")
            f.close()


    def buffer(self, info):
        if info not in self.brain:
            self.brain.append(f"[]{info}")
            print("Message added to buffer successfully")



    def remove(self, info):
        try:
            self.brain.remove(f"[]{info}")
            print("Message removed from buffer successfully")
        except ValueError:
            print("This message is not present in the buffer")


    def write_to_file(self):
        with open("save.txt", "wt") as file:
            print("File to write to is open")
            for lines in self.brain:
                file.write(lines)
                file.write("\n")
        print("List written to file")


    def show_text(self):
        for lines in self.brain:
            print(f"{lines}")