import streamlit as st
import streamlit_extras.let_it_rain
from streamlit_extras.card import card
import streamlit_extras.theme
import streamlit_shadcn_ui as ui
import streamlit_antd_components as sac
import os



r1col1, r1col2, r1col3 = st.columns([1, 2, 1])
r2col1, r2col2, r2col3 = st.columns([1, 2, 0.5])


nav_pages = ["Notes", "PMAQ", "Chat"]
selected_page = st.sidebar.radio("Navigation", nav_pages)







# Display content based on the selected page
if selected_page == nav_pages[0]:
    st.subheader("Welcome to the OMS Latin Website!")
    st.write("Nil sine magnō labore — Nothing without great labor (Brooklyn)")

    for i in range(10):
        st.write("")
    
    st.header("Ecce Romani")
    card(title="Chapter 4", text="Ecce Romani")


if selected_page == nav_pages[1]:
        st.title("Latin PMAQ")
        st.write("Daily Phrase or Quote")
        st.write("")
        st.write("")
        st.write("")
        st.write("")


    
        st.write("Notā bene — Note well")
        st.write("Et cetera (etc.) — And the rest")
        st.write("Et alia (et al.) — And the others")
        st.write("Ante meridiem (a.m.) — Before mid day")
        st.write("Post meridiem (p.m.) — After midday")
        st.write("Senatus Populusque Romanus (SPQR) — The Senate and People of Rome")
        st.write("Ab urbe conditā (A.U.C.) — From the founding of the city (Rome, 753 BCE)")
        st.write("Ex nihilō nihil fit — Nothing comes from nothing")
        st.write("Id est (i.e.) — That is")
        st.write("Modus operandī (M.O.) — Way of operating")
        st.write("Circa (c. or c.a.) — Around")
        st.write("Pro tempore (pro tem.) — For the time being")
        st.write("Nihil per os (n.p.o.) — Nothing through the mouth")
        st.write("Veritas — Truth (Harvard)")
        st.write("Lux et veritas — Light and truth (Yale)")
        st.write("Nil sine magnō labore — Nothing without great labor (Brooklyn)")
        st.write("Vox clamantis in desertō — The voice of one calling out in the desert (Motto of Dartmouth)")
        st.write("Esse quam viderī — To be rather than to seem (Motto of North Carolina)")
        st.write("Ad astra per aspera — To the stars through difficulties (Motto of Kansas)")
        st.write("Labor omnia vincit — Work conquers all (Motto of Oklahoma)")
        st.write("Dirigō — I lead (Maine)")
        st.write("Excelsior — Ever Upward (New York)")
        st.write("Veritas Vos liberabit — The truth will set you free (John Hopkins University)")
        st.write("Sapientia et suā et docendī causā — Knowledge for both its own sake and for teaching (University of Albany)")
        st.write("Labor omnia vincit — Work conquers all (Motto of Oklahoma)")
        st.write("Lo Saturnalia! — Hey Saturnalia!")
        st.write("Diēs festus — Holiday")
        st.write("Saturnalibus optimō dierum — …on Saturnalia, the best of days")
        st.write("Dum Spiro Spero — While I breathe I hope (Motto of South Carolina)")
        st.write("Ditat Deus — God Enriches (Motto of Arizona)")
        st.write("Deo Gratias habeamus — Let have thanks to God (Motto of Kentucky)")
        st.write("Sine Quā nōn — Not Without Which / The Necessities (English Grammar)")
        st.write("Crescit Eundo — It Grows By Going (Motto of New Mexico)")
        st.write("Eureka — I found it! (Motto of California)")
        st.write("Esto perpetua — May it last forever (Motto of Idaho)")
        st.write("Ensemble Petit Placidam Sub Libertate Quietem — With a Sword She Seeks Peaceful Quiet Under The Liberty (Motto of Massachusetts)")
        st.write("Ē Pluribus Unum — One Out Of Many (United States)")
        st.write("Annuit Coeptīs — He Has Favored Our Undertaking (Motto of United States)")
        st.write("Ordo seclōrum — a new order (United States)")
        st.write("Novus ordo seclōrum — a new order of the ages (United States)")
        st.write("Alīs volat propriīs — she flies by her own wings (Motto of Oregon)")
        st.write("Cedant arma togae — Let arms (weapons) yield to the toga (Let war give way to peace) (Motto of Wyoming)")
        st.write("Q isra nostra defendere — We dare to defend our rights (Motto of Alabama)")
        st.write("Justitia omnibus — Justice for all (Motto of Washington D.C)")
        st.write("Io Saturnalia! — Hey, Saturnalia! (Festive Holidays)")
        st.write("Optimō diērm— on the best of days (Catullus, writing about Saturnalia)")
        st.write("Opalia — the festival for Ops (Saturnalia)")
        st.write("Annus novus — New Year (Felicam annus novus— Happy New Year)")
        st.write("Imperium in imperio — An empire in an empire (Motto of Ohio)")
        st.write("Motanī simper liberī — Mountain people (are) always free (Motto of West Virginia)")
        st.write("Nil sine nominee — Nothing without good (Motto of Colorado)")
        st.write("Qui transtulit sustinet — He who transplate (us) sustains (us) (Motto of Connecticut)")
        st.write("Regnat populus — The people rule (Motto of Arkansas)")
        st.write("Salus populi supermen lex esto — Let the welfare of the people be the highest law (Motto of Missouri)")
        st.write("Scutō bones voluntatius tube coronatsi nōs — You have crowned us with the shield of your good will (Motto of Maryland)")
        st.write("Si quaeris peninsulam amoenam, circumspice — If you seek a pleasant peninsula look around (Motto of Michigan)")
        st.write("Aic simper tyranis — Thus always to tyrants (Motto of Virginia)")
        st.write("Virtute et armīs — By courage and arms")
        st.write("Aut I am inveniam aut faciam — I’ll either find a way or I’ll make one (Hannibal, the enemy of Rome)")
        st.write("Aut Caesar aut nihil — It’s Caesar or its nothing")
        st.write("Gerit — wears")
        st.write("Gerunt — they wear")
        st.write("Velocius quam asparagi coquantur — Faster than boiled asparagus! — Favorite saying of Augustus")
        st.write("Vox populī — The Voice Of The People")
        st.write("Semper paratus — Always Prepared")
        st.write("Semper fidelis — Always Faithful")
        st.write("Errare humanum est — Air is human (mistakes are human/ mistakes are good)")
        st.write("Ex nihilo nihil fit — Nothing comes from nothing (Lucretiu)")

if selected_page == nav_pages[2]:
    CHAT_FILE = "chat.json"

    if not os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "w") as f:
            json.dump([], f)
    
    with open(CHAT_FILE, "r") as f:
        messages = json.load(f)
    
    st.title("💬 Streamlit Chatroom (Multi-User)")
    
    # Display messages
    for message in messages:
        with st.chat_message(message["role"]):
            st.write(f"**{message['user']}**: {message['text']}")
    
    # User input
    user_input = st.chat_input("Type a message...")
    username = st.text_input("Enter your name:", key="username")  # User ID
    
    if user_input and username:
        new_message = {"role": "user", "user": username, "text": user_input}
        messages.append(new_message)
    
        # Save chat history
        with open(CHAT_FILE, "w") as f:
            json.dump(messages, f)
    
        st.experimental_rerun()



streamlit_extras.let_it_rain.rain('•', 20, falling_speed=5, animation_length="infinite")

