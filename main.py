print('''
                                  ___                                         
                              .-"    `-.      ,                               
                            .'          '.   /j\                              
                           /              \,/:/#\                /\           
                          ;              ,//' '/#\              //#\          
                          |             /' :   '/#\            /  /#\         
                          :         ,  /' /'    '/#\__..--""""/    /#\__      
                           \       /'\'-._:__    '/#\        ;      /#, """---
                            `-.   / ;#\']" ; """--./#J       ':____...!       
                               `-/   /#\  J  [;[;[;Y]         |      ;        
""""""---....             __.--"/    '/#\ ;   " "  |     !    |   #! |        
             ""--.. _.--""     /      ,/#\'-..____.;_,   |    |   '  |        
                   "-.        :_....___,/#} "####" | '_.-",   | #['  |        
                      '-._      |[;[;[;[;|         |.;'  /;\  |      |        
                      ,   `-.   |        :     _   .;'    /;\ |   #" |        
                      !      `._:      _  ;   ##' .;'      /;\|  _,  |        
                     .#\"""---..._    ';, |      .;{___     /;\  ]#' |__....--
          .--.      ;'/#\         \    ]! |       "| , """--./_J    /         
         /  '%;    /  '/#\         \   !' :        |!# #! #! #|    :`.__      
        i__..'%] _:_   ;##J         \      :"#...._!   '  "  "|__  |    `--.._
         | .--""" !|""""  |"""----...J     | '##"" `-._       |  """---.._    
     ____: |      #|      |         #|     |          "]      ;   ___...-"T,  
    /   :  :      !|      |   _______!_    |           |__..--;"""     ,;MM;  
   :____| :    .-.#|      |  /\      /#\   |          /'               ''MM;  
    |""": |   /   \|   .----+  ;      /#\  :___..--"";                  ,'MM; 
   _Y--:  |  ;     ;.-'      ;  \______/#: /         ;                  ''MM; 
  /    |  | ;_______;     ____!  |"##"""MM!         ;                    ,'MM;
 !_____|  |  |"#"#"|____.'""##"  |       :         ;                     ''MM  
  | """"--!._|     |##""         !       !         :____.....-------"""""" |'
  |          :     |______                        ___!_ "#""#""#"""#"""#"""|  
__|          ;     |MM"MM"""""---..._______...--""MM"MM]                   |   
  "\-.      :      |#                                  :                   |  
    /#'.    |      /##,                                !                   |  
   .',/'\   |       #:#,                                ;       .==.       |  
  /"\'#"\',.|       ##;#,                               !     ,'||||',     |  
        /;/`:       ######,          ____             _ :     M||||||M     |  
       ###          /;"\.__"-._   """                   |===..M!!!!!!M_____|  
                           `--..`--.._____             _!_                    
                                          `--...____,="_.'`-.____  
''')
print("Welcome to Vampire Castle.")
print("Your mission is to find the lost sword of Oriath.\n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input("You are at lake nearby the great castle of Oriath. Home to vampires of the most vile ilk, who suck the blood of man and feast on the bones of children. You were given the task by your lord to find the wicked vampire Oriath's sword as it is said that this is the only way to defeat him. You are by the great lake of the titans, the water looks refreshing you think. Shall you go for a quick swim? or proceed to the castle on your task? type 'swim' or 'castle' to choose.\n ").lower()

if choice1 == 'castle':
  print(" ")
  print("You decided to go the castle and continue with your quest.\n")
  choice2 = input("You arrive at the castle doors. They are like large black iron walls. They open as you lay a hand on them. You enter the gothic structure with slight fear. As you enter Oriath himslef appears in front of you. 'Here to take my head are we?'Do you fight this beast or flee to further inside the castle? type 'fight' or 'flee' to choose.\n").lower()
  if choice2 == 'flee':
    choice3 = input("You choose to flee! Smart, you run begind the vmapire lord into the depths of the castle, dodging traps and vampires galore, you finally come to three doors. Black, White and Grey. What do you choose? type your answer.\n ").lower()
    if choice3 == 'black':
      print(" ")
      print("Black.....you open the door and are met with an axe coming down onto your head and splits you in two. GAME OVER")
    elif choice3 == 'white':
      print("")
      print("White.....You open the white door and ae met with a female vampire that leaps towards you and bites on your neck draining your blood. GAME OVER")
    else:
      print(" ")
      print("Grey....You find Oriaths sword and go back to slay the beast with one strike, YOU WIN")
  else:
    print(" ")
    print("You choose to fight! but you are no match without the sword. Oriath the vampire lord strikes you down quick. He then leaps to your neck and drains your blood. GAME OVER")
else: 
  print(" ")
  print("You enter the cold dark lake. The water hits splashes up on your face, your mind starts to wander back to the past when you were but a child at the beach with friends. You remember swimming in the sea of Kings and how fun it was...suddenly you are pulled from this memory back to the present as something grabs your foot. You struggle and scream until it pulls you under. GAME OVER")

