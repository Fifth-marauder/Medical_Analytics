import streamlit as st
import pandas as pd
# import opstrat as op
# import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import altair as alt

st.set_page_config(page_title="Medical Analytics", layout="wide")
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


option = st.sidebar.radio(
    'Choose a dashboard to view',
    ('Modalities', 'Diseases'))


st.sidebar.markdown(""" 
## Developers

This web software is created as a part of Medical Analytics course by 
- Anu Varshini
- Abishek
- Anjan Krishnan
- Sreemathi
- Hari Govind
- Kailash 
  

#### Guided by
Dr Rakesh Nigam and Dr Bhagyam Raghavan
""")

st.title("Study of Human Anatomy through Modalities")

st.markdown(""" 
**This project aims to study Human Anatomy through various imaging techniques and modalities** 
""",True)


with st.container():

    if option == 'Modalities':
        body_part=st.selectbox("Sections of Body : ",("Brain & Skull", "Chest", "Abdomen", "Extremities (Others)"))
        modalities=st.selectbox("Modalities : ",("X-ray","Ultrasound","CT","MRI"))
        if modalities == 'X-ray' and body_part=='Abdomen' :
            views=st.selectbox("Views : ",("AP Supine","KUB","PA Erect","Others-Lateral","Others-PA Prone"))

            with st.container():
                st.write("---")
                if views=='AP Supine':
                    st.header("AP Supine View")
                    image = Image.open('abdomen_Xray_supine.png')
                    st.image(image, caption='AP Supine View')
                    st.write("""
                    The AP supine view can be used to detect various abdominal conditions, such as:
- Bowel obstruction: This can be indicated by the presence of dilated bowel loops on the X-ray.
- Kidney stones: These may appear as radio-opaque densities on the X-ray.
- Abdominal masses: Tumors or other masses may be visible on the X-ray as areas of increased density.
- Pneumoperitoneum: The presence of air in the abdominal cavity, which may indicate a perforated organ or bowel, can be detected on an AP supine view.
- Foreign objects: The presence of foreign objects, such as swallowed objects or surgical instruments, can be detected on an X-ray.

                    """)
                    left_column, right_column=st.columns(2)
                    with left_column:
                        st.header("Positioning of the Patient")
                        st.write(
                            """
                                - The AP (Antero-Posterior) supine view is a common radiographic view used in abdominal X-rays. In this view, the patient lies flat on their back, and the X-ray beam passes through the abdomen from the front to the back of the body.
            - Exposure: 70-80 kVp and 30-120 mAs
            """)
                    with right_column:
                        image2=Image.open('ab_xray_supine_pos.png')
                        st.image(image2, caption= 'Patient Position',use_column_width=True)
                    st.write("---")
                    st.header("Normal View Vs Abnormal View")
                    left_column2, right_column2=st.columns(2)
                    with left_column2:
                        image3=Image.open('ab_xray_supine_n.png')
                        st.image(image3, caption= 'Normal',use_column_width=True)
                    with right_column2:
                        image4=Image.open('ab_xray_supine_d.png')
                        st.image(image4, caption= 'Abnormal',use_column_width=True)
                if views =='KUB':
                    st.header("KUB View")
                    image5=Image.open('ab_xray_kub.png')
                    st.image(image5, caption='KUB View')
                    st.write("""
                    - It is performed to assess the abdominal area for causes of abdominal pain, or to assess the organs and structures of the urinary and/or gastrointestinal (GI) system. 
- A KUB X-ray is the first diagnostic procedure used to assess the urinary system.
- In the case of the KUB Xray the bones of the pelvis and spine and any calcifications or stones in the urinary tract absorb more Xrays than the soft tissues resulting in a white or bright appearance on the Xray image
- The bladder which contains air appears black on the Xray and the intestines and other soft tissues appear gray.
- KUB is also called flat plate of the abdomen is a non-invasive imaging test that uses X-rays to produce an images of the kidneys, ureters, bladder collectively known as the urinary tract

                    """)
                    left_column3, right_column3=st.columns(2)
                    with left_column3:
                        st.header("Positioning of the Patient")
                        st.write(
                            """
                            Before positioning on patient be sure to remove all metal, plastic, or other removable object from the patient's head.
- To obtain a KUB view, the patient will lie flat on their back on an X-ray table. The X-ray machine will then be positioned over the patient's abdomen, and a beam of X-rays will be passed through the body and onto the X-ray detector located on the opposite side.
- The X-ray machine is positioned over the patient's abdomen, and the X-ray beam passes through the body from front to back. The image produced by the X-ray is then used to visualize the urinary system, including the kidneys, ureters, and bladder.
- In terms of specific positioning of the parts, the kidneys are located on either side of the spine, just below the ribcage. The ureters are the tubes that carry urine from the kidneys to the bladder, and they run from the kidneys down to the bladder in the pelvis. The bladder is a hollow muscular organ that stores urine until it is ready to be expelled from the body. It is located in the lower part of the abdomen, just above the pubic bone.
- When obtaining a KUB view, the entire abdomen and pelvis are included in the image, so all of these structures will be visible to some degree. However, the primary focus of the view is on the urinary system and any abnormalities or issues that may be present in this area.

                            """)
                    with right_column3:
                        image6=Image.open('ab_xray_kub_pos.png')
                        st.image(image6, caption= 'Patient Position')
                    st.write("---")
                    st.header("Normal View Vs Abnormal View")
                    left_column4, right_column4=st.columns(2)
                    with left_column4:
                        image7=Image.open('ab_xray_kub_n.png')
                        st.image(image7, caption= 'Normal')
                    with right_column4:
                        image8=Image.open('ab_xray_kub_d.png')
                        st.image(image8, caption= 'Abnormal')
                if views =='PA Erect':
                    st.header("PA Erect View")
                    image9=Image.open('ab_xray_erect.png')
                    st.image(image9,caption="PA Erect View", width=500)
                    st.write("""
                    - The PA erect abdominal radiograph is the standard view for assessing air-fluid levels and free air in the pediatric abdomen. 
                    - This view may be taken alongside the AP supine and lateral decubitus views
                    - As radiation protection is an essential consideration in pediatrics, some departmental protocols may only perform one view (either the PA erect or AP supine view) depending on the clinical indications 
                    - This view is valuable in visualizing gas-fluid levels and free gas in the abdominal cavity as it allows the assessment of ascites, perforation, intra-abdominal masses, ileus, or postoperative complications

                    """)
                    left_column5, right_column5=st.columns(2)
                    with left_column5:
                        st.header("Positioning of the Patient")
                        st.write("""
                        -The patient is standing, with ventral abdomen toward the image detector
                        -No rotation of shoulders or pelvis
                        -Standing erect with the abdomen pressed against the cassette holder. The patient should be asked to stop breathing while the exposure is taken.
                        -The diaphragm should be seen on the image – otherwise, the centering should be adjusted and another film should be obtained.

                        """)
                    with right_column5:
                        image10=Image.open('ab_xray_erect_pos.png')
                        st.image(image10, caption= 'Patient Position')
                    st.write("---")
                    st.header("Normal View Vs Abnormal View")
                    left_column6, right_column6=st.columns(2)
                    with left_column6:
                        image11=Image.open('ab_xray_erect_n.png')
                        st.image(image11, caption= 'Normal', width=350)
                    with right_column6:
                        image12=Image.open('ab_xray_erect_d.png')
                        st.image(image12, caption= 'Abnormal', width=350)


                if views =='Others-Lateral':
                    st.header("Lateral View")
                    image13=Image.open('ab_xay_lateral.png')
                    st.image(image13,caption="Lateral View", width=500)
                    st.write("""
                    - The purpose of lateral decubitus x-rays are; 
                      To demonstrate the abdominal cavity for gut perforation, intestinal obstruction etc. 
                    - These x-rays are usually taken for patients who are not ambulatory. 
                    - Lateral Decubitus is taken to identify intraperitoneal gas (pneumoperitoneum) 
                    - Usually performed when the person is unable to be transferred to, or other imaging modalities such as the CT are not available. The centering point or the focus should be the xiphisternum just superior to the iliac crest. 
                    """)
                    left_column7, right_column7=st.columns(2)
                    with left_column7:
                        st.header("Positioning of the Patient")
                        st.write("""
                        - The patient can lay either the left or right lateral side. 
                        - The detector should be placed anteriorly or posteriorly.
                        - To avoid superimposing on the region of interest, patients hand must be raised and the legs be flexed or balanced. 
                        - The pelvis should not be rotated and the shoulders rotation should be minimized

                        """)
                    with right_column7:
                        image14=Image.open('ab_xray_lateral_pos.png')
                        st.image(image14, caption= 'Patient Position')
                    st.write("---")
                    st.header("Normal View Vs Abnormal View")
                    left_column8, right_column8=st.columns(2)
                    with left_column8:
                        image15=Image.open('ab_xay_lateral.png')
                        st.image(image15, caption= 'Normal', width=350)
                    with right_column8:
                        image16=Image.open('ab_xray_lateral_d.png')
                        st.image(image16, caption= 'Abnormal', width=350)

                if views =='Others-PA Prone':
                    st.header("PA Prone View")
                    image17=Image.open('ab_xay_lateral.png')
                    st.image(image17,caption="PA Prone View", width=500)
                    st.write("""
                    - The PA prone radiograph is rarely performed.
                    - It is often utilized when a patient is unable to lay supine. 
                    - The projection is adequate for the examination of the abdominal cavity, however, not as practical for the renal structures due to magnification.
                    - Centering point - the midsagittal place (equidistant from each PSIS) at the level of the iliac crest
                    - Collimation (i.e bringing into line)- laterally to the lateral abdominal wall, superior to the diaphragm,inferior to the inferior pubic rami (the group of bones that form the pelvis).
                        """)
                    left_column9, right_column9=st.columns(2)
                    with left_column9:
                        st.header("Positioning of the Patient")
                        st.write("""
                    - The patient is face-down, either on the x-ray table (preferred) or on a trolley
                    - Patients should be changed into a hospital gown, with radiopaque items (e.g. belts, zippers) removed
                    - The patient should be free from rotation; both shoulders and hips equidistant from the table/trolley
                    - The x-ray is taken in full inspiration (breathe in and holding the breath).
                    - Lateral abdominal wall should be included
                    - Inferior pubic rami should be included inferiorly
                    - If possible, the diaphragm should be included superiorly

                        """)
                    with right_column9:
                        image18=Image.open('ab_xay_prone_pos.png')
                        st.image(image18, caption= 'Patient Position')
                    st.write("---")
                    st.header("Normal View Vs Abnormal View")
                    left_column10, right_column10=st.columns(2)
                    with left_column10:
                        image19=Image.open('ab_xray_prone_n.png')
                        st.image(image19, caption= 'Normal', width=350)
                    with right_column10:
                        image20=Image.open('ab_xay_prone_d.png')
                        st.image(image20, caption= 'Abnormal', width=350)
                    
