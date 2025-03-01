# Guide to Automatically Chart Radiographics Top 10 Articles in Google Sheets

This guide explains how to create a Google Sheets chart to index and organize Radiographics top 10 articles. By following these step-by-step instructions, you will navigate the Radiographics website, extract key article data, and populate a structured Google Sheets document. This document can later be used in your Python programs or other applications.

## Table of Contents

1. [Accessing the Radiographics Website](#accessing-the-radiographics-website)
2. [Navigating and Selecting Categories](#navigating-and-selecting-categories)
3. [Setting Up Your Google Drive and Sheet](#setting-up-your-google-drive-and-sheet)
4. [Populating the Google Sheet with Article Data](#populating-the-google-sheet-with-article-data)
5. [Formatting the Google Sheet](#formatting-the-google-sheet)
6. [Final Touches and Completion](#final-touches-and-completion)

---

## Accessing the Radiographics Website

1. **Search for the Top 10 Articles:**
   - Open your web browser.
   - In your search engine (e.g., Google), enter "Radiographics top 10 articles".
   - Click on the first result, typically labeled "RG TEAM Top 10 Reading List".

2. **View the Top 10 Articles Page:**
   - Once on the page, you will see several categories such as Breast Imaging, Cardiac, etc., organized by residency years (e.g., R1, R2, etc.).

## Navigating and Selecting Categories

3. **Explore Article Categories:**
   - Zoom in if necessary to clearly see the available categories.
   - Identify the categories available (for example: Basic, Intermediate, Advanced levels, and residency years like R1, R2, etc.).

4. **Select an Article for Detailed View:**
   - Click on one of the categories to view its list of articles.
   - Choose an article (e.g., a paper under the "Basic" category for R1 residents) to see its details. Note: The full link may not be accessible, but that is acceptable for charting purposes.

## Setting Up Your Google Drive and Sheet

5. **Access Google Drive:**
   - Open a new browser tab and navigate to [drive.google.com](https://drive.google.com).
   - Ensure you are logged into your Google account. If you are not, log in using your credentials. (You might need to switch to a specific account or input a passkey depending on your setup.)

6. **Create a New Folder for the Project:**
   - Click on the **New** button and select **Folder**.
   - Name the folder (for example, `RG-Top10-Articles`).
   - Open the newly created folder.

7. **Create a New Google Sheet:**
   - Inside the folder, click **New** and select **Google Sheets** to create a blank spreadsheet.
   - Rename the spreadsheet to something descriptive, such as `Top 10 Articles`.

## Populating the Google Sheet with Article Data

8. **Set Up Dual Tabs:**
   - Arrange your window so that the Radiographics website and Google Sheets are visible simultaneously, allowing easy copy-pasting between them.

9. **Define Column Headers:**
   - In your Google Sheet, create the following column headers:
     - Title
     - Author list
     - DOI
     - Year
     - R Year
     - Level
     - Abstract

10. **Extract Article Information:**
    - **Title:** Copy the article title from the Radiographics page and paste it under the "Title" column.
    - **Author List:** Copy and paste the list of authors into the "Author list" column. To ensure no extra spaces or formatting issues, consider copying into your browser's address bar first and then pasting it into the Sheet.
    - **DOI:** Copy the DOI link and paste it into the "DOI" column.
    - **Year:** Enter the publication year (e.g., 2019).
    - **R Year & Level:** For each article, assign the correct residency year (e.g., R1) and article level (e.g., Basic). Later on, these fields will be formatted as drop-down selections.
    - **Abstract:** Copy the article abstract and paste it in the "Abstract" column. If the abstract is long and contains unwanted characters, copy it into the address bar first to clean the text before pasting.

11. **Repeat the Process:**
    - Go back to the Radiographics page and repeat the above extraction steps for every article across all categories (different residency years and levels).

## Formatting the Google Sheet

12. **Create Dropdown Menus for Standard Fields:**
    - **Level Column:**
      - Select the cells in the Level column.
      - Apply data validation to create a dropdown menu with options: "Basic", "Intermediate", and "Advanced".
      - Optionally, assign each option a distinct color for visual clarity.
    - **R Year Column:**
      - Similarly, apply data validation to create a dropdown menu with options: "R1", "R2", "R3", "R4".
      - Optionally, assign colors to these options.

13. **Adjust Column and Row Settings:**
    - Remove any extra columns that are not needed for a clean layout.
    - Apply text wrapping to the "Title" and "Abstract" columns if needed, making sure that the abstract is readable but not overly wrapped if too many line breaks are present.

14. **Enhance Visual Formatting:**
    - Bold the header row for better visibility.
    - Delete any extra rows that are unused to maintain a neat appearance.

## Final Touches and Completion

15. **Review Your Chart:**
    - Ensure all data fields (Title, Author list, DOI, Year, R Year, Level, Abstract) are populated correctly for each article.
    - Verify dropdown menus are working properly and that the formatting is visually appealing.

16. **Finish Up:**
    - Once you have completed charting all the items, notify the user (or yourself) that the Google Sheet is ready to be loaded into your Python programs or any other processing tool.
    - Save your work, and optionally share the Google Sheet with others if required.

---

By following these steps, you will have successfully created a detailed chart of Radiographics top 10 articles in Google Sheets, set up for further automated processing.

Happy charting!