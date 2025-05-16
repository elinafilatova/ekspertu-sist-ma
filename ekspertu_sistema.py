import streamlit as st

def sakuma_ekrans():
    st.markdown("<h1 style='font-size: 40px;'>Ko Jūs redzat sev priekšā? 🤔</h1>", unsafe_allow_html=True)
    objekta_tips = st.selectbox("Izvēlieties objektu:", ["", "dzīvnieks", "koks", "sēne"])
    
    if objekta_tips == "koks":
        koki()

    if objekta_tips == "sēne":
        senes()

    if objekta_tips == "dzīvnieks":
        dzivnieki()


# koki klase
def koki():
    st.markdown("<h1 style='font-size: 40px;'>Kas aug uz koka zariem? 🤨</h1>", unsafe_allow_html=True)
    uz_zariem = st.radio("Izvēlieties:", ["", "lapas", "adatas"])

    if uz_zariem == "adatas":
        st.markdown("<h2 style='font-size: 35 px;'>Kur sāk augt zari? 🧐</h2>", unsafe_allow_html=True)
        adatas = st.radio("Izvēlieties:", ["", "no pamata", "no koka vidus"])

        if adatas == "no pamata":
            egle()
        
        if adatas == "no koka vidus":
            priede()

    
    if uz_zariem == "lapas":
        st.markdown("<h2 style='font-size: 35 px;'>Kā izskatās koka lapas? 🧐</h2>", unsafe_allow_html=True)

        lapas_tips = st.radio(
            "Izvēlieties:",
            ["", "1", "2", "3", "4"],
            horizontal=True
        )

        col1, col2, col3, col4 = st.columns([2, 1, 1, 2])

        # kļava:
        with col1:
            st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Acer_platanoides3.jpg/1280px-Acer_platanoides3.jpg", use_container_width=True)
        
        # liepa:
        with col2:
            st.image("https://www.fitoterapija.lv/wp-content/uploads/2017/02/liepa.jpg", use_container_width=True)
        
        # ozols:
        with col3:
            st.image("https://upload.wikimedia.org/wikipedia/commons/a/af/Quercus_robur.jpg", use_container_width=True)

        # bērzs: 
        with col4:
            st.image("https://kokskaste.lv/cdn/shop/files/berzs.jpg?v=1708840068&width=750", use_container_width=True)


        if lapas_tips == "1":
            kļava()

        if lapas_tips == "2":   
            liepa()
        
        if lapas_tips == "3":
            ozols()

        if lapas_tips == "4":
            berzs()



# sēnes klase
def senes():
    st.markdown("<h1 style='font-size: 40px;'>Kāda krāsa ir sēnes cepurītei? 🤨</h1>", unsafe_allow_html=True)
    cepurites_krasa = st.radio("Izvēlieties:", ["", "brūna", "dzeltena", "sarkana"])
    
    st.markdown("<h1 style='font-size: 40px;'>Kāds kātiņš ir sēnei? 🧐</h1>", unsafe_allow_html=True)
    katins = st.radio("Izvēlieties:", ["", "plāns", "biezs"])

    st.markdown("<h1 style='font-size: 40px;'>Kāda tekstūra ir sēnei zem cepurītes? 🤔</h1>", unsafe_allow_html=True)
    tekstura = st.radio("Izvēlieties:", ["", "loksnītes", "poras"])


    if cepurites_krasa == "brūna" and katins == "biezs" and tekstura == "poras":
        baravika()

    if cepurites_krasa == "dzeltena" and katins == "plāns" and tekstura == "loksnītes":
        gailenes()
    
    if cepurites_krasa == "brūna" and katins == "plāns" and tekstura == "poras":
        bekas()
    
    if cepurites_krasa == "sarkana" and katins == "plāns" and tekstura == "loksnītes":
        
        st.markdown("<h1 style='font-size: 40px;'>Vai uz cepurītes ir baltie punkti? 😮</h1>", unsafe_allow_html=True)
        punkti = st.radio("Izvēlieties:", ["", "jā", "nē"])

        if punkti == "jā":
            musmire()

        if punkti == "nē":
            berzlape()


