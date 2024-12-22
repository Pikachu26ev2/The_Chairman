REQUIREMENTS:
-Python 3.8 or later
-Tkinter (Library)
-Time (Library)



This is how it works:


Add a character:

1-Add your character's png to "char", rename it to _# replace # with its id (Recommend using 1, 2, 3... for idle and 1a, 1b, 1c... for character's current state)

2-In "names.txt" add the name of your character, following the character's id


Add a background:

1-Add your background in png format in "background", name it _1.png, _2.png, _3.png...
Please use a 720x960 image


Make your own story:

A ".tronsky" file is the format that this engine uses, edit it as a text.

It is made of sections divided by "|", when you're done, rename it to "story.tronsky"

Start - STR

End - end

Text - text
It's format is text|character1|character2|character3|speaker|text|
Replace character# with the character's id (example 1 = _1.png 4b = _4b.png) leave a 0 for empty, the speaker is the one that speaks, use its id, if in a special state (1a, 1b, 1c...) use idle (1, 2, 3...), the text is what the characters says.
Example:
text|1c|0|8d|1|Hello World|

Change background - bg
Change the background, use bg followed by background id
bg|5|

Example of story.tronsky:
STR|bg|0|text|0|0|0|1|Paragraph of text, press SPACE to continue|text|0|0|0|1|this is a demo, press space|end|

Settings:
In settings.txt, the order is:
Screen Width (Not working, don't change)
Your Name (Credit yourself)
Text Speed (0 = instant 0.01 = fast 0.1 = slow 1 = very slow, time is in seconds)
