def player(prev_opponent_play, opponent_history=[], play_order={}, count=[0]):
  if count[0] % 1000 == 0:
    opponent_history = []
    play_order = {}

  count[0] += 1

  if not prev_opponent_play:
    prev_opponent_play = 'R'

  opponent_history.append(prev_opponent_play)

  n = 4
  ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

  if (len(opponent_history) < n):
    prediction = max(opponent_history, key=opponent_history.count)
    return ideal_response[prediction]
  
  last_n_plays = "".join(opponent_history[-n:])

  if last_n_plays not in play_order:
    play_order[last_n_plays] = 1
  else:
    play_order[last_n_plays] += 1

  last_n_minus_1_plays = last_n_plays[1:]

  potential_plays = [
    last_n_minus_1_plays + "R",
    last_n_minus_1_plays + "P",
    last_n_minus_1_plays + "S",
  ]

  sub_order = {
    k: play_order[k] if k in play_order else 0
    for k in potential_plays
  }

  prediction = max(sub_order, key=sub_order.get)[-1]

  return ideal_response[prediction]