# dzīvnieki klase:
def dzivnieki():
    st.markdown("<h1 style='font-size: 40px;'>Kāda krāsa ir dzīvniekam? 🤨</h1>", unsafe_allow_html=True)
    krasa = st.radio("Izvēlieties:", ["", "pelēka", "oranža"])
    
    st.markdown("<h1 style='font-size: 40px;'>Kur dzīvo dzīvnieks? 🧐</h1>", unsafe_allow_html=True)
    dzivo = st.radio("Izvēlieties:", ["", "uz zemes", "uz kokiem"])

    if krasa == "oranža" and dzivo == "uz zemes":
        lapsa()

    if krasa == "oranža" and dzivo == "uz kokiem":
        vavere()

    if krasa == "pelēka" and dzivo == "uz zemes":
        
        st.markdown("<h1 style='font-size: 40px;'>Vai dzīvniekam ir adatas? 😮</h1>", unsafe_allow_html=True)
        dz_adatas = st.radio("Izvēlieties:", ["", "jā", "nē"])

        if dz_adatas == "jā":
            ezis()

        if dz_adatas == "nē":
            vilks()

# --------------------------------------------- ekrāni ------------------------------------------------------------------------------

# koki:
def egle():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir egle! 🎄</h1>", unsafe_allow_html=True)
    
    st.image("https://upload.wikimedia.org/wikipedia/commons/8/81/Picea_abies.jpg")

    st.markdown("""
    Egle ir mūžzaļš koks - tā paliek zaļa visu gadu - pat ziemā.
    Eglei ir asas, smailas skujas lapu vietā.
    Egles ir svarīgas dzīvniekiem – tās dod mājvietu putniem un citām mēža iedzīvotājiem.
    """)

def priede():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir priede! 🌲</h1>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Pinus_sylvestris_blue.jpg/800px-Pinus_sylvestris_blue.jpg")

    st.markdown("""
    Priede ir mūžzaļš koks, kas nozīmē, ka tā paliek zaļa visu gadu.
    Tai ir garas, tievas skujas lapu vietā.
    Mežā priedes dod patvērumu dzīvniekiem, kā arī no priedes izaug čiekuri, kuros ir sēkliņas – tās patīk gan vāverēm, gan citiem dzīvniekiem.                 
    """)

def kļava():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir kļava! 🍁 </h1>", unsafe_allow_html=True)

    st.image("https://www.redzet.lv/images/large/1/12/A-396-17.jpg")

    st.markdown("""
    Kļava ir lapu koks, kas rudenī kļūst ļoti krāsaina – tās lapas var būt dzeltenas, oranžas vai sarkanas.
    Kad pienāk ziema, kļava nomet savas lapas, bet pavasarī no kļavas sulas var iegūt kļavu sīrupu. 
    Kļavas ir skaisti koki, kas dod ēnu un priecē mūs ar savām krāsām un formām.                        
    """)

def liepa():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir liepa! 🍁 </h1>", unsafe_allow_html=True)

    st.image("https://pic.la.lv/2018/02/liepa-koks-vasara-1024x683.jpg")

    st.markdown("""
    Liepa ir lapu koks ar zaļām, mīkstām lapām, kas vasarā smaržo ļoti patīkami.
    Liepa dod patvērumu putniem un citām meža iedzīvotājiem, bet vasarā uz liepas var redzēt mazas dzeltenīgas ziedu bumbas, no kurām bites vāra gardu medu.                             
    """)

def ozols():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir ozols! 🌳 </h1>", unsafe_allow_html=True)

    st.image("https://www.mezataksacija.lv/wp-content/uploads/ozols.jpg")

    st.markdown("""
    Ozols ir liels un spēcīgs koks ar platām, dziļi iegrieztām lapām.
    Ozoli aug ļoti ilgi un var kļūt par veciem kokiem, kuros dzīvo daudzi putni un kukaiņi, ka arī ozola riekstus ļoti mīl ēst vāveres un citi dzīvnieki.                         
    """)

def berzs():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir bērzs! 🍃 </h1>", unsafe_allow_html=True)\
    
    st.image("https://stadiblidene.lv/images/com_hikashop/upload/betula_papyrifera.jpg")

    st.markdown("""
    Bērzs ir skaists koks ar baltu, gludu stumbru un zaļām, smalkām lapām. 
    No bērza pavasarī var iegūt saldo bērzu sulu, kas ir garšīga un veselīga.                                      
    """)



# sēnes:
def baravika():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir baravika! 🌼 </h1>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4b/Boletus_edulis_JPG9.jpg")

    st.markdown("""
    Baravika ir liela un stingra sēne ar brūnu cepurīti un biezu kātiņu. 
    Baraviku sauc arī par “sēņu karalieni”, jo tā ir ļoti garšīga un iecienīta zupās un citos ēdienos.  
    Baravikas parasti ir drošas ēšanai, bet jābūt uzmanīgiem, lai tās nesajauc ar līdzīgām indīgām sēnēm.                                      
    """)

