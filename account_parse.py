## USAGE: 

from libs import files
from libs import parse

header = ['date', 'description', 'currency', 'amountNIS', 'amountUSD', 'balance', 'account']

if __name__ == "__main__":
    filesList = files.listFiles()
    print('Found ' + str(len(filesList)) + " files to process, starting processing...\n")

    for f in filesList:
        print('Processing file: ' + f)
        content = files.readFile(f)
        items = parse.parseContent(content)
        print(items)
        print("Done processing file\n")