with st.container():

    if option == 'Diseases':
        body_part=st.selectbox("Sections of Body : ",("Head", "Chest", "Abdomen", "Extremities (Others)"))
        if body_part=='Head' :
            organ=st.selectbox("Organ : ",("Neck","Skull","Other parts of Head"))
            if organ=='Other parts of Head':
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Hypercementosis
                In the area highlighted you will notice a large whitish mass around the roots of a tooth. This mass is an increased number of cells that line the root surface of the tooth. This is quite common and is generally not treated as it is an increase in the number of normal tissue cells and not cancerous. This does, however, pose a concern if the tooth ever requires extraction as this mass can make it very difficult to remove the tooth.

                """)
                image = Image.open('hypercementosis.png')
                st.image(image, caption='hypercementosis')

                st.markdown("""
                #### Calcified Lymph Node due to TB
                In this case, the mass highlighted on the radiograph is that of a calcified lymph node in the patient’s neck. The cause of this has been diagnosed as childhood exposure to TB. This case is dormant and non-contagious.

                """)
                image = Image.open('calcified_lymphnode.png')
                st.image(image, caption='calcified_lymphnode')

                st.markdown("""
                #### Abnormal number of teeth
                
                """)
                image = Image.open('abnormal_no_of_teeth.png')
                st.image(image, caption='abnormal_no_of_teeth')

            if organ=='Neck':
                image = Image.open('cervical_spine_label.png')
                st.image(image, caption='cervical_spine_label')
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Military Neck
                Military neck (or cervical kyphosis) is an abnormal curve of the cervical spine. In this case your neck is either abnormally straight.

                """)
                image = Image.open('military_neck.png')
                st.image(image, caption='military_neck')

                st.markdown("""
                #### Cervical Spondylitis
                
                """)
                image = Image.open('Cervical_Spondylitis.png')
                st.image(image, caption='Cervical_Spondylitis')

            if organ=='Skull':
                image = Image.open('skull_labelled.png')
                st.image(image, caption='skull')
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Cellulitis
                Plain X-ray of patient with left orbital cellulitis and widespread sinusitis. Preoperatively, gas outlines some of the structures within the left orbit (light arrows), the ethmoid sinuses are opaque and fluid levels (dark arrows) are present in the left frontal sinus and both maxillary sinuses.

                """)
                image = Image.open('cellulitis.png')
                st.image(image, caption='cellulitis')

                st.markdown("""
                #### Fractured Skull
                
                """)
                image = Image.open('fracture_skull.png')
                st.image(image, caption='fracture_skull')

                st.markdown("""
                #### Tripod Fracture
                
                """)
                image = Image.open('Tripod_Fracture.png')
                st.image(image, caption='Tripod_Fracture')


        if body_part == 'Chest' :
            organ=st.selectbox("Organ : ",("Lungs","Heart","Other parts of Chest"))
            if organ=='Lungs':
                image = Image.open('chest_labelled.png')
                st.image(image, caption='chest')
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Mass in the Lung
                In the area annotated you will notice a large mass and could be lung cancer if the mass is malignant
                """)
                image = Image.open('mass_in_lung.png')
                st.image(image, caption='mass_in_lung')

                st.markdown("""
                #### Lung Damage due to smoking
                """)
                image = Image.open('lung_smoking.png')
                st.image(image, caption='lung_smoking')

                st.markdown("""
                #### Covid Pneumonia
                """)
                image = Image.open('covid_pneumonia.png')
                st.image(image, caption='covid_pneumonia')

                st.markdown("""
                #### COPD (Chronic Obstructive Pulmonary Disease)
                """)
                image = Image.open('COPD.png')
                st.image(image, caption='COPD')

                st.markdown("""
                #### Acute Pulmonary Edema
                """)
                image = Image.open('Acute_pulmonary_edema.png')
                st.image(image, caption='Acute_pulmonary_edema')

                st.markdown("""
                #### Lung Adenocarcinoma
                """)
                image = Image.open('lung_adenocarcinoma.png')
                st.image(image, caption='lung_adenocarcinoma')

                st.markdown("""
                #### Lung Cancer Nodes
                Lung xray showing a solitary pulmonary     nodule aka coin lesion. either dormant or cancerous.
                """)
                image = Image.open('Lung_cancer_nodes.png')
                st.image(image, caption='Lung_cancer_nodes')

                st.markdown("""
                #### Pleural effusion
                Excess liquid in the lungs
                """)
                image = Image.open('Pleural_effusion.png')
                st.image(image, caption='Pleural_effusion')
                 
                st.markdown("""
                #### Acute Bactorial Lobar Pneumonia
                
                """)
                image = Image.open('Acute_Bactorial_Lobar_Pneumonia .png')
                st.image(image, caption='Acute_Bactorial_Lobar_Pneumonia')

            if organ=='Heart':
                image = Image.open('chest_labelled.png')
                st.image(image, caption='chest')
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Heart Enlargement
                The left cardiac border refers to the left border of the heart as seen on a chest X-ray. A bulge in this area may indicate an abnormality or enlargement of the heart due to cardiomegaly, tumor,etc.
