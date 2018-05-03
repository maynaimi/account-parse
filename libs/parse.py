import re

itemRegex = '\d\d-\w\w\w-\d\d.*'

def parseContent(content):
    account = None
    items = []

    content = _cleanupContent(content)
    content = _consolidateContent(content)
    content = _filterContent(content)

    for c in content:
        if _accountLookup(c) is not None:
            account = _accountLookup(c)
            continue
            
        item = c.strip().split('\t')
        item.append(account)
        if len(item) != 7:
            print('***ERROR*** skipping item', item)

        items.append(item)

    return items


def _accountLookup(text):
    accountText = {
        '0200 - Staff Current Accounts'  : 'current'  
      , '0202 - Staff Clothing Accounts' : 'clothing' 
      , '0204 - Staff Holiday Accounts'  : 'holiday'  
    }

    if accountText.get(text) is None:
        return None

    return accountText[text]

def _cleanupContent(content):
    # Replace any double (or more) spaces with a tab
    return [re.sub('\s\s+', '\t', c) for c in content] 

def _consolidateContent(content):
    for idx, c in enumerate(content):
        # If the line is an item
        if re.search(itemRegex, c):
            # find the next line
            nextLine = content[idx+1]
            # if the next line is not an item, it is a continuation of the current line
            if not re.search(itemRegex, nextLine):
                # consolidate it with the current line
                content[idx] = content[idx] + '\t' + content[idx+1]
                del content[idx+1]

    return content

def _filterContent(content):
    return [c for c in content if re.search(itemRegex, c) and not re.search('Beginning Period Balance', c) or _accountLookup(c)]