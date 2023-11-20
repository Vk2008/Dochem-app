from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.core.text.markup import MarkupLabel
from kivy.uix.boxlayout import BoxLayout
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import OneLineIconListItem
from kivy.base import runTouchApp
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.scrollview import ScrollView
from kivy.uix.recycleview import RecycleView
import pandas as pd
import numpy as np
import random as rd

class HomeScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class FydScreen(Screen):
    global symptom_1
    global symptom_2
    global symptom_3
    global symptom_4
    global symptom_5

    symptom_1, symptom_2, symptom_3,symptom_4, symptom_5 = '','','','',''
    def spinner_clicked_1(self, value):
        self.ids.s_1_l.text = f'Symptom 1: {value}'
        global symptom_1
        symptom_1 = value
    def spinner_clicked_2(self, value):
        
        self.ids.s_2_l.text = f'Symptom 2: {value}'
        global symptom_2
        symptom_2 = value
    def spinner_clicked_3(self, value):
        
        self.ids.s_3_l.text = f'Symptom 3: {value}'
        global symptom_3
        symptom_3 = value
    def spinner_clicked_4(self, value):
        
        self.ids.s_4_l.text = f'Symptom 4: {value}'
        global symptom_4
        symptom_4 = value
    def spinner_clicked_5(self, value):
        
        self.ids.s_5_l.text = f'Symptom 5: {value}'
        global symptom_5
        symptom_5 = value

    global l1
    l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
    'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
    'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
    'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
    'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
    'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
    'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
    'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
    'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
    'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
    'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
    'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
    'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
    'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

    global disease
    disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
        'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
        ' Migraine','Cervical spondylosis',
        'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']
    
    global l2
    l2 = []
    
    for x in range(0,len(l1)):
        l2.append(0)

    tr = pd.read_csv("Testing.csv")
    tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)

    global X_test
    X_test = tr[l1]
    global y_test
    y_test = tr[['prognosis']]
    np.ravel(y_test)

    df = pd.read_csv("Training.csv")
    df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)
    global X
    X = df[l1]
    global y
    y = df[['prognosis']]
    np.ravel(y)

    def NaiveBayes():
        #X = X
        #y = y
        #X_test = X_test
        #y_test = y_test
        #l1 = l1
        #disease = disease
        #l2 = l2
        from sklearn.naive_bayes import MultinomialNB
        gnb = MultinomialNB()
        gnb=gnb.fit(X,np.ravel(y))
        from sklearn.metrics import accuracy_score
        y_pred = gnb.predict(X_test)
        print(accuracy_score(y_test, y_pred))
        print(accuracy_score(y_test, y_pred, normalize = False))

        psymptoms = [symptom_1, symptom_2, symptom_3, symptom_4, symptom_5]

        for k in range(0,len(l1)):
            for z in psymptoms:
                if z == l1[k]:
                    l2[k] = 1
        inputtest = [l2]
        predict = gnb.predict(inputtest)
        predicted = predict[0]

        global h
        h = 'no'
        for a in range(0,len(disease)):
            if disease[predicted] == disease[a]:
                h = 'yes'

        if h == 'yes':
            global dis
            dis = disease[a]
            print(dis)
        else:
            print('no disease')
        

    def change_text(self):
        FydScreen.NaiveBayes()
        name= [['Dr. Vineet Kumar Soni', '23 years', '9718990201'], ['Dr. Vishwas Madhav Thakur', '33 years', '9971700688'], ['Dr Brij Mohan Dhawan', '40 years', '9971541600']]
        doc = rd.choice(name)
        doctor = doc[0]
        experience = doc[1]
        ph = doc[2]
        
        global h
        if h == 'no':
            self.ids.doc_l.text = 'No Disease Found/n Our Specialist to guide you further:'
            self.ids.detail_l.text = 'Name: '+ str(doc[0])+ '\n Experience: '+ str(doc[1]) + '\n Contact: '+ str(doc[2])
        elif h == 'yes':
            self.ids.doc_l.text = 'Nothing to worry, Contact our specialist for more:'
            self.ids.detail_l.text = 'Name: '+ str(doc[0])+ '\n Experience: '+ str(doc[1]) + '\n Contact: '+ str(doc[2])

