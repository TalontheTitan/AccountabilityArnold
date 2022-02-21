import re

def process_message(message, response_array, response):
    #splits the message and the punctuation into an array
    list_message = re.findall(r"[\w']+|[.,!?;]", message.lower())

    #score the amount of words
    score = 0
    for word in list_message:
        if word in response_array:
            score = score + 1

    #returns the response and the score of the response
    # print(score, response)
    return [score, response]

def get_response(message):
    #adding custom responses
    response_list =[
        process_message(message, ['hello', 'hi', 'hey', 'sup'], 'Hey There'),
        process_message(message, ['bye', 'goodbye',], 'Take Care'),
        process_message(message, ['help', 'me'],"Use Command /help"),
        process_message(message, ['your', 'name'], 'My name is Arnold, I\'m from the Accountability Department'),
        process_message(message, ['purpose','function','do'], 'I check in with you daily about physical activity'),
        process_message(message, ['no'], 'That\'s okay, You can try again Tomorrow' ),
        process_message(message, ['yes'], 'Congratulation\'s on working out, Keep up the Good Work')
        #enter more responses here
    ]

    #checks all of the responses and returns the best matching response
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    #get the max value for the best response and store it in a var
    winning_response = max(response_scores)
    matching_response = response_list[response_scores.index(winning_response)]

    #return the winning response to the user
    if winning_response ==0:
        bot_response = 'I didn\'t understand what you wrote'
    else:
        bot_response = matching_response[1]

    #print('Bot response:', bot_response)
    return bot_response


#testing
#get_response('can you help me?')