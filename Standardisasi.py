import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os

st.set_page_config(page_title="Haxxor_Standarisasi", page_icon=(":rabbit:"), layout="centered", initial_sidebar_state="auto", menu_items=None)

st.markdown("""
<style>
.big-font {
    font-size:25px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.medium-font {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.badag-font {
    font-size:60px !important;
}
</style>
""", unsafe_allow_html=True)

#Sidebar-----------------------------------------------------------------------------------------------------------------------------------

with st.sidebar :
    pilihan = option_menu("Menu Utama", ["Tentang Kami", "Informasi Standarisasi", "Program Standarisasi"], 
        icons=['people-fill', 'info-circle','gear'], menu_icon="cast", default_index=1)
    st.write(f':white[{pilihan}]')
    
#Tentang ----------------------------------------------------------------------------------------------------------------------------------
if pilihan =="Tentang Kami" :
    st.title('KELOMPOK 1')
    st.write('\n')
    st.write('\n')
    st.image(Image.open('logo.png'))
    
   
    #Teks
    st.write('\n')
    st.write('\n')
    st.header("Anggota :\n")
    st.markdown('<p class="big-font">1. Ksatria Pakualam (2219094)<br>2. Muhamad Faiz Ichsan P (2219111) <br>3. Muhammad Rifqi (221918)<br>4. Rizieq Hidayat (2219159)<br>5. Wisnu Riyadi (2219183)</p>', unsafe_allow_html=True)
    

#Informasi Standarisasi--------------------------------------------------------------------------------------------------------------------
elif pilihan == "Informasi Standarisasi" :
    st.title("Standarisasi")
    st.write("---")
    st.markdown("""<p class = medium-font> <FONT COLOR="#00FF00">Standarisasi</FONT> adalah  suatu usaha menentukan konsentrasi yang tepat dari larutan baku yang akan digunakan untuk titrasi. Setelah melakukan standarisasi dapat ditentukan konsentrasi dari larutan baku sekunder tersebut dengan mengetahui bobot sampel yang ditimbang, volume yang dibutuhkan pada saat titrasi untuk mencapai titik akhir titrasi, berat ekuivalen dari sampel dan mengetahui faktor pengenceran/pengali.</p>
    <p class = medium-font>Dalam melakukan penentuan konsentrasi yaitu salah satunya dengan cara perhitungan melalui rumus, tentu saja bisa terjadi galat/kesalahan yang diakukan oleh manusia atau human error. Kesalahan tersebut sangat fatal yang menyebabkan kesalahan data.  Salah satu antisipasi dari kesalahan tersebut adalah dengan adanya aplikasi pengolahan data yang sangat bermanfaat dan memberi kemudahan seperti halnya dalam perhitungan konsentrasi.</p>""",unsafe_allow_html = True)
   
    st.subheader('Rumus : ')
    
    st.write('\n')
    st.write('\n')
    
    st.latex(r'\boxed{N_{larutan}=\frac {mg\medspace baku\medspace primer}{fp\enspace x\enspace mL\,larutan \enspace x\enspace BE\,baku\,primer}}')
    
    st.write('\n')
    st.write('\n')
    st.markdown("""Keterangan :\n
                   N larutan = Konsentrasi larutan hasil Standarisi\n
                   mg baku primer = Massa baku primer yang ditimbang dalam mg\n
                   fp = Faktor pengali\n
                   mL larutan = Volume larutan yang distandarisasi dalam mL\n
                   BE baku primer = Berat Ekivalen baku primer""")
                   
    


#Program ----------------------------------------------------------------------------------------------------------------------------------
elif pilihan == "Program Standarisasi" :
    
    st.title(':green[Webapps Standarisasi]')    
    st.write("---")
    larutan = st.selectbox ('Silahkan pilih larutan yang ingin :blue[distandardisasi]', 
                       ('NaOH','HCl','Kalium Permanganat','Natrium Tio Sulfat','EDTA'))

    V_larutan = st.number_input(f'**mL** larutan :blue[{larutan}] ', value = 20.00, format = '%.2f', step = 1.00 )

    st.write("---")
    if larutan == 'NaOH' :
                            baku_primer = st.selectbox('Silahkan pilih :red[baku primer]',
                                                  ('Asam Oksalat','Kalium Hidrogen Ftalat'))
    elif larutan == 'HCl' :
                            baku_primer = st.selectbox('Silahkan pilih :red[baku primer]',
                                                  ('Boraks','Natrium Karbonat'))
    elif larutan == 'Kalium Permanganat' :
                            baku_primer = st.selectbox('Silahkan pilih :red[baku primer]',
                                                  ('Asam Oksalat',))
    elif larutan == 'Natrium Tio Sulfat' :
                            baku_primer = st.selectbox('Silahkan pilih :red[baku primer]',
                                                   ('Kalium Dikromat',))
    elif larutan == 'EDTA' : 
                            baku_primer = st.selectbox('Silahkan pilih :red[baku primer]',
                                                   ('Kalsium Karbonat',))
    

    if baku_primer == 'Asam Oksalat' :
            BE = 63
    elif baku_primer == 'Kalium Hidrogen Ftalat' :
            BE = 204.2
    elif baku_primer == 'Boraks' :
            BE = 190.7
    elif baku_primer == 'Natrium Karbonat' :
            BE = 53
    elif baku_primer == 'Kalium Dikromat' :
            BE = 49
    else :
            BE = 100

    
    if larutan == 'Natrium Tio Sulfat' :
        
        mg_primer = st.number_input(f'**mg** :red[{baku_primer}] yang ditimbang', value = 100.0, format = '%.2f', step = 10.0)
        st.write("---")
        
        N_larutan = mg_primer/(V_larutan * BE)
       
        if st.button('Tampilkan Konsentrasi Larutan') :
            st.subheader(f':green[{round(N_larutan,4)} N]')
        else :
            st.write()
    
    elif larutan == 'EDTA' :
        
        mg_primer = st.number_input(f'**mg** :red[{baku_primer}] yang ditimbang', value = 100.0, format = '%.2f', step = 10.0)
        st.write("---")
        
        V_awal = st.number_input(f'**mL** Volume :red[{baku_primer}] yang dibuat', value = 100.00, step = 1.00)
        V_pipet = st.number_input(f'**mL** Volume :red[{baku_primer}] yang dipipet', value = 25.00, step = 1.00)
        FP = (V_awal/V_pipet)

        N_larutan = mg_primer/(V_larutan * BE * FP)
       
        if st.button('Tampilkan Konsentrasi Larutan') :
            st.subheader(f':green[{round(N_larutan,4)} M]')
            
        else :
            st.write()
        
    else :    
        
        mg_primer = st.number_input(f'**mg** :red[{baku_primer}] yang ditimbang', value = 100.0, format = '%.2f', step = 100.0)
        st.write("---")
        
        V_awal = st.number_input(f'**mL** Volume :red[{baku_primer}] yang dibuat', value = 100.00, step = 1.00)
        V_pipet = st.number_input(f'**mL** Volume :red[{baku_primer}] yang dipipet', value = 25.00, step = 1.00)
        FP = (V_awal/V_pipet)

        N_larutan = mg_primer/(V_larutan * BE * FP)
    
        if st.button('Tampilkan Konsentrasi Larutan') :
            st.subheader(f':green[{round(N_larutan,4)} N]')
        else :
            st.write()


    