""")
                image = Image.open('Heart_enlargement.png')
                st.image(image, caption='Heart_enlargement')

                st.markdown("""
                #### Alcoholic Cardiomyopathy
                """)
                image = Image.open('alcoholic_cardiomyopathy.png')
                st.image(image, caption='alcoholic_cardiomyopathy')

                st.markdown("""
                #### Mitral Annular Calcification
                calcification between ventricle and left atrium 

                
                """)
                image = Image.open('Annular_Calcification.png')
                st.image(image, caption='Annular_Calcification')

            if organ=='Other parts of Chest':
                image = Image.open('chest_labelled.png')
                st.image(image, caption='chest')
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Rib Fractures
                Left side rib fractures
                """)
                image = Image.open('rib_fractures.png')
                st.image(image, caption='rib_fractures')

                st.markdown("""
                #### Anaphylaxis
                """)
                image = Image.open('Anaphylaxis.png')
                st.image(image, caption='Anaphylaxis')

                st.markdown("""
                #### Achalasia
                Chest x-ray is largely unremarkable. Minor patchy opacities in the left base are noted. A small gastric air bubble is visible.

                """)
                image = Image.open('Achalasia.png')
                st.image(image, caption='Achalasia')

                st.markdown("""
                #### GERD (Gastroesophageal reflux disease)
                Frontal radiograph of the chest shows a small ovoid foreign body (arrow), which represents a wireless esophageal monitoring device, projecting over the midline posterior mediastinum in the expected location of the middistal esophagus

                """)
                image = Image.open('GERD.png')
                st.image(image, caption='GERD')
                
                st.markdown("""
                #### Peptic Stricture
                
                """)
                image = Image.open('Peptic_Stricture.png')
                st.image(image, caption='Peptic_Stricture')

                st.markdown("""
                #### Enlarged Liver (Hepatomegaly)
                The liver itself cannot be seen, but the disorder has been revealed by the raised diaphragm (white, lower left). 

                """)
                image = Image.open('enlarged_liver.png')
                st.image(image, caption='enlarged_liver')

                st.markdown("""
                #### Amyloidosis
                Frontal X ray showing patchy airspace opacities bilaterally consistent with the diagnosis of pulmonary amyloidosis (yellow arrows). 

                """)
                image = Image.open('Amyloidosis.png')
                st.image(image, caption='Amyloidosis')

                st.markdown("""
                #### Opacity
                Pleural-based opacity identified within the right lower hemithorax. No rib fractures were identified

                """)
                image = Image.open('Opacity.png')
                st.image(image, caption='Opacity')

                st.markdown("""
                #### Acute Lupus Nephritis
                Flask-shaped enlargement of the cardiac silhouette in keeping with pericardial effusion. Obliteration of the left costophrenic sulcus in keeping with probable pleural effusion. 

                """)
                image = Image.open('Acute_lupus_nephritis.png')
                st.image(image, caption='Acute_lupus_nephritis')
            

                st.markdown("""
                #### Alpha 1 Antitrypsin Deficiency
                Increased lung volumes with symmetric hyperlucency in the lower zones. Thick vertical band of plate atelectasis in the right lower zone. Pleural spaces are clear. Cardiomediastinal contours are normal.

                """)
                image = Image.open('Alpha1_Antitrypsin_Deficiency.png')
                st.image(image, caption='Alpha1_Antitrypsin_Deficiency')

                st.markdown("""
                #### Hepatocellular Carcinoma
                Diffuse bilateral ribs expansion. Lateral paravertebral and rib masses in keeping with extramedullary hematopoiesis

                """)
                image = Image.open('Hepatocellular_Carcinoma.png')
                st.image(image, caption='Hepatocellular_Carcinoma')

                st.markdown("""
                #### Hypertension due to Budd-Chiari Syndrome
                Azygous vein dilation due to portal hypertension

                """)
                image = Image.open('Hypertension.png')
                st.image(image, caption='Hypertension')

                st.markdown("""
                #### Pneumothorax
                Catamenial pneumothorax; Yellow marker shows pneumothorax and black shows diaphragmatic defect

                """)
                image = Image.open('Pneumothorax.png')
                st.image(image, caption='Pneumothorax')

                st.markdown("""
                #### Pulmonary Fibrosis
                Pulmonary fibrosis causes reticular (net-like) shadowing of the lung peripheries which is typically more prominent towards the lung bases It may cause the contours of the heart to be less distinct or ‘shaggy’

                """)
                image = Image.open('Pulmonary_Fibrosis.png')
                st.image(image, caption='Pulmonary_Fibrosis')


                
        if body_part=='Abdomen' :
            organ=st.selectbox("Organ : ",("KUB","Pelvic","Other parts of Abdomen"))
            if organ=='KUB':
                image = Image.open('abdomen_Xray_supine.png')
                st.image(image, caption='KUB')
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Abdominal aortic aneurysm
                The supine abdominal radiograph showed a large mass of soft tissue density with peripheral calcification (black arrow) over the lower abdomen, which lost its right-side margin (white arrow), with an unvisualized right psoas border, indicating a ruptured abdominal aortic aneurysm.

                """)
                image = Image.open('Abdominal_Aortic_Aneurysm.png')
                st.image(image, caption='Abdominal_Aortic_Aneurysm')

                st.markdown("""
                #### Emphysematous Cholecystitis
                Gas within gall bladder lumen, Gaseous ring, Large Gall Bladder, Disordered motility of the gallbladder

                """)
                image = Image.open('Emphysematous_Cholecystitis.png')
                st.image(image, caption='Emphysematous_Cholecystitis')

                st.markdown("""
                #### Appendicitis
                In xray examination it is neither sensitive nor specific but can provide clues on a radiograph. The presence of a calcified appendicolith in the right lower quadrant, combined with abdominal pain, has a high positive predictive value for acute appendicitis. Other signs are less specific and include caecal wall thickening, small bowel ileus and decreased small bowel gas in the RIF. Free peritoneal fluid can lead to loss of the psoas outline, loss of the fat planes around the bladder and loss of definition the inferior liver outline.

                """)
                image = Image.open('Appendicitis.png')
                st.image(image, caption='Appendicitis')

                st.markdown("""
                #### Fibroid - Calcified
                Longstanding uterine fibroids can calcify and become visible on an abdominal x ray. They are usually asymptotic
