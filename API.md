# API endpoint #

**user login endpoint**
----

* **URL**

  `/api/v1/auth/login/`

* **Method:**

  `POST`

*  **URL Params**

   `username`: the username

   `password`: the user password


* **Success Response:**

  * **Code:** 200 OK <br />
  * **Content:**

```javascript
{"auth_token":"token"}
```

**user ads management endpoint**
----
this endpoint handles 3 user operations (save ads, delete ads,get ads)

* **URL**

  `/ads-management/current/`

* **Method:**

  `GET`

*  **Header Params**

  'Authorization: token key'


* **Success Response:**

  * **Code:** 200 OK <br />
  * **Content:**

```javascript
  list_ads:{
    'auto_ads':{ [
                 {'id':1,'title':'ad1','image':'/image/url','description':'desc'}
                 ]
               }
    'manual_ads':{ [
                 {'id':1,'title':'ad1','image':'/image/url','description':'desc'}
                 ]
               }
}
```

* **URL**

  `/ads-management/`

* **Method:**

  `POST`

*  **Header Params**

  'Authorization: token key'

*  **Data Params**

  ```javascript
{'ad_type':'auto or manual','ad_id':'ad_id'}
```

* **Success Response:**

  * **Code:** 201 Created <br />

* **Error Response:**

  * **Code:** 400 Bad request <br />

* **URL**

  `/ads-management/ad_id`

* **Method:**

  `DELETE`

*  **Header Params**

  'Authorization: token key'


* **Success Response:**

  * **Code:** 200 OK <br />

* **Error Response:**

  * **Code:** 400 Bad request <br />