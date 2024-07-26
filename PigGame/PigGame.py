"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
import random

from rxconfig import config


class State(rx.State):
    """The app state."""
    score1: int = 0
    score2: int = 0
    roll1: int = 0
    roll2: int = 0
    currentInstance: int = 1
    dice: str = "/dice-6.png"
    bgCurrplayer = "rgba(255, 255, 255, 0.45)"
    bgNxtplayer = "rgba(255, 255, 255, 0.35)"
    winner = ""
    endCheck = False
    firstCheck = True

    def newCheck(self):
        if self.firstCheck == True:
            self.firstCheck = not self.firstCheck
        elif self.firstCheck == False:
            self.firstCheck = not self.firstCheck

    def newGame(self):
        self.score1 = 0
        self.score2 = 0
        self.roll1 = 0
        self.roll2 = 0
        self.currentInstance = 1
        self.dice = "/dice-6.png"
        self.bgCurrplayer = "rgba(255, 255, 255, 0.45)"
        self.bgNxtplayer = "rgba(255, 255, 255, 0.35)"
        self.winner = ""
        self.endCheck = False 

    def winnerEnd(self):
        if self.score1 >= 100:
            self.winner = 'PLAYER 1'
            self.endCheck = True                
        elif self.score2 >= 100:
            self.winner = "PLAYER 2"
            self.endCheck = True   
        else:
            pass         

    def score(self): 
        if self.currentInstance == 1:
            self.score1 += self.roll1
            self.winnerEnd()
            self.currentInstance = 2
            self.roll1 = 0
            self.bgCurrplayer = "rgba(255, 255, 255, 0.35)"
            self.bgNxtplayer = "rgba(255, 255, 255, 0.45)"
        else:
            self.score2 += self.roll2
            self.winnerEnd()
            self.currentInstance = 1  
            self.roll2 = 0 
            self.bgCurrplayer = "rgba(255, 255, 255, 0.45)"
            self.bgNxtplayer = "rgba(255, 255, 255, 0.35)" 

    def diceRoll(self):
        roll = random.randint(1,6)
        self.dice = f"/dice-{roll}.png"
        if self.currentInstance == 1:
            if roll != 1:
                self.roll1 += roll
            else:
                self.roll1 = 0
                self.currentInstance = 2
                self.bgCurrplayer = "rgba(255, 255, 255, 0.35)"
                self.bgNxtplayer = "rgba(255, 255, 255, 0.45)"
        elif self.currentInstance == 2:
            if roll != 1:
                self.roll2 += roll
            else:
                self.roll2 = 0
                self.currentInstance = 1
                self.bgCurrplayer = "rgba(255, 255, 255, 0.45)"
                self.bgNxtplayer = "rgba(255, 255, 255, 0.35)"

