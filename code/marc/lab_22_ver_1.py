# Lab 22 counting imported text and calculating an ari value
    #tomorrow take a closer look at string and list operators to see how thit manipulate this 
    #data. You basically have a big string to work with it
    #create list that you can then create the equations from
    #1. Step one import the text
    #2. Manipulate the text so that you can get all the equations you need for the ARI formula
    #   -This means strip the text of punctuation. 
    #   -Seperate it by spaces into words
    #   -Create seperate lists of words and characters(I think)
    #   -Write the equation out, accessing the lists to create the score
    #3. Cut and paste and bring in the list and dictionary from the document to use
    #4. Take the score to acces the proper list and dicitonary
    #5. Return the statement with the correct score and reading level
def main():
    import string
    import re
    import math
    ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}}
    with open('lincoln.txt', 'r') as open_linc:
        contents = open_linc.read() #This opens the text file and turns it into a variable
    
    contents_low = contents.lower().strip().strip(".?!") #this strips the text of white space, and punctuation at the end
   
    contents_punc = contents_low.translate(str.maketrans(' ', ' ', string.punctuation)) #this is magic and I am not sure how it works but it strips punctuation
    
    words = contents_punc.split() #this creates a word list
    
    chars = contents_punc.replace(" ", "").replace("\n", "") #this creates total charecters
    
    sentences = (re.split('[.?!]', contents_low)) #this more magic using a 're' method to get sentences
    
    ARI = math.ceil(4.71 * (len(chars)/len(words)) + .5 * (len(words)/len(sentences)) - 21.43)
    if ARI > 14: #this is the massive ARI equation followed by an if statement covering items scores over 14
        ARI = 14
   
    ARI_message = f'''\nThe ARI for this text is {ARI} which corresponds to
    the {ari_scale[ARI]['grade_level']} grade level. It is suitable for the
    average person age {ari_scale[ARI]['ages']}.'''
    print(ARI_message)

main()