<div align="center">
 <h1 align="center"> Depression Detection</h1>

 <img src="Screenshots/brain.png" alt="Logo-brain" width="150" height="150">
  
</div>

This project aims to detect early indicators of depression by analyzing data from a range of social media platforms, including images and texts. 

---

<!-- List of table of contents -->
<details open="open">
  <summary name="tbc"> Table of Contents</summary>

  <ol>
    <li> <a href="#data-collection--">Data collection </a> 
       <ol>
          <li> <a href="#visual-data">Visual Data</a> </li>
          <li> <a href="#textual-data">Textual Data</a> </li>
     </ol>
    </li>
    <li> <a href="#models">Models</a> </li>


  </ol>
</details>
 

---

## Data collection <a href="#top">&#8593; </a>
Data were collected from <a href="https://www.pexels.com/"> Pexels, </a> <a href="https://unsplash.com/"> Unsplash and </a> <a href="https://twitter.com/?lang=ang"> Twitter </a>.
Pexels and Unsplash are two freely-usable images platforms. <br>Tweets used are publicly available. 
### Visual Data: 
The overall process of scraping images from unsplash and pexels is presented as follows:
<div> <img src="Screenshots/crawl_images.PNG" alt="Image sample" width="900" height="200" align="center"> </div>

Images were crawled from Pexels using Selenium and from Unsplash using UnsplashAPI.  

Images scrapped are: 
<ul>
           <li> 6250 images labeled as "Depressed" </li>
           <li> 5234 images labeled as "Not Depressed" </li>
</ul>

This is a sample of the dataset is: 
<div> <img src="Screenshots/ImageSample.png" alt="Image sample" width="800" height="400" align="center"> </div>
  
Images can be loaded as shown in <a href="Project Cheat Sheet.ipynb"> Project Cheat Sheet</a> and codes are available <a href="https://github.com/BouzidiImen/Social_media_Prediction_depression/tree/main/Scripts/Images_functions"> here <a>.
### Textual Data: 

Hashtags that were used are trending hashtags using Keywords inspired from DSM-5(Diagnostic and Statistical Manual of Mental Disorders). 
Textual data were collected from Twitter users sharing their posts publicly using twint. 
Overall, 5460 tweets were collected.
The process was: 
 <div> <img src="Screenshots/crawl_texts.PNG" alt="Image sample" width="800" height="300" align="center"> </div>
 
You can check the result of texts loader in <a href="Project Cheat Sheet.ipynb"> Project Cheat Sheet</a> and codes are available <a href="https://github.com/BouzidiImen/Social_media_Prediction_depression/tree/main/Scripts/Twitter_Crawler"> here <a>.


## Models <a href="#top">&#8593; </a>

You can check the results of each model in the notebooks avilable in the home repository. <br>
For the best models I actually chose, you can find three notebooks: <br> 
• For images: <a href="https://github.com/BouzidiImen/Social_media_Prediction_depression/blob/main/Test_Best_Model.ipynb">this notebook </a> to test the best model.  <br> 
• For Texts:  <a href="https://github.com/BouzidiImen/Social_media_Prediction_depression/blob/main/Testing_models.ipynb">this notebook </a> to test the best model.  <br> 
• For integrating models: <a href="https://github.com/BouzidiImen/Social_media_Prediction_depression/blob/main/Integrating_Models.ipynb">this notebook </a> is to test the model.  <br> 

You can find the saved weights for images' model and texts' model <a href="https://drive.google.com/drive/folders/1R2nh2mDIhL1Z99O9XHPefwaaCNrKvFan?fbclid=IwAR1b-ZcUq7A9Xb8uV9Tv6m4ailydNWp6Pj3sr4SZ-Qm62U4tFPuVBoA_RvA">here. </a>


---

### Finally, I hope you enjoyed my work and got inspired to help people get noticed :monocle_face:. If you want more details you can find my report <a href="https://github.com/BouzidiImen/Social_media_Prediction_depression/blob/main/Report.pdf">  here </a> . 

Please contact me for more details, I would be really happy to share more infos :yum:. 


