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
          <li> <a href="#">Visual Data</a> </li>
          <li> <a href="#">Textual Data</a> </li>
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
<ol>
          <li> Unsplash:
                    We created a function to crawl the links of all images of a specific keyword
                    using the API of unsplash. To crawl links we can simply call this function with
                    the proper parameters to save links in a csv file. </li>
          <li> Pexels:
                   We did not use the Pexels’ API to crawl links of images for a specific keyword,
                   we created a function using Selenium Python 1 to save links in a csv file easy
                   to implement.
        </li>
     </ol>





