import docx

template = docx.Document('Test.docx')

fullText = []
for paragraph in template.paragraphs:
    fullText.append(paragraph.text)


print(fullText)