class DietScreen(Screen):
    checks = []
    def checkbox_click(self, instance, value, modes):
        breakfast_veg = [['Chocolate Banana Smoothie with Milk', 'Idli/Dosa', 'Wheat Upma'], ['Red Poha', 'Brown Rice Idli and Sambar', 'Sprouts and Oats'], ['Brown Bread Sandwich', 'Chole Parantha', 'Besan Chila with Veggies']]
        lunch_veg = [['Raw Vegies', 'Brown Rice/Barley Khichdi', 'Yogurt'],['Brown Rice', 'Whole Wheat Phulka', 'Stuffed Mixed Grain Parantha'], ['Rice', 'Multigrain Roti', 'Moong Dal Khichdi']]
        dinner_veg = [['Mixed Grain roti', 'Coconut Lentil Soup', 'Fried Rice with Vegetables'], ['Whole Wheat Phulka', 'Pumpkin Dal Soup with Oats', 'Whole Wheat Phulka'], ['Broken Wheat Khichdi', 'Paneer Wrap', 'Jowar Phulka']]

        breakfast_nveg = [['Multigrain Chicken Salted Sandwich', 'Red Rice', 'Ragi Porridge'], ['Whole Wheat Bread & Egg White Omelette', 'Soya Khaman Dokhla', 'Onion & Tomato Uttapam'], ['Vermicelli Vegetable Egg Dish', 'Milk and Oats', 'Vegetable Fishy Bites']]
        lunch_nveg = [['Jeera Rice', 'Whole Wheat Pasta', 'Appam with Chicken Stew'], ['Oats', 'Tomato Rice', 'Brown Rice with Fish Curry'], ['Herby Pot Chicken Pulav', 'Millets and Chicken', 'Chicken Vegetable Khichada']]
        dinner_nveg = [['Chapati with Methi Sabzi', 'Methi Thepla', 'Grilled Fish with Avocado Salad'], ['Chapati with green peas', 'Grilled Chicken', 'Chapati with Egg Curry'], ['Broccoli Walnut Soup', 'Grilled Chicken', 'Amaranth crusted Fish with stir fried vegetables']]

        if value == True:
            DietScreen.checks.append(modes)
            mode = ''
            for x in DietScreen.checks:
                mode = f'{mode}{x}'
                if mode == 'Vegetarian':
                    b_v = rd.choice(breakfast_veg)
                    l_v = rd.choice(lunch_veg)
                    d_v = rd.choice(dinner_veg)
                    self.ids.b_d_1.text = b_v[0]
                    self.ids.b_d_2.text = b_v[1]
                    self.ids.b_d_3.text = b_v[2]

                    self.ids.l_d_1.text = l_v[0]
                    self.ids.l_d_2.text = l_v[1]
                    self.ids.l_d_3.text = l_v[2]

                    self.ids.d_d_1.text = d_v[0]
                    self.ids.d_d_2.text = d_v[1]
                    self.ids.d_d_3.text = d_v[2]
                elif mode == 'Non-Vegetarian':
                    b_n = rd.choice(breakfast_nveg)
                    l_n = rd.choice(lunch_nveg)
                    d_n = rd.choice(dinner_nveg)
                    self.ids.b_d_1.text = b_n[0]
                    self.ids.b_d_2.text = b_n[1]
                    self.ids.b_d_3.text = b_n[2]

                    self.ids.l_d_1.text = l_n[0]
                    self.ids.l_d_2.text = l_n[1]
                    self.ids.l_d_3.text = l_n[2]

                    self.ids.d_d_1.text = d_n[0]
                    self.ids.d_d_2.text = d_n[1]
                    self.ids.d_d_3.text = d_n[2]
        else:
            DietScreen.checks.remove(modes)
            mode = ''
            for x in DietScreen.checks:
                mode = f'{mode}{x}'
                if mode == 'Vegeterian':
                    b_v = rd.choice(breakfast_veg)
                    l_v = rd.choice(lunch_veg)
                    d_v = rd.choice(dinner_veg)
                    self.ids.b_d_1.text = b_v[0]
                    self.ids.b_d_2.text = b_v[1]
                    self.ids.b_d_3.text = b_v[2]

                    self.ids.l_d_1.text = l_v[0]
                    self.ids.l_d_2.text = l_v[1]
                    self.ids.l_d_3.text = l_v[2]

                    self.ids.d_d_1.text = d_v[0]
                    self.ids.d_d_2.text = d_v[1]
                    self.ids.d_d_3.text = d_v[2]
                elif mode == 'Non-Vegetarian':
                    b_n = rd.choice(breakfast_nveg)
                    l_n = rd.choice(lunch_nveg)
                    d_n = rd.choice(dinner_nveg)
                    self.ids.b_d_1.text = b_n[0]
                    self.ids.b_d_2.text = b_n[1]
                    self.ids.b_d_3.text = b_n[2]

                    self.ids.l_d_1.text = l_n[0]
                    self.ids.l_d_2.text = l_n[1]
                    self.ids.l_d_3.text = l_n[2]

                    self.ids.d_d_1.text = d_n[0]
                    self.ids.d_d_2.text = d_n[1]
                    self.ids.d_d_3.text = d_n[2]

class YogaScreen(Screen):
    pass


# kv = Builder.load_file('main.kv')



class DocApp(MDApp):
    def build(self):
        self.title = 'Dochem'
        #self.theme_cls.theme_style = "Dark"
        #self.theme_cls.primary_palette = "DeepPurple"
        self.root = Builder.load_file('main.kv')
    def change_screen(self, screen_name):
        screen_manager= self.root.ids['screen_manager']
        screen_manager.current = screen_name

if __name__ == '__main__':  
    DocApp().run()
