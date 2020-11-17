# CS518 : Web Programming Project
## Project Title: Eye of Sauron
***Anoop Reddy Ananthula | aanan002 |***

### About

Eye of Sauron(EOS) is a search engine developed using Django, Elastic search, MySQL. This search engine returns the patent figures from the repository based on the the search string.

### Milestone 1 : Build Basic Framework

***Basic requirements***

1. The website should provide a search box at the landing page. The searching function
may not be working;

2. There should be a search button next to the search box;

3. Users must be able to register new accounts using email addresses;

4. Password must be encrypted before storing in the database;

5. Users cannot register duplicate accounts using the same email address, or phone number;

6. Users should be able to log into your website using the accounts they registered;

7. Users should be able to reset their passwords if they forget it;

8. The user login process must use the HTTP POST method;

9. User information shall be stored in a MySQL database;

10. The website should have a homepage for each user, where they can view their profiles, change passwords, and update information.

***Optional requirements (Get Ahead)***
1. Users should be able to get a confirmation email to verify their email addresses;

2. The website provides an “Advanced Search” button in which users can specify more
information.

### Milestone 2 :  Build the search function using Elastic Search

***Base requirements***

1. Users should be able to get a confirmation email to verify their email addresses for registration or password reset; --- done

2. The website has an “Advanced Search” function so users can search multiple fields; -- done

3. The advanced search should return results satisfying multiple specifications; -- done

4. The website should index at least 5000 “documents” (a document can be metadata of an image or metadata of an ETD); -- done

5. The search engine accepts a text query in the search box; -- done

6. The search engine should return search results on the search engine result page (SERP), which can be links to documents or images; -- done

7. The search engine should display the number of returned items on SERP; -- done

8. The SERP should contain a search box; -- done

9. The search engine can prevent XSS vulnerability by removing tags existing in the query; -- done 

10. Users should be able to insert a new entry (document) and search engine will index it. -- done

***Optional requirements (Get Ahead)***

1. The search engine can return paginated results;

2. The search engine can highlight results that contain search terms;

3. Users can save search history in their profile.

#### Milestone 3

***Base requirements [15 points]***

1. The search engine can return paginated results; [2 points] -- in progress

2. The search engine can highlight results that contain search terms; [2 point] -- need More Info

3. The SERP should display the actual term (after sanitization) shown on top; [2 point] -- done

4. Users can click each item on SERP and go to either an external link or a page containing 
more information of the item; [2 point] -- done

5. Users can save items in search result to their profiles; [2 points] -- done

6. Users have to login first to save search history to their profiles; [2 point] -- done

7. reCAPTCHA should be used for both the logging in and the signing up page; [3 points] -- done

***Optional requirements (Get Ahead)***

1. The search engine can do spell check;

2. The search engine can do autocompletion;

3. The search engine uses at least one of these APIs: Google Map API, Speech-to-text API.

#### Milestone 4

#### References

* Django Authentication, https://www.ordinarycoders.com/blog/article/django-user-register-login-logout

* card columns, bricklayer, https://github.com/ademilter/bricklayer

* XSS in DJango, https://tonybaloney.github.io/posts/xss-exploitation-in-django.html

* Adding ReCAPTCHA to Django Application v2, https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html

* Adding ReCAPTCHA v3 to Django,  https://blog.ihfazh.com/how-to-implement-google-recaptcha-v3-on-your-django-app.html

* pagination, https://medium.com/@sumitlni/paginate-properly-please-93e7ca776432
