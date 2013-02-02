$ ->
  vKey = 86

  $('#input').keydown (e) ->
    if e.ctrlKey and (e.keyCode == vKey)
      # allow paste to finish
      setTimeout (-> $('form').submit()), 10
