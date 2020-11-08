#! /user/bin/env python
import sys
import yaml

class Sentence:
    
    def __init__(self, text):
        self.sentence_string = str(text)
        self.document = str(filePath)
        self.line_number = count

    def count_characters(self):
        return(len(self.sentence_string))
    
    def count_words(self):
        return(len(self.sentence_string.split()))

    def __repr__(self):
        return f"Sentence(Sentence = {self.sentence_string}, Document = {self.document}, Line Number = {self.line_number}, Character Count = {self.character_length}, Word Count = {self.word_length})"
    
    def read(self):
        print(self.sentence_string)

    def write(self, file):
        with open(file, "a") as f:
            f.write("\n---")
            yaml.dump(self, f, sort_keys=False)
            f.write("{}: {}\n".format("count_characters", text_obj.count_characters()))
            f.write("{}: {}\n".format("count_words", text_obj.count_words()))   

if __name__ == "__main__":
    files = [sys.argv]
    for filePath in files:
        with open(filePath, "r") as f:
            count = 1
            line = f.readline()
            text_obj = Sentence(line)
            while line:
                text_obj.write("output.yaml")
                count += 1
                line = f.readline()
                text_obj = Sentence(line)         