Also demonstrates incidental phleboliths.

                """)
                image = Image.open('Fibroid.png')
                st.image(image, caption='Fibroid - Calcified')

                st.markdown("""
                #### Crohn's Disease
                Supine and erect projections. Dilated small loops with air-fluid levels within the central portion of the abdomen are suggestive of bowel obstruction. Moderate fecal loading within the rectum is noted. There are no signs of pneumoperitoneum. The pleural bases are clear. 


                """)
                image = Image.open('Crohns disease.png')
                st.image(image, caption='Crohns disease')

                st.markdown("""
                #### Cholecystitis
                Radiograph showing: Arrow points to air within the lumen of GB. Arrowheads point to air in the GB wall
                """)
                image = Image.open('Cholecystitis.png')
                st.image(image, caption='Cholecystitis')

                st.markdown("""
                #### Kidney Stone
                KUB X-ray showing a 2X3 cm stone in the right upper quadrant.""")
                image = Image.open('Kidney_stone.png')
                st.image(image, caption='Kidney_stone')

                st.markdown("""
                #### Bladder Stone
                X-ray of urinary bladder, showed calculi within the bladder""")
                image = Image.open('Bladder_stone.png')
                st.image(image, caption='Bladder_stone')

                st.markdown("""
                #### Chronic Renal Failure
                Xray Showing Hyperdense kidneys""")
                image = Image.open('Chronic_Renal_Failure.png')
                st.image(image, caption='Chronic_Renal_Failure')

                st.markdown("""
                #### Emphysematous pyelonephritis

                Extensive gas overlying the renal parenchyma, collecting system, and perinephric tissues on the right side. Additional linear gas shadows along the paraspinal region, representing retroperitoneal air.
