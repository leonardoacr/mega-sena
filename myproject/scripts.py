import main
import verify_guesses


def run():
    random_play = main.create_random_play(10)
    result = verify_guesses.verify_guesses(random_play)
    your_game = 'Seu jogo: ' + str(random_play)
    correct_guesses = 'Você acertou: ' + str(result[0]) + ' números.'
    type_of_prize = 'Prêmio: ' + str(result[4])
    if result[0] >= 4:
        past_result = 'Resultado passado: ' + str(result[1])
        game_number = 'Você ganhou um prêmio no jogo de número: ' + \
            str(result[2])
        data = 'Data: ' + str(result[3])
    else:
        past_result = ''
        game_number = ''
        data = ''
        type_of_prize = ''

    return your_game, correct_guesses, past_result, game_number, data, type_of_prize
