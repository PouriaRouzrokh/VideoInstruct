# Automated Cataloging of Radiographics Top 10 Articles in Google Sheets

This guide explains how to extract bibliographic data from the Radiographics website's top 10 articles and organize it into a structured Google Sheet. The process prepares this data for further analysis or for use in automation scripts (e.g., in Python). Follow these step-by-step instructions to complete the task.

## Table of Contents

1. [Accessing the Radiographics Website](#1-accessing-the-radiographics-website)
2. [Navigating Article Categories and Viewing Article Details](#2-navigating-article-categories-and-viewing-article-details)
3. [Logging into Google Drive and Creating a Workspace](#3-logging-into-google-drive-and-creating-a-workspace)
4. [Setting Up Your Google Sheet and Configuring Dropdowns](#4-setting-up-your-google-sheet-and-configuring-dropdowns)
5. [Extracting Article Data](#5-extracting-article-data)
6. [Cleansing Pasted Text Using the Address Bar Trick](#6-cleansing-pasted-text-using-the-address-bar-trick)
7. [Finalizing Your Spreadsheet](#7-finalizing-your-spreadsheet)

---

## 1. Accessing the Radiographics Website

1. Open your preferred web browser.
2. In the search bar, type "radiographics top 10 articles".
3. Click on the first result titled "RG TEAM Top 10 reading list." This page lists the curated Radiographics articles.

```
[SCREENSHOT_PLACEHOLDER]
Name: Website Search
Purpose: To show the search results for "radiographics top 10 articles."
Content: A search engine results page with the "RG TEAM Top 10 reading list" link highlighted.
Value: Assists users in identifying the correct website link for the task.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 2. Navigating Article Categories and Viewing Article Details

1. Once on the Radiographics page, review the available article categories (e.g., Breast Imaging, Cardiac, Musculoskeletal, etc.).
2. Click on a category (for example, "Breast Imaging") to display articles grouped by residency years and levels (e.g., Basic, Intermediate, Advanced).
3. Select any article from one of the categories. On the article’s detail page, you will typically see the following fields:
   - **Title**: The name of the article (usually at the top).
   - **Author List**: Listed near the title or in a metadata section.
   - **DOI**: A clickable link representing the article’s Digital Object Identifier. Use the full URL (e.g., `https://doi.org/10.1148/rg.202019001`) if available; if not, copy the DOI identifier (e.g., `10.1148/rg.202019001`).
   - **Abstract**: A summary of the article, typically located further down the page.
   - **Year**: The publication year which is usually part of the metadata found near the DOI or header. Look for additional publication details that may include the publication date.

```
[SCREENSHOT_PLACEHOLDER]
Name: Article Details
Purpose: To display an example of an article detail with key elements highlighted.
Content: A close-up view of a Radiographics article page with labels or highlights around the Title, Author List, DOI link, Abstract, and Year (found in metadata near the DOI/header).
Value: Guides users on where to locate the required information for extraction.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 3. Logging into Google Drive and Creating a Workspace

1. Open a new browser tab and go to [drive.google.com](https://drive.google.com).
2. If you are not logged in, sign in using your Google account (enter your email and follow any additional login prompts such as entering a passkey or password).
3. Once logged in, prepare your workspace:
   - Click **New** and select **Folder**.
   - Name the folder (e.g., `RG-Top10-Articles`).
   - Open this folder, then click **New** again and select **Google Sheets** to create a new blank spreadsheet.
   - Rename the spreadsheet to `Top 10 Articles`.

```
[SCREENSHOT_PLACEHOLDER]
Name: New Folder
Purpose: To show the process of creating a new folder in Google Drive.
Content: The Google Drive interface with the "New" button, folder creation dialog, and folder name `RG-Top10-Articles` entered.
Value: Ensures users organize their data properly in Google Drive.
[/SCREENSHOT_PLACEHOLDER]

[SCREENSHOT_PLACEHOLDER]
Name: New Sheet
Purpose: To display the newly created blank Google Sheet.
Content: A blank Google Sheet open in the created folder with the file name `Top 10 Articles` visible.
Value: Provides a visual reference for setting up the workspace.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 4. Setting Up Your Google Sheet and Configuring Dropdowns

1. In the blank Google Sheet, set up the following column headers in the first row:
   - Title
   - Author List
   - DOI
   - Year
   - R Year (Residency Year)
   - Level
   - Abstract
2. **Configure Dropdown Menus:**
   - For the **Level** column, create a dropdown with the options: `Basic`, `Intermediate`, and `Advanced`:
     a. Select the entire Level column.
     b. Navigate to **Data > Data validation...**.
     c. Under **Criteria**, choose "List of items" and enter: Basic, Intermediate, Advanced.
   - For the **R Year** column, set up a dropdown with options: `R1`, `R2`, `R3`, and `R4` using the same Data validation process.
3. Optionally adjust column widths and apply any desired formatting (e.g., bold headers, cell coloring) to enhance clarity.

```
[SCREENSHOT_PLACEHOLDER]
Name: Sheet Headers
Purpose: To show the initial setup of the Google Sheet with the appropriate column headers.
Content: A Google Sheet displaying the headers "Title", "Author List", "DOI", "Year", "R Year", "Level", and "Abstract".
Value: Provides a clear template for users to enter data consistently.
[/SCREENSHOT_PLACEHOLDER]

[SCREENSHOT_PLACEHOLDER]
Name: Dropdown Setup
Purpose: To illustrate configuring dropdown menus in Google Sheets for Level and R Year.
Content: The Data validation dialog in Google Sheets showing list options for Level (Basic, Intermediate, Advanced) and R Year (R1, R2, R3, R4).
Value: Ensures users know how to standardize inputs for these columns.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 5. Extracting Article Data

For each article on the Radiographics website, follow these steps:

1. **Copy the Article Title**:
   - Highlight the article title (usually at the top of the article page) and copy it.
   - Paste the title into the corresponding cell under the "Title" column in your Google Sheet.

2. **Copy the Author List**:
   - Locate the author names (typically displayed near the title or in a metadata section) and copy them.
   - Paste the author list into the "Author List" column.

3. **Copy the DOI**:
   - Find the DOI link on the article page. If the page displays the full URL (e.g., `https://doi.org/10.1148/rg.202019001`), copy the entire URL.
   - If only the DOI number (e.g., `10.1148/rg.202019001`) is visible, copy that identifier.
   - Paste the DOI into the "DOI" column. **Note:** Consistently use either the full URL or the DOI number across all entries.

4. **Copy the Abstract**:
   - Scroll to where the abstract is displayed on the article page.
   - Highlight the abstract text and copy it. Paste it into the "Abstract" column.

5. **Extract the Year**:
   - Locate the publication year, which is usually found in the metadata near the DOI or in the header of the article page.
   - Manually enter the year (e.g., `2019`) into the "Year" column.

6. **Populate Residency Year and Level Dropdowns**:
   - Using your pre-configured dropdown menus in the Google Sheet, select the correct residency year (e.g., `R1`) and level (e.g., `Basic`). These details are part of the article categorization displayed on the Radiographics page.

```
[SCREENSHOT_PLACEHOLDER]
Name: Data Extraction Detail
Purpose: To show a zoomed-in view of a Radiographics article with DOI, Author List, and Abstract clearly marked.
Content: A close-up screenshot of an article page with annotations highlighting the Title, Author List, DOI link, Abstract, and Year (from metadata).
Value: Directly guides users on where to find crucial elements on the article page.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 6. Cleansing Pasted Text Using the Address Bar Trick

Sometimes, when you copy text (especially the Author List or Abstract), extraneous formatting characters or extra spaces may be included. To clean the text:

1. Paste the copied text into your browser's address bar. This action automatically removes extra line breaks and unwanted formatting, giving you a continuous string of text.
2. Once pasted, re-copy the cleansed text directly from the address bar.
3. Then, paste the cleaned text into the appropriate cell in your Google Sheet.

_Example:_ If the abstract appears with multiple line breaks and irregular spacing, pasting it into the address bar will reformat it to a cleaner version (e.g., "Before: messy abstract text | After: clean text after address bar paste").

```
[SCREENSHOT_PLACEHOLDER]
Name: Address Bar Trick
Purpose: To illustrate the process of cleansing copied text using the browser's address bar.
Content: A screenshot showing a split view: on the left, text with formatting issues labeled "Before"; on the right, the cleaned text in the address bar labeled "After: clean text after address bar paste".
Value: Helps users understand how to remove unwanted characters and ensure data consistency.
[/SCREENSHOT_PLACEHOLDER]
```

---

## 7. Finalizing Your Spreadsheet

1. Review each row to verify that all required fields (Title, Author List, DOI, Year, R Year, Level, and Abstract) are correctly populated for each article.
2. Remove any unused rows or columns to maintain a tidy sheet.
3. Make any formatting adjustments (e.g., bolding article titles, adjusting text wrapping in the Abstract column) for visual clarity.
4. Confirm that the dropdown menus are working correctly by clicking on a cell in the Level column and verifying that the options (Basic, Intermediate, Advanced) appear. Do the same for the R Year column.
5. Once reviewed, notify the relevant stakeholders or integrate the sheet with your Python project for further processing.

```
[SCREENSHOT_PLACEHOLDER]
Name: Completed Sheet Final
Purpose: To display the finalized Google Sheet with populated data and active dropdown menus in use.
Content: The finished Google Sheet showing populated rows with data, with an open dropdown in the Level column displaying its options (Basic, Intermediate, Advanced) and a similar view for the R Year column.
Value: Confirms to users that the data is correctly imported and the dropdowns are functioning as configured.
[/SCREENSHOT_PLACEHOLDER]
```

---

## Conclusion

By following these detailed steps, you can automate the process of cataloging Radiographics top 10 articles into a Google Sheet. This organized sheet is ready for further data analysis or integration with automation and Python programs. If you encounter any issues, refer back to the relevant section of this guide for clarification.

Happy cataloging!