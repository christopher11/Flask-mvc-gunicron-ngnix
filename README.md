# Flask Service


***NGNIX** ==> **GUNICORN** ==> **FLASK***


-----------------------

**Deployment**

* Checkout code

   ```
   git clone git@eng-gitlab.juniper.net:lary/lary-ml.git
   cd lary-ml

   ```

* Run Docker Compose to Build the apps.

  ```
   docker-compose up
  ```

OR

* Just run star_app.sh, This will clean up the current running containers and build a fresh images and containers

  ```
    ./start_app.sh
  ```
