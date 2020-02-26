#! python3
# randomQuizGenerator.py - Creats quizzes with questions and answers in
# random order,along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.

capitals = {'a':'montgeomery','hbka':'juneau','arizonatw':'phoneix',
            'b':'little rock','csdlifornia':'sacramento','crbolorado':'denver',
             'c':'montgeomery','albjaska':'juneau','arizonaflb':'phoneix',
            'd':'little rock','caliuhfornia':'sacramento','cmdolorado':'denver',
            'e':'montgeomery','alaskagz':'juneau','arizonatw':'phoneix',
            'fs':'little rock','califorsjnia':'sacramento','fjcolorado':'denver',
            'ba':'montgeomery','alaskatj':'juneau','arizonajms':'phoneix',
            'g':'little rock','califonjrnia':'sacramento','hlscolorado':'denver',
            'h':'montgeomery','alasksxa':'juneau','arizonaheb':'phoneix',
            'ias':'little rock','calisxfornia':'sacramento','lncolorado':'denver',
            'j':'montgeomery','alasknxa':'juneau','arizonajl':'phoneix',
            'kjs':'little rock','califxjornia':'sacramento','sdcolorado':'denver',
            'l':'montgeomery','alaskags':'juneau','arizonajs':'phoneix',
            'm':'little rock','califorqhnia':'sacramento','zjcolorado':'denver',
            'an':'montgeomery','alaskaxz':'juneau','arizonahn':'phoneix',
            'aj':'little rock','califorynnia':'sacramento','cgxolorado':'denver',
            'k':'montgeomery','califorydsnnia':'sacramento','cgxolordxado':'denver'}

#generate 35 quiz files.

for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1),'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum +1),'w')
    
    # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capital Quiz (From %s)' % (quizNum + 1))
    quizFile.write('\n\n')
    
    # TODO: Shuffle the order of the states.
    states = list(capitals.keys())
    #print('州总数目为'+ str(len(states)))
    random.shuffle(states)

    
    # TODO: Loop through all 50 staes, making a question for each.
    for questionNum in range(50):
                # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers =random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
                # TODO: Write the question and answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n\n' % (questionNum + 1,states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s   ' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n\n')
                        # TODO: Write the answer key to a file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
        