""")
                image = Image.open('Emphysematous_pyelonephritis.png')
                st.image(image, caption='Emphysematous_pyelonephritis')


                st.markdown("""
                #### Polycystic Kidney Disease
                Abdominal x-rays demonstrate large kidneys (arrows). This patient had adult polycystic kidney disease. The radiodensities along the right abdomen are related to old contrast in the colon.
""")
                image = Image.open('Polycystic_Kidney.png')
                st.image(image, caption='Polycystic_Kidney')

                st.markdown("""
                #### Renal Cell Carcinoma
                Increased density over the right lumbar region""")
                image = Image.open('Renal_Cell_Carcinoma.png')
                st.image(image, caption='Renal_Cell_Carcinoma')

                st.markdown("""
                #### Wilms Tumor
                Large mass mainly on the left but crossing the midline, which displaces the bowel loops around it. No calcification seen. No bony abnormality""")
                image = Image.open('Wilms_Tumor.png')
                st.image(image, caption='Wilms_Tumor')

                st.markdown("""
                #### Neurogenic Bladder
                Vertical urinary bladder with wall hypertrophy which causes an irregular outline. There is also left sided vesicoureteral reflux
""")
                image = Image.open('Neurogenic_Bladder.png')
                st.image(image, caption='Neurogenic_Bladder')

                st.markdown("""
                #### Bladder Outlet Obstruction
                The urinary bladder is small and shows wall irregularity with multiple diverticula. Mild bilateral vesicoureteral reflux is also evident. 
