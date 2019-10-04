# Lab 4: A simple weather app

The app displays weather and temperature for the selected city and country, including the possibility to change the temperature units between celsius and fahrenheit. The default unit is celsius. The app accepts both "metric", "imperial", "celsius" and "fahrenheit" as units. Examples of utterances are in interaction_tests_eng.txt.

## Enable RASA

RASA is enabled and test examples can be found in RASA.txt and RASA_tests.txt. There are tests for RASA in the interaction_tests_eng.txt file. The finished output for tests without RASA are in sucess.txt and with RASA enabled in success_RASA.txt. 
I did several test using thanks, plese by changing the letters for city and country. 
When making a request, it's possible to use please in the end of the utterance, but not thanks. Saying "weather please" and "whats the weather in gothenburg please" worked. It did however not work to say "Gothenburg please" when replying to the question "what city?" I tried chaning London to Londin and Londen, and Sweden to Swiden and Sweeden but it could never understand, it repeated the question about which county. I also changed or removed some characters in Gotheburg but it could never understand.

## Assessment

The lab was a good way of learning about how to deal with API:s for the upcoming project, it seemed to be a reasonable sized assignment. If you have used API before though it wasn't very hard. I'm not sure if I did the RASA test correctly, it would have been nice to get a little more instructions to know if you suceeeded or not. The tests sometime gave different results and I don't know if that's the point of if it's because it's unstable.
