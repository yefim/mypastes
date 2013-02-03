$ ->
  vKey = 86

  $('#input').keydown (e) ->
    if e.ctrlKey and (e.keyCode == vKey)
      # allow paste to finish
      setTimeout (-> $('form').submit()), 10

  $('.paste-content').each ->
    paste = $(@).text()
    $(@).html paste.replace /(http[^\s]+)/g, (str, match) -> "<a href='#{match}'>#{match}</a>"
