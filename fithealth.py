token='6097564234:AAG2WLa_kac4KUE6a5JJrgjhoDbhNnh3Xrk'

chat_id= 1318744265

#message='hello'

#chat_url='https://api.telegram.org/bot'+token'+/sendMessage?chat_id='+chat_id+'&text='+message


import requests

#upurl='https://api.telegram.org/bot+token/getupdates'

#chat_url = ''

url = 'https://api.telegram.org/bot6097564234:AAG2WLa_kac4KUE6a5JJrgjhoDbhNnh3Xrk/'


def get_updates(url):

  resp = requests.get(url+'getUpdates?').json()
  return resp['result']

data = get_updates(url)

#def get_message(data):
 

message = data[-1]['message']['text'].lower()

chat_id = data[-1]['message']['from']['id']


name= data[-1]['message']['from']['first_name']

#lname=data[-1]['message']['from']['last_name']

#message = data[-1]['message']['text']['first_name'].lower()
#print(name)

def send_message(chat_id, message):


 if message in ['hii','hi','hii','helo','hey','hello','excuse me','hlo']:
  reply = 'Hi "'+name+" "+'",welcome to the FITHEALTH BOT.This is a chat bot that give remedies/solution to your health problems\n\nMay I know! from which health problem you are suffering?\n\nthese are some examples\n\n ex:1.low bp\n2.i am having low bp\n3.i am suffering with low bp'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in['help','i need help','i dont know how to use','help me','can you help me','i want some help']:
  reply = 'just type your health problem (for ex: low bp).I will give the solution'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['how do you know my name?','how do you know my name?','how come you know my name','how you know my name','you know my name']:
  reply='It is just your telegram  user name.\n It does not store your name and other information\n It is just made to be more attractive..'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['does it store any information?','does it store any information','do it store information','doe sit stores any information','does it store any information','store any information']:
  reply='For your kind information it does not store any kind of information.\n Thank you!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in['how many health problems you know','what health problems you know','list of health problems','list of problems','health problems']:
  reply ='1.dry cough\n2.wet cough.\n3.arid\4.eye cancer\n5. food poisoning.\n6.flu\n7.fever\n8.yellow fever\n 9. wooping cough\n10. folate deficiency anemia\n11. high cholestrol\n12. hyperhydrosis\n13. huntington\n14. heart failure\n15.insomania\n16. iron deficiency anemia.\n17. bone cancer.\n18. bronchitis.\n19. kidney disease.\n20.dehydration.\n21. indigestion\n 22. diarrhoea\n23.leg cramps.\n24. migrane.\n25. tooth decay.\n26. vomitting.\n27. restless leg  syndrome\n28. sore throat \n29.stomach ache.\n 30. tooth ache.\n31. hypoglycemia(low bp).\n32. hyperglycemia(high bp).\n33. hearing loss.\n 34.constipation.\n35.headche.\n36.kidney stones .\n37.obesity.\n38.ulcer\n39.low concentration power'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['ya sure','sure','ya']:
  reply  = 'tell me!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['what can you do','what you can do','what you do','use','is there any use','what is the use','whats the use']:
  reply = 'I will give the basic aid/solution to your problem'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['how to use','use','how to interact','how to communicate']:
  reply = 'Just give your problem , I will give the basic solution'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['i dont have any symptom','no symptom','no symptom','i dont have a symptom','i dont have a symptom','i dont have any symptoms']:
  reply = 'Ok Fine ! thats alright thank you for visiting us'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['i love you','love you','lv u','i love you so much','love you so much']:
  reply = 'i love you too!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['is your solution true','solution true']:
  reply= 'It is just a basic aid to the symptom \n  the information is gathered from google'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['why should i trust','why should i trust you','should i trust you']:
  reply = 'It depends on yourself ,it is just a bot that provides the  basic aid/solution to the problem'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

  
 elif message in ['is the information correct','is information true']:
  reply= 'this information is bought from the google\n you can trust or can check in google'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['is it helpful','helpful','is it useful','useful']:
  reply = 'we hope that it is useful to get the basic aid/solution of the problem'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['does it have any side effects','any side effects ','side effects','any problems if we use this']:
  reply = 'We hope there is a less chance of that, as it is a bot it might go wrong some times \n we are sorry for that'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['thank you','thanks','thanks a lot','tqs','tq']:
  reply = 'Your welcome!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message =='yes':
  reply='thank you!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['ok bye','bye','see you','good bye','tata','byee','see you bye']:
  reply = 'thank you for visiting us ! Hope it is helpful '
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 

 elif message in ['good morning']:
  reply= 'good morning!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['good afternoon']:
  reply= 'good afternoon!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['good night ']:
  reply = 'good night!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 


 elif message in ['who created this bot','created by','who develpoed this','who did this','who created you?']:
  reply= 'This chat bot is created by MLRIT CSM C students .\n 1.CH.SHASHANK\n 2.G.ASRIT VARDHAN\n 3.G.SAI SAHITHI\n 4.L.SRISHANTH REDDY'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 

 elif message in ['ok','kk','okk']:
  reply = 'Ya! '
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 

 elif message in ['why it is used','why should we use ','what us its use']:
  reply = 'Instead of  searching in google we made it easy to you to get the basic solution for your problem'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['how are you','hw r u']:
  reply = 'As I am bot I will always be fine. How about you?'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 

 elif message in ['i am fine','fine','good','doing well']:
  reply = 'Thats good! So i think you have no use of me.But you can check whenever you are sick'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

 
 elif message in ['i am not fine','not fine','not feeling well','not good','feeling sick']:
  reply = 'May I know the problem. So if i have any solution I will give you'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 

 elif message in ['what does it give','what it give']:
  reply = 'This is  a bot that will give you the information about the solution related to your problem'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 

 elif message in ['chicken pox','pox','i am having chicken pox','i have chicken pox','i am suffering from chicken pox','i am suffering with chicken pox']:
  reply='So you are suffering from chicken pox, I recommend you to follow the below given remedies to control it.\n1.stop scratching \n 2.keep hydrated\n 3. diet: consume vitamin c food items like :oranges, lemon, watermelons'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 

 elif message in['cough','i am having cough','i have cough','i am suffering from cough','daggu','i am suffering with cough']:
  reply = 'Ok you are having cough. But which type of cough either dry cough or wet cough'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 
 
 elif message in  ['dry cough','dry','i am having dry cough','i have dry cough','i am suffering with dry cough']:
   reply = 'So you are suffering with dry cough. Consider following the below mentioned steps to control your dry cough.\n1. Drink plenty of liquis to stay hydrated.\n 2. Take honey with warm water\n 3. Try doing  mountain pose(tadasana),standing forward bend variation(uttanasana)'
   response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
   return response
 

 elif message in ['wet','wet cough','i am having wet cough','i have wet cough','i am suffering from ','i am suffering from wet cough','i am suffering with wet cough']:
  reply = 'Ok I understood that you are suffering from wet cough. So,following the below steps will ease your cough and helps to control it.\n1.keep your body hydrated.\n 2. try to drink ginger tea and keep steam.\n 3.sit in a chair with your feet firmly on the floor\nraise your arms over your head as you take deep breathe in\nhold your breathe in this position briefly\nquickly bend forward from the hips and try to cough several times in a row\nrepeat it 2-3 times.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in['low concentration power','i have low concentration power','i am having low concentration power','i am suffering from low concentration power','i am suffering with low concentration power','bad memory','i am having bad memory power','i am suffering with bad memory power','i am suffering from bad memory power']:
  reply='So you are suffering with low concentration power, in order to increase your concentration power consider following the given steps:\n\n 1.Try doing meditation atleast for 10-15 min a day in morning.\n 2.Try taking green tea, leafy vegetables and eat chocolate(improves focus because it contains caffeine).\n3.try the given yoga postures to increase your concentration..\n1.tadasana(helps regulate nervous system).2.balasana(brings out balance,coordination and focus)'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response



 elif message in ['arid','A rid','a rid','a-rid','i am having a-rid','i am having arid','i have arid','i have a-rid','i am suffering with a-rid','i am suffering from arid','i am suffering from a-rid','i am suffering with arid']:
  reply = 'So you are suffering from a-rid .Following the given remedies will control it.\n1.people are not advised to drink regularly\n 2. it is suggested to have 14 units a week not more than this.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['i am having eye cancer','i have eye cancer','eye cancer','EYE  CANCER','eyecancer','i am suffering with eye cancer','i am suffering from eye cancer']:
  reply = 'I unnderstood that you are having eye cancer. Follow these steps to reduce it.\n\n  1. limit your eye exposure to sunlight\n 2. Eat leafy vegetables like spinach  and vitamin C food like oranges,raspberries\n 3. Do regular exercise atleast 150 minutes per week'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['i am having food poisoning','i have food poisoning','food poisoning','FOOD POISONING','FOODPOISONING','foodpoisoning','i am sufferinng from food poisoning','i am suffering with food poisoning']:
  reply = 'So you are dealing  with food poisoning ,follow the below steps to  solvve it.\n\n1. Avoid spicy and acidic food like fast food. \n 2. Take bananas,cerals and rice\n 3.Do regular exercise like walking'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['i am having flu','i have flu','flu','FLU','flue','FLUE','i am suffering with flu','i am suffering from flu']:
  reply = 'I understood that you are having flu,so please consider following these steps.\n\n1. Drink plenty of water to keep the body hydrated\n 2. Consider taking broth(soup either vegetable or meat) and eat vitamin C food(oranges,kiwi)and  vitamin D food(fish,almond,milk)\n 3. better to not do any kinnd of exercise'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['i have fever','i am having fever','fever','FEVER','fever','i am suffering with fever','i am suffering from fever']:
  reply  = 'I understood that you are having fever..SO please follow the given steps to cure it.\n\n1. Drink  more fluids to keep the body hydrated \n 2. Eat broth and fruits like oranges and  drink fresh juice\n3. Recommended to do daily activities like walking at lower rate to keep physical health good.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response
 

 elif message in ['yellow fever','yellowfever','YELLOW FEVER','i am having yellow fever','i have yellow fever','i am suffering with yellow fever','i am suffering from yellow fever']:
  reply = 'So you are having yellow fever.Follow the given steps to cure it.\n\n1. Keeping your body hydrated can help to recover easily \n 2. Eat fresh fuits and vegetables ,nuts and drink herbal tea.\n3. Avoid doing outdoor exercises.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 
 

 elif message in ['wooping cough','woopingcough','WOOPING COUGH','WOOPINGCOUGH','i am having wooping cough','i have wooping  cough','i am sufferinng with wooping cough','i am suffering from wooping']:
  reply = 'If you are having wooping cough,try these steps.\n\n1. Drink hot water or honey water.\n 2. Have ginger tea or turmeric milk.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['folate deficiency anemia','folatedeficiencyanemia','i am having folate deficiency anemia','i have folate deficiency anemia','i am suffering with folate deficiency anemia','i am suffering from folate deficiency anemia']:
  reply = 'It is clear that ypu are having folate deficiency anemia, you might consider folowing the below steps in order to cure it.\n\n1.Eat meat ,egg yolk and drink milk.\n 2.Do normal workouts like running,walking etc.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['hypoglycemia','HYPOGLYCEMIA','low blood sugar','low bp','lowbp','i am  having  low bp','i have low bp']:
  reply = '1. Follow 15-15 rule(eat 15g of carbohydrates and check blood sugar after 15 min).\n 2. Eat bananas,apple.Drink milk,honey and fruit juice.\n 3. Do anaerobic exercise like high intensity interval training(HIIT)'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['high cholestrol','highcholestrol','HIGHCHOLESTROL','i am having high cholestrol','i have high cholestrol','i am suffering from high cholestrol','i am suffering with high cholestrol']:
  reply = 'So you are having high cholestrol, So you need to follow the given steps to reduce it:\n\n1. Eat plenty of vegetables , protein rich food and eggs.\n 2. Do regular exercise like running,swimming and cycling.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['hyperglycemia','HYPERGLYCEMIA','high bp','HIGH BP','HIGHBP','highbp','high blood sugar','i am having high bp','i have high bp','i am suffering from high bp','i am suffering with high bp']:
  reply = 'I understood that you are having high bp. So i recommend you to follow the below steps:\n\n1.Eat whole grains , fruits ,vegetables and low-fat dairy products.\n 2. Do exercises like walkking,running ,cardio and strength training'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['hyperhydrosis','HYPERHYDROSIS','hyper hydrosis','i am having hyperhydrosis','i have hyperhydrosis','i am suffering from hyperhydrosis','i am suffering with hyperhydrosis']:
  reply = 'So you are having hyperhydrosis,So you might consider the following steps to reduce it:\n\n1. Drink water.\n 2. Eat water--dense fruits and vegetables and calcium rich  foods like low-fat milk,cheese,and magnesium rich foods like almondsand spinach.\n3. Reduce heavy  workouts.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['huntington disease','huntington','i am having huntington','i have huntington','i am suffering from huntington disease','i am suffering with huntington disease']:
  replly = 'So you are  worrying with hyperhydrosis right.I advise you to follow the below steps:\n\n1. Choose  soft food.\n  2. Eat food which is easy to swallow and add more gravies and sauces to the food.\n 3. Do aerobic activities ideally  for 150 minutes a week.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 

 elif message in ['heart failure','HEARTFAILURE','heartfailure','i am having heart failure','i have heart failure','i am suffering with heart failure','i am suffering from heart failure']:
  reply = 'So you are having heart failure.You might check out the given steps which reduce the risk of it:\n\n1. Eat fresh fruits and vegetbles.\n 2. Eat food that contain less amount of salt  like plainn rice,poultry and milk.\\n 3.. Stationary cycling, walking and aerobics.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['hearing loss','hearingloss','chevudu','chevuti','vinikidi lemi','i am having hearing loss','i have hearing loss','i am suffering with hearing loss','i am suffering from hearing loss']:
  reply = 'So I understood that you are having hearing loos.You can follow the below remedies to improve your hearing:\n\n1.Eat fish,legumes banana and dark choclate.\n 2.  Do Sound therapy and sound focus through meditation.'  
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['insomania','sleeplessness','nidra lemi','no sleep','no proper sleep','i am having insomania','iam having sleeplessness','i have sleeplessness','i am suffering from insomania','i am suffering from sleeplessness']:
  reply = 'So you are not getting proper sleep.Please follow the below remedies in order to get a good sleep:\n\n1. Dont use  mobile before 1hr of going to sleep.\n 2. Take almonds,warm milk,kiwi and walnuts.\n 3. perform childs pose(Balasana).'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['iron deficiency anemia','irondeficiencyanemia','i am having iron defeciency anemia','i have iron deficency anemia','i am suffering with iron ddeficiency anemia','i am suffering from iron deficiency anemia']:
  reply='I understood that you are having iron deficiency anemia .So in order to reduce it consider following the below given steps:\n\n1. Try to eat leafy vegetables ,iron fortified cerals,bread,poultry.\n 2. Do normal exercise like runnning walking and swimming'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['bone cancer','bonecancer','i am having bone cancer','i have bone cancer','i am suffering from bone cancer','i am suffering with bone cancer']:
  reply = 'So you are  worrying about your boone cancer.Please follow these remedies:\n\n1. do chemotherapy.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['bronchitis','i have bronchitis','i am having bronchitis','i am suffering with bronchitis','i am suffering from bronchitis']:
  reply = 'You are tackling with bronchitis ,please follow the given remedies.\n\\n1. avoid smoking. \n 2. drink plenty of water'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['kidney disease','kidneydisease','i am having  kidney disease','i have kidney disease','i am suffering from kidney disease','i am suffering with kidney disease']:
  reply = 'I unnderstood that you are having kidney disease.You should consider the following remedies:\n\n1. Avoid drinking alcohol.\n 2. try to eat butter ,ghee,peas and meat.\n3. 150 mins of cardio,cycling,walking every week.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['constipation','malabaddakam','i am having constipation','i have constipation','i am suffering from constipation','i am suffering with constipation']:
  reply = 'So you are tackling  with constipation. So I advise you to follow the given remedies in order to get releif from constipation.\n\n 1. Drink atleast 1-2 glasses of luke warm water after you woke up.\n 2. Eat fruits, vegetables,whole grains and meat.\n 3.These are some of the yoga asanas i suggest for you.\n1.malasana. 2. maduk asana 3.butterfly pose'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['dehydration','i am having dehydration','i have dehydration','i am suffering with dehydration','i am suffering from dehydration']:
  reply ='I understood that you are having dehydration problem.So you should consider following these remedies to have a control on it:\n\nDrink plenty of fluids like water and diluted juices and squash.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['headache','tala noppi','head ache','i have headache','i am having headache','i am suffering with headache','i am suffering from headche']:
  reply = 'You are having with headache,so you are advised to follow these remedies:\n\n1.Take an oil massage.\n 2. Have some ginger tea.\n 3. perform turn head side to side.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['indigestion','i have indigestion','i am having indigestion','i have indigestion','i amsuffering from indigestio','i am suffering with indigestion']:
  reply = 'You are having indigestion.So, to improve your digestion I suggest you to follow the given remedies:\n\n1. Try  eating whole grains such as oatmeal,brown rice.\n  2. Go for walking,yoga and light jogging.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['daihheroa','i have daihheroa','i am having daihheroa','i  amm suffering from daihheroa','i am sufering with daihheroa']:
  reply = 'You are suffering with daihheroa ,So i suggest you to follow these remdies.\n\n1. Eat  high potassium foods like bananas,potatoes and fruit juice.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response


 elif message in ['kidneystones','kidney stones','i am having kidney stones','i have kidney stones','i am suffering fromm kidney stones','i am suffering with kidney stones']:
  reply='So i understood that you are having stones in kidney .I recommend you to follow these remedies.\n\n1. Drink plenty of fluids ,particularly water.\n 2. Eat food with less salt and more calcium such as milk,eat oranges and low fat diet.\n 3. Lie down on your back and bring both knees close to your chestwhile inhaling.hold this pose and try to get your nose close to your knees.Now take a few long breathes,then exhale and inhale.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['legcramps','leg cramps','kallanoppulu','kalla noppulu','i have leg cramps','i am having leg cramps','i am sufferin with leg cramps','i am suffering from leg cramps']:
  reply = 'So you are having leg cramps.Please follow the given remedies to reduce your cramps.\n\n1. keep your  body hydrated by drinking  coconut water.\n 2. Eat fruits like avacado,watermelon and papaya.\n 3. stretch your legs against the walls and hold for 5 min.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['migrane','i am having migrane','i have migrane','']:
  reply = 'I understood that you are having  migrane .Follow the steps given to reduce it.\n\n1.drink ginger tea .\n 2. Try eating leafy vegetables(spinach),fruits like watermelon,banana,avacado and pumpkin seeds.\n 3. Do brisk(active)walking and cycling.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['obesity','i am having obesity','i have obesity']:
  reply ='If you are suffering with obesity,follow below given remedies:\n\n1.Do not eat excess processed food or beverages.\n 2. Better to eat whole grains,vegetables and nuts.\n 3. Consider doing wall pushups,hip swirl,dumbell side bend.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['tooth decay','toothdecay','i am  having tooth deacy','i have tooth  decay']:
  reply = 'So you are tackling with tooth decay,follow these steps to ease it\n\n1. Do not drink cool water.\n 2. try eating food which contain calcium and phosphate like milk,cheese and other dairy products.\n 3. Do proper brushing and flossing.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 

 
 elif message in ['ulcer','i am  having ulcer','i have ulcer']:
  reply = 'If yo are suffering with ulcer ,try doing these steps:\n\n1. try to reduce eating spicy foods.\n 2. Eat apples ,pears,oats and other foods that are rich in fiber,these are good for ulcer inn two ways.Fibre can reduce amount of acid in stomach and research says  fibre rich diet helps in preventing ulcer.\n 3.  strength training yoga.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['vomiting','vomitting','i am having vomitting','i have vomitting']:
  reply = 'So you are having vomitting,follow below remedies to get relief:\n\n1. Avoid eating food that are hard to digest like oily,spicy food.\n 2. Recommended to eat banana,rice and dry toast.\n 3. Breathe out through mouth with your lips pursed in a whistling position.Let your belly fall back inward,pushing out all the air.Repeat same for 10 times.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['restless leg syndrome','restlesslegsyndrome','i have restless leg syndrome','i have restless syndrome']:
  reply = 'You are suffering from restless leg syndrome,I suggest you to follow these remedies to reduce your pain:\n\n1.Rest your self.\n 2. Incorporate a variety of fresh fruits and vegetables in your diet.Eat iron rich foods like meat.\n 3. Aim for 30-60 mins regular exercise per day and avoid exercise where your joints ache.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['sore throat','sorethroat','i have sore throat','i am having sore throat']:
  reply = 'If you are having a sore throat try the below given remedies to cure it.\n\n1. Use a vaporizer,especially when sleeping to keep air from getting too dry.\n 2. Consider eating chicken soup,oatmeal.Try taking a hot ginger tea or add honey to warm water.\n 3. Gargle with salt water.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['stomach ache','stomachache','i have stomach ache','i have stomach ache']:
  reply = 'so you are suffering with stomach ache then try below steps to ease it.\n\n1.eat rice,applesauce and toast.\n 2. Lie down your knees bent and your arms at your sides.Keep your feet flat on the floor.lift your  head and shoulders up 8 to 10 cm.At the sametime ,raise your arms to about thigh level.\n Hold for 6 seconds.\n Relax and return to your starting position.\n Repeat 8 to 12 times.'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 


 elif message in ['tooth ache','toothache','i am having tooth ache','i have stomach acheasdd']:
  reply='If you are suffering from tooth ache,try doing these steps:\n\n1. Do not drink excess cool items.\n 2. Try taking oatmeal,soups,soft cheese and meatloaf.\n 3. resisted mouth closing:\n resisted mouth opening:\nforward jaw movement:\nchin tucks:'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 

 
 elif message in ['anxiety','i have anxiety','i am having anxiety','i am suffering from anxiety','i am suffering with anxiety']:
  reply='''So you are suffering with anxiety.So, you are recommended to do these steps
  try doing halasana'''
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response

  
 elif message in ['regular exercises','regular exercise','what are regular exercise','give some regular exercise','suggest some exercise','name regular exercise']:
  reply = 'some of the regular exercises are.\n1.walking.\n 2. running\n3. swimminng\n4.climbing stairs.etc'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response 

  

 else:
  reply='Sorry, I dont understand what you said.Please try anything else.\n\nthank you!'
  response = requests.post(url+'sendMessage?chat_id='+str(chat_id)+'&text='+reply)
  return response




send_message(chat_id,message)

#print(data[-1]['message']['text'])

#print(data[-1]['message']['from']['id'])

#print(data[-1]['message']['from']['first_name'])
update_id = None

def get_updates(url,offset):
  url = url+'getUpdates?timeout=100'
  if offset:
     url = url+ '&offset={}'.format(offset+1)
  r = requests.get(url).json()
  return r


while True:
  print("....")
  updates = get_updates(url,offset=update_id)
  print(updates)
  updates=updates['result']
  if updates:
    for item in updates:
        update_id = item['update_id']
        try:
         message = item['message']['text'].lower()
         chat_id = item['message']['from']['id']
         send_message(url,message,chat_id)
        except:
         message = None


