# Name: Husen Yusuf
# ID No: UGR/7575/13
# ---------------------------------
# Name: Amir Ahmedin
# ID No: UGR/4119/13

# ---------------------------------
# Section 4

from stack import Stack


def htmlValidator(htmlFile):
    stringFile = open(htmlFile, 'r').readlines()
    tagsStack = Stack()
    startTag = ""
    lineIndex = 0
    while lineIndex < len(stringFile):  # a loop to iterate every line in the file
        charIndex = 0
        while charIndex < len(stringFile[lineIndex]):  # a loop to iterate every character in the line

            if stringFile[lineIndex][charIndex] == "<":

                if stringFile[lineIndex][charIndex + 1] != "/":

                    while charIndex < len(stringFile[lineIndex]):

                        if stringFile[lineIndex][charIndex] != ">" and stringFile[lineIndex][charIndex] != " ":

                            if charIndex == len(stringFile[lineIndex]) - 1:
                                # if this is true, then we have reached the last element (because our element index
                                # is charIndex) but there is no a closing brace yet, so it sends an error message
                                charIndex += 1
                                raise Exception("Tag is not properly closed at line " + str(lineIndex + 1))
                            else:
                                startTag += stringFile[lineIndex][charIndex]
                                charIndex += 1

                        elif stringFile[lineIndex][charIndex] == " " or stringFile[lineIndex][charIndex] == ">":

                            if stringFile[lineIndex][charIndex] == " ":

                                while charIndex < len(stringFile[lineIndex]):

                                    if stringFile[lineIndex][charIndex] == ">":
                                        startTag += stringFile[lineIndex][charIndex]
                                        charIndex += 1
                                        break
                                    charIndex += 1

                            elif stringFile[lineIndex][charIndex] == ">":
                                startTag += stringFile[lineIndex][charIndex]

                            if isEmptyTag(startTag):
                                # if it is an empty element we simply remove it by setting startTag to empty string
                                startTag = ""
                                charIndex += 1

                            else:
                                tagsStack.push(startTag)
                                lineNum = lineIndex + 1
                                startTag = ""
                                charIndex += 1
                                break

                elif stringFile[lineIndex][charIndex + 1] == "/":
                    endTag = ""
                    endTag += stringFile[lineIndex][charIndex]

                    while (charIndex + 2) < len(stringFile[lineIndex]) and stringFile[lineIndex][charIndex + 2] != ">":

                        if charIndex == len(stringFile[lineIndex]) - 3:
                            # if this is true, then we have reached the last element (because our element index
                            # is charIndex + 2) but there is no a closing brace yet, so it sends an error message
                            charIndex += 1
                            raise Exception("Tag is not properly closed at line " + str(lineIndex + 1))
                        else:
                            endTag += stringFile[lineIndex][charIndex + 2]
                            charIndex += 1

                    endTag += stringFile[lineIndex][charIndex + 2]
                    charIndex = charIndex + 2

                    if endTag == tagsStack.top():
                        tagsStack.pop()
                        endTag = ""
                    else:
                        charIndex += 1
                        raise Exception("mismatch in start tag and end tag at line " + str(lineIndex + 1))

            charIndex += 1
        lineIndex += 1

    if tagsStack.isEmpty():
        print("No errors found :) ")

    else:  # if the stack is not empty then there is a tag that has been pushed (i.e. opened)
        # but not popped yet (i.e. not closed)
        raise Exception("Unclosed tag " + str(tagsStack.top()) + " found at line " + str(lineNum))


def isEmptyTag(tag):
    emptyTags = ["<area>", "<base>", "<br>", "<col>", "<embed>", "<hr>", "<img>", "<input>", "<keygen>", "<link>",
                 "<meta>", "<param>", "<source>", "<track>", "<wbr>"]
    return tag in emptyTags


# the time complexity of the program is O(n), because even though we have nested so many loops, the iteration
# variable (charIndex) got updated on each loop, thus the outer loop will not iterate over the charIndex that has
# been iterated by an inner loop. for example, the while loop in line 27 will jump those values that has been
# iterated by the other loop in line 43 . thus each character is accessed only ones. thus the total time complexity
# became O(n)
