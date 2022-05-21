
moves = ['Scissors','Fire','Rock','Gun','Lightning','Devil','Dragon','Water','Air','Paper','Sponge','Wolf','Tree','Human','Snake']
loses_to = { 
        "Scissors": {"Fire","Rock","Gun","Lightning","Devil","Dragon","Water"},
        "Fire": {"Rock","Gun","Lightning","Devil","Dragon","Water","Air"},
        "Rock": {"Gun","Lightning","Devil","Dragon","Water","Air","Paper"},
        "Gun": {"Lightning","Devil","Dragon","Water","Air","Paper","Sponge"},
        "Lightning": {"Devil","Dragon","Water","Air","Paper","Sponge","Wolf"},
        "Devil": {"Dragon","Water","Air","Paper","Sponge","Wolf","Tree"},
        "Dragon": {"Water","Air","Paper","Sponge","Wolf","Tree","Human"},
        "Water": {"Air","Paper","Sponge","Wolf","Tree","Human","Snake"},
        "Air": {"Paper","Sponge","Wolf","Tree","Human","Snake","Scissors"},
        "Paper": {"Sponge","Wolfe","Tree","Human","Snake","Scissors","Fire"},
        "Sponge": {"Wolf","Tree","Human","Snake","Scissors","Fire","Rock"},
        "Wolf": {"Tree","Human","Snake","Scissors","Fire","Rock","Gun"},
        "Tree": {"Human","Snake","Scissors","Fire","Rock","Gun","Lightning"},
        "Human": {"Snake","Scissors","Fire","Rock","Gun","Lightning","Devil"},
        "Snake": {"Scissors","Fire","Rock","Gun","Lightning","Devil","Dragon"},
    }

def play(player1_move, player2_move):
    if player2_move in loses_to[player1_move]:
        print (f"{player2_move} wins")
    if player1_move in loses_to[player2_move]:
        print (f"{player1_move} wins")
    else:
        print("tie")



    