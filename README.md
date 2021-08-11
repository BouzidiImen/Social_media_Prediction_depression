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
    <li> <a href="#">Models</a> </li>


  </ol>
</details>
 

---

## Data collection <a href="#top">&#8593; </a>
Data were collected from <a href="https://www.pexels.com/"> Pexels, </a> <a href="https://unsplash.com/"> Unsplash and </a> <a href="https://twitter.com/?lang=ang"> Twitter </a>.
Pexels and Unsplash are two freely-usable images platforms. I used the publicly available tweets. 
### Visual Data: 
Codes are in Scripts/Images_functions/

<ol>
          <li> Unsplash:
                    I created a function to crawl the links of all images of a specific keyword
                    using the API of unsplash. To crawl links, I can simply call this function with
                    the proper parameters to save links in a csv file. </li>
          <li> Pexels:
                   I did not use the Pexels’ API to crawl links of images for a specific keyword,
                  I created a function using Selenium Python 1 to save links in a csv file easy
                   to implement.
        </li>
</ol>

I scrapped: 
• 6250 images labeled as "Depressed" <br>
• 5234 images labeled as "Not Depressed"

A sample of the dataset is as follow: 
<div> <img src="Screenshots/ImageSample.png" alt="Image sample" width="800" height="400" align="center"> </div>
  
Images can be loaded as shown in the project sheet cheat. 
### Textual Data: 
Textual data was collected from Twitter users sharing their posts publicly using Twitter Intelligence Tool. 
Overall, I got 5460 tweet.
You can see exmples in the project sheet cheat on how to load data. 





