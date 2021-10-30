# UAE-Event-Tracker
This is an Event-Tracker Website for UAE. Built in HTML5, CSS3, Javascript, Python and Flask.

<img width="506" alt="Output-1" src="https://user-images.githubusercontent.com/50153606/139543111-dcff58cf-61ec-45ce-93bc-d2fb6fa89eae.png">

Here, the problem at hand has been solved using 2 Approaches.

The 1st Approach requires the use of the PredictHQ Events Explore API just for the Event Data Scraping purposes, which is then manually fed to the geoJSON section of the HTML (index.html) File. Here, the Mapbox API has been used and the Markers are seen for the Upcoming 10 Events in the United Arab Emirates (UAE) on the base map thus obtained.
Whenever more events need to be added, that can directly be done by using the PredictHQ Events Explore API for scraping information about more Events, and can thus be added to the geoJSON section of the HTML (index.html) file in the main branch, and automatically a Marker shall be added for those longitude and latitude points on the base map, with a popup option to display the description (Title, Date and Location) of that event.

<img width="506" alt="Output-1" src="https://user-images.githubusercontent.com/50153606/139543111-dcff58cf-61ec-45ce-93bc-d2fb6fa89eae.png">

<img width="960" alt="Output-3" src="https://user-images.githubusercontent.com/50153606/139544125-c513fbb8-d2c1-42ab-be4b-9bb71e004e15.png">

The 2nd Approach (contents enclosed in the Map Directory) involves the use of both the APIs, i.e. the PredictHQ Events API and the Google Maps API. THis Approach makes use of HTML, CSS, Javascript, Python and Flask. Even though the Event location markers are not seen on the Map, however upon running the App.py file, all the necessary information as the 'Title' of the Event, the 'Logitude Coordinates' and the 'Latitude Coordinates' are seen in the Debugger Terminal Console. All the Upcoming events can be spotted from there, along with their exact location coordinates. So to update the list of events, all that needs to be done is to just run the App.py file again, and it dynamically updates the list of all the upcoming events in the UAE Region.

<img width="470" alt="Output-2" src="https://user-images.githubusercontent.com/50153606/139543742-83d173a1-cf06-49e8-811e-3e1e1a5df4df.png">

<img width="521" alt="Output-4" src="https://user-images.githubusercontent.com/50153606/139544233-a067dcb9-733f-4397-b1f1-01812ca3cf4a.png">
