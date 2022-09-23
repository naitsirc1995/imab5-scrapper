# imab5-scrapper

To build the image execute the following command 

**docker build . -f backend.dockerfile -t imab5-reporter**

In order to run it execute the following command 

**docker run -p 81:80 imab5-reporter**


After that the endpoint http://localhost:81/api/v1/cota will be available to receive requests. 