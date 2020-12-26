# Welcome to MedicPlace!

Hello this is my final project for cs50 harvards course, i´ve work very hard in doing, so i hope you will find it to your liking, im deeply proud of it.

## How the idea came to me:

Im from Venezuela,the country has really poor stadistics in economy,and thus in medical attention, most of venezuelans cant pay up the cost of medic consults and the hopitals are in a wicked state, so i thought i could create a page that is based in medical content, and besides we are in times of the Covid-19.

## What is MedicPlace:

As i said before is a page based on medical content, in the page doctors can create an user for them as well a profile, the doctor then can create articles in which they can inform the people of new advance in science, in treatments for diseases, methods on how to take care of oneself and love ones, opinions on others articles and more!. Besides the articles, doctors can create entrys of medicines (In venezuela we often have to change the brand and even the principal ingredient of a treatment, because it might be scarce or too expensive) in which they can explain for what purporse is used, principal ingredients,negative effects,contraindications (Very important!), and set it into a category of medicine (I will explain better below).

## Structure of the Website:

The Website has about 7-8 diferrent pages, first is the **layout.html**, its basically a navbar which has several links in it, for movement between pages, and the register,login and logout links.In this navbar not every user can see all the links, the links to create an article or a medicine entry can only be seen by users that are doctors, every other user can only see the medicine entrys, articles and profiles of doctor or other users.Finally this layout is present in every html file in the website.

In the **index.html** we have the index view in this page we have 3 list, the first one is a list of links to all the doctors that are registered, every links shows the first and last name of each doctor.The second list is for the different types of medicines, there is a link for every type of medicine (I did my research! but in any case if you see that the list is lacking one type you can contact me in 15-10627@usb.ve).The last list is a list of links for every article in the page.

**Register.html** is the basic register page it has a form which ask for firstname, lastname,age,email,username and password, it also ask the user if he/she is a doctor and with some javascript it shows or hides a input form for a doctor to write the clinic or hospital they work in.

**Login.html** simply shows a form that ask for the username and password, is the user in login without problems then its taken to the index page.

Then we have **data_sheet.html** this page works like a profile it shows the users firstname,lastname,age (if they are a normal user) and it also shows the workplace for the doctors and a rating system which the users can click to rate the doctors rating. The database loads different pages based in the user status (Doctor or not) if the page is from a doctor it also shows a list of links of article the doctor has written.

**New_Medic_article.html** loads a page with a form in where the doctors can fill the article's title and content, it also shows at the start of the page an brief explication of what they can write of and are redirected to the article's page.

**Medic_article.html** displays an article,this is, its title, content and which doctor create it. If the doctor who created the page is the request.user it displays an edit button and a delete button. The edit button lets the doctor edit the title and content of the article with javascript in the same page and it gets a response back from the server and shows it to the user. The delete button on the other hand is a form that sends a post request to the database and reedirects the user to the index page.Finally the articles have a feature of comments so they display a comment section for each article, every user (normal and doctors) can comment out and edit such comments (the edit is made with javascritp via a post request send to the database and the response is shown in the page).

**Medicine_type.html** shows a list of links for every entry of a certain type of medicine, it displays the brand name and the principal ingredient. If there isnt any entry in a type of medicine it shows a message.

**New_Medicine.html**  shows a form in which the doctors can write down the name of the medicine,type of medicine,summary and principal ingredient, then the user is redirected to the Medicine.html entry.

**Medicine.html** is the last page of the website and it displays the contents of a medicine entry, which is its name,type of medicine, the doctor who created it and summary. As in articles the doctor who created it the medicine can edit it via javascript with a post request to the database.