def gailenes():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir gailene! 🌻 </h1>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/9/9a/Chanterelle_Cantharellus_cibarius.jpg")

    st.markdown("""
    Gailene ir spilgti dzeltena sēne ar viļņainu cepurīti un stingru kātiņu.
    Gailenes ir ļoti iecienītas, jo tās ir garšīgas un reti sastopamas indīgas sēnes, kas izskatās līdzīgi.                                           
    """)

def musmire():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir mušmire! 🍄 </h1>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/3/32/Amanita_muscaria_3_vliegenzwammen_op_rij.jpg")

    st.markdown("""
    Esi uzmanīgs - mušmire ir skaista, bet indīga sēne!!  
    Tai ir sarkana vai oranža cepurīte ar baltiem punktiņiem un balts kāts.
    Lai gan mušmire izskatās kā pasaku sēne, tā nedrīkst tikt ēsta, jo ir bīstama veselībai.                                                                
    """)

def bekas():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir bekas! 🌸 </h1>", unsafe_allow_html=True)

    st.image("https://static.lsm.lv/media/2020/08/large/1/dpgq.jpg")

    st.markdown("""
    Beka ir meža sēne ar stingru kātiņu un cepurīti, kas var būt brūngana, oranža vai pelēka – atkarībā no tā, kur tā aug.
    Bekas ir ēdamas un ļoti iecienītas, bet pirms vākšanas vienmēr jāpārliecinās, vai tā ir īstā! Svaiga beka ir stingra un patīkama pēc smaržas.            
    """)

def berzlape():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir bērzlape! 🌷 </h1>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/0/0f/Russula_emetica_in_Poland.jpg")

    st.markdown("""
    Bērzlape ir spilgta un krāsaina sēne ar plakanu cepurīti, kas var būt sarkana, zaļa, dzeltena vai pat violeta. 
    Tās kātiņš ir balts un viegli lūst, kā krīts.   
    Dažas bērzlapes ir ēdamas, bet citas var būt rūgtas vai kairinošas, tāpēc tās nevajag nogaršot – vienmēr jājautā pieaugušajiem, vai konkrētā bērzlape ir droša.         
    """)


# dzīvnieki:
def vavere():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir vāvere! 🐿 </h1>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/0/02/Eichh%C3%B6rnchen_D%C3%BCsseldorf_Hofgarten_edit.jpg")

    st.markdown("""
    Vāvere ir mazs, ātrs meža dzīvnieks ar pūkainu asti un asa prātu. 
    Tā ļoti mīl riekstus un sēklas, ko tā rūpīgi krāj ziemai. 
    Vāveres lieliski lec no koka uz koku un dzīvo lielās midzenēs, kas saucas ligzdas.        
    """)

def lapsa():
    st.markdown("<h1 style='font-size: 40px;'>Jūs aprakstījat lapsu! 🦊 </h1>", unsafe_allow_html=True)

    st.image("https://pic.la.lv/2016/11/lapsa.jpg")
    
    st.markdown("""
    Lapsa ir viltīgs un gudrs meža dzīvnieks ar skaistu sarkanu kažoku un garu asti. 
    Tā ir ļoti veikla un spēj klusām staigāt pa mežu, lai atrastu ēdienu. 
    Lapsas bieži dzīvo alās un naktī meklē barību.    
    """)

def vilks():
    st.markdown("<h1 style='font-size: 40px;'>Jūs aprakstījat vilku! 🐺 </h1>", unsafe_allow_html=True)

    st.image("https://media.lasi.lv/media/cache/gallery__jpeg/uploads/media/image/2024052521243266522ce00cfd4.jpg")

    st.markdown("""
    Vilks ir stiprs un drosmīgs dzīvnieks.
    Viņi labi sadarbojas, lai kopīgi medītu un aizsargātu savu māju. 
    Vilki ir ļoti skaļi, un viņu skaļa ulšana naktī var dzirdēt tālu mežā.
    """)

def ezis():
    st.markdown("<h1 style='font-size: 40px;'>Jums priekšā ir ezis! 🦔 </h1>", unsafe_allow_html=True)

    st.image("https://upload.wikimedia.org/wikipedia/commons/d/d4/Igel01.jpg")

    st.markdown("""
    Ezis ir mazs dzīvnieks ar īsiem kājiņām un daudzām adatiņām mugurā, kas viņu sargā no briesmām. 
    Kad ejot pa mežu, viņš jūt draudus, viņš sarullējas bumbiņā, lai pasargātu sevi. 
    Eži ēd kukaiņus un dzīvo tumšās, mierīgās vietās.
    """)


sakuma_ekrans()

