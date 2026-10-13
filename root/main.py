# Choose Your Own Adventure - The Midnight Bakery

user_choice = None

story = """
THE MIDNIGHT BAKERY

Chef Marisol is working the night shift at her bakery.

Suddenly the big oven starts to hum.

The clock says 3:00 AM.

The oven is glowing and there are sparkly flour footprints
on the floor that lead out the back door.

A : Open the oven and look inside.
OR
B : Follow the footprints out the back door.
"""

print(story)

user_choice = input()

user_choice = user_choice.lower()

# choice 1
if user_choice == "a":
    story = """
Marisol opens the oven.

Inside there is a tiny dragon the size of a loaf of bread!

It is roasting a marshmallow.

A : Give the dragon some sourdough bread.
OR
B : Put the dragon in a mixing bowl.
"""
    print(story)

    user_choice = input().lower()

    # choice 2 (after opening the oven)
    if user_choice == "a":
        story = """
The dragon eats the bread and purrs.

It points at all the empty trays on the counter.

A : Give the dragon a name.
OR
B : Ask the dragon to help you bake.
"""
        print(story)

        user_choice = input().lower()

        # choice 3
        if user_choice == "a":
            story = """
Marisol names the dragon Crumb.

Crumb is so happy that it sneezes sparkles everywhere.

The bakery becomes famous for having a dragon and there
is a huge line outside.

THE END (Ending 1: The Mascot)
"""
            print(story)
        else:
            story = """
Crumb breathes fire on the trays and everything bakes perfectly.

The bread is golden and the cinnamon rolls are amazing.

Marisol wins the Golden Whisk Award.

THE END (Ending 2: The Perfect Bake)
"""
            print(story)

    else:
        story = """
The dragon does NOT like the bowl.

It jumps out and flies to the top shelf and glares at Marisol.

A : Say sorry and give it a cookie.
OR
B : Use a spatula to chase it out the window.
"""
        print(story)

        user_choice = input().lower()

        # choice 3
        if user_choice == "a":
            story = """
The dragon eats the cookie and forgives her.

It leaves a shiny scale on the counter and flies away.

Marisol sells the scale to a museum and buys a bigger oven.

THE END (Ending 3: The Shiny Scale)
"""
            print(story)
        else:
            story = """
The dragon gets mad and breathes fire on all the bread.

Every loaf turns into charcoal.

Marisol sells it as extra crispy toast and people love it.

THE END (Ending 4: Extra Crispy)
"""
            print(story)

else:
    story = """
Marisol follows the footprints down a dark alley.

They stop at a little green door.

A sign says:

GUILD OF MIDNIGHT BAKERS

She can hear laughing and smell cinnamon inside.

A : Knock on the door.
OR
B : Sneak to the window and peek inside.
"""
    print(story)

    user_choice = input().lower()

    # choice 2 (after following the footprints)
    if user_choice == "a":
        story = """
A baker in a cape opens the door.

"Chef Marisol! We have been waiting for you!
Tonight is the Midnight Bake-Off and we need one more chef."

A : Join the bake-off.
OR
B : Be a judge instead.
"""
        print(story)

        user_choice = input().lower()

        # choice 3
        if user_choice == "a":
            story = """
Marisol bakes her grandma's secret recipe.

The judges take one bite and give her the trophy.

THE END (Ending 5: The Champion)
"""
            print(story)
        else:
            story = """
Marisol gets a giant spoon and tastes fifty desserts.

She makes new friends and gets a really bad stomachache.

It was totally worth it.

THE END (Ending 6: The Happy Judge)
"""
            print(story)

    else:
        story = """
Marisol looks through the window.

All the bakers turn around and stare at her.

One of them holds up a rolling pin.

"A SPY!" they yell.

A : Run back to the bakery.
OR
B : Wave and say hi.
"""
        print(story)

        user_choice = input().lower()

        # choice 3
        if user_choice == "a":
            story = """
Marisol runs back and locks the door.

The next morning there is a tiny cake outside with a note.

The note says: NEXT TIME JUST KNOCK.

THE END (Ending 7: The Warning Cake)
"""
            print(story)
        else:
            story = """
Marisol waves.

The bakers laugh and pull her inside.

The rolling pin was just for a pinata.

They make her an honorary member and the party lasts all night.

THE END (Ending 8: The Honorary Member)
"""
            print(story)