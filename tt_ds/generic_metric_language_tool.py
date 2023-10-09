import language_tool_python
import sys

tool = language_tool_python.LanguageTool('en-US')

with open(sys.argv[1], 'r') as file:
	text = file.read()

matches = tool.check(text)

spelling_mistakes = []
for match in matches:
    if match.ruleId == "MORFOLOGIK_RULE_EN_US":
        spelling_mistakes.append(match)

print(len(spelling_mistakes))

