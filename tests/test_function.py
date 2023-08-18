import os

class MockFileSystem:
    def __init__(self):
        self.files = {}

    def create_file(self, file_path):
        if file_path in self.files:
            print(f"File '{file_path}' already exists.")
            return
        self.files[file_path] = ""

    def write_file(self, file_path, content):
        if file_path in self.files:
            self.files[file_path] = content
        else:
            print(f"File '{file_path}' does not exist.")

    def read_file(self, file_path):
        if file_path in self.files:
            return self.files[file_path]
        else:
            print(f"File '{file_path}' does not exist.")

    def copy_file(self, source_path, destination_path):
        if source_path in self.files:
            self.files[destination_path] = self.files[source_path]
        else:
            print(f"File '{source_path}' does not exist.")

    def move_file(self, source_path, destination_path):
        if source_path in self.files:
            self.files[destination_path] = self.files.pop(source_path)
        else:
            print(f"File '{source_path}' does not exist.")

    def list_files(self):
        return list(self.files.keys())


# Example usage:
if __name__ == "__main__":
    fs = MockFileSystem()

    fs.create_file("/documents/file1.txt")
    fs.create_file("/documents/file2.txt")

    fs.write_file("/documents/file1.txt", "Hello, this is file 1 content.")
    fs.write_file("/documents/file2.txt", "This is file 2 content.")

    print(fs.list_files())

    print("File1 Content:", fs.read_file("/documents/file1.txt"))
    print("File2 Content:", fs.read_file("/documents/file2.txt"))

    fs.copy_file("/documents/file1.txt", "/documents/file3.txt")
    print("After Copy:", fs.list_files())

    fs.move_file("/documents/file2.txt", "/new_location/file2.txt")
    print("After Move:", fs.list_files())
