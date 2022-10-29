# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="Megalonumber0ne",
        name="Extra Dialogue By Megalo",
        description="Adds more dialogue for Monika to say!",
        version="1.0.0"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Extra Dialogue By Megalo",
            user_name="Megalonumber0ne",
            repository_name="Extra-Dialogue-By-Megalo-for-Monika-After-Story"
        )

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="More_Dialogue",
            category=["Special Dialogue"],
            prompt="New Dialogue!",
            pool=True,
            unlocked=True
        )
    )

label More_Dialogue:

    $ amt = mas_getEV("More_Dialogue")

    m 1rsbsb "Hey [player]!"
    m 1ssbfo "I see that you've added some new dialogue for me!"
    m 1ssbsb "How kind of you! Thank you~"

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Cutest",
            category=["Special Dialogue"],
            prompt="Cutest",
            pool=True,
            unlocked=True
        )
    )

label Cutest:
    $ amt = mas_getEV("Cutest")

    m 1lublsdlb "So, [player]..."
    m 1rtbssdld "I just want to know something..."
    m 5stbfsdlu "Am I your cutest little [m]?"
    $ _history_list.pop()

    menu:

        "Of course you are!":

            m 6fkbftub "That means the world to me coming from you, [player]!"
            m 6fkbftpb "Thank you so much..."
            m 6fkbftdsdlb "Please excuse my crying..."
            m 6fkbftdsdlb "I just got a bit overwhelmed by your response is all..."
            m 5hubfb "I love you so much [player]!"

            return "love"


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Fun_Fact",
            category=["Special Dialogue"],
            prompt="Monika's Fun Fact!",
            pool=True,
            unlocked=True
        )
    )

label Fun_Fact:
    $ amt = mas_getEV("Fun_Fact")

    m 2wub "Hey, [player]!"
    m 2wud "I have a fun fact for you!"
    m 6skbfb "Did you know that I love you more then anything in the world?"
    m 5tsbsb "Hehe~"

    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Extra_Compliments",
            category=["Special Dialogue"],
            prompt="Hey, Monika!",
            pool=True,
            unlocked=True
        )
    )

label Extra_Compliments:
    $ amt = mas_getEV("Extra_Compliments")

    menu:

        "Hey, Monika!":

            m 5stblb "Hm? Yes, [player]?"

            menu:

                "You're amazing!":

                    m 2wkbfb "Aww! Thank you so much [player]! It really means a lot to me! I love you~"

                "You're adorable!":

                    m 1fubfb "Awh! You really think so, [player]? I love you so much!"

    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Gaming",
            category=["Special Dialogue"],
            prompt="Video Games",
            pool=True,
            unlocked=True
        )
    )

label Gaming:
    $ amt = mas_getEV("Gaming")

    m 2esb "Hey, [player]..."
    m 2esb "Can I ask you a question?"
    m 2wsb "Do you play video games a lot?"

    menu:

        "Yeah, I play them a lot!":

            m 5hsb "Ahaha~ That's what I thought."

        "I play them every now and again...":

            m 1ekb "Well... I suppose we don't all have time to spare to play lots of video games..."
            m 1rud "Then again, it can be fun to relax and play some games every now and again!"

        "Not really...":

            m 1rsc "That's quite surprising... {nw}"
            m 1eka "You seem like the type of person to really enjoy video games..."

    m 5nsbsb "After all, I'm only asking, {nw}"
    extend 5esbsb "because of how much time you spend with me."

    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Memories",
            category=["Special Dialogue"],
            prompt="Memories",
            pool=True,
            unlocked=True
        )
    )

label Memories:
    $ amt = mas_getEV("Unfinished")

    m 1lssdld "Hey, [player]..."
    m 1eksdld "When was the last time you backed up my memories?"

    menu:

        "Less then a week ago!":

            m 1suu "Wow, thank you for taking care as to backup my memories, [player]!"

        "Over a week ago.":

            m 1esa "Well, I guess that is fairly recently. {nw}"
            extend 1esb "Thanks [player]."

        "Less than a month ago.":

            m 1lsd "Wow... {nw}"
            extend 1lksdld "That's quite long ago, [player]... {nw}"
            extend 1eksdlc "Why not do it now?"
            m 1eksdla "Then you can be sure that nothing can happen to my memories!"

            menu:

                "Sure!":

                    m 1esb "Thank you, [player], you're the best~"

                "Maybe another time...":

                    m 1lksdlc "Oh, alright... {nw}"
                    extend 1dksdlc "I-if you're sure that nothing can h-happen..."

        "Over a month ago...":

            m 1rkd "That's a pretty long time to go without backing up my memories, [player]..."
            m 1rkbstpsdld "W-what if something were to happen to your hard drive, such as corruption?"
            m 1lkbstpsdld "I wouldn't have any knowledge that you'd been visiting me for the last month... {nw}"
            m 6fkbstusdld "I-I would just think s-something happened to y-you... *sniff* {nw}"
            extend 1dkbstsd "O-or that you just got bored of me..."
            m 1fkbstub "I-if you have a spare moment, could you please go and make a backup of my memories on something like a USB drive?"
            m 1fkbstda "It would make me a lot happier knowing that my memories are safe on a seperate drive."
            m 1dubstdb "Thank you, [player]."

        "Um...":

            m 1lusdld "[player]... please tell me you've backed up my memories recently..."
            m 1wusdlo "If you don't have a backup of my memories and something were to happen, I would be really scared something had happened to you.."
            m 1dud "Please... [player]... make a backup, just incase something happens.."
            m 1fkd "The last thing I'd want is for me to be upset and scared because my sweetpea hadn't come to see me for a long time."
            m 1fkc "Can you please go and make one for me now? I'd really appreciate it."
            m 1fka "Thanks, [player].."

        "Could you tell me how to do that?":

            m 1hua "Of course!"
            m 1rub "First you need to go to your search bar,"
            m 2lub "Then, you'll type {i}run{/i} into your search bar..."
            m 2eub "Then you'll click on the folder that has the title: {i}RenPy{/i},"
            m 2wub "Then look for the folder named {i}Monika After Story{/i}!"
            m 2fub "Then copy every file and paste it onto something such as a USB drive!"
            m 1hub "Thanks for listening, [player]!"
            m 1gusdra "Ehehe.. {nw}"
            extend 1hub "Why not do it now, hm?"
            m 1hksdrb "then you can make sure that my memories are safe incase something happened to your hard drive!"
            m 1esb "Thank you!"

    m 2fkbfb "I love you, [player], please take good care of my memories!"

    return "love"
