import random
import textwrap

# ASCII art cats
CATS = [
    r"""
    |\---/|
    | o_o |
     \_^_/
    """,
    r"""
     /\_/\
    ( o.o )
     > ^ <
    """,
    r"""
        |\__/,|   (`\
      _.|o o  |_   ) )
    -(((---(((--------
    """,
    r"""
          |\      _,,,---,,_
    ZZZzz /,`.-'`'    -.  ;-;;,_
         |,4-  ) )-,_. ,\ (  `'-'
        '---''(_/--'  `-'\_)  Felix Lee 
    """,
    r"""
     _._     _,-'""`-._
    (,-.`._,'(       |\`-/|
        `-.-' \ )-`( , o o)
              `-    \`_`"'-
    """,
    r"""
          \    /\
           )  ( ')
          (  /  )
    jgs    \(__)|
    """,
    r"""
     /\_/\
    ( o o )
    ==_Y_==
      `-'
    """,
    r"""
     |\__/,|   (`\
     |_ _  |.--.) )
     ( T   )     /
    (((^_(((/(((_/
    """,
    r"""
        /\_/\           ___
       = o_o =_______    \ \  -Julie Rhodes-
        __^      __(  \.__) )
    (@)<_____>__(_____)____/
    """,
    r"""
      ^~^  ,
     ('Y') )
     /   \/ 
    (\|||/) hjw
    """,
    r"""
    ("`-''-/").___..--''"`-._
     `6_ 6  )   `-.  (     ).`-.__.`) 
     (_Y_.)'  ._   )  `._ `. ``-..-' 
       _..`--'_..-_/  /--'_.'
      ((((.-''  ((((.'  (((.-' 
    """,
    r"""
               __..--''``---....___   _..._    __
     /// //_.-'    .-/";  `        ``<._  ``.''_ `. / // /
    ///_.-' _..--.'_    \                    `( ) ) // //
    / (_..-' // (< _     ;_..__               ; `' / ///
     / // // //  `-._,_)' // / ``--...____..-' /// / //
    """,
    r"""
       _
    |\'/-..--.
   / _ _   ,  ;
  `~=`Y'~_<._./
   <`-....__.'  fsc
    """,
    r"""
    /\_/\  (
   ( ^.^ ) _)
     \"/  (
   ( | | )
   (__d b__)
    """,
    r"""
       ,-''''''''-.
    /\___/\  (  \`--.
   hjw  \`@_@'/  _)  >--.`.
       _{.:Y:_}_{{_,'    ) )
      {_}`-^{_} ```     (_/
    """,
    r"""
                       /)
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
    hjw ----------{_}^-'{_}----------
    """,
    r"""
      _  ,/|
     '\`o.O'   _
      =(_*_)= (
        )U(  _)
       /   \(
      (/`-'\)
    """,
    r"""
        ,-. __ .-,
      --;`. '   `.'
       / (  ^__^  )
      ;   `(_`'_)' \
      '  ` .`--'_,  ;
    ~~`-..._)))(((.'
    """,
    r"""
       |\---/|
       | ,_, |
        \_`_/-..----.
     ___/ `   ' ,""+ \  sk
    (__...'   __\    |`.___.';
      (_,...'(_,.`__)/'.....+
    """,
]


def meowspeak(message, cat_index=None, width=40):
    """
    Displays a message "spoken" by an ASCII cat.

    :param message: The message to be displayed.
    :param cat_index: Index of the cat to use, or None to pick one at random.
    :param width: The width to wrap the message.
    """
    # Wrap the message
    wrapped_message = textwrap.fill(message, width=width)

    # Generate speech bubble
    lines = wrapped_message.splitlines()
    max_length = max(len(line) for line in lines)
    top_border = " " + "_" * (max_length + 2)
    bottom_border = " " + "-" * (max_length + 2)

    if len(lines) == 1:
        bubble_lines = f"< {lines[0]} >"
    else:
        bubble_lines = "\n".join(
            (
                f"/ {line.ljust(max_length)} \\"
                if i == 0
                else (
                    f"| {line.ljust(max_length)} |"
                    if i < len(lines) - 1
                    else f"\\ {line.ljust(max_length)} /"
                )
            )
            for i, line in enumerate(lines)
        )

    speech_bubble = f"{top_border}\n{bubble_lines}\n{bottom_border}"

    # Select the cat
    if cat_index is None:
        cat_index = random.randint(0, len(CATS) - 1)
    cat = CATS[cat_index]

    # Combine speech bubble and cat
    print(f"{speech_bubble}\n{cat}")


def list_cats():
    """Lists all available cats with their index."""
    for index, cat in enumerate(CATS):
        print(f"Cat {index}:\n{cat}\n{'-' * 40}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="meowspeak: Cats that say things!")
    parser.add_argument("message", nargs="?", help="The message for the cat to say.")
    parser.add_argument(
        "--cat", type=int, help="The index of the cat to use (0-based)."
    )
    parser.add_argument(
        "--width", type=int, default=40, help="Width of the message bubble."
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available cats with their indices.",
    )
    args = parser.parse_args()

    if args.list:
        list_cats()
    elif args.message:
        meowspeak(args.message, args.cat, args.width)
    else:
        parser.print_help()
