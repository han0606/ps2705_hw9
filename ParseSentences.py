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
        return 'Setence(sentence_string = %s, document = %s, line_number = %s, character_count = %s, word_count = %s)' % (self.sentence_string, self.document, self.line_number, self.character_length, self.word_celngth)

    def read(self):
        print(self.sentence_string)

    def write(self, file):
        with open(file, "a") as f:
            f.write("\n---")
            yaml.dump(self, f, sort_keys=False)
            f.write("{}: {}\n".format("count_characters", text_obj.count_characters()))
            f.write("{}: {}\n".format("count_words", text_obj.count_words()))   

if __name__ == "__main__":
    files = sys.argv[1:]
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
