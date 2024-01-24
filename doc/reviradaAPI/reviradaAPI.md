* Using the Revirada API
  Translation engine
  Revirada has an API through which you can integrate machine translation into your programs and applications. 
  To query it, you can send the parameters by POST method using the URL https://api.revirada.eu/translate_string.

  * To use the Revirada API, you need an API key. 
   If you would like to obtain one, contact Lo Congrès: info@locongres.org.

  * The parameters required to query the API are:

   “api_key”: your API key
   “engine”: “apertium”
   “content_type”: the type of content you are sending for translation (“txt”, “html”, “xml”,"po","org","md")
   “text”: the content to translate, in the form of a character string
   “source_language”: the language of the text to be translated (“fra” for French, [[“oci_gascon”]] for Gascon Occitan, [[“oci”]] for Languedoc Occitan, "eng" for British English, [["eng_us"]] for American English)
   “target_language”: the language of the translation ([[“fra”]] for French, [[“oci_gascon”]] for Gascon Occitan, [[“oci”]] for Languedoc Occitan, "eng" for British English, [["eng_us"]] for American English)

   Please note, the possible translation pairs are French-Occitan Gascon, French-Occitan Languedoc, Occitan Gascon-French, Occitan Languedoc-French, British English-Gascon Occitan, British English-Languedoc Occitan, American English-Gascon Occitan, American English-Languedoc Occitan.
   Other occitan dialect translations could be developped later.

* You get a response like:

```
{

"original_text": "",
"translated_text": "",
"words": "", #number of words translated
"execution_time": "73.4", #execution time in seconds

}
``
