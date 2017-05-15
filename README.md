Name of Project: iCry

Team Members: Vanessa Nava, Genesis Valdez, Erick Acedo

Class: CST 205

Link to GitHub repo: https://github.com/Vanessa-Nava/Proj3-team043.git

TA: Samuel

Explanation: Many times when a baby cries the parent or caregiver has no idea why the baby is crying. Parents are tired and can't remember the actions they took with the baby. For example, 
            "baby's diaper was changed at 2:00 pm." iCry would take in your voice so you can speak to it and it would save the child's schedule. As soon as the app detected a baby cry, it 
            would send you the past action taken on the baby and at what time so that you can have an idea of why the baby is crying. We created a web app in which we used flask to get the app to run. 
            Bootstrapand Javascript were used for the aesthetics. The user will enter their email address, and the app will begin. We used a web API to get the voice recognition so the user can
            store their event(s). Via SMTP the user will receive the email as soon as we compare the babies cry frequency and the code detects it it's a baby cry
             

Accomplishments: We were able to use voice recognition to save the events of the baby. We were also able to access the webcam 
                 through html using getUserMedia(). We were able to open a wave file and find the frequency of the file as well
                 as plot it. 
                
                -We were able to improve our python coding skills
                -Get better at our team communication skills
                -Improve out time management skills
                
Envision: We chose to come up with iCry because a big problem new parents have is trying to figure out
          why their new born is crying. In the beginning the plan was to access a camera and detect the 
          movements of a parent and child so that it could recognize if a caregiver was feeding the baby,
          changing the diapper, etc. 

How it works: We hard coded a file of a baby cry for testing purposes. 
             - Launch the app
             - Push the recording icon
             -As soon as the code reads the file of the baby crying:
                    -check email
             -You should recieve an email of passed events the baby experienced
             -Have an idea of why thr baby is crying. 
