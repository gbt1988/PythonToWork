#! python3
# randomQuizGenerator.py - Creats quizzes with questions and answers in
# random order,along with the answer key.

import random

# The quiz data. Keys are states and values are their capitals.

capitals = {'alabama':'montgeomery','alaska':'juneau','arizona':'phoneix',
            'arkansas':'little rock','california':'sacramento','colorado':'denver',
            'alabama':'montgeomery','alaska':'juneau','arizona':'phoneix',
            'arkansas':'little rock','california':'sacramento','colorado':'denver',
            'alabama':'montgeomery','alaska':'juneau','arizona':'phoneix',
            'arkansas':'little rock','california':'sacramento','colorado':'denver',
            'alabama':'montgeomery','alaska':'juneau','arizona':'phoneix',
            'arkansas':'little rock','california':'sacramento','colorado':'denver',
            'alabama':'montgeomery','alaska':'juneau','arizona':'phoneix',
            'arkansas':'little rock','california':'sacramento','colorado':'denver',
            'alabama':'montgeomery','alaska':'juneau','arizona':'phoneix',
            'arkansas':'little rock','california':'sacramento','colorado':'denver',
            'alabama':'montgeomery','alaska':'juneau','arizona':'phoneix',
            'arkansas':'little rock','california':'sacramento','colorado':'denver',
            'alabama':'montgeomery','alaska':'juneau','arizona':'phoneix',
            'arkansas':'little rock','california':'sacramento','colorado':'denver',
            'alabama':'montgeomery','alaska':'juneau'}

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
            quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1,states[questionNum]))
                for i in range(4):
                    quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
                    quizFile.write('\n')
                        # TODO: Write the answer key to a file
                    answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD' [answerOptions.index(correctAnswer)]))
                    quizFile.close()
                    answerKeyfile.close()
        

