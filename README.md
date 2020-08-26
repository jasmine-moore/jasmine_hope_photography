# Capstone Proposal 

# NAME 
 The name of this capstone is ... jasmine_hope_photography 
 
# Project Overview 
This web development application is a professional photography website. It will be used to connect photographer to clientele, and create a place for clients to access digital copies of their photographs.  
    Frameworks and libaries: 
       - Django and django restwork for creating the database and api for storage of images and user information. 
    
# Features
A guest should be browse to see previous works with no ability to download images and have the ability fill in a form to contact the photographers if interested in gaining their services. Once someone has become a client, the client should be able to create an account, and have access to their digital watermarked copies of their photos. Once they have paid for their photos and have requested a code, a the client will also have the ability to access and download non-watermarked copies of their photos with no limits to the number of downloads or time constraints. Once they have access, they have access for ever. Clients/Users should only be able to access their photos for download, and no one elses.

There should be a secondary user-view/dashboard for adminstrators/photographers, where they can create, update, delete image folders/libaries.

# User Stories 

User Client:  as the user I want the ability to view/download my photos

  ** Tasks ** 
   - create user account form
   - create photo folder for watermarked and original photos
   - create button pinging for code to original photos, once client has paid for services
 
Admin: As the admin, I want the ability to create, update, delete images and allow clients access to thier paid for photos. 

  ** Tasks **
    - create database, to allow admin to create, update, delete image galleries/folders
    - allow admin access to client information
    - in view, link email account for ping when client/user requests access to original photos, 
      - check box/button signifying if customer has paid (checked box allows access to original photos for downloads)
    - create form in html/javascript for guests that are interested in service/getting more information, have it send information to email
 
   
# Data Models 

Types of models  -- 
  * user account:  return back homepage with linked of their photos from gallery, request for original photos,  has box with their personal information, username,   password 
  * Gallery: make watermarked photos avaliable to the public, filter and link one photo folder in ther gallery to user account
  * admin model : (page with) access to all photos, give full editing and adding abilities to all galleries/photos, check box (boolean) for marking paid for photos
  
 
 ## Schedule 
 
 5 Days: First two days, create database and api for public gallery with watermarked image and create admin model to allow or creating, updating and deleting image galleries.  
           The last day, create frontend and do minimal styling. 
           
 5 days: create database and api for users accounts, link gallery to user accounts, create form for creating account. Complete minimal styling of front end. 
 
 5 days:  Linking everything together and making sure it works. Doing major styling. creating a test account. If time allows embedding instagram feeds into side panel. 
 
 Essentials: 
   - Image Gallery (publicly available/ user available)
   - user account
   - admin account
   - inquiry form for visitors (link to send entered information straight to email)
 
 Really Great To Haves: 
   - admin ability to upload photos from front end
   - admin dashboard
   - have gallery display most recent work on homepage, if not enough time just have link to gallery
 Nice to haves: 
  - instagram feed embedded in html 
  - photographer profile
  - links to social media profile (front end)
 
 
 Long-Term Goals: 
 
 I would like to have the admin dashboard on the frontend, as one won't have to go into the django admin to update photos. If I can implement it initially, then that would be great, but it's not a non-negoitable. Eventually, I'll want to add in a payment method, and add a blog.  
 
 
 
  
