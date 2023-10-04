from datasets import load_dataset

dataset = load_dataset("nampdn-ai/tiny-textbooks")

tiny_textbooks = "\n\n".join(dataset['train'][:]['text'])

tt_file = open('tiny_textbooks.txt', 'w')

tt_file.write(tiny_textbooks)

tt_file.close()
