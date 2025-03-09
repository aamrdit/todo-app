
content = ["All carrots are to be  sliced "
           "longitudinally.",
           "The carrots were repeatedly sliced",
           "The slicing process was well presented"]

filenames = ["doc.txt", "report.txt","presentations.txt"]


for content, filename in zip(content, filenames):
    file = open(f"../files/{filename}", 'w')
    file.write(content)