""")
                image = Image.open('Bladder_outlet_obstruction.png')
                st.image(image, caption='Bladder_outlet_obstruction')

                st.markdown("""
                #### Unilateral Vesicoureteral reflux
                Spot film taken during VCUG shows unilateral grade 4 vesicoureteral reflux.
                Grade 4: Tortuous ureter with moderate dilatation. Blunting of fornicies but preserved papillary impressions.""")
                image = Image.open('Unilateral_Vesicoureteral_reflux.png')
                st.image(image, caption='Unilateral_Vesicoureteral_reflux')

                st.markdown("""
                #### Vesicovaginal Fistula
                Contrast fills the urinary bladder via a catheter, then promptly fills the vagina, via a short fistulous tract at the posterosuperior aspect of the bladder into the upper vagina.
""")
                image = Image.open('Vesicovaginal_Fistula.png')
                st.image(image, caption='Vesicovaginal_Fistula')

                st.markdown("""
                #### Ovarian Cysts
                Ovarian cyst on plain abdominal radiograph – Teeth forming structure in left side of the pelvis (red arrow)
""")
                image = Image.open('Ovarian_cysts.png')
                st.image(image, caption='Ovarian_cysts')

                st.markdown("""
                #### Vaginal Ring Pessary
                Ring shaped density projected over the central pelvis, just above the pubic symphysis.
