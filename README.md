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

1. The search engine can return paginated results; [2 points] -- done

2. The search engine can highlight results that contain search terms; [2 point] -- done but need More Info

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

***Base requirements [20 points]***

1. Users can delete items from their favorite list. [5 points] -- done

2. Items in the favorite lists should be descriptive (can’t be just a link) and are linked to and
external page or a summary page of the item. [5 points] -- done

3. The search engine implements at least one of the features spell check, autocomplete,
Google Map API, Speech-to-text API, or other APIs permitted by the instructor. [5
points]

4. There is a button from which users can download documents (or images) from the
summary page or from the SERP (or both). [5 points] -- done

***Bonus points [4 points]***

1. A RESTful API is implemented by which used can query search engine and obtain a
default number of desired results (metadata only) without using the web interface. [4
points]

2. Logged in users can like a document like Facebook. Specifications are

  1. There should be a like button for a document (a paper or an image) on the document
summary page or on the SERP;

  2. A logged in user can press the like button if he did not like the document before.

  3. The user can toggle the “like” button so if he clicks it again, the previous action was
reverted.

  4. The total number of likes is shown next to the like button. 

#### References

* Django Authentication, https://www.ordinarycoders.com/blog/article/django-user-register-login-logout

* django elastic search reference, https://apirobot.me/posts/django-elasticsearch-searching-for-awesome-ted-talks

* card columns, bricklayer, https://github.com/ademilter/bricklayer

* XSS in DJango, https://tonybaloney.github.io/posts/xss-exploitation-in-django.html

* Adding ReCAPTCHA to Django Application v2, https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html

* Adding ReCAPTCHA v3 to Django,  https://blog.ihfazh.com/how-to-implement-google-recaptcha-v3-on-your-django-app.html

* pagination, https://medium.com/@sumitlni/paginate-properly-please-93e7ca776432

* highlight search results, https://stackoverflow.com/questions/56128231/how-to-highlight-searched-queries-in-result-page-of-django-template

* storing json in db, https://www.laurencegellert.com/2018/09/django-tricks-for-processing-and-storing-json/