print()
def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.box(            
            rx.hstack(
                rx.section(
                    rx.heading("PLAYER 1",align="center",font_family="Rubik",weight="300",margin_top='50px',font_size='3rem',color='#272727'),
                    rx.text(f"{State.score1}",align="center",font_family="Rubik",weight="300",margin_top='50px',font_size='5rem',color='#036361'),
                    rx.section(
                        rx.text("CURRENT",align="center",font_family="Rubik",weight="300",font_size='2rem',color='#272727',margin_top="-20px"),
                        rx.text(f"{State.roll1}",align="center",font_family="Rubik",weight="300",font_size='2rem',color='#272727',margin_top="2px"),
                        background_color="#3686c7",
                        height= "25%",
                        border_radius="9px",  
                        width="50%", 
                        margin_top="17%",
                        margin_right='50%',
                        margin_left='25%',
                        justify='center',
                    ),                    
                    background_color=f"{State.bgCurrplayer}",                    
                    border_radius="9px 0px 0px 9px",
                    height= "95%",
                    width="65%",
                    backdrop_filter='blur(200px)',                    
                ),
                rx.section(
                    rx.heading("PLAYER 2",align="center",font_family="Rubik",weight="300",margin_top='50px',font_size='3rem',color='#272727'),
                    rx.text(f"{State.score2}",align="center",font_family="Rubik",weight="300",margin_top='50px',font_size='5rem',color='#036361'),
                    rx.section(
                        rx.text("CURRENT",align="center",font_family="Rubik",weight="300",font_size='2rem',color='#272727',margin_top="-20px"),
                        rx.text(f"{State.roll2}",align="center",font_family="Rubik",weight="300",font_size='2rem',color='#272727',margin_top="2px"),
                        background_color="#3686c7",
                        height= "25%",
                        border_radius="9px",  
                        width="50%", 
                        margin_top="17%",
                        margin_right='50%',
                        margin_left='25%',
                        justify='center',
                    ),
                    background_color=f"{State.bgNxtplayer}",
                    border_radius="0px 9px 9px 0px",
                    height= "95%",
                    width="65%",
                    backdrop_filter='blur(200px)',           
                ),
                rx.dialog.root(
                    rx.dialog.content(
                        rx.dialog.title("Rules",color='#272727'),
                        rx.dialog.description(
                            """Each turn, a player repeatedly rolls a die until either a 1 is rolled or the 
player decides to "hold":r
* If the player rolls a 1, they score nothing and it becomes the next 
  player's turn.
* If the player rolls any other number, it is added to their turn total and the 
  player's turn continues.
* If a player chooses to "hold", their turn total is added to their score, and it 
  becomes the next player's turn.
The first player to score 100 or more points wins.
Enjoy! 😊""",
                            color='#272727',
                            white_space="pre",
                        ),
                        rx.dialog.close(
                            rx.button(
                                "Close",
                                on_click=State.newCheck, 
                                color='#444', 
                                border_radius="50rem", 
                                size="3",
                                background_color= "rgba(255, 255, 255, 0.6)",
                                backdrop_filter= "blur(10px)",
                                ),
                        ),
                        background_color="#169aa6",                      
                    ),    
                    open=State.firstCheck,                                
                ),                  
                rx.dialog.root(
                    rx.dialog.content(
                        rx.dialog.title(f"The Game has ended and the winner is {State.winner}",color='#272727'),
                        rx.dialog.description(
                            "Thank you for Playing! 😊",
                            color='#272727',
                        ),
                        rx.dialog.close(
                            rx.button(
                                "🔄 NEW GAME",
                                on_click=State.newGame, 
                                color='#444', 
                                border_radius="50rem", 
                                size="3",
                                background_color= "rgba(255, 255, 255, 0.6)",
                                backdrop_filter= "blur(10px)",
                                ),
                        ),
                        background_color="#169aa6",                      
                    ),    
                    open=State.endCheck,                                
                ),                                
                gap='0em',
                height="100vh",
                width="100%",
                justify='center',           
            ),
            rx.button(
                "🔄 NEW GAME",  
                on_click=State.newGame,              
                position="absolute",
                top="15%",
                left="50%",
                transform="translate(-50%, -50%)",
                z_index="1",
                color='#444',
                border_radius="50rem",
                font_size="1.2rem",
                background_color= "rgba(255, 255, 255, 0.6)",
                backdrop_filter= "blur(10px)",
                width="12%",
                height="3rem",
                box_shadow= "0 2rem 5rem rgba(0, 0, 0, 0.2)",
            ),  
            rx.button(
                "🎲 ROLL DICE",
                on_click=State.diceRoll,
                position="absolute",
                top="67%",
                left="50%",
                transform="translate(-50%, -50%)",
                z_index="1",
                color='#444',
                border_radius="50rem",
                font_size="1.2rem",
                background_color= "rgba(255, 255, 255, 0.6)",
                backdrop_filter= "blur(10px)",
                width="12%",
                height="3rem",
                box_shadow= "0 2rem 5rem rgba(0, 0, 0, 0.2)",
            ), 
            rx.button(
                "📥 HOLD",
                on_click=State.score,
                position="absolute",
                top="77%",
                left="50%",
                transform="translate(-50%, -50%)",
                z_index="1",
                color='#444',
                border_radius="50rem",
                font_size="1.2rem",
                background_color= "rgba(255, 255, 255, 0.6)",
                backdrop_filter= "blur(10px)",
                width="12%",
                height="3rem",
                box_shadow= "0 2rem 5rem rgba(0, 0, 0, 0.2)",
            ),     
            rx.image(
                f"{State.dice}",
                position="absolute",
                top="35%",
                left="50%",
                transform="translate(-50%, -50%)",
                z_index="1",
                width="125px",
                height="125px",
                box_shadow= "0 2rem 5rem rgba(0, 0, 0, 0.2)",
            ),
            rx.dialog.root(
                rx.dialog.title(f"The Game has ended and the winner is {State.winner}"),
                rx.dialog.description(
                    "Thank you for Playing! 😊",
                ),
                rx.dialog.close(
                    rx.button("🔄 NEW GAME",on_click=State.newGame, size="3"),
                ),
                top="35%",
                left="50%",    
                transform="translate(-50%, -50%)",                
                z_index="1",                 
            ),                                                                      
        ),      
        height='100vh', 
        overflow="hidden",  
    )

style = {
    "background-image":"linear-gradient(to top left, #366582 0%, #2ebf94 100%)",
}
app = rx.App(style=style,
             stylesheets=[
        "https://fonts.googleapis.com/css2?family=Rubik:ital,wght@0,300..900;1,300..900&display=swap",
    ],
)
app.add_page(index)