""")
                image = Image.open('Vaginal_Ring_Pessary.png')
                st.image(image, caption='Vaginal_Ring_Pessary')

                st.markdown("""
                #### Adenomyosis
                Multiple small diverticula extending to myometrium, especially in the left uterine wall, compatible with adenomyosis. There are also a cesarean section scar, mild dilatation of the ampullary portion of the left fallopian tube and the contrast media doesn't flow freely around the peritoneal cavity assuming the presence of peritoneal adhesions.
""")
                image = Image.open('Adenomyosis.png')
                st.image(image, caption='Adenomyosis')

                st.markdown("""
                #### Uterine Leiomyoma
                Abnormal configuration of the uterine cavity is noted, with elongation of the lower part of the uterine cavity and cervix where its left border is seen splayed over a large soft tissue shadow. 
                The injected dye spills freely out from the ends of the fallopian tube. No filling defects.

""")
                image = Image.open('Uterine_Leiomyoma.png')
                st.image(image, caption='Uterine_Leiomyoma')
            
            if organ=='Pelvic':
                image = Image.open('Pelvis.png')
                st.image(image, caption='Pelvis')
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Acetabular fracture
                """)
                image = Image.open('Acetabular_fracture.png')
                st.image(image, caption='Acetabular_fracture')

                st.markdown("""
                #### Posterior hip dislocation
                The left femoral head (white arrow) lies superior (and posterior) to the acetabulum (blue arrow). No Pelvic fracture is seen.

                """)
                image = Image.open('Hip_dislocation.png')
                st.image(image, caption='Hip_dislocation')

                st.markdown("""
                #### Pipkin Fracture Dislocation
                """)
                image = Image.open('Pipkin_Fracture_Dislocation.png')
                st.image(image, caption='Pipkin_Fracture_Dislocation')

                st.markdown("""
                #### Subcapital Femoral Neck fracture
                """)
                image = Image.open('Subcapital_Femoral_Neck_fracture.png')
                st.image(image, caption='Subcapital_Femoral_Neck_fracture')
            
            if organ=='Other parts of Abdomen':
                image = Image.open('abdomen_Xray_supine.png')
                st.image(image, caption='abdomen_Xray_supine')
                st.markdown("""
                ### Normal Vs Diseased View
                """)
                st.markdown("""
                #### Irritable bowel syndrome (IBS),
                Irritable bowel syndrome (IBS), barium enema X-ray (frontal view)
                The transverse colon (centre) and the descending colon (right) have a stacked appearance.

                """)
                image = Image.open('IBS.png')
                st.image(image, caption='IBS')

                st.markdown("""
                #### POLYPS
                Multiple polyps and large mass at the hepatic flexure

                """)
                image = Image.open('Polyps.png')
                st.image(image, caption='Polyps')

                st.markdown("""
                #### Colonic Inertia
                Colonic inertia in a constipated patient with Chagas' disease (ChC). An X-ray obtained on day 7 shows stasis of the radiopaque markers in the ascending colon
                """)
                image = Image.open('Colonic_Inertia.png')
                st.image(image, caption='Colonic_Inertia')

                st.markdown("""
                #### Rectum Stenosis 
                Barium enema, posteroanterior view of the abdomen showing the site of rectal stenosis with proximal colonic dilatation.

                """)
                image = Image.open('Rectum_Stenosis.png')
                st.image(image, caption='Rectum_Stenosis')

                st.markdown("""
                #### Colonic Diverticular Disease
                Barium contrast X- ray showing numerous diverticula along the length of the descending colon (right).
                """)
                image = Image.open('Colonic_Diverticular_Disease.png')
                st.image(image, caption='Colonic_Diverticular_Disease')

                st.markdown("""
                #### Ulcerative Colitis
                Dilated transverse colon noted. The abdomen demonstrates markedly dilated transverse colon (9 cm) with impression of slight dilatation of the descending colon with some "thumbprinting" in the wall (consistent with mucosal inflammation in the clinical circumstances).No free subphrenic gas is seen.
                """)
                image = Image.open('Ulcerative_Colitis.png')
                st.image(image, caption='Ulcerative_Colitis')

            


        if body_part=='Extremities (Others)' :
            organ=st.selectbox("Organ : ",("Extremities","Spine & Bone"))


