# codewars-scraper
A fun scraper to showcase your well-thought solutions on Codewars!


Let's imagine this...you have discovered this wonderful website called Codewars.com, amazing to put your coding skills to practice. You maybe practice Python, C++, Haskell, and plenty of other languages. But everything is online, and maybe you want to save all those great solutions of yours. That's where the Codewars Scraper comes in!

The way it is written for now, you would need to manually copy the HTML for all your solutions, but I'm working on improving this :)

Here are the steps on using it:

Step 1: Go to the 'Solutions' tab on your profile and reach the end of the page to load all solutions

Step 2: Reach the top of the page, Inspect Element at the name of the first solution, and find the first tag before the selected solution that reads:

```html
<div class="items-list w-full md:w-2/3 md:pl-4 md:border-l md:flex-grow">
 ```

Right-click on this tag and 'Edit as HTML', and copy the contents.
  
Step 3: Clone this repository, navigate to "/CodeWarsScraper" and create a HTML file, where you paste the contents

Step 4: Run the 'CodeWarsScraper.py', answer the prompts, and get scraping away!

According to the ![Codewars Code of Conduct](https://github.com/Codewars/codewars.com/wiki/Community-Code-of-Conduct), you CANNOT make the solutions publicly available though, so please try not to post these solutions on a public repo on GitHub!

(P.S. This is my first public repo so feel free to submit PRs that could improve anything from my description to the code itself)
