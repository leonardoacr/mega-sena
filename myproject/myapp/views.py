from django.shortcuts import render
import scripts


def run_script(request):
    result = scripts.run()
    your_game = result[0]
    correct_guesses = result[1]
    past_result = result[2]
    game_number = result[3]
    data = result[4]
    type_of_prize = result[5]

    render_object = {'your_game': your_game, 'correct_guesses': correct_guesses,
                     'game_number': game_number, 'past_result': past_result, 'data': data, 'type_of_prize': type_of_prize}

    return render(request, 'script_result.html', render_object)
# your_game, correct_guesses, past_result, game_number, data, type_of_prize
