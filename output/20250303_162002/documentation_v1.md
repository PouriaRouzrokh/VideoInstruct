# Automated Cataloging of Radiographics Top 10 Articles in Google Sheets

This guide explains how to automatically extract bibliographic data from the Radiographics website's top 10 articles and organize it in a Google Sheets document. The steps below walk you through accessing the website, extracting data such as the article title, authors, DOI, year, residency year, level, and abstract, and finally setting up a polished, formatted spreadsheet that can later be used for further processing (e.g., with Python scripts).

## Table of Contents

1. [Accessing the Radiographics Website](#1-accessing-the-radiographics-website)
2. [Navigating the Article Categories](#2-navigating-the-article-categories)
3. [Logging into Google Drive](#3-logging-into-google-drive)
4. [Creating a New Folder and Sheet in Google Drive](#4-creating-a-new-folder-and-sheet-in-google-drive)
5. [Setting Up Your Google Sheet](#5-setting-up-your-google-sheet)
6. [Extracting and Pasting Article Data](#6-extracting-and-pasting-article-data)
7. [Enhancing Data Integrity and Formatting](#7-enhancing-data-integrity-and-formatting)
8. [Finalizing Your Spreadsheet](#8-finalizing-your-spreadsheet)

---

## 1. Accessing the Radiographics Website

1. Open your preferred web browser.
2. In the search bar, type "radiographics top 10 articles".
3. Locate and click on the first result titled "RG TEAM Top 10 reading list". This page displays the curated list of Radiographics articles.

```
[SCREENSHOT_PLACEHOLDER]
Name: Website Search
Purpose: To show the browser search results for "radiographics top 10 articles"
Content: The search engine results page with the "RG TEAM Top 10 reading list" link highlighted
Value: Helps users verify they are selecting the correct link to access the articles
[/SCREENSHOT_PLACEHOLDER]
```

---

## 2. Navigating the Article Categories

1. Once on the Radiographics page, review the list of article categories (e.g., Breast Imaging, Cardiac, Musculoskeletal, etc.).
2. Notice that articles are grouped by residency years and levels (e.g., basic, intermediate, advanced).
3. Click on one of the categories (for example, "Breast Imaging") to display the articles under that category.

```
[SCREENSHOT_PLACEHOLDER]
Name: Category List
Purpose: To show the article categories on the Radiographics page
Content: The Radiographics page displaying various article categories along with labels for residency years and level classifications
Value: Assists users in understanding where to find the articles and how they are organized
[/SCREENSHOT_PLACEHOLDER]
```

---

## 3. Logging into Google Drive

1. Open a new tab in your browser and navigate to `https://drive.google.com`.
2. If you are not already logged in, sign in using your designated Google account. (If prompted, use your email and follow the on-screen instructions such as entering your passkey or password.)
3. Ensure that you are signed in and have full access to create files and folders on your Google Drive.

```
[SCREENSHOT_PLACEHOLDER]
Name: Google Drive Login
Purpose: To show the Google Drive login screen
Content: The Google Drive login interface with the email field and sign-in instructions visible
Value: Helps users confirm they have access and know how to log in before proceeding
[/SCREENSHOT_PLACEHOLDER]
```

---

## 4. Creating a New Folder and Sheet in Google Drive

1. In Google Drive, click on the **New** button and select **Folder**.
2. Name the folder (for example, `RG-Top10-Articles`).
3. Open the newly created folder by double-clicking it.
4. Inside the folder, click on **New** again and choose **Google Sheets** to create a new blank spreadsheet.
5. Rename the spreadsheet to `Top 10 Articles`.

```
[SCREENSHOT_PLACEHOLDER]
Name: New Folder
Purpose: To show the process of creating a new folder in Google Drive
Content: The Google Drive interface with the "New" button, a folder creation dialog box, and the name `RG-Top10-Articles` entered
Value: Ensures users create and organize their data in the correct location on Google Drive
[/SCREENSHOT_PLACEHOLDER]

[SCREENSHOT_PLACEHOLDER]
Name: New Sheet
Purpose: To display the blank Google Sheet in the new folder
Content: A blank Google Sheets window with the file name `Top 10 Articles` visible at the top
Value: Guides users on how to set up their workspace for data entry
[/SCREENSHOT_PLACEHOLDER]
```

---

## 5. Setting Up Your Google Sheet

1. In the newly created spreadsheet, set up the following column headers in the first row:
   - Title
   - Author List
   - DOI
   - Year
   - R Year (Residency Year)
   - Level
   - Abstract
2. Optionally, adjust the column widths and text alignment to ensure a clean layout.

```
[SCREENSHOT_PLACEHOLDER]
Name: Sheet Headers
Purpose: To show the initial setup of column headers in the Google Sheet
Content: The Google Sheet with the first row displaying the headers: "Title", "Author List", "DOI", "Year", "R Year", "Level", "Abstract"
Value: Provides a reference for users on how to organize and label data in the spreadsheet
[/SCREENSHOT_PLACEHOLDER]
```

---

## 6. Extracting and Pasting Article Data

For each article on the Radiographics website, follow these steps:

1. **Copy the Article Title:**
   - Highlight the title of the article on the Radiographics page.
   - Copy the title and paste it into the corresponding cell under the "Title" column in your Google Sheet.

2. **Copy Other Data (Author List, DOI, Year, etc.):**
   - For the author list and DOI, highlight the text on the page, then copy it.
   - If the copied text includes extra spaces or special characters, paste it first into your browser's address bar to cleanse the text before copying it again into the sheet.

3. **Extract Additional Information:**
   - Copy the abstract of the article and paste it under the "Abstract" column. Use the address bar trick as needed to remove formatting issues (like extra line breaks or spaces).
   - Enter the year of publication manually (for example, `2019`).
   - Populate the "R Year" column by selecting the correct residency year from the drop-down list (this will be set up in the next step).
   - For the "Level" column, input the appropriate classification (e.g., Basic, Intermediate, or Advanced) using the dropdown feature.

```
[SCREENSHOT_PLACEHOLDER]
Name: Data Extraction
Purpose: To illustrate the copy-paste data entry process from Radiographics to the Google Sheet
Content: A split screen showing the Radiographics article page on one side and a Google Sheet with data being pasted into it on the other
Value: Helps users understand the dual-window workflow and verify they are extracting the correct data
[/SCREENSHOT_PLACEHOLDER]
```

---

## 7. Enhancing Data Integrity and Formatting

1. **Setting Up Dropdown Menus:**
   - For the **Level** column, set up a dropdown menu with these options:
     - Basic
     - Intermediate
     - Advanced
   - In Google Sheets, this can be accomplished by selecting the column, clicking on **Data > Data validation...**, choosing **List of items**, and entering the options separated by commas.

2. **Assigning Colors to Dropdown Options:**
   - Optionally, add color coding to the dropdown selections (e.g., assign a specific color to each level) to improve visual clarity.

3. **Residency Year Dropdown:**
   - Similarly, create a dropdown menu for the **R Year** column with options such as `R1`, `R2`, `R3`, and `R4`. Apply colors if desired to differentiate the residency levels.

4. **Cleaning Up Data:**
   - Remove any extra columns that are not needed to keep the spreadsheet clean.
   - Bold the column headers or article titles as necessary to enhance readability.

```
[SCREENSHOT_PLACEHOLDER]
Name: Dropdown Setup
Purpose: To show the process of setting up dropdown menus in Google Sheets
Content: The Data validation dialog in Google Sheets with fields for entering dropdown options for both "Level" and "R Year"
Value: Ensures that users understand how to standardize inputs and maintain data consistency
[/SCREENSHOT_PLACEHOLDER]
```

---

## 8. Finalizing Your Spreadsheet

1. After all articles have been processed and entered into the Google Sheet using the steps above, perform a final review:
   - Check that each row corresponds to a single article and that all fields (Title, Author List, DOI, Year, R Year, Level, Abstract) are correctly filled in.
   - Remove any unused rows to keep the spreadsheet tidy.
   - Adjust any formatting settings, such as text wrapping in the abstract column, to ensure that the data is clearly visible and uniform.
2. Notify the end user or your project team that the data collection is complete and the Google Sheet is ready for further processing (e.g., integration with Python programs).

```
[SCREENSHOT_PLACEHOLDER]
Name: Completed Sheet
Purpose: To show the final, polished Google Sheet with all article data populated
Content: The Google Sheet after data entry is complete, with neat column formatting, dropdown menus enabled, color-coded data, and no extra rows or columns
Value: Provides a clear example of the finished product, assuring users that they followed all steps correctly
[/SCREENSHOT_PLACEHOLDER]
```

---

## Conclusion

Following these steps, you should now have a complete and well-organized Google Sheet cataloging the Radiographics top 10 articles. This structured spreadsheet is suitable for further analysis or integration with your Python projects. If you encounter any issues during the setup process, review the respective section in this guide and verify each step for accuracy.

Happy